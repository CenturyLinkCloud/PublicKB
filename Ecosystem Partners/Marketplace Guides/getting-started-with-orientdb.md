{{{
  "title": "Installing OrientDB on CentOS 7",
  "date": "12-30-2015",
  "author": "OrientDB LTD",
  "attachments": [],
  "contentIsHTML": false
}}}

![OrientDB-Logo](http://../../images/orientdb-logo.png)

### Technology Profile

OrientDB Community Edition 2.1.8 Multi-Model Database

### Description

OrientDB is a 2nd Generation, Distributed Graph Database with the flexibility of Documents in one product with an Open Source commercial friendly license (Apache 2 license), multi-master replication, sharding, and more flexibility for modern complex use cases.

For more information, please visit http://www.orientdb.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be familiar with launching and using the OrientDB Blueprint.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443
    * Be sure to also allow access to TCP port 2480 (OrientDB Studio).

### Deploying the OrientDB Community Edition Blueprint

#### Steps to Deploy Blueprint
1. **Locate the latest OrientDB Community Edition Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “orientdb” in the keyword search on the right side of the page.
  3. Locate the OrientDB 2-X-X CE Blueprint

2. **Choose and Deploy the Blueprint.**
   Click the "OrientDB 2-X-X CE" Blueprint.

3. **Customize the Blueprint**
  1. **Build Server(s)**
    1. Enter a valid password for the server.
    2. For "Primary DNS" be sure to choose the server's name (specified below).

  2. **Server Name(s)**
    1. Use the default or enter an appropriate name.

  3. **Oracle JDK 1.8-XX**
    1. Be sure to select "YES" under "License Accepted".

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your OrientDB Community Edition server
After your Blueprint deploys successfully, please follow these instructions to access your server:
  1. To login, use SSH and the 'root' user along with the password you specified when creating the server.
  2. Once logged in, to find the OrientDB server password view the '/opt/orientdb/config/orientdb-server-config.xml' file.
  3. To stop your OrientDB server instance, use "systemctl stop orientdb".
  4. To start your OrientDB server instance, use "systemctl start orientdb".


### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no OrientDB LTD license costs or additional fees bundled in.

### About OrientDB LTD
CenturyLink Cloud works with [OrientDB LTD](http://www.orientdb.com) to provide the latest OrientDB Community Edition Multi-Model Database.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the OrientDB LTD Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [OrientDB Support website](http://www.orientdb.com/support)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
