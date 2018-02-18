#!/usr/bin/python


import sys


count = 0
total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    count += 1
    total += float(thisSale)

print "Total:\t", total, "\nCount:\t", count

