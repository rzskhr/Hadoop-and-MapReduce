#!/usr/bin/python


import sys


i = 0

for line in sys.stdin:
    url = line.strip()

    if url == '':
        i += 1

print i

