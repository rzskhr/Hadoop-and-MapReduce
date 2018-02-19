## Configure SSH

Firstly, you’ll want to change the permissions on the private key file, or you’ll get an error when you try connecting through ssh. To change permission on Linux and OS X, ```$ sudo chmod 600 /path/to/key_file.pem```, ```where key_file.pem``` is the private key you created earlier.

Test logging in to the instance. Here ```instance_hostname``` is the public hostname of your instance:

```
$ ssh -i /path/to/key_file.pem ubuntu@instance_hostname
```
Now copy the private key to the instance:
```
$ scp -i /path/to/key_file.pem /path/to/key_file.pem ubuntu@instance_hostname:~/.ssh
```


## Install Java and Hadoop
Update and upgrade:
```
$ sudo apt-get update && sudo apt-get dist-upgrade
```
Install OpenJDK:
```
$ sudo apt-get install openjdk-7-jdk
```
Download Hadoop from one of these mirrors. Change the version number appropriately:
```
$ wget http://apache.mirrors.tds.net/hadoop/common/hadoop-2.7.2/hadoop-2.7.2.tar.gz -P ~/Downloads
```
Extract it to /usr/local:
```
$ sudo tar zxvf ~/Downloads/hadoop-* -C /usr/local
```
Rename the directory to just hadoop:
```
$ sudo mv /usr/local/hadoop-* /usr/local/hadoop
```

## Set Environment Variables
Find Java with:
```
readlink -f $(which java)
```
Environment variables:
```
export JAVA_HOME=/path/to/java
export PATH=$PATH:$JAVA_HOME/bin
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export HADOOP_CONF_DIR=/usr/local/hadoop/etc/hadoop
```
Load variables:
```
$ source ~/.bashrc
```

