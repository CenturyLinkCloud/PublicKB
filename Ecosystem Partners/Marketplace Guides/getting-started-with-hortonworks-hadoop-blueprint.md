{{{
"title": "Getting started with Hortonworks Hadoop - Blueprint",
"date": "04-30-2015",
"author": "Jeff Demuth and Bob Stolzberg",
"attachments": [],
"contentIsHTML": false
}}}

![Hortonworks Hadoop logo](../../images/hortonworks-logo.png)

### Technology Profile
Apache Hadoop® is an open source framework for distributed storage and processing of large sets of data on commodity hardware. Hadoop enables businesses to quickly gain insight from massive amounts of structured and unstructured data.

### Description
Lumen has created a Blueprint that makes it extremely easy to spin up a Hortonworks Hadoop Server in minutes. You can start using your Hortonworks Hadoop server immediately after the Blueprint completes. The Blueprint will automatically install all required packages and settings required for Hortonworks.

Advantages of running Hortonworks in Lumen Cloud:
* Fast provisioning - get Hadoop running within minutes- No long term server commitment - pay as you go each month.
* On-demand Scalability - Add more CPU, Disk or Memory resources on the fly as your data grows.
* Save money - Run your Hadoop server only when you use it. You can host a server just during business hours and power it off during nights and weekends. You can use the Lumen Cloud mobile app to start and stop your server anytime, anywhere.
* Fast Bandwidth - Your Hadoop server has a 2GB inbound network throughput ensuring low latency data transfers.
* No technical experience required - Don't worry about setting kernel variables and preloading database and software packages, we did that for you. Just run the Blueprint, enter some basic configuration details and start importing data.

### Audience
Lumen Cloud Users, Data Scientists and Big Data Enthusiasts.

### Impact
After reading this article, the user should feel comfortable getting Hortonworks Hadoop up and running with Server Blueprint technology on Lumen Cloud.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.

### Postrequisite
* If you want to access your VM with Hortonworks Hadoop over the internet, please perform the following tasks once you receive an email confirming you Blueprint completed successfully.

* If you need to connect to your server via the Internet, Add a [Public IP](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal. Alternatively, you can [setup a VPN using OpenVPN](../../Network/Lumen Cloud/how-to-configure-client-vpn.md) or similar technology.

* [Allow incoming traffic](../../Network/Lumen Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal. Hortonworks listens on port `8080`.

#### Steps to Deploy Blueprint
1. Locate the Hortonworks Install Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Hortonworks” in the keyword search on the right side of the page.
   * Locate the 'Install Hortonworks on RHEL6' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the “Install Hortonworks on RHEL6” Blueprint.

3.	Configure the Blueprint.
    * Use the standard information. There is nothing special required.

4.	Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click on the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the Hortonworks Server until you have received this email notification.

### Accessing your Hortonworks Hadoop Server
After your Blueprint deploys successfully, please follow these instructions to access your server.

#### Steps
1. Check your email to obtain Server Name and IP Address Login information.

2. Click on the link to the server and then add a firewall port as referenced in the post requisite section.

3. Open a Web browser and navigate to your servers IP using port `8080`.
   * This should look like the following URL `http://<your-ip-here>:8080`.
   * Login as the user admin with password admin to customize your Hadoop server.
   * Once logged in click on “Launch Install Wizard”.
   * Type in your preferred cluster name in the “Cluster Name” Field. Click next.
   * Select “HDP 2.1” and click next.
   * Type in “localhost” in the field “Target Hosts”.

4. For this next section we will need the RSA private key from the server. SSH to the server and copy the text from the command `cat /root/.ssh/id_dsa` and paste it into the `Host Registration Information` field.

5. Click OK to confirm localhost as the FQDN.

6. Click next after host registration.

7. You may receive a firewall notice just click ok to accept.

8. Click next to confirm desired services.

9. Click next to confirm master assignments.

10.	Click next to confirm slave assignments.

11.	Click on the Nagios tab, enter in your preferred Nagios password and preferred Email address.

12.	Click on the Hive tab, enter in your preferred Hive password.

13.	Click on the Oozie tab and enter in your preferred oozie password.

14.	Click on the Falcon tab.
   * for `.falcon.graph.blueprints.graph` enter `com.thinkaurelius.titan.core.TitanFactory`.
   * for `.falcon.graph.storage.backend` field enter `berkeleyje`.

15.	Scroll to the bottom of the page and click Next.

16.	Click Deploy.

17.	After configuration is complete hit Next.

18.	On Summary page click Complete.

19.	You will then be redirected to the Hortworks Dashboard: http://your-ip:8080/#/main/dashboard/metrics

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Hortonworks Hadoop license costs or additional fees bundled in.

### Frequently Asked Questions

#### What does the Blueprint do?
* Provision a VM with 2CPU and 4GB of RAM.
* Install RedHat Enterprise Linux 6 x64.
* Initial deployment includes 17GB of Storage. You can grow storage on-demand.
* Run the “Hortonworks Install' Script Package.

#### What does the HortinWorks Install Script Package do?
* Generate ssh key.
* Disable SELinux.
* Open up firewall ports.
* Enable “transparent_hugepage” in kernel.
* Start NTPD service.
* Install postgresql client and server.
* Add Ambari repo to yum repository.
* Install Ambari Hortonworks Hadoop Installer.
* Start Ambari process.
* Add Ambari ssh key to authorized keys file.

#### Where can I get more information on Hortonworks?
* For more information visit [Hortonworks](http://www.Hortonworks.com).

#### Who should I contact for support?
* Lumen Cloud does not support the Hortonworks Hadoop Server software. Please contact Hortonworks for any support around Hortonworks Hadoop.
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint, please open a Lumen Cloud Support ticket by emailing help@ctl.io or [through the support website](https://t3n.zendesk.com/tickets/new).
