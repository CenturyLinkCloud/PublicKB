{{{
"title": "Getting started with Hortonworks Hadoop - Blueprint",
"date": "4-30-2015",
"author": "Jeff Demuth and Bob Stolzberg",
"attachments": [],
"contentIsHTML": false
}}}

![Hortonworks Hadoop logo](http://info.hortonworks.com/rs/h2source/images/hortonworks-logo00.jpg)

### Technology Profile
Apache Hadoop® is an open source framework for distributed storage and processing of large sets of data on commodity hardware. Hadoop enables businesses to quickly gain insight from massive amounts of structured and unstructured data.

### Description
CenturyLink has created a Blueprint that makes it extremely easy to spin up a Hortonworks Hadoop Server in minutes. You can start using your Hortonworks Hadoop server immediately after the Blueprint completes. The Blueprint will automatically install all required packages and settings required for Hortonworks.

Advantages of running Hortonworks in CenturyLink Cloud:
- Fast provisioning - get Hadoop running within minutes- No long term server commitment - pay as you go each month
- On-demand Scalability - Add more CPU, Disk or Memory resources on the fly as your data grows.
- Save money - Run your Hadoop server only when you use it. You can host a server just during business hours and power it off during nights and weekends.  You can use the CenturyLink Cloud mobile app to start and stop your server anytime, anywhere.
- Fast Bandwidth - Your Hadoop server has a 2GB inbound network throughput ensuring low latency data transfers.
- No technical experience required - Don't worry about setting kernel variables and preloading database and software packages, we did that for you.  Just run the blueprint, enter some basic configuration details and start importing data.

### Audience
CenturyLink Cloud Users, Data Scientists and Big Data Enthusiasts.

### Impact
After reading this article, the user should feel comfortable getting Hortonworks Hadoop up and running with Server Blueprint technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
- If you want to access your VM with Hortonworks Hadoop over the internet, please perform the following tasks once you receive an email confirming you Blueprint completed successfully:

1. If you need to connect to your server via the Internet, Add a [Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal. Alternatively, you can [setup a VPN using OpenVPN](../../Network/how-to-configure-client-vpn.md) or similar technology.

2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal. Hortonworks listens on port 8080

### Install Hortonworks on RHEL6 Blueprint
1.	Locate the Hortonworks Install Blueprint
1.	Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
2.	Search for “Hortonworks” in the keyword search on the right side of the page.
3.	Locate the 'Install Hortonworks on RHEL6' Blueprint
2.	Choose and Deploy the Blueprint. Click the “Install Hortonworks on RHEL6” Blueprint.
3.	Configure the Blueprint using the standard information. There is nothing special required.
4.	Review and Confirm the Blueprint.
1.	Click “next: step 2”
2.	Verify your configuration details.
5.	Deploy the Blueprint.
1.	Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
2.	This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.
6.	Monitor the Activity Queue.

* Monitor the Deployment Queue to view the progress of the blueprint.
* You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
* Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the Hortonworks Server until you have received this email notification.

### Accessing your Hortonworks Hadoop Server
After your Blueprint deploys successfully, please follow these instructions to access your server:
1.	Check your email to obtain Server Name and IP Address Login information
2.	Click on the link to the server and then add a firewall port as referenced in the post requisite section
3.	Open a Web browser and navigate to your servers IP using port 8080.  This should look like the following URL “http://<your-ip-here>:8080”.  Login as the user admin with password admin to customize your Hadoop server.
4.	Once logged in click on “Launch Install Wizard”
5.	Type in your preferred cluster name in the “Cluster Name” Field. Click next.
6.	Select “HDP 2.1” and click next.
7.	Type in “localhost” in the field “Target Hosts”.
8.	For this next section we will need the RSA private key from the server.  SSH to the server and copy the text from the command “cat /root/.ssh/id_dsa” and paste it into the “Host Registration Information” Field.
9.	Click OK to confirm localhost as the FQDN.
10.	Click next after host registration.
11.	You may receive a firewall notice just click ok to accept.
12.	Click next to confirm desired services.
13.	Click next to confirm master assignments.
14.	Click next to confirm slave assignments
15.	Click on the Nagios tab, enter in your preferred Nagios password and preferred Email address.
16.	Click on the Hive tab, enter in your preferred Hive password 
17.	Click on the Oozie tab and enter in your preferred oozie password.
18.	 Click on the Falcon tab, for *falcon.graph.blueprints.graph enter com.thinkaurelius.titan.core.TitanFactory
19.	For *.falcon.graph.storage.backend field enter berkeleyje
20.	Scroll to the bottom of the page and click Next.
21.	Click Deploy
22.	After configuration is complete hit Next
23.	On Summary page click Complete
24.	You will then be redirected to the Hortworks Dashboard: http://your-ip:8080/#/main/dashboard/metrics

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Hortonworks Hadoop license costs or additional fees bundled in.

### Frequently Asked Questions

#### What does thie Blueprint do?
1.	Provision a VM with 2CPU and 4GB of RAM
2.	Install RedHat Enterprise Linux 6 x64
3.	Initial deployment includes 17GB of Storage.  You can grow storage on-demand.
4.	Run the “Hortonworks Install' Script Package

#### What does the HortinWorks Install Script Package do?
1.	Generate ssh key
2.	Disable SELinux
3.	Open up firewall ports
4.	Enable “transparent_hugepage” in kernel
5.	Start NTPD service
6.	Install postgresql client and server.
7.	Add Ambari repo to yum repository
8.	Install Ambari Hortonworks Hadoop Installer
9.	Start Ambari process
10.	Add Ambari ssh key to authorized keys file.

#### Where can I get more information on Hortonworks?
* For more information view [www.Hortonworks.com](http://www.Hortonworks.com)

#### Who should I contact for support?
* CenturyLink Cloud does not support the Hortonworks Hadoop Server software. Please contact Hortonworks for any support around Hortonworks Hadoop.
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing noc@ctl.io or [through the support website](https://t3n.zendesk.com/tickets/new) 
