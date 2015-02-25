{{{
  "title": "Getting Started with Alfresco - Blueprint",
  "date": "2-24-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](http://www.alfresco.com/sites/www/themes/alfrescodotcom/img/logo.svg)

###Technology Profile

Alfresco was founded in 2005 by John Newton who, many years earlier, cofounded Documentum, one of the pioneers of document management. Alfresco Community is an enterprise-ready, Java-based platform used for document management, records management, image management and more. Features include versioning, Lucene-powered search, federated servers, clustering, roles-based permissions and more. You’ll be in good company with Alfresco; other users include NASA, KLM, Merck and Ricoh.

### Description

Alfresco Community Edition provides a standards-compliant content repository. It includes granular access control, support for social networks, and an embedded workflow engine that integrates with business processes. federated servers, clustering, roles-based permissions and support for mobile clients. Other features (only available in the Enterprise Edition) include an integrated administration console, storage policies, clustering and additional database support.

Alfresco Community is an enterprise-ready, Java-based platform used for document management, records management, image management and more. Features include versioning, Lucene-powered search, federated servers, clustering, roles-based permissions and more.

For more information, please view http://www.alfresco.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Bitnami Blueprint technology on CenturyLink Cloud.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Existing Linux x64 server (and access) to install the Blueprint on

### Postrequisite

- Adding an external ip-address to an existing or new CenturyLink server
![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

- Allow incoming Alfresco traffic for ports to an existing server
![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)

- View this Alfresco wiki page for common port numbers: https://wiki.alfresco.com/wiki/Port_numbers

### Install Bitnami Alfresco Community on Linux Blueprint
1. Locate the Bitnami Alfresco Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Alfresco” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami Alfresco Community on Linux 64bit' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami Alfresco Community on Linux 64bit” blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: a Linux 64bit server to deploy the Blueprint on.
  2. Base User Real Name, e.g. John Doe
  3. Base User Email Address, e.g. john@doe.com
  4. Base User Account Name, e.g. admin
  5. Base Users Password
  6. Apache Web Server Port, e.g. 80
  7. SSL Web Service Port, e.g. 443
  8. Web Server Domain, e.g. 127.0.0.1 or whatever.com
  9. MySQL Server Port, e.g. 3306
  10. MySQL root password
  11. MySQL Database Name, e.g. alfresco
  12. MySQL Database Username, e.g. admin
  13. MySQL Database User Password
  14. Alfresco Admin Password, e.g. admin
  15. JDBC Database Name, e.g. alfrescodatabase
  16. JDBC Database Username, e.g. admin
  17. JDBC Database User Password
  18. Start Alfresco Community after install, e.g. Yes


4. Review and Confirm the Blueprint.
  1. Click “next: step 2”
  2. Verify your configuration details.

5. Deploy the Blueprint.
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.


### Access your Alfresco Community server
After your Blueprint deploys successfully, please follow these instructions to access your server:
  1. Check email to obtain Server Name and IP Address Login information
  2. Log in to the server via ssh and start having fun!


### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with Bitnami to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the Bitnami Support website: http://www.bitnami.com/support
* For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
