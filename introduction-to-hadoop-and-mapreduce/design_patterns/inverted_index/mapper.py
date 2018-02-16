#!/usr/bin/python

import sys
import csv
import re

"""
# TEST
FILE = '/Users/Raj/Root/GitHub/Hadoop-and-MapReduce/introduction-to-hadoop-and-mapreduce/sample_data/form_node_100.tsv'

with open(FILE, 'r') as f:
    for line in f:

        text = line.strip().split('\t')

        # HEADING => Length = 19
        # "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"	"parent_id"	"abs_parent_id"	"added_at"	"score"
        # "state_string"	"last_edited_id"	"last_activity_by_id"	"last_activity_at"	"active_revision_id"
        # "extra"	"extra_ref_id"	"extra_count"	"marked"

        if len(text) == 19:
            print text[4]
f.close()
"""
reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)

for line in reader:
    if len(line) == 19:
        node_id = line[0]
        node_body = line[4]
        # find all the words
        node_body_words = re.findall(r'[a-zA-Z]+', node_body)
        node_body_words = [word.lower for word in node_body_words]
        for word in node_body_words:
            print "{0}\t{1}".format(word, node_id)
