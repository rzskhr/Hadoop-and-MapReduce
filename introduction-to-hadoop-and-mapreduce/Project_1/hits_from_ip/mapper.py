#!/usr/bin/python


import sys


for line in sys.stdin:

    data = line.strip().split()

    if len(data) == 10:
        ip_address, identity, username, date_time, time_zone, request_method, path, protocol_name, status_code, \
                obj_size = data

        print(ip_address)
