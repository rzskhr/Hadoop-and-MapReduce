#!/usr/bin/python


import sys

last_url = None
count = 0
most_pop_url = None
most_pop_count = 0


# TODO

for line in sys.stdin:
    curr_url = line.strip()
    if last_url and last_url != curr_url:
        count = 0
    
    last_url = curr_url
    count += 1
    
    if count > most_pop_count:
        most_pop_count = count
        most_pop_url = curr_url

if last_url is not None:
    if count > most_pop_count:
        most_pop_count = count
        most_pop_url = last_url

print most_pop_url, '\t', most_pop_count

