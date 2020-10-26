{{{
  "title": "Installing ClustrixDB v7.0.1 on CentOS 6",
  "date": "10-26-2015",
  "author": "Jesse Bornfreund",
  "attachments": [],
  "contentIsHTML": false
}}}

![Clustrix Logo](../../images/clustrix_blue.png)

### Technology Profile
Clustrix provides the leading scale-out SQL database engineered for the cloud. It is the first database built specifically to meet the revenue scaling, performance and availability demands of today’s web sites and applications such as those for eCommerce, healthcare and finance. With ClustrixDB, you can build business critical applications that support massive transactional volume and real-time reporting of business performance metrics.


### Description
ClustrixDB is a drop-in replacement for MySQL that provides simplicity of management and scaling using commodity server infrastructure. ClustrixDB offers key features for companies who need an easily managed, easily scaled RDBMS:

* First scale-out relational database designed to meet the elastic scaling requirements of high-volume online transactions needed by e-commerce and other Web applications.
* Architecture that massively scales both reads and writes, while ensuring transaction integrity.
* ACID Compliant.
* Scales linearly with a shared-nothing architecture, automated, intelligent data distribution and distributed query processing.
* “Clustered” database architecture provides automatic redundancy at deployment and assures high-availability of RDBMS across any load with automated fault recovery.
* FLEX licensing model allows deployment of additional database resources for “spikes” due to seasons, promotions or planned heavy loads.
* Code compatible with MySQL, with added benefit that adding servers (and scaling read/write capacity) requires no coding changes to application code.
* ClustrixDB is seen by the application as a single logical database, no matter how many database server nodes are deployed.
* Our patented slicing method delivers performance that is superior to that of sharding and sharding-like approaches, which are costly to manage and fragile.
* Can be deployed across geography with asynchronous replication, using MySQL replication protocol.
* Self-managing, eliminates many DBA operations tasks, significantly reducing the cost of ownership and allowing engineers to focus on innovation.
* Realtime reporting and dashboards allow developers and DBAs to quickly gauge the health of the database and workload.

Current Release is v 7.0.1 (6/15/2015)

For more information, please visit www.clustrix.com.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should understand what ClustrixDB does, how to deploy it, and how to contact Clustrix to get more information or product license/keys for evaluation and production.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.
* A Clustrix Evaluation or Production License key -- You can email us at clcsales@clustrix.com to request an evaluation license key.
* Adequate CLC infrastructure will be deployed for evaluation or typical production as part of the ClustrixDB Blueprint execution.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
* The blue print will configure a public IP address.
* The default ports to access the application are: `22`, `80`, `3306`.

### Deploying the “Install ClustrixDB v-7-0-1" Blueprint

#### Steps to Deploy Blueprint
1. Locate the “Install ClustrixDB v-7-0-1" Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Clustrix” in the keyword search on the right side of the page.
   * Locate the "ClustrixDB v-7-0-1" Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "Install ClustrixDB v-7-0-1" Blueprint.

3. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * On the first Deploy page you will be able to setup the Password, Group, Network, DNS and Server Names to match your requirements.
   * You need to set the Server Type to provision local SSD storage.
   * Once you've completed the required modifications push the `next` button to review your settings.
   * Now click the `deploy blueprint` button again to begin deployment.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.

4. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your ClustrixDB cluster
After your Blueprint deploys successfully, please follow these instructions to access your server:

1. Deploy or Identify an Existing Server.
   * Connect by browser to the public IP of one of the ClustrixDB nodes and complete the ClustrixDB wizard to setup your cluster.
   * You'll need the private IP's of all the nodes as well as your ClustrixDB license key to complete the wizard.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. CenturyLink Cloud customers must have a separate subscription and license and license key from Clustrix to use the ClustrixDB software after deployed. For more information on pricing and licensing, please contact Clustrix @ +1 877.806.5357 or +1 415.501.9560 or at [clcsales@clustrix.com](mailto:clcsales@clustrix.com).

### About Clustrix
CenturyLink Cloud works with [[Clustrix](http://www.clustrix.com)] who provides the leading scale-out SQL database engineered for the cloud and the first database built specifically to meet the unique growth, performance and availability demands of today’s transactional web sites and web applications. With ClustrixDB, you can build business critical applications that support massive transactional volume and real-time reporting of business performance metrics.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Clustrix Blueprint on CenturyLink Cloud, licensing or accessing the deployed software, please visit the [Clustrix website](http://docs.clustrix.com) or by emailing [clcsales@clustrix.com](mailto:clcsales@clustrix.com).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
