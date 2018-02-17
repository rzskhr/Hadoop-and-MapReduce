#!/usr/bin/python

import sys


total_sale = 0
count = 0
old_key = None

for line in sys.stdin:
    data = line.strip().split('\t')

    # double check
    if len(data) != 2:
        continue

    key, sale = data

    if old_key and old_key != key:
        print old_key, '\t', float(total_sale/count)
        old_key = key
        total_sale = 0
        count = 0

    old_key = key
    total_sale += float(sale)
    count += 1


if old_key is not None:
    print old_key, '\t', float(total_sale/count)
