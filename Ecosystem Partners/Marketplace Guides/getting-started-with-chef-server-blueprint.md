
{{{
"title": "Getting started with Chef Server - Blueprint",
"date": "3-5-2015",
"author": "Bob Stolzberg and Ken McDowell",
"attachments": [],
"contentIsHTML": false
}}}


<img src="http://s3.amazonaws.com/opscode-corpsite/assets/121/pic-chef-logo.png" style="border:0;float:right;" height="100">

### Description

Chef turns infrastructure into code. With Chef, you can automate how you
build, deploy, and manage your infrastructure. Your infrastructure
becomes as versionable, testable, and repeatable as application code.

Chef relies on reusable definitions known as recipes to automate
infrastructure tasks. Examples of recipes are instructions for
configuring web servers, databases, and load balancers. Together,
recipes describe what your infrastructure consists of and how each part
of your infrastructure should be deployed, configured and managed.

The Chef server acts as a hub for configuration data. The Chef server
stores cookbooks, the policies that are applied to nodes, and metadata
that describes each registered node that is being managed by the
chef-client. Nodes use the chef-client to ask the Chef server for
configuration details, such as recipes, templates, and file
distributions. The chef-client then does as much of the configuration
work as possible on the nodes themselves (and not on the Chef server). A
node can be a physical server, a virtual server or a container instance
located anywhere so long as it can communicate with the Chef Server. The
Chef client periodically polls the Chef server for the latest recipes
and checks to see if the node is in compliance with the policy defined
by these recipes. If the node is out of date, the Chef client runs them
on the node to bring it up to date.  This scalable approach distributes
the configuration effort throughout the organization.

![chef.svg](https://www.chef.io/images/chart-what-is-chef.svg)

### Solution

CenturyLink has integrated Chef Server in to a Blueprint that will
automatically install and configure Chef Standalone Server on Red Hat
Enterprise Linux.  For more information on the infrastructure deployed,
please see the Frequently Asked Questions section below. The CenturyLink
Chef Server Blueprint includes the following options:

- ##### Management Console
Use the web-based management console to control access to objects, such
as nodes and cookbooks, through RBAC. You can also edit and delete
nodes, and reset private keys. Keep up to date with what's happening
during chef client runs across an entire organization or on specific
nodes.

- ##### Chef Replication
With replication, you can use a single Chef server as a central location
for developing policy. Other Chef servers in other geographic areas
periodically poll the primary for any changes. They stay current with
your latest cookbooks, environments, roles and databags. Maintain a
single worldview across multiple locations and ensure consistency across
your network, no matter how many data centers or cloud availability
zones you use in your enterprise.

- ##### Chef Analytics / Reporting
Get visibility into your Chef servers, verify compliance and keep up
with changes, all with the Chef analytics platform. See what's happening
on your Chef server in real time with action logs. Use the information
to enforce compliance with your company's policies. Integrate the data
with your favorite external systems, such as HipChat. Notify the
relevant people or automated tools about changes to the Chef server so
that they can react in real time.

- ##### Push Jobs
Chef push jobs allows jobs to be run against nodes independently of a
chef-client run. A job is an action or a command to be executed against
a subset of nodes; the nodes against which a job is run are determined
by the results of a search query made to the Chef server.

The installation and configuration steps in this Blueprint are based on
this Chef documentation: http://docs.chef.io/server/install_server.html

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting
started using Chef Server on CenturyLink Cloud.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user
- Ability to create DNS Records to support Chef's requirement to use a
Fully Qualified Domain Name

### Postrequisite
- Create a DNS record for your Chef Server so that it has a Fully
Qualified Domain Name and can resolve


### Deploy Chef Server on CenturyLink Cloud
1. Locate the Install Chef Server on Linux Blueprint
  + Starting from the CenturyLink Control Panel, navigate to the
Blueprints Library.
  + Search for “Chef” in the keyword search on the right side of the
page.
  + Locate the 'Install Chef Server on Linux' Blueprint
  + Choose and Deploy the Blueprint
1. Configure the Blueprint with information below:
 + Build Server Details: Root Password & Server Group
 + Network / VLAN to put the server on
 + Set the Primary DNS to use 8.8.8.8
 + Set the Secondary DNS to use 4.2.2.2
 + Service Level = Standard
1. Install Chef Server on linux Details:
  + This Servers Fully Qualified Domain Name, e.g.
chef.projectx.centurylinkcloud.com or chef.domain.com
(NOTE: This is a really important step!  Once the server has been
created and you obtain the Public IP, you will need to create a DNS A
Record so the new Chef server has a Fully Qualified Domain Name and can
resolve a forward DNS lookup requests based on the FQDN you specify
here.)
1. Configure Chef Server on Linux Details:
  + Chef User Name  [Example: chefadmin]
  + Chef User Real Name [Example: Chef Admin]
 + Chef User's Email [Example: chefadmin@chef.io]
 + Chef User's Password
 + Path to save Chef User's Key [Absolute path to save users key to,
Example = /root/chefadmin-key.pem]
  + Organization Short Name [Organization name must be in all lower
case without space. Example = chef]
  + Organization Full Name [Example = Chef Software, Inc.]
  + Path to save Chef Organization Key [Absolute path to save
organization key to, Example = /root/chef-organization-key.pem]
1. Install Chef Features: [Default = Select Everything]
  + Chef Manage
  + Chef Push Jobs
  + Chef Replication
  + Chef Reporting
1. Click the Next: Step 2 button
1. Review and Confirm the Blueprint
  + Verify your configuration details
  + Click “Deploy Blueprint" button
1. Monitor the Activity Queue.
  + Monitor the Deployment Queue to view the progress of the blueprint.
  + You can access the queue at any time by clicking the Queue link
under the Blueprints menu on the main navigation drop-down.
1. Once the Blueprint completes successfully, you will receive an
email stating that the blueprint build is complete. Please do not login
to the Chef server until you have received this email notification.
1. You can create a DNS record at this point.  You can obtain the
Public IP of the VM from the Blueprint Build Log.  You can also obtain
the Public IP from the Control portal by navigating to the new Chef
server once the server build process is complete.
1. Create a Fully Qualified Domain Name for your Chef server:
  + Create a DNS record for your Chef Server so that it has a Fully
Qualified Domain Name and can resolve with a forward lookup, e.g.
nslookup chef.domain.com.  If you don't have a domain or can't manage
DNS for your existing domain, you can create DNS zones and records on
CenturyLinkCloud.com through the Control portal.
1. If you have an existing domain and can manage DNS, follow these
instructions to create a FQDN for your Chef server:
  + Create a new A Record and use the information below:
  + Sepcify the Short Name of the server, e.g. chef
  + Specify the Public IP of the CenturyLink Cloud VM
1. If you don't have an existing domain or can't manage DNS for an
existing one, follow these instructions to create a FQDN for your Chef
server on the CenturyLinkCloud.com domain
  +  Click on the DNS link in the Control portal main dropdown
  +  Click the Add New Zone button
  +  Provide the following details:
  + Zone - Provide the full name of the zone you want to use.
Include ".CenturyLinkCloud.com" domain in your Zone name! Example:
projectx.CenturyLinkCloud.com
  + TTL - Select the dropdown and adjust your TTL. Example = 1 Day
  + Email - Your Email Address
  + Click OK Button when complete
  + Click on the zone you would like to create the Chef server entries
under
  + Click the Add Record button
  + On the New Record window that pops up, provide the following
details:
  + Type - Select A
  + Name - Provide a short name for your server.  This short name will
precede the Zone. Example: chef  (In this example, the FQDN will now
resolve as chef.projectx.centurylinkcloud.com)
  + Address - Provide the Public IP address of your Chef Server.  You
can obtain the Public IP address from the Control portal by navigating
to the Chef server.



### Access your CenturyLink Cloud Chef Server
After your Blueprint deploys successfully, please follow these
instructions to access your Chef Server:

1. Check email to obtain Chef server information and click on the link
to view the new server's details
2. Obtain your Chef Servers Public IP address by viewing the server in
the Control portal
3. To configure Chef, connect to the Chef server via web browser by
browsing to the FQDN or Public IP address, Examples:
https://chef.projectx.centurylinkcloud.com or https://PUBLICIP
4. Login to the Chef Web Portal using the Chef User Name and Chef
User's Password credentials specified when the Blueprint was deployed
5. To login to the Linux server, connect via SSH and login as root
(NOTE: Port 22/ssh is accessible over the internet)
5. Have fun using your Chef Server on CenturyLink Cloud!


### Troubleshooting
Below are some common issues

- FQDN: The Chef Server requires a fully resolvable FQDN.  The Chef
Server needs to use a FQDN hostname that can resolve a forward lookup
DNS request.  In order to resolve a forward lookup request, a DNS A
record must be in place. The A record needs to contain the Public IP of
the server.
- If you create your DNS record after your Chef server is provisioned
and the software install completes, reboot your Chef server so the
numerous daemons don't have any issues.


### Pricing
The costs associated with this Blueprint deployment are for the
CenturyLink Cloud infrastructure only.  There are no Chef Enterprise
license costs or additional fees bundled in, unless you need to manage
more than 25 nodes and in that case you will need to contact Chef.  Additional charges for outbound internet bandwidth may be applicapble if nodes external to CenturyLink Cloud are connected to your CenturyLink Chef Server.


### Frequently Asked Questions

#### How much CPU and Memory does the Chef Server Blueprint contain?
Based on Chef Server best practices, the CenturyLink Chef Server
Blueprint will provision VM with 4CPU's and 8GB of Memory and an
additional 100GB storage dedicated for Chef data

#### What version of Chef Server is installed?
Chef Server (Standalone) version 12.0.5-1.el6

#### What Platform is the Chef Server installed on?
Red Hat Enterprise Linux 6 64bit OS

#### What Firewall Ports have been opened for the Public IP?
The following ports have been opened on the Public IP:  22, 80, 443

#### What customizations have been made?
- The Installation Script will bring the RHEL6 OS up to date by running
yum update
- The 100GB storage for Chef data is automatically mounted
to /var/opt/opscode/drbd/data
- The Installation Script will create a new /etc/hosts and include the
FQDN specified during Blueprint deployment
- The Installation Script will set the servers hostname to the FQDN
specified during Blueprint deployment by modifying /etc/sysconfig/network


#### Who should I contact for support?
- For issues related to Chef Server, Licensing or Using the Chef
software, please visit the Chef Support Website: http://docs.chef.io
- For issues related to cloud infrastructure (VM’s, network, etc) or if
you experience errors during Blueprint deployment, please open a ticket
using the CenturyLink Cloud Support Process.
