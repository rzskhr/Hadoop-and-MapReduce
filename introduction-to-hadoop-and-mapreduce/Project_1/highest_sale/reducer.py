#!/usr/bin/python


import sys


highest_sale = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print(oldKey, "\t", highest_sale)
        oldKey = thisKey
        highest_sale = 0

    oldKey = thisKey

    if highest_sale < float(thisSale):
        highest_sale = float(thisSale)

if oldKey != None:
    print(oldKey, "\t", highest_sale)
