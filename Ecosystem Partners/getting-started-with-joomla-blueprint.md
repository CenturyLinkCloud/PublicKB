{{{
  "title": "Getting Started with Joomla - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](http://developer.joomla.org/manual/Common_Content/images/title_logo.png)

### Technology Profile
CenturyLink and Bitnami have developed Blueprints to provide a one-click install and configure solution for Joomla on the CenturyLink Cloud platform.

While there are a lot of content management systems out there, few can boast as many downloads as Joomla! Originally released in 2005, Joomla! has some very powerful features such as an intuitive WYSIWYG editor, content scheduling, SEO-friendly URLs, and more. You won’t feel alone or stranded if you use Joomla! because the very active and vibrant community behind the CMS has contributed thousands of free and commercial plugins, offers global and local meetups (and even a Joomla! community magazine), and commits frequently to the code base.

### Description

Joomla! includes all the critical features needed to manage Web content, including WYSIWYG editing, a file manager, navigation manager and templating system. It's easy to build mobile websites and integrate RSS feeds, and Joomla! also includes built-in page caching and page compression for maximum performance. Since Joomla! uses a modular architecture, it's easy to add new custom functionality to a Joomla! website, by installing a community or commercial plugin or even by writing your own.

The Bitnami Joomla! Stack makes it easy to create rich websites and web applications with Joomla!. Some examples include:

- Personal or family website
Use Joomla! to tell the world about yourself and your family. Modules are available for photo galleries and social media, and it's easy to create a personal online presence that reflects your family's personality and lets you share news easily.

- Intranet
Joomla! makes it easy to set up an intranet presence for your company or team. Users can be assigned different roles and privileges, and the built-in file manager makes it easy to share documents and collaborate on projects.

- Corporate website
Joomla! is used by large, well-known companies, including IKEA, eBay and General Electric. It supports content publishing workflows, is scalable to high workloads, and can be easily extended to support new requirements.

- E-commerce website
Joomla! can be extended with modules for inventory and order management, shopping carts and online payments, making it easy to sell products online.

For more information, please view http://www.joomla.org

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

- Allow incoming Joomla! traffic for ports to an existing server

![port.jpg](https://t3n.zendesk.com/attachments/token/1Ufw0JjIWW8XfASYLh4x3Irl9/?name=port.jpg)

- View this documentation for common port numbers and connecting to an external database: https://docs.joomla.org/Connecting_to_an_external_database

### Install Bitnami Joomla on Linux Blueprint
1. Locate the Bitnami Joomla! Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Joomla” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami Joomla on Linux x64' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami Joomla on Linux x64” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: a Linux x64 server to deploy the Blueprint on.
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
  14. Joomla! Admin Password, e.g. admin
  15. JDBC Database Name, e.g. alfrescodatabase
  16. JDBC Database Username, e.g. admin
  17. JDBC Database User Password
  18. Start Joomla! after install, e.g. Yes


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


### Access your Joomla! server
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
* For issues related to cloud infrastructure (VM’s, network, etc), please open a CenturyLink Cloud Support ticket: https://t3n.zendesk.com/tickets/new