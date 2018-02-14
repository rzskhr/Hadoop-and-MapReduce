#!/usr/bin/python


import sys


for line in sys.stdin:

    data = line.strip().split(" ")

    if len(data) == 10:
        # ip_address, identity, username, date_time, time_zone, request_method, path, protocol_name, status_code, \
        #         obj_size = data

        url_str = 'http://www.the-associates.co.uk'

        if data[6].find(url_str) == -1:
            print data[6]
        else:
            data[6] = data[6][len(url_str):]
            print data[6]
