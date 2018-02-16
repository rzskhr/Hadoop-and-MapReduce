import sys
from collections import defaultdict

inverted_index = defaultdict(list)

for line in sys.stdin:
    data = line.strip().split('\t')

    # double check
    if len(data) != 2:
        continue

    node_word = data[0]
    node_id = data[1]

    inverted_index[node_word].append(node_id)

for word in inverted_index:
    if word == 'fantastic' or word == 'fantastically':
        print "{0}\t{1}\t{2}".format(word, len(inverted_index), inverted_index[word])
