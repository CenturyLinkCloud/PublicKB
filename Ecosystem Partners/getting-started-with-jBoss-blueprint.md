{{{
  "title": "Getting Started with JBoss - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](https://issues.jboss.org/secure/attachmentzip/unzip/12451839/12348941%5B15%5D/images/jboss_logo.png)

### Technology Profile
Bitnami JBoss Stack provides a complete development environment for JBoss that can be deployed in one click. It includes ready-to-run versions of Apache, JBoss, MySQL and Java and required dependencies.

### Description
Through the CenturyLink Blueprint integration, Bitnami JBoss Stack provides a click-through solution to install and configure JBoss on the Linux platform.

For more information, please view http://www.JBoss.org

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Bitnami Blueprint technology on CenturyLink Cloud.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Existing Linux x64 server and login access

### Postrequisite

- If you need to connect to your server via internet, add a Public IP address to your server.  For more information view this link: http://www.centurylinkcloud.com/knowledge-base/network/how-to-add-public-ip-to-virtual-machine/

	![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

- Allow incoming traffic for ports to an existing server by managing Firewall rules.  Fore more information, vie this link: http://www.centurylinkcloud.com/knowledge-base/network/creating-cross-data-center-firewall-policies/

	![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)


### Install Bitnami JBoss on Linux Blueprint
1. Locate the Bitnami JBoss Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “JBoss” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami JBoss on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami JBoss on Linux” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  3. Apache Web Server Port, e.g. 80
  4. SSL Web Service Port, eg. 443
  5. Web Server Domain, e.g. 127.0.0.1 or Example.com
  6. MySQL Server Port, e.g. 3306
  7. MySQL root password
  8. MySQL Database Name, e.g. mysql_db
  9. MySQL Database Username, e.g. mysql_user
  10. MySQL Database User Password
  11. JBoss directory, e.g. /jboss
  12. JBoss HTTP Connector Port, e.g. 8080
  13. HTTPS connector port, e.g. 8443
  14. AJP connector port, e.g. 8009
  15. JBoss Management HTTP port, e.g. 9990
  16. JBoss Management HTTPS port, e.g. 9443
  17. JBoss Management Command Line Console port, e.g. 9999
  18. JBoss Username, e.g. manager
  19. JBoss Password
  
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


### Access your JBoss server
After your Blueprint deploys successfully, please follow these instructions to access your server:
  1. Check email to obtain Server Name and IP Address Login information
  2. Log in to the server and start having fun!

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with Bitnami to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the Bitnami Support website: http://www.bitnami.com/support
* For issues related to cloud infrastructure (VM’s, network, etc), please open a CenturyLink Cloud Support ticket: https://t3n.zendesk.com/tickets/new
* For JBoss Support, please visit http://www.jboss.org/