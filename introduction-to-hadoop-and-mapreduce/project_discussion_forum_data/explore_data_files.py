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
            """
            The ones that are the most relevant to the task are:
                - "id": id of the node
                - "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
                - "tagnames": space separated list of tags
                - "author_id": id of the author
                - "body": content of the post
                - "node_type": type of the node, either "question", "answer" or "comment"
                - "parent_id": node under which the post is located, will be empty for "questions"
                - "abs_parent_id": top node where the post is located
                - "added_at": date added
            """

f.close()


with open(FORM_USERS_FILE, 'r') as f:

    for line in f:
        data = line.strip().split('\t')

        # HEADER, length = 5
        # ['"user_ptr_id"', '"reputation"', '"gold"', '"silver"', '"bronze"']

        if len(data) == 5:
            user_ptr_id, reputation, gold, silver, bronze = data
            """
            It contains fields for:
                - "user_ptr_id" - the id of the user. 
                - "reputation" - the reputation, or karma of the user, earned when other users upvote their posts,
                - and the number of "gold", "silver" and "bronze" badges earned
            """

f.close()
