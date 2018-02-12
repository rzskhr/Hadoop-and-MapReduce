#!/usr/bin/python


FILE_PATH = "/Users/Raj/Root/GitHub/Hadoop-and-MapReduce/introduction-to-hadoop-and-mapreduce/sample_data/access_log_100"


path_list = list()

with open(FILE_PATH, 'r') as f:
    for line in f:
        data = line.strip().split()

        ip_address, identity, username, date_time, time_zone, request_method, path, protocol_name, status_code, \
            obj_size = data

        # print(date_time.strip("["))
        # print(time_zone.strip("-").strip("]"))
        # print(request_method.strip('"'))
        # print(protocol_name.strip('"'))

        path_list.append(path)
        print(username, " ==> ", path)

    count = 0
    path_nme = set()
    for i in path_list:
        path_nme.add(i)

f.close()
