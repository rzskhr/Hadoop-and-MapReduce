#!/usr/bin/python


import sys


i = 0

for line in sys.stdin:

    if line.strip() == '10.99.99.186':
        i += 1

print i

