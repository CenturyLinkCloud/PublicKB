{{{
  "title": "Getting Started with Drupal - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](https://www.drupal.org/files/drupal_logo-blue.png)

### Technology Profile
Drupal is one of the most versatile open source content management systems on the market. Over a thousand developers contributed to the code in the most recent version. Drupal is built for high performance and is scalable to many servers, has easy integration via REST, JSON, SOAP and other formats, and features a whopping 15,000 plugins to extend and customize the application for just about any type of website. You won’t feel alone if you use Drupal; the hundreds of thousands of Drupal users around the world have built a very robust community with local meetups and global user conferences.

### Description

Drupal includes comprehensive content management features, including the ability to create new content types and import content from other sources. Drupal modules make it possible to add nearly unlimited functionality, ranging from photo galleries to e-commerce workflows, and extensive free documentation enables both new users and expert developers to quickly start using and developing with Drupal.

The Bitnami Drupal Stack makes it easy to create content-driven websites and web applications with Drupal. Some examples include:

- Personal portfolio websites: Use Drupal to tell the world about yourself, your company and your work. Modules are available to easily add photo galleries and support social media and it's easy to create a theme that reflects your personality and style.

- Enterprise websites: Drupal is used by large, well-known websites, including those belonging to the University of Oxford and the White House. It includes professional content management and collaboration tools and is scalable to high workloads.

- E-commerce websites: Drupal can power an e-commerce website. Modules are available for payment and shipping integration, notifications, order management and shopping cart workflows, and it's easy to find or develop themes for online storefronts.

For more information, please view http://www.Drupal.org


### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Bitnami Blueprint technology on CenturyLink Cloud.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Existing Linux x64 server and access

### Postrequisite

- If you need to connect to your server via internet, add a Public IP address to your server.  For more information view this link: http://www.centurylinkcloud.com/knowledge-base/network/how-to-add-public-ip-to-virtual-machine/

	![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

- Allow incoming traffic for ports to an existing server by managing Firewall rules.  Fore more information, vie this link: http://www.centurylinkcloud.com/knowledge-base/network/creating-cross-data-center-firewall-policies/

	![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)


### Install Bitnami Drupal on Linux Blueprint
1. Locate the Bitnami Drupal Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Drupal” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami Drupal on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami Drupal on Linux” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  2. Base User Real Name, e.g. John Doe
  3. Base User Email Address, e.g. john@doe.com
  4. Base User Account Name, e.g. admin
  5. Base Users Password
  6. Apache Web Server Port, e.g. 80
  7. SSL Web Service Port, e.g. 443
  8. Web Server Domain, e.g. 127.0.0.1 or whatever.com
  9. MySQL Server Port, e.g. 3306
  10. MySQL root password
  11. MySQL Database Name, e.g. Drupal
  12. MySQL Database Username, e.g. admin
  13. MySQL Database User Password
  14. PHPMyAdmin Password
  15. Start Drupal after install, e.g. Yes


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


### Access your Drupal server
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