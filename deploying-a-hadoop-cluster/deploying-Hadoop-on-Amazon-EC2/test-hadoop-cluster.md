# Test the Hadoop Cluster

Create a home directory on HDFS
```
$ hdfs dfs -mkdir /user
$ hdfs dfs -mkdir /user/ubuntu
```
Create random data for the Terasort example,
```
$ hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar teragen 500000 random-data
```
Sort random data,
```
$ hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar terasort random-data sorted-data
```
Write files to disk with TestDFSIO:
```
$ hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-*-tests.jar TestDFSIO -write -nrFiles 10 -fileSize 5MB
```
Read files from disk with TestDFSIO:
```
$ hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-*-tests.jar TestDFSIO -read -nrFiles 10 -fileSize 5MB
```
