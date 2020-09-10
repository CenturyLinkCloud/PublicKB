{{{
  "title": "RackWare Management Module v5",
  "date": "03-28-2016",
  "author": "Todd A. Matters",
  "attachments": [],
  "contentIsHTML": false
}}}

![Rackware Logo](../../images/rackware-logo.jpeg)

### Technology Profile
RackWare provides a software management suite for cloud called RackWare Management Module (RMM). The RMM solution is Enterprise focused, making cloud computing viable and economical for Enterprises. While Enterprise focused, handling large complex applications, RackWare is also applicable to a wide variety of other computing environments including SMB and test dev. The RMM solution enables Enterprises to implement 4 major use cases: workload mobility, backup, disaster recovery, and AutoScaling. The underpinning technology is a patented any to any replication engine that includes physical servers on both origin and target, is hypervisor and cloud agnostic. The use cases and replication confluence spans data centers, private, and public clouds.

### Description
The latest features in the RMM include:
Discover and Analysis
Image replication
	Physical servers (as origin and target)
	All major hypervisors (across disparate hypervisors)
	Cloud agnostic
	All major databases
	Custom applications
	Tiered applications
	Enterprise class applications
Backup with multiple recovery points
Disaster Recovery
	Aggressive RPO and RTO
	Dynamic provisioning (provision compute only on failover)
	Pre-provisioned (optimize RTO)
	Test mode
	Entirely automated failover and fallback

For more information, please visit www.rackwareinc.com.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be understand the use cases for the RackWare RMM and to provision and install the RMM software.

### Prerequisite
IP level network connectivity is required from the RMM Server to the Origin workloads. Additional information regarding prerequisites can be found in the RMM v5 Prerequisites and Operational Requirements document.

### Postrequisite
If using the RMM to migrate workloads to the CenturyLink cloud, the RMM Server can be decommissioned after the replications are complete.

If using the RMM to for Disaster Recovery, the DR configuration and operation can be monitored by configuring email alerts in the DR Policy. Consult the RackWare v5 Disaster Recovery Guide for more information.

### Deploying the Rackware Blueprint
#### Steps to Deploy Blueprint
1. Locate the "Install RackWare RMM on Linux" Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for 'RackWare RMM' in the keyword search on the right side of the page.
   * Locate the 'Install RackWare RMM on Linux' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the 'Install RackWare RMM on Linux' Blueprint.

3. Customize the Blueprint.
   Provide the input global Blueprint values.
   * Customer name
   * License Type (proc/prod)
   * Functional License Type (DR, Migration)
   * Number of licenses
   * Customer email ID
   * RMM installer web link
   * Provide build server password and other network details to access server after deployment.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy the RMM to an existing server (alternate option)  
The RMM is available as a Script Package for deployment on a newly provisioned server or an existing server based on your own sizing requirements.

####Deploy or Identify an Existing Server  
Identify the server targeted for RMM installation. The Operating system must be supported by the Script Package. The server must be a server within your CenturyLink Cloud account.

Installation set up for RackWare is comprised of a dedicated server (physical or virtual) running the RMM. The RMM server requirements are as follows:
* x86_64 architecture (Intel or AMD)
* RHEL / CentOS v6 (6.5 or higher)
* 10 GB or more of storage on /opt/
* 5 GB or more storage on /srv/   
* 5 GB or more of storage on /tmp
* 16 GB memory
* 4 cores (vCPU)
* Additional storage on /srv/ sufficient to hold captured Images

The RMM installation requires the following additional configuration:
* Working yum manager with EPEL package
* SELinux is disabled
* Name resolution must be configured and working.
* Access to the Internet for additional packages
* Install as root

If mount points are set up for /opt, /srv, or /tmp, be sure to set up those mount points in the /etc/fstab file.

The following ports are required to the Internet: TCP port `443`.

*** These requirements are necessary only during the installation. After a successful installation, these requirements do not apply for normal RMM operation.

After installing RHEL/CentOS, ensure that the kernel, packages, and state information is consistent with the repository by executing “yum update kernel”.

A general "yum update" should be executed as long as the kernel update is included.

After executing the ‘yum update’ or ‘yum update kernel’ command, you must reboot the server.

If using RHEL without a subscription, a DVD should be configured as the repo.

####Execute the RMM Pre-installation script**
Download and execute the "rackware-pre-installation_v1.1.sh" script on the RMM Server.

This script must be executed from root or with sudo with root permissions.  It will generate a file called:
rackware-pre-install-output-(date-time)

This file must be emailed to licensing@rackwareinc.com. RackWare will generate a license file called:
rackware-license-(date-time)

Where the (date-time) is the original date-time in the original rackware-pre-install-output-(date-time).

Next, create the directory /etc/rackware, and copy the rackware-license-(date-time) to /etc/rackware/.

####Execute the Installation Script
From root user, execute:
     ./rackware-(VERSION)-x86_64.sh

Read and accept the EULA and the Microsoft licenses by entering "yes".

Answer the prompts.

There will be a series of prompts. Accept the default values for all Yes/No questions, as well as for questions related to the VPN subnet, the GUI type, unless instructed otherwise by RackWare.

Select the network interfaces the RMM will use to interface with Client Hosts. In general, select all available interfaces. If using the Image mobility features (migrations and DR) see the section Image Mobility Requirements.

####Verify the RMM Installation
A couple of commands will ensure that the software is installed correctly.

This series of tests will:
* Verify that the RMM is running.
* Query general information about the RMM.

Verify the RMM is running correctly.
   Execute: "$ rwadm status all"

*** Note that rwadm commands should be run from root.

The expected output is:

Dependent services:

 - running: httpd[(process id)]
 - running: dhcpd[(process id)] (may not be running)
 - running: xinetd[(process id)] (may not be running)
 - running: ietd[(process id)]
 - running: proftpd[(process id)]
 - running: syslog-ng[(process id)]
 - running: rmm[(process id)]
 - running: sshd[(process id)]

Services dhcp and xinetd are not required for the RMM to run, and will not be running unless configured otherwise.

Query the RMM.
   Execute "$ rw rmm show"

This will display general information about the RMM.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. RackWare licensing information can be obtained by email info@rackwareinc.com.

### About RackWare
CenturyLink Cloud works with [RackWare](http://www.rackwareinc.com) to provide a software management suite for cloud called RackWare Management Module (RMM). The RMM solution enables Enterprises to implement 4 major use cases: workload mobility, backup, disaster recovery, and AutoScaling.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the RackWare Management Module (RMM) Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please contact RackWare at:

support@rackwareinc.com
1 844-797-8776

* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
