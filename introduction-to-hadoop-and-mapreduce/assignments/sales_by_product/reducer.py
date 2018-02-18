#!/usr/bin/python


import sys


salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey
        salesTotal = 0

    oldKey = thisKey

    salesTotal += float(thisKey)

if oldKey != None:
    print oldKey, "\t", salesTotal
