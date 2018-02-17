#!/usr/bin/python


# FILE = "/Users/Raj/Root/GitHub/Hadoop-and-MapReduce/introduction-to-hadoop-and-mapreduce/sample_data/purchases_100"
# with open(FILE, 'r') as f:
#     for line in f:
#         data = line.strip().split('\t')
#         if len(data) == 6:
#             date, time, store, item, cost, payment = data
#             weekday =  datetime.strptime(date, '%Y-%m-%d').strftime('%A')
#             print "{0}\t{1}".format(weekday, cost)
#
# f.close()


import sys
from datetime import datetime


for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
        print "{0}\t{1}".format(weekday, cost)
