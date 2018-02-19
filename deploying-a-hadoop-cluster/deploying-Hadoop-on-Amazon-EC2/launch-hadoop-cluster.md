## Launch Hadoop Cluster

On the NameNode, format the file system, then start HDFS.
```
$ hdfs namenode -format
$ $HADOOP_HOME/sbin/start-dfs.sh
```
Start YARN:
```
$ $HADOOP_HOME/sbin/start-yarn.sh
```
Start the job history server:
```
$ $HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver
```
To see the Java processes (Hadoop daemons for instance), enter
```
$ jps
```
