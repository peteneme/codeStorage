Code Screen
===========

When our customer needs new servers configured, they send a CSV file of the server hostname, the serial number, and the primary IPv4 address, netmask, and gateway to be configured on the server. The CSV may contain anywhere from 10-30 severs.

We need either a command line client or a rest api (you choose) that reads this CSV file in on startup and provides us with a REST API endpoint at /server/{serial} which returns the corresponding row as JSON formatted data.

Sometimes a customer will provide invalid data. We can't fix all data entry problems but we do want to handle the following cases:

- If a hostname has extra whitespace on the beginning or end, remove the whitespace before returning the result
- IP addresses are not strings, make sure that the ip,netmask, and gateway are valid IPv4 addresses or netmasks. If not, return an error for that server.
- Bonus: If the combination of ip address, netmask, and gateway would provide an invalid network (gateway outside of network/subnet), return an error for that server instead of the invalid configuration

CSV Format
----------

- filename: newservers.csv
- Assume a properly formatted CSV
- One header row
- Fields: serial,hostname,ip,netmask,gateway

JSON Format
-----------

JSON Return data format will match same fields names and data as from the CSV.

```json
{
    "serial": "sn1241",
    "hostname": "server001",
    "ip": "192.168.0.18",
    "netmask": "255.255.255.0",
    "gateway": "192.168.0.1"
}
```

CLI Tool Requirements
---------------------

- require one argument, the serial number
- by default, tool will read "newservers.csv" in the current directory
- you may optionally pass in a flag to read a different filename or path
- return only properly formatted json as output (unless there is an error)
- if there is an error, return a status code of 1

TIP: You should be able to pipe the output of this through a json processing tool such as `| jq '.'` or `| python -mjson.tool`.
BONUS: If there is an error, return that as stderr so the error message does not get piped and can be still readable by the operator.

Rest API requirements
---------------------

- A GET to /server/{serial} return the JSON as described above

Final notes
-----------

The application should be easy to run for testing.

Do not spend too much time on this. Consider it a minimum viable product, one in which you want to present for feedback before iterating on the next version. But please be prepared to explain how you would approach adding any features that didn't make it into the initial release and how you would improve this application.

Here are some other backlog feature requests that you don't have to implement, but be prepared to discuss:

- The application only reads in one CSV on startup. You have to restart the service each time the customer sends us a new file. Can we improve on this?
- For invalid configurations, the server will never successfully download its configuration. Thoughts?
- The service technically only has to live until each service has retrieved their configuration. The rest of the time, the service is running uninitialized, costing us in cloud hosting fees. How can you improve the program to save us money?
