{{{
  "title": "Getting Started with Couchbase",
  "date": "02-15-2016",
  "author": "Couchbase, Inc.",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile
Couchbase Server is the world’s **most complete, scalable, and highest performing NoSQL database**. We engineered the product to meet the most demanding enterprise and big data requirements for distributed database performance and scalability.

### Description
Couchbase Server provides highly elastic, available, scalable & real-time big data management system with consistently high performance, flexible global deployment topologies and a set of native SDKs to ease development & deployment of modern applications.   

Couchbase Server comes with a shared nothing, fully scale-out, memory-centric architecture, designed to take full advantage of the speed of memory rather than disk, which all translates into a blazingly fast performance. Couchbase Server is the only NoSQL database that integrates a native caching tier and a document-oriented database, eliminating the need to install and manage a separate cache service.   

Couchbase is also the only big data database that offers a native integrated NoSQL mobile solution [Couchbase Mobile](http://www.couchbase.com/nosql-databases/couchbase-mobile?gclid=COfC4_rG7skCFUaCfgodaEIEnA), including pre-built data synchronization (Couchbase Sync Gateway) and an embedded database (Couchbase Lite), enabling fast and easy development of mobile apps with online/offline data access.

For more information, please visit [Couchbase](http://www.couchbase.com).

### Audience
* Lumen Cloud Users  
* Developers wishing to migrate from Relational Databases to a NoSQL Document Database  

### Impact
After reading this article, users should  be able to start a server running Couchbase Server, create a Couchbase Server cluster, connect to that server using an IP address and start accessing Couchbase Server cluster in their application.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.
* An Couchbase Server Enterprise license from Couchbase Inc. See Enterprise Subscription [License Agreement](http://www.couchbase.com/agreement/subscription) for details.

### Postrequisite
After you successfully install a Blueprint, you will receive a notification email. If you want to access your application from a computer that is outside of the Lumen Cloud network, you need to perform the following steps:
* [Add a Public IP](https://../../Network/network/how-to-add-public-ip-to-virtual-machine/) to your server through the Lumen the Control Portal.
* Click on the Servers Public IP through the Control Portal and configure the ports. The default port for Couchbase Server is 8091. For the additional available network ports, refer to the Couchbase Server [documentation](http://developer.couchbase.com/documentation/server/4.1/install/install-ports.html).

### Deploying the Couchbase Server Blueprint

#### Steps to Deploy Blueprint
1. Locate the Couchbase Server Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Use the keyword search on the right to select among multiple blueprints. In our case, choose from the available displayed blueprint thumbnails.            

2. Choose the Blueprint.  
   * Click on **Install Couchbase Server on CentOS6**.     

3. Deploy the Blueprint.      
   * Click the `deploy blueprint` button.

4. Customize the Blueprint.
   * Password: *password*
   * Confirm the same password: *password*
   * Group: **default**.
   * Network: *network ID*
   * Primary DNS: **Manually Specify**
   * Secondary DNS: **Manually Specify**
   * Server Type: **Standard (default)**.
   * Service Level: choose between **Premium** or **Standard**.
   * **Server Name(s)**. Enter a name, such as **CBNODE**.
   * **Specify Credentials**. To run the task under the default administrative account, leave **NO** for credentials.   
   * Click the `next: step 2` button.

5. Review the Blueprint.             
   * Verify the information.

6. Deploy the Blueprint.    
   * If your information is correct, click the `deploy blueprint` button.   

7. Monitor the Activity Queue.        
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email confirming that the Blueprint build is complete.
   * Do not use the application until you have received this email notification.

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no  license costs or additional fees bundled in. You will need a valid [Enterprise Edition license](http://www.couchbase.com/agreement/subscription) from Couchbase Inc.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to the Couchbase Server Blueprint on Lumen Cloud or Licensing, please visit [Couchbase Support website](http://support.couchbase.com/home).
* For issues related to cloud infrastructure (VMs, network, etc.) or if you experience a problem deploying the Blueprint or Script Package, open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
