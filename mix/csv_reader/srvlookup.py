#!/usr/bin/python

import sys
import ipaddress
import json
import csv
import re
from netaddr import *
from flask import Flask, request, render_template_string
import requests
import argparse



def csv_to_json(filename=None):
    jsonList = []

    with open(filename, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            for key in row.keys():
                ### AVOID SPACES IN DATA START/END ###
                row[key] = str(row.get(key, str())).strip()
            jsonList.append(row)
    return jsonList


def checkNetwork(row=None):
    net = str()
    err_list = []
    net_ok = True
    gateway_found_in_range = False

    ### CHECK IPV4 ADDRESSES ###
    if not row.get('ip', str()):
        net_ok = False
        err_list.append('ip is void')
    if not row.get('netmask', str()):
        net_ok = False
        err_list.append('ip is void')
    if not row.get('gateway', str()):
        net_ok = False
        err_list.append('ip is void')

    ### 0<=IP<=255 check to implement in future

    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", row.get('ip', str())):
        net_ok = False
        err_list.append('ip problem')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", row.get('netmask', str())):
        net_ok = False
        err_list.append('netmask problem')
    if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", row.get('gateway', str())):
        net_ok = False
        err_list.append('gateway problem')

    if net_ok:
        ### GET NETWORK FROM IP/MASK ###
        net = ipaddress.ip_network(row.get('ip', str()) + '/' + row.get('netmask', str()), strict=False)
        network_address = str(net.network_address)
        network_mask = str(net.netmask)

        ### USE ANOTHER LIBRARY ###
        network_in_cidr = IPNetwork(network_address + '/' + network_mask)
        network_range = list(network_in_cidr)

        ### CHECK IF GATEWAY IS INSIDE NETWORK AND NOT BROATCAST OR NW ADDR ###
        for iploop in network_range:
           if str(network_in_cidr.broadcast) == str(iploop): pass
           elif network_address == str(iploop): pass
           elif row.get('gateway', str()) == str(iploop): gateway_found_in_range = True

        if not gateway_found_in_range:
           net_ok = False
           err_list.append('gateway %s not in ip range %s' % (row.get('gateway', str()), str(network_in_cidr)))

        ### CHECK IP FOR NW ADDR/BROADCAST ADDR ###
        if network_address == row.get('ip', str()):
           net_ok = False
           err_list.append('ip %s is network address' % (row.get('ip', str())))

        if str(network_in_cidr.broadcast) == row.get('ip', str()):
           net_ok = False
           err_list.append('ip %s is broadcast address' % (row.get('ip', str())))

        ### CHECK GATEWAY FOR NW ADDR/BROADCAST ADDR ###
        if network_address == row.get('gateway', str()):
           net_ok = False
           err_list.append('ip %s is network address' % (row.get('gateway', str())))

        if str(network_in_cidr.broadcast) == row.get('gateway', str()):
           net_ok = False
           err_list.append('ip %s is broadcast address' % (row.get('gateway', str())))

    #print(row.get('ip', str()) , row.get('netmask', str()) , row.get('gateway', str()), net_ok, gateway_found_in_range, err_list)
    return net_ok, err_list


def rest_serve(data, server_port):
    app = Flask(__name__)

    @app.route('/', methods=['GET'])
    def root_path():
       json_dumps = json.dumps(data, indent=2)
       return json_dumps

    @app.route('/server/<string:serial_number>', methods=['GET'])
    def receive_data_add_one(serial_number):
        json_dumps = str()
        for row in data:
            if str(serial_number) == row.get('serial',str()):
                net_ok, err_list = checkNetwork(row)
                if net_ok:
                    json_dumps = json.dumps(row, indent=2)
                else: json_dumps = str(err_list)
        return json_dumps

    @app.route('/exit', methods=['GET','POST','PUT'])
    def send_exit():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        return "==> Shutting down..."

    app.run(debug=True, port=server_port, use_reloader=False)


def cli_json_print(data, serial_number):
    json_dumps = str()
    serial_found = False
    for row in data:
        if str(serial_number) == row.get('serial', str()):
            net_ok, err_list = checkNetwork(row)
            if net_ok:
                print(json.dumps(row, indent=2))
                serial_found = True
                sys.exit(0)
    if not serial_found: sys.exit(1)


def cli_parser():
    ######## Parse program arguments ##################################
    parser = argparse.ArgumentParser(
                        description = "Script %s" % (sys.argv[0]),
                        epilog = "e.g: \n" )
    parser.add_argument("--csvfile",
                        action = "store", dest = 'csvfile', default = str(),
                        help = "input csv file")
    parser.add_argument("--serial",
                        action = "store", dest = 'serial', default = str(),
                        help = "specify serial number")
    parser.add_argument("--rest",
                        action = "store_true", dest = 'rest', default = str(),
                        help = "use rest interface")
    args = parser.parse_args()
    return args


### MAIN ######################################################################
if __name__ != '__main__': sys.exit(0)

args = cli_parser()

if args.csvfile: csvfile = str(args.csvfile)
else: csvfile = 'newservers.csv'

jsonList = csv_to_json(csvfile)

if args.rest: rest_serve(jsonList, 8888)
else: cli_json_print(jsonList, args.serial)
