{{{
  "title": "Installing Clusterpoint all-in-one on RedHat Enterprise Linux 7/CentOS 7",
  "date": "12-22-2015",
  "author": "Peteris Krisjanis, Clusterpoint support",
  "attachments": [],
  "contentIsHTML": false
}}}

![Clusterpoint Logo](../../images/clusterpoint-logo.png)

### Technology Profile

Clusterpoint is a database, which represents convenience options for data modeling that standard SQL do not offer, like modeling of class hierarchies and composition relationships through JSON or XML document models. At the same time these hierarchical objects are accessible through JS/SQL API, which allows hierarchical objects to be manipulated through a procedural JavaScript extensions. Clusterpoint delivers a robust, ACID-compliant, document-oriented database solution for enterprises and application developers. With hundreds of customers, Clusterpoint offers a proven, stable NoSQL database platform that can support real-time access and analysis of billions of documents. Clusterpoint features rapid database deployment, scalability up to petabytes of data, sub-second database response times, powerful text searches, and much more — all at an attractive price-point.

### Description
ACID Compliant - Clusterpoint’s patented, ACID compliant transaction processing method allows real-time consistency even in a distributed and highly parallel environment.
* SQL and NoSQL through one API - Clusterpoint’s JS/SQL query language allows computational workloads to be run right next to the data. You can extend common SQL query structure with procedural JavaScript code and access relational and hierarchical data through one API.
* OLTP - Enterprises can use Clusterpoint as a business intelligence platform and a fully transactional OLTP database in one solution.
* Indexing - Advanced indexing techniques are optimized for in-memory and on-SSD indices, allowing fast access. Clusterpoint uses a unique feature known as relevance ranking that intelligently sorts data and displays the most relevant results first. It works by ranking and indexing data based on the current query, which reduces the amount of data that needs to be processed and displayed. The end result: much faster queries that provide more relevant answers.
* Real-time analytics - Clusterpoint has the ability to execute arbitrary JavaScript code at any step during query processing, which allows enterprises to build powerful and extensible analytical applications that can run computations alongside the data using indices. This leads to ultra-fast query processing that can rival Hadoop in terms of analytical performance.
* Built in full-text search - Simply type in a keyword, and in milliseconds Clusterpoint’s powerful text-based search displays the most relevant information from your database. Compared to SQL-based queries, Clusterpoint’s text search is dramatically faster!
Scalability - Clusterpoint’s distributed architecture allows to scale horizontally on commodity hardware and parallelise processing.

For more information, please visit https://www.clusterpoint.com/docs/.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to deploy Clusterpoint Blueprint to install all-in-one installation of Clusterpoint manager, hub and node with web manager, and separate installation of additional Clusterpoint node/hub for your database cloud.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
* [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
* Port to access the Clusterpoint Web Console is TCP 5580. Open it if you want to access Clusterpoint On Premises Web Console to manage your Clusterpoint databases and users, and use REST API interface to access Clusterpoint databases.
* Port to access Clusterpoint Hub for API access is TCP 25007. Open it if you want to access Clusterpoint databases trough TCP from outside your CenturyLink network.
* All additional nodes speak to core server with manager trough local IP. However, if you want to get additional hub access for TCP connections you need to assign public IP and open port TCP 25007 for additional node/hub machines as well.

### Deploying the Clusterpoint All Blueprint (to install core structure for your database cloud with manager, hub, and node)

#### Steps to Deploy Blueprint
1. Locate the Clusterpoint All Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Clusterpoint” in the keyword search on the right side of the page.
   * Locate the 'Clusterpoint All' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "Clusterpoint All" Blueprint.

3. Customize the Blueprint.
   * Provide root password for server.
   * Enter your root password in field 'Password'. Follow indications how strong your password is, add numbers or special characters to make it stronger if required.
   * Enter root password again in field 'Confirm Password'. Follow indications that password entered in both field matches.
   * Customize server name. You can provide customized server name in 'Server Name(s)' section, if desired.

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

### Deploying the Clusterpoint Node Blueprint (for adding new node to your database cloud)

#### Steps to Deploy Blueprint
1. Locate the Clusterpoint Node Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Clusterpoint” in the keyword search on the right side of the page.
   * Locate the 'Clusterpoint Node' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "Clusterpoint Node" Blueprint.

3. Customize the Blueprint.
   * Provide root password for server.
     * Enter your root password in field 'Password'. Follow indications how strong your password is, add numbers or special characters to make it stronger if required.
     * Enter root password again in field 'Confirm Password'. Follow indications that password entered in both field matches.
   * Provide Your Clusterpoint Manager local IP.
     * Locate "Install Clusterpoint Database (Node and Hub)" section.
     * Provide your Clusterpoint Manager's local IP in field 'ManagerHost'. Be sure it's valid IP or hostname, otherwise node and hub services will fail to start.
   * Customize server name.
     * You can provide customized server name in 'Server Name(s)' section, if desired.

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

### Deploy Clusterpoint All or Clusterpoint Node to an existing server (alternate option)
Clusterpoint is available as a Software Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps
1. Deploy or Identify an Existing Server.
   * Identify the server targeted for Clusterpoint installation.
   * The Operating system must be supported by the Software Package. The server must be a server within your CenturyLink Cloud account.

2. Select 'Execute the Package on a Server Group'.
   * Packages can be executed on one more more servers in a Group.
   * Search for the public software package named **Install Clusterpoint Database (Manager)** or **Install Clusterpoint Database (Node and Hub)** accordingly what you want to install.
   * See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. Deploy the Script Package.
   * Once verified, click the `execute package` button.
   * This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

4. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your Clusterpoint Databse cloud
After your Blueprint deploys successfully, please follow these instructions to access your database cloud:
* To access Clusterpoint On Premises Web Console use server IP where you installed 'Clusterpoint All' Blueprint with manager http://manager_public_ip_address:5580/ (default creditentials 'root' and password 'password'). It is highly recommended to change root password right after you log in for first time.
* To access Clusterpoint REST API use http://manager_public_ip_address:5580/v4/.
* To access any of Clusterpoint servers trough secure shell (SSH) use ssh root@public_ip_address and password you provided during configuring Blueprint.
* You can verify hubs and nodes installed trough 'Clusterpoint Node' Blueprint and connected to your database cloud via On Premises Web Console logging in as administrator with user 'root' and then accessing 'Hubs' and 'Nodes' sections of interface at the top of the interface (last two icons in menu at left).

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. CenturyLink Cloud customers must have a separate subscription and license and license key from Clusterpoint to use the Clusterpoint 4.0 software after deployed. For more information on pricing and licensing, please contact  Clusterpoint @ USA 1-650-681-9710  Europe +371-6693-8800 or at sales@clusterpoint.com

### About Clusterpoint
CenturyLink Cloud works with [Clusterpoint] (https://www.clusterpoint.com/) to provide ACID compliant, document oriented database built for Cloud. Clusterpoint deals with both - structured and unstructured data through one API. There is a minimal learning curve to start working with Clusterpoint as two major technologies - JavaScript and SQL are used to access and transform the data.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Clusterpoint Blueprint on CenturyLink Cloud, licensing or accessing the deployed software, please visit the [Clusterpoint] Support chat (https://www.clusterpoint.com/) or send an [e-mail](mailto:support@clusterpoint.com).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
