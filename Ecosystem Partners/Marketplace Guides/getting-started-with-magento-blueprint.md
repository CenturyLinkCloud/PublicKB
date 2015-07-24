{{{
  "title": "Getting Started with Magento - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](https://wiki.magento.com/download/attachments/2952491/MAGE2DOC?version=1&modificationDate=1378339878000&api=v2)

### Technology Profile
Magento is one of the most popular open source ecommerce shopping cart systems. It is extremely flexible and has a huge variety of features to build just about any store. Features include SEO-readiness, multi-store support, marketing tools, deep analytics, catalog management, a robust shopping cart with support for multiple shipping addresses and more. The Magento project is backed by eBay, so you can be confident that it will be around for the long run, and it offers multiple editions, including small business and enterprise editions, to help grow with your business. Magento’s flexible, feature-rich open source and enterprise eCommerce solutions help you get the most from your online channel.

### Description
Magento Community Edition is the perfect solution if you're a developer or tech-savvy merchant that wants to explore the flexibility of the Magento eCommerce platform. You can modify—and even contribute to—the core code and engage with our passionate community for support and guidance.  This Blueprint will install and configure Magento 1.9.1.0-1 (64-bit) on Linux.

For more information, please view http://www.Magento.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Bitnami Blueprint technology on CenturyLink Cloud.


### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Existing Linux x64 server and login access

### Postrequisite

- If you need to connect to your server via internet, add a Public IP address to your server.  For more information view this link: http://www.ctl.io/knowledge-base/network/how-to-add-public-ip-to-virtual-machine.md

    ![ip.jpg](https://t3n.zendesk.com/attachments/token/kObGC9P2IjP1ate0NexwFNiXz/?name=ip.jpg)

- Allow incoming traffic for ports to an existing server by managing Firewall rules.  Fore more information, vie this link: http://www.ctl.io/knowledge-base/network/creating-cross-data-center-firewall-policies/

    ![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)


### Install Bitnami Magento on Linux Blueprint
1. Locate the Bitnami Magento Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Magento” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami Magento on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami Magento on Linux” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  2. Magento Site Name, e.g. Spatula City
  3. Base User Real Name, e.g. John Doe
  4. Base User Email Address, e.g. john@doe.com
  5. Base User Account Name, e.g. magentoadmin
  6. Base User Password
  7. Apache Web Server Port, e.g. 80
  8. SSL Web Service Port, e.g. 443
  9. Web Server Domain, e.g. 127.0.0.1 or whatever.com
  10. MySQL Server Port, e.g. 3306
  11. MySQL root password
  12. MySQL Database Name, e.g. magentodb
  13. MySQL Database User Name, e.g. dbadmin
  14. MyDQL Database User Password
  15. PHPMyAdmin Password
  16. Magento Admin Password
  17. Start Magento after install?, e.g. Yes

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


### Access your Magento server
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
* For Magento Support, please visit http://www.magentocommerce.com/knowledge-base
