#!/usr/bin/python


import sys
import csv
from datetime import datetime


reader = csv.reader(sys.stdin, delimiter='\t')
reader.next()

for data in reader:

    if len(data) == 19:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,\
            last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, \
            extra, extra_ref_id, extra_count, marked = data

        print author_id, '\t', datetime.strptime(added_at[1:-4], "%Y-%m-%d %H:%M:%S.%f").hour
