{{{
  "title": "Getting Started with Clusterpoint - Blueprint",
  "date": "12-30-2015",
  "author": "Peteris Krisjanis, Clusterpoint support",
  "attachments": [],
  "contentIsHTML": false
}}}



### Technology Profile

<img src="../../images/clusterpoint/clusterpoint-logo.png" style="border:0;float:right;max-width: 150px;">

Clusterpoint is a database, which represents convenience options for data modelling that standard SQL do not offer, like modelling of class hierarchies and composition relationships through JSON or XML document models. At the same time these hierarchical objects are accessible through JS/SQL API, which allows hierarchical objects to be manipulated through a procedural JavaScript extensions. Clusterpoint delivers a robust, ACID-compliant, document-oriented database solution for enterprises and application developers. With hundreds of customers, Clusterpoint offers a proven, stable NoSQL database platform that can support real-time access and analysis of billions of documents. Clusterpoint features rapid database deployment, scalability up to petabytes of data, sub-second database response times, powerful text searches, and much more — all at an attractive price-point.

https://www.clusterpoint.com/


##### Customer Support

|Sales Contact   	| |
|:-	| |
| sales@clusterpoint.com<br>USA 1-650-681-9710<br>Europe +371-6693-8800  	| [Clusterpoint Support chat](https://www.clusterpoint.com/)<br>support@clusterpoint.com<br>&nbsp;|


### Description

* ACID Compliant - Clusterpoint’s patented, ACID compliant transaction processing method allows real-time consistency even in a distributed and highly parallel environment.
* SQL and NoSQL through one API - Clusterpoint’s JS/SQL query language allows computational workloads to be run right next to the data. You can extend common SQL query structure with procedural JavaScript code and access relational and hierarchical data through one API
* OLTP - Enterprises can use Clusterpoint as a business intelligence platform and a fully transactional OLTP database in one solution.
* Indexing - Advanced indexing techniques are optimised for in-memory and on-SSD indices, allowing fast access. Clusterpoint uses a unique feature known as relevance ranking that intelligently sorts data and displays the most relevant results first. It works by ranking and indexing data based on the current query, which reduces the amount of data that needs to be processed and displayed. The end result: much faster queries that provide more relevant answers.
* Real-time analytics - Clusterpoint has the ability to execute arbitrary JavaScript code at any step during query processing, which allows enterprises to build powerful and extensible analytical applications that can run computations alongside the data using indices. This leads to ultra-fast query processing that can rival Hadoop in terms of analytical performance.
* Built in full-text search - Simply type in a keyword, and in milliseconds Clusterpoint’s powerful text-based search displays the most relevant information from your database. Compared to SQL-based queries, Clusterpoint’s text search is dramatically faster!
* Scalability - Clusterpoint’s distributed architecture allows to scale horizontally on commodity hardware and parallelise processing.

For more information, please visit https://www.clusterpoint.com/docs/


### Audience

CenturyLink Cloud Users


### Impact

After reading this article, the user should be able to deploy Clusterpoint blueprint to install all-in-one installation of Clusterpoint manager,
hub and node with web manager.



### Deploying the Clusterpoint All Blueprint

You can achieve a single-button deployment of a new Clusterpoint instance using CenturyLink Cloud Blueprints.  

1. **Locate the Blueprint in the Blueprint Library**

 Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "Clusterpoint" in the keyword search on the right side of the page.

  <img src="../../images/clusterpoint/blueprint_tile.png" style="border:0;max-width:250px;">

2. **Click the Deploy Blueprint button.**

3. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

4. **Review and Confirm the Blueprint**

5. **Deploy the Blueprint**

  Once verified, click on the **deploy blueprint** button. You will see the deployment details stating the Blueprint is queued for execution.

6. **Deployment Complete**

  Once the Blueprint has deployed you will receive an email confirming the newly deployed assets within a few minutes.  If you do not receive
  an email you may have had a deployment error - check the *Blueprints Queue* or review the *Blueprint Build Log* to for error messages.

7. **Access your Clusterpoint server**

  To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks:
  * [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP
    through Control Portal and configuring appropriately.
    * Port to access the Clusterpoint Web Console is TCP 5580. Open it if you want to access Clusterpoint On Premises Web Console to manage
      your Clusterpoint databases and users.
    * Port to access Clusterpoint Hub for API access is TCP 25006. Open it if you want to access Clusterpoint databases from outside your CenturyLink network.

  After your Blueprint deploys successfully, please follow these instructions to access your server:

  * To access Clusterpoint On Premises Web Console use http://public_ip_address:5580/ (default creditentials 'root' and password 'password')
  * To access Clusterpoint server secure shell (SSH) use ssh root@public_ip_address and password you provided during configuring blueprint


### Deploying Clusterpoint to an existing server (alternate option)

You may also deploy Clusterpoint to an existing server that matches your sizing requirments.

1. **Deploy or Identify an Existing Server**
  Identify the server targeted for Clusterpoint installation.  The Operating system must be supported by the Software Package (Red Hat or CentOS 7).  
  The server must be a server within your CenturyLink Cloud account.

2. **Select 'Execute the Package on a Server Group'**

  * Packages can be executed on one more more servers in a Group.  Search for the public software package named **Install Clusterpoint Database (Manager)**.
  * See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for
     more information on how to complete the next few steps.

3. **Deploy the Script Package**

  Once verified, click on the `execute package` button. This will kick off the deployment process and load a page where you can track the progress.
  Deployment will typically complete within a few minutes.

4. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use
    the application until you have received this email notification.

5. **Access your Clusterpoint server**

  To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks:
  * [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP
    through Control Portal and configuring appropriately.
    * Port to access the Clusterpoint Web Console is TCP 5580. Open it if you want to access Clusterpoint On Premises Web Console to manage
      your Clusterpoint databases and users.
    * Port to access Clusterpoint Hub for API access is TCP 25006. Open it if you want to access Clusterpoint databases from outside your CenturyLink network.

  After your Blueprint deploys successfully, please follow these instructions to access your server:

  * To access Clusterpoint On Premises Web Console use http://public_ip_address:5580/ (default creditentials 'root' and password 'password')
  * To access Clusterpoint server secure shell (SSH) use ssh root@public_ip_address and password you provided during configuring blueprint



### Pricing

The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.

CenturyLink Cloud customers must have a separate subscription and license and license key from Clusterpoint to use the Clusterpoint 4.0
software after deployment. For more information on pricing and licensing, please contact  Clusterpoint @  USA 1-650-681-9710  
Europe +371-6693-8800  or at sales@clusterpoint.com.


### About Clusterpoint

CenturyLink Cloud works with [Clusterpoint](https://www.clusterpoint.com/) to provide ACID compliant, document oriented database built for Cloud. Clusterpoint deals with both - structured and unstructured data through one API. There is a minimal learning curve to start working with Clusterpoint as two major technologies - JavaScript and SQL are used to access and transform the data.


### Frequently Asked Questions

**Who should I contact for support?**

* For issues related to deploying the Clusterpoint Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Clusterpoint Support chat](https://www.clusterpoint.com/) or send an [e-mail](mailto:support@clusterpoint.com).
* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
