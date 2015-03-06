{{{
  "title": "Getting Started with Nginx - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](http://wiki.nginx.org/local/nginx-logo.png)

### Technology Profile
Bitnami Nginx Stack provides a complete, fully-integrated and ready to run PHP, MySQL and Nginx development environment. In addition, it bundles phpMyAdmin, SQLite, ImageMagick, FastCGI, Memcache, GD, CURL, PEAR, PECL and other components. Nginx is known for its high performance, stability, rich feature set, simple configuration, and low resource consumption.  

### Description
Nginx, pronounced engine-x, is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. Igor Sysoev started development of Nginx in 2002, with the first public release in 2004. 

Unlike traditional servers, Nginx doesn't rely on threads to handle requests. Instead it uses a much more scalable event-driven (asynchronous) architecture. This architecture uses small, but more importantly, predictable amounts of memory under load.

Even if you don't expect to handle thousands of simultaneous requests, you can still benefit from Nginx's high-performance and small memory footprint. Nginx scales in all directions: from the smallest VPS all the way up to clusters of servers.

For more information, please view http://www.Nginx.org

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


### Install Bitnami Nginx on Linux Blueprint
1. Locate the Bitnami Nginx Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Nginx” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami Nginx on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami Nginx on Linux” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  3. Base User Real Name, e.g. John Doe
  4. Base User Email Address, e.g. john@doe.com
  5. Base User Account Name, e.g. admin
  6. Base User Password
  7. MySQL Server Port, e.g. 3306
  8. MySQL root password
  9. MySQL Database Name, e.g. mysql_db
  10. MySQL Database User Name, e.g. mysql_user
  11. MyDQL Database User Password
  12. Nginx Port, e.g. 80
  13. Nginx SSL Port, e.g. 443
  14. Varnish Port, e.g. 8080
  15. PHPMyAdmin Password
  16. PHP FPM Port, e.g. 9000
  17. Start Nginx after install?, e.g. Yes

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


### Access your Nginx server
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
* For Nginx Support, please visit http://nginx.org/en/support.html