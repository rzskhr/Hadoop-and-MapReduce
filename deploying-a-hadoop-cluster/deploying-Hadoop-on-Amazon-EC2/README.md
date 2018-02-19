# Launch an EC2 Instance
Hadoop is built for running on commodity hardware in a data center. However, I imagine few of you have server racks in your garage. Since you don’t have access to a bunch of hardware, you’re going to deploy a Hadoop cluster on [Amazon Web Service](https://aws.amazon.com/) (AWS) EC2 (Elastic Compute Cloud) virtual machines.<br/><br/>
These are virtual machines we can request and run from anywhere in the world, typically at some cost per hour, per machine. Each virtual machine, an instance for shorthand, has a configurable number of CPUs and amount of memory and storage. We’re going to be using a free offering, but most organizations will need more resources to store and analyze their data.<br/><br/>

After logging in, choose a region that is closest to you shown here.<br/><br/>
![AWS Account](https://raw.githubusercontent.com/rzskhr/Hadoop-and-MapReduce/master/deploying-a-hadoop-cluster/img/aws-account.png)


#### Now we’re ready to create some instances. Here's what we should do:

1. From “Services”, select “EC2”.
2. Click the “Launch Instance” button.
3. Choose Ubuntu 64-Bit.
4. Choose t2.micro. Click “Next: Configure Instance Details.”
5. Leave the number of instances to 1. We’re going to install Hadoop on this instance and use it as a generic Hadoop node. Click “Next: Add Storage”
6. This is where you set the storage for your instance, 8 GB is fine. Of course, if you’re doing this for an organization, you’ll need to choose an appropriate storage size to fit your data. Click “Next: Tag Instance”
7. Here you can assign a tag to your instance. Anything is fine, I used “Hadoop node”. Click “Next: Configure Security Group.”
8. The security group determines who can connect to your instances. The default is “SSH” and 0.0.0.0/0. This means that any computer can connect to your instance over ssh. In practice, you would assign a restricted list of IP addresses that can access your cluster. However, for ease, you should leave it open. You’ll also need to change the type to “All Traffic” so that we can access the instances over HTTP as well as SSH. Then, click “Review and Launch” to launch your instances.

![Creating EC2 instance](https://raw.githubusercontent.com/rzskhr/Hadoop-and-MapReduce/master/deploying-a-hadoop-cluster/img/creating-ec2.gif)

<br/><br/>
At the end of the process, you’ll be prompted to create and download a private key. This key will allow you to connect to your instances with SSH. If you don’t download this, or delete it somehow, you won’t be able to connect to your cluster. If you lose it, don’t panic, but you’ll have to shut down the instances and start up new ones. Name it whatever you like, I just used “hadoop.” Click “View Instances” to see your instance booting up in the EC2 dashboard. You'll want to write down the public hostname, called “Public DNS” on the instance panel.

- After this is done, follow [further-steps](https://github.com/rzskhr/Hadoop-and-MapReduce/blob/master/deploying-a-hadoop-cluster/deploying-Hadoop-on-Amazon-EC2/further-steps.md).
- Then save all the work on an image.
- After that [Launch Cluster nodes from the image](https://github.com/rzskhr/Hadoop-and-MapReduce/blob/master/deploying-a-hadoop-cluster/deploying-Hadoop-on-Amazon-EC2/launching-nodes-from-image.md).
- [Configure the Hadoop Cluster](https://github.com/rzskhr/Hadoop-and-MapReduce/blob/master/deploying-a-hadoop-cluster/deploying-Hadoop-on-Amazon-EC2/configure-hadoop-cluster.md).
- [Launch Hadoop Cluster](https://github.com/rzskhr/Hadoop-and-MapReduce/blob/master/deploying-a-hadoop-cluster/deploying-Hadoop-on-Amazon-EC2/launch-hadoop-cluster.md).
- [Test](https://github.com/rzskhr/Hadoop-and-MapReduce/blob/master/deploying-a-hadoop-cluster/deploying-Hadoop-on-Amazon-EC2/test-hadoop-cluster.md).
<br/><br/><br/><br/>
[reference](https://classroom.udacity.com/courses/ud1000/lessons/7427734703/concepts/74229414570923)
