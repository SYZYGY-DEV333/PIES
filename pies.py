#!/usr/bin/env python
# PIES v2.0
# SYZYGY-DEV333
# Simple TCP port scanner in Python
# Apache Version 2

from socket import *
import sys, time
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("min", help="Minimum port number to scan")
parser.add_argument("max", help="Maximum port number to scan")
parser.add_argument("host", help="host address to scan")
args = parser.parse_args()

host = args.host
max_port = args.max
min_port = args.min
def scan_host(host, port, r_code = 1):
    try:
        s = socket(AF_INET, SOCK_STREAM)
        code = s.connect_ex((host, port))
        if code == 0:
            r_code = code
        s.close()
    except Exception, e:
        pass
    return r_code

hostip = gethostbyname(host)
print("\n>> Host: %s IP: %s" % (host, hostip))
print(">> Scanning Started At %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()
for port in range(eval(min_port), eval(max_port)):
    try:
        response = scan_host(host, port)
        if response == 0:
            print(">> Port %d: Open" % (port))
    except Exception, e:
        pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("\n>> Scanning Finsihed At %s ..." % (time.strftime("%H:%M:%S")))
print(">> Scanning Duration: %s ..." % (total_time_duration))
print(">> Have a nice day!")
#!EoF
