{{{
  "title": "Demo Account Setup for Partners",
  "date": "2-11-2015",
  "author": "",
  "attachments": [],
  "contentIsHTML": false
}}}


### Overview

This Document explains how to setup a Demo Account in CenturyLink Cloud. It also gives step-by-step process for how to setup a Demo Account. Partners can use this account to perform demonstrations of CenturyLink Cloud for their customers.  

###Demo Account Setup for Partners on CenturyLink Cloud

The setup process for creating a demo account takes about 2 hours. 

1. Create a Hyperscale Anti-Affinity Policy (just the policy):  https://t3n.zendesk.com/entries/40070050-CenturyLink-Cloud-Anti-Affinity-Policies
2. Rename the network that the OpenVPN services are deployed to OpenVPN Services xx.xx.xxx.x/24 (vlan address required)
3. Add up to 4 Additional Networks (customers can use less if they choose):  https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs
4. Create 8 Virtual Instances in VA1, UC1, CA3 or GB3 as follows.  Use Groups to organize the VM’s and place them in the appropriate networks defined in step #3
  1. 1 x (Standard) Windows 2012 Domain Controller (Production Infrastructure Group)
  2. 1 x (Standard) Windows 2012 File Server (Production Infrastructure Group)
  3. 1 x (Standard) Windows 2012 SQL Server (Production Database Group)
  4. 3 x (Hyperscale) Windows 2012 IIS Web Servers (Production Web Servers Group), place Hyperscale VM’s in the policy created on step #1
  5. 1 x (Standard) Windows 2012 IIS Web Server (Development Group)
  6. 1 x (Standard) Windows 2012 SQL Server (Development Group)
  The most efficient way to do this is by using blueprints: https://t3n.zendesk.com/forums/20199443-Blueprints

  Alternatively, you can create server 1 by 1: https://t3n.zendesk.com/entries/22603877-Creating-a-New-Enterprise-Cloud-Server

  I try to layer Active Directory, IIS, SQL, File etc via the blueprint.  Sample blueprints can be seen @ https://t3n.zendesk.com/entries/31749940-Building-Blueprints-To-Install-Windows-2012-Server-Roles
5. Create Alert Policies for CPU/RAM/Disk and apply them to each of the VM’s build:  https://t3n.zendesk.com/entries/27202824-Cloud-Server-Alerting-FAQ
6. Create a Vertical Autoscale Policy for Development, Production SQL & Production Infra VMs and apply the policy to those VMs:  https://t3n.zendesk.com/entries/22032834-Creating-and-Applying-Autoscale-Policies
7. Configure Firewall <any> rules between production & development environments:  https://t3n.zendesk.com/entries/22196842-Connecting-Data-Center-Networks-Through-Firewall-Policies
8. Configure the (3) Production Web Servers with a default.html file in the IIS root to a live website page is shown.  Code sample:
9. Create a Load Balancer VIP and Pool for the (3) Production Web Servers:  https://t3n.zendesk.com/entries/22110695-Creating-a-Self-Service-Load-Balancing-Configuration
10. Create a horizontal autoscale policy with a minimum of (2) web servers for the Production Web Servers Group and bind it to the Load Balancer VIP:  https://t3n.zendesk.com/entries/22032834-Creating-and-Applying-Autoscale-Policies
11. Create a user and bucket for Object Storage (Ideally place some data in there:
  https://t3n.zendesk.com/forums/20789095-Object-Storage
12. Create a Windows & Linux Blueprint that encompasses scripts, software and server builds to show the value of the engine: https://t3n.zendesk.com/forums/20199443-Blueprints
13. Configure the Development Group to shutdown & Power on the (2) VM’s that Group on a daily basis at 8 PM (shutdown) and 7 AM.
  (Start): https://t3n.zendesk.com/entries/22586501-Creating-a-Schedule TaskPatch all Windows Servers and set them to auto update patches
14. Recommend all Windows VM’s are domain joined and set the domain security policy & local security policies to not expire passwords (in case you need to login to them later)
