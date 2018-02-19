# Configuring the cluster
You’ll need the public hostname of each instance going forward, so it’s really convenient to copy them down in a file. You can see each public hostname by selecting all the instances.

Hadoop has an intimidating number of configuration options.

### Hadoop environment variables
The first file to take note of is hadoop-env.sh, it holds environment variables used by Hadoop. Here, you'll just need to set ```JAVA_HOME```.
```
export JAVA_HOME=/path/to/java
```

### Cluster-wide configuration
First, you’ll deal with the configuration on each node, then get into specific configurations for the NameNode and DataNodes. On each node, go to the Hadoop configuration folder, you should be able to get there with ```$ cd $HADOOP_CONF_DIR``` since we set that in ```.bashrc``` earlier. When editing these configuration files, you'll need root access so remember to use ```$ sudo```. In the configuration folder, edit ```core-site.xml```:
```xml
<configuration>
  <property>
    <name>fs.defaultFS</name>
    <value>hdfs://namenode_public_hostname:9000</value>
  </property>
</configuration>
```
where ```namenode_public_hostname``` is the public hostname of your NameNode. This configuration ```fs.defaultFS``` tells the cluster nodes which machine the NameNode is on and that it will communicate on port 9000.

On each node, in ```yarn-site.xml``` you set options related to YARN, the resource manager:
```xml
<configuration>

<!— Site specific YARN configuration properties -->

  <property>
    <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
  </property>
  <property>
    <name>yarn.resourcemanager.hostname</name>
    <value>namenode_public_hostname</value>
  </property>
</configuration>
```
Similarly with fs.defaultFS, yarn.resourcemanager.hostname sets the machine that the resource manager runs on.

On each node, copy ```mapred-site.xml``` from ```mapred-site.xml.template```
```
$ sudo cp mapred-site.xml.template mapred-site.xml
```
and add:
```xml
<configuration>
  <property>
    <name>mapreduce.jobtracker.address</name>
    <value>namenode_public_hostname:54311</value>
  </property>
  <property>
    <name>mapreduce.framework.name</name>
    <value>yarn</value>
  </property>
</configuration>
```
Again, ```mapreduce.jobtracker.address``` sets the machine the job tracker runs on, and the port it communicates with. The other option here ```mapreduce.framework.name``` sets MapReduce to run on YARN.

### NameNode specific configuration
Now, NameNode specific configuration, these will all be configured only on the NameNode. First, add the DataNode hostnames to ```/etc/hosts```. You can get the hostname for each DataNode by entering ```$ hostname```, or ```$ echo $(hostname)``` on each DataNode.

Now edit ```/etc/hosts``` and include these lines:
```
127.0.0.1 localhost
namenode_public_hostname namenode_hostname
datanode1_public_hostname datanode1_hostname
datanode2_public_hostname datanode2_hostname
datanode3_public_hostname datanode3_hostname
```
Now, on the NameNode, edit ```hdfs-site.xml```:
```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  <property>
    <name>dfs.namenode.name.dir</name>
    <value>file:///usr/local/hadoop/data/hdfs/namenode</value>
  </property>
</configuration>
```
```dfs.replication``` sets how many times each data block is replicated across the cluster. ```dfs.namenode.name.dir``` sets the directory for storing NameNode data (```.fsimage```). You’ll also have to create the directory to store the data:
```
$ sudo mkdir -p $HADOOP_HOME/data/hdfs/namenode
```
Next, you’ll create the ```masters``` file in ```HADOOP_CONF_DIR```. The ```masters``` file sets which machine the secondary namenode runs on. In your case, you'll have the secondary NameNode run on the same machine as the NameNode, so edit ```masters```, add the hostname of NameNode (**Note**: Not the public hostname, but the hostname you get from ```$ hostname```). Typically though, you would have the secondary NameNode run on a different machine than the primary NameNode.

Next, edit the ```slaves``` file in ```HADOOP_CONF_DIR```, this file sets the machines that are DataNodes. In ```slaves```, add the hostnames of each datanode (**Note**: Again, not the public hostname, but ```$ hostname``` hostnames). The slaves file might already contain a line localhost, you should remove it, otherwise the NameNode would run as a DataNode too. It should look like this:
```
datanode1_hostname
datanode2_hostname
datanode3_hostname
```
Finally on the NameNode, change the owner of ```HADOOP_HOME``` to ```ubuntu```:
```
$ sudo chown -R ubuntu $HADOOP_HOME
```

### DataNode specific configuration
Now on each DataNode, edit ```HADOOP_CONF_DIR/hdfs-site.xml```:
```xml
<configuration>
  <property>
    <name>dfs.replication</name>
    <value>3</value>
  </property>
  <property>
    <name>dfs.datanode.data.dir</name>
    <value>file:///usr/local/hadoop/data/hdfs/datanode</value>
  </property>
</configuration>
```
Again, this sets the directory where the data is stored on the DataNodes. And again, create the directory on each DataNode:
```
$ sudo mkdir -p $HADOOP_HOME/data/hdfs/datanode
```
and change the owner of the Hadoop directory
```
$ sudo chown -R ubuntu $HADOOP_HOME
```
