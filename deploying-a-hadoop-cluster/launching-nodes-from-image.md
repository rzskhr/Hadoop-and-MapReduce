# Launching nodes from the image
Now that you have an image with Java and Hadoop installed, you can use this as nodes in our cluster. Select the Hadoop node image, then click launch. Choose 4 instances, one will be the NameNode, the other three will be DataNodes.
<br/><br/>
Continue with configuration as before, remember to set the security to “All Traffic.” When launching, select “Choose an existing key pair” and the private key that you created before. The new instances will use this private key for connecting over SSH.
<br/><br/>
You should see all four nodes in the instances panel. You’ll need the public hostname of each instance often, so it's best to write each one in a file for reference.
<br/><br/>
To make logging into the instances more convenient, let’s create an SSH config file. First, on your computer, create the file with ```$ touch ~/.ssh/config```, then edit ```~/.ssh/config``` in your favorite editor. Add these lines to the file.
<br/><br/>
```
Host namenode
  HostName namenode_public_hostname
  User ubuntu
  IdentityFile ~/.ssh/key_file.pem

Host datanode1
  HostName datanode1_public_hostname
  User ubuntu
  IdentityFile ~/.ssh/key_file.pem

Host datanode2
  HostName datanode2_public_hostname
  User ubuntu
  IdentityFile ~/.ssh/key_file.pem

Host datanode3
  HostName datanode3_public_hostname
  User ubuntu
  IdentityFile ~/.ssh/key_file.pem
```
This file lets SSH associate a shorthand name with a hostname, a user, and the private key, so you don't have to type those in each time. This is assuming your private key ```key_file.pem``` is in ```.ssh```. If it isn't be sure to move or copy it there: ```cp key_file ~/.ssh/key_file.pem```. Now you can log into the NameNode with just ```$ ssh namenode```. Also, copy the config file to the NameNode:
```
$ scp ~/.ssh/config namenode:~/.ssh
```
You need to make sure the NameNode can connect to each DataNode over ssh without needing a password. You’ll do this by creating a public key for the NameNode and adding it to each DataNode.

On the NameNode (remember ```$ ssh namenode```), create a public key and copy it into ```authorized_keys```:
```
$ ssh-keygen -f ~/.ssh/id_rsa -t rsa -P ""
$ cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
Copy authorized_keys to each DataNode to enable passwordless login. On the NameNode:
```
$ ssh datanode1 'cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub
$ ssh datanode2 'cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub
$ ssh datanode3 'cat >> ~/.ssh/authorized_keys' < ~/.ssh/id_rsa.pub
```
Test this by logging into a DataNode from the NameNode:
```
$ ssh datanode1
```
You can get back to the NameNode with
```
$ exit
```
