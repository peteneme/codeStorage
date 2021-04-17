#!/usr/bin/python

import sys
import ipaddress
import json
import csv
import re
from netaddr import *




def csv_to_json(filename=None):
    jsonList = []

    with open(filename, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        for row in csvReader:
            for key in row.keys():
                ### avoid spaces in data ###
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

    #print(row.get('ip', str()) , row.get('netmask', str()) , row.get('gateway', str()), net_ok, gateway_found_in_range, err_list)
    return net_ok, err_list




### MAIN ######################################################################
if __name__ != '__main__': sys.exit(0)

jsonList = csv_to_json('newservers.csv')

for row in jsonList:
    net_ok, err_list = checkNetwork(row)
    print(row, ' --> ', 'OK ' if net_ok else 'PROBLEM%s' % (str(err_list)))



