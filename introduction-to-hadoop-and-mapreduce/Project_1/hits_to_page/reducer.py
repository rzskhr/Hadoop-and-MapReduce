#!/usr/bin/python


import sys


i = 0

for line in sys.stdin:
    
    if line.strip() == '/assets/js/the-associates.js':
        i += 1

print(i)

