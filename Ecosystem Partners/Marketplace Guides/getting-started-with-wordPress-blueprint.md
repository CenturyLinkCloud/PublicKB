{{{
  "title": "Getting Started with WordPress - Blueprint",
  "date": "2-25-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![logo](https://s.w.org/about/images/logos/wordpress-logo-stacked-rgb.png)

### Technology Profile
WordPress is one of the world’s most popular web publishing platforms for building blogs and websites. It can be customized via a wide selection of themes, extensions and plug-ins.  

WordPress is a popular blogging software and powers more than 10% of all websites globally. Developed by Automattic, WordPress rose to popularity quickly because of it's up-to-date development framework, extensive feature set, flexibility, rapid and multilingual publishing ability, multi-author support, and thriving community. Thousands of free and commercial themes and plugins are available to extend and personalize WordPress for just about every situation.

### Description

WordPress is a powerful and flexible blog publishing platform. While it's best known and arguably most widely used for blogging, dozens of different solutions have been built by WordPress users. WordPress can be used for just about any online publishing scenario and can easily be extended with free or commercial plugins and add-ons. Some solutions include:

- Build a blog or website:  Install WordPress on your desktop, customize it and migrate it to the cloud or to another public hosting provider when you're ready.

- Create a portfolio: WordPress is ideal for creating portfolios for photographers, videographers, writers and others who have a large body of work. There are many optional themes available for displaying portfolios.

- Launch a store:  WordPress is way more than a blog. Many people use it for building portfolios, as landing pages, and even for e-commerce (there are several plugins to choose from).

- Your unique solution here: The beauty of WordPress is how flexible it is for building just about any publishing solution you can conceive of. 

For more information about the Bitnami WordPress Stack, please view https://bitnami.com/stack/wordpress/README.txt

For more information, please view http://www.WordPress.org


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


### Install Bitnami WordPress on Linux Blueprint
1. Locate the Bitnami WordPress Blueprint
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “WordPress” in the keyword search on the right side of the page.
  3. Locate the 'Install Bitnami WordPress single site on Linux' Blueprint

2. Choose and Deploy the Blueprint. Click the “Install Bitnami single site WordPress on Linux” Blueprint.

3. Configure the Blueprint. Complete the information below:
  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  2. Your Real Name, e.g. John Doe
  3. Your Email Address, e.g. john@doe.com
  4. WordPress Login, e.g. admin
  5. WordPress Password Password
  6. Apache Web Server Port, e.g. 80
  7. SSL Web Service Port, e.g. 443
  8. Web Server Domain, e.g. 127.0.0.1 or whatever.com
  9. MySQL Server Port, e.g. 3306
  10. Blog Name, e.g. User's Blog!
  11. Hostname, e.g. 127.0.1.1
  12. Default email provider, e.g. gmail
  13. Configure Email Support?, e.g. no
  14. SMTP Username
  15. SMTP Password
  16. SMTP Host
  17. SMTP Port
  18. Secure Connection, e.g. None


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


### Access your WordPress server
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