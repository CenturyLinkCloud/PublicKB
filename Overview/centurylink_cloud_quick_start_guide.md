---
title: CenturyLink Cloud Quick Start Guide
author: Joe Smith
preview: This is a preview of the article
tags:
  - four
  - five
date: 7-10-2014
---

#CenturyLink Cloud Quick Start Guide
This document describes how to utilize the basic functions of the CenturyLink Cloud (CLC).

**This document include an overview of the Control Portal as well as instructions on how to:**
* Deploy Windows and Linux-based servers
* Manage servers
* Connect existing systems to CenturyLink Cloud
* Manage users within the Control Portal

**Overview of the Control Portal**

The Control Portal ([https://control.tier3.com](https://control.tier3.com)) is a web-based graphical interface for managing CenturyLink Cloud
(CLC) services. Once you login, your account’s Dashboard page will be displayed – which includes:

* A billing summary
* List of available CLC data centers and any of your corresponding resource metrics associated to each data
center
* Network bandwidth utilization
* List of Upcoming Events your organization has pending (e.g., server reboot scheduling)
* An activity log of recent actions completed within your account on the platform
Scrolling back to the top of the Dashboard is a black bar that contains (from left to right):
* Your user ID’s Profile page. NOTE: If you should ever contact our NOC they will ask you to verify your
identity by providing your unique PIN number that is listed within the Profile this page
* The “?” will display options to: search are very extensive knowledge base articles, email our NOC, submit
a feature request, and/or chat with our NOC
* The search window provides customers the ability to search for virtual machines and/or associated
metadata about systems provisioned within your account.

Beneath the black bar you will see a green bar, and hovering your mouse over this bar will display following services:
￼￼{EMBEDDED IMAGES}
* **Servers.** Provision and manage virtual machines (VMs). Create alerts, autoscale policies, and anti-affinity pools.
* **Blueprints.** Create, edit, and run Blueprints, CenturyLink Cloud’s orchestration engine. Blueprints allow users to combine virtual machine configurations, infrastructure tasks, scripts, and software packages into environments that can then be quickly deployed. Simple and complex applications alike can be deployed with the click of a button after the Blueprint is created.
* **Network.** Access the platform’s self-service networking capabilities, including:
	* Manage VLANs configured for your account
	* Manage assigned private/RFC1918 and/or public address space
	* Managed firewalls within a data center, and between data centers
	* VPN – view VPN configurations, and install OpenVPN clients for desktop/laptop connectivity and
management of point-to-point VPN tunnels
* **Services.** Deploy and manage various services including Object Storage, DNS, site redirect, SMTP relay, Web Fabric, and shared load balancers.
* **Account.** Create and manage account settings for Contacts, Billing, Sub Accounts, Users, Permissions, and API access. Additionally, from the Account drop-down, customers can add credit card or payment information, view invoices, and open support tickets.

**Getting Started**

Below are a series of step-by-step instructions for completing the most common tasks for new customers.

* **Deploying a Windows or Linux Server/Virtual Machine**
	1. Once authenticated within Control Portal, rollover the Servers tab and click on create server.
	2. Select where you’d like to deploy the new virtual machine.
	3. Select the group the server should be a member of – servers will be placed in the “Default Group” if no other group is created beforehand.
	4. Complete the server Name and Description fields.
	5. Choose the appropriate Storage Type (Standard or Premium) for the new virtual machine. The
performance characteristics of VM storage are the same for Standard or Premium (see: [http://help.tier3.com/entries/21819996-Cloud-Server-Instance-Size-and-Performance](http://help.tier3.com/entries/21819996-Cloud-Server-Instance-Size-and-Performance)) – and only differ in backup data retention and DR/BC functionality (see: [http://help.tier3.com/entries/21861680-Tier-3-Backup-and-Recovery-Services](http://help.tier3.com/entries/21861680-Tier-3-Backup-and-Recovery-Services)). Lastly within the dropdown, if you are provisioning a server that has Hyperscale available within a data center you will see as an option to deploy such a system. Hyperscale server are optimized for NoSQL workloads, Hadoop, and other web-scale architectures.
	6. Type in a root/administrator password in the fields provided.
	7. Select the Next button to proceed to Step 2.
	8. Place the Virtual Machine in the appropriate network VLAN.
	9. Utilize the DNS servers listed or change the IPs for specific DNS needs.
	10. Select the desired number of virtual processors and RAM and operating system for the server.
	
		Notes:
		* Please observe the hourly price changes as various resource attributes are
modified. Also, please be advised that organizations can set server/Group resource limits to help manage costs – please see Control Portal Server Administration section below for more details.
		* The hourly Platform fee includes the disk space for the operating system (see: [http://help.tier3.com/entries/21748870-Operating-System-Root-Drive-Size](http://help.tier3.com/entries/21748870-Operating-System-Root-Drive-Size)).
		* If a commercial operating system (e.g., Windows) is selected, the cost of this
OS licenses will be reflected in the hourly rate of the server. Customers who already have their own licensing agreements (e.g., MSFT EA) can contact the NOC to arrange so these fees are not charged to these specific servers.
	11. If additional storage is required beyond the OS template (see notes above), select add storage, disk, type in drive name (Note: In regards to Windows systems type any drive letter than C or D, and for Linux do not use any of the Linux filesystem directories), and then chose the space needed. Select add storage, disk and repeat the aforementioned steps if another drive is required.
	12. SelectthenextbuttontoproceedtoStep3.
	13. The final page provides optional server tasks to be performed during the server provisioning
process. These tasks are performed after the server and its OS is deployed –option include:
		* <u>server task</u> – reboot, add disk, add IP address, snapshot server
		* <u>install software</u> – browse the Platform’s public and private software library and then select which software you wish to have installed. Note: Commercial software license fees may be apply.
		* <u>execute script</u> - browse the Platform’s public and private library of scripts to be performed after the OS is installed.
		* <u>Schedule a server lifespan</u> – schedule the virtual machine to be deleted at a defined period.

	14. Select the Create upon completion
server task – reboot, add disk, add IP address, snapshot server
install software – browse the Platform’s public and private software library and then select which software you wish to have installed. Note: Commercial software license fees may be apply.
execute script - browse the Platform’s public and private library of scripts to be performed after the OS is installed.
Schedule a server lifespan – schedule the virtual machine to be deleted at a defined period.
Server button to initiate the server build. A notification email will be delivered of the build process. Clients can also check the Queue for detailed information
on the build status.

**Managing Servers & Groups** – Once a server is provisioned, customers can manage their server via the Control Portal or directly via Remote Desktop, SSH, etc. The following highlight how this server management can be performed.

* Control Portal Server Administration – All servers deployed on the Platform are placed into “Groups”. The Groups feature allows users to logically group virtual machines by environment type, application, or any other user-specified criteria for easier server management such as:
	* **Administration.** Schedule or perform management tasks (such as stopping and starting, rebooting, or setting to maintenance mode) across all servers in a group or sub-group.
	* **Consistent sizing.** Set default server configurations (e.g. OS version, DNS settings, VLAN) when a new server is provisioned within a group.
	* **Policy enforcement.** Adjust an environment’s footprint as needed by archiving and restoring a group of VMs with all policy and configuration settings intact, or take a group’s snapshot for enhanced disaster recovery capabilities.
	
Once a specific server is selected within a Group, customers can perform basic server administration features such as: viewing the configuration, rebooting, managing IPs, installing software, recover administrator/root password, server monitoring/alerting, schedule maintenance, etc. The steps for viewing these individual server features within the Control Panel are as follows:

* Select Servers (Beta) from the Control Portal menu (hover over the green bar).
* Navigate to the group you deployed your server(s) into (unless otherwise specified, the
server will appear in the “Default Group”)
* Click on the name of the server you provisioned

**Direct Server Administration** – When a server is provisioned on CenturyLink Cloud, this system is placed into a private/RFC1918 network address space VLAN. Unless the server is configured with a public IP address, access to the servers will need to be established via the OpenVPN client, a point-to-point VPN tunnel, and/or dedicated private circuit (see: [http://help.tier3.com/entries/20518933-network-access- options-for-connecting-to-tier-3-s-platform](http://help.tier3.com/entries/20518933-network-access- options-for-connecting-to-tier-3-s-platform) for more information). Additionally, as a security best practice, it is recommended that servers be administered over secure channels (e.g., VPNs, etc). The steps below describe how a Windows client can administer a Windows-based server (Note: Customers who deploy Linux servers on CenturyLink Cloud can also connect directly to their servers with SSH via the aforementioned options) on the CenturyLink Cloud via the OpenVPN client and Remote Desktop Connection.:

1. Within the Control Portal select Network, and then VPN
Page 4
rev. 20140509
2. Select the client’s operating system (currently Windows or Mac are available) and follow the instructions for installing the OpenVPN client (see: [http://help.tier3.com/entries/20914433-how-to-configure-client-vpn](http://help.tier3.com/entries/20914433-how-to-configure-client-vpn))
3. Start the OpenVPN client - for Windows users, make sure to start the application as an administrator by right clicking on the icon – see below:
4. Right click on the OpenVPN client in the Windows Systems Tray, and select Default, and then Connect (Note: OpenVPN authentication is facilitated by the certificate that was installed during the OpenVPN installation performed in Step 3. Hence, no ID or password is required.)
5. Once the OpenVPN has established connectivity, utilize Remote Desktop Connection (RDC, or aka RDP) to directly manage the server(s). Instructions:
	1. Select: Start, Programs, Accessories, and then Remote Desktop Connection
	2. Once the RDC application has started, type in the server’s IP to remote control, and then
Connect. Note, the server’s IP address can be obtained from Servers section of Control
Portal (please see screen shot above)
	3. When prompted, type in Administrator and the password assigned in the steps above
(see the Server configuration page to retrieve the password).
	4. The RDC session should now display the Windows desktop for the server

**Provisioning Additional Administrators to your Account** – For business continuity purposes, it is recommended you have at least two administrators in the CenturyLink Cloud. Administrators can configure access permissions for either Full Control or Read Only. Managing Portal users and permissions is performed by selecting Account from the top menu, then Users.

**For more information regarding the topics discussed in this document please contact the CenturyLink Cloud NOC (noc@tier3.com) and/or your CenturyLink Account Executive.**
