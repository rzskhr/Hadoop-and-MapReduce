#!/usr/bin/python

FORM_NODE_FILE = '/Users/Raj/Root/GitHub/Hadoop-and-MapReduce/introduction-to-hadoop-and-mapreduce/sample_data' \
           '/form_node_100.tsv'
FORM_USERS_FILE = '/Users/Raj/Root/GitHub/Hadoop-and-MapReduce/introduction-to-hadoop-and-mapreduce/sample_data/form_users_100.tsv'


with open(FORM_NODE_FILE, 'r') as f:
    for line in f:
        data = line.strip().split('\t')
        # HEADER, length = 19
        # ['"id"', '"title"', '"tagnames"', '"author_id"', '"body"', '"node_type"', '"parent_id"', '"abs_parent_id"',
        #  '"added_at"', '"score"', '"state_string"', '"last_edited_id"', '"last_activity_by_id"',
        #  '"last_activity_at"', '"active_revision_id"', '"extra"', '"extra_ref_id"', '"extra_count"', '"marked"']
        if len(data) == 19:
            id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string,\
                last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, \
                extra, extra_ref_id, extra_count, marked = data

f.close()


with open(FORM_USERS_FILE, 'r') as f:
    for line in f:
        data = line.strip().split('\t')

        # HEADER, length = 5
        # ['"user_ptr_id"', '"reputation"', '"gold"', '"silver"', '"bronze"']
        if len(data) == 5:
            user_ptr_id, reputation, gold, silver, bronze = data
            
f.close()
