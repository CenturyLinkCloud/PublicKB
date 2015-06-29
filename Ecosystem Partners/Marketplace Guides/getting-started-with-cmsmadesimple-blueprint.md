{{{
  "title": "Getting Started with CMS Made Simple - Blueprint",
  "date": "05-30-2015",
  "author": "Bitnami",
  "attachments": [],
  "contentIsHTML": false
}}}

![CMS Made Simple logo](https://bitnami.com/assets/stacks/cmsmadesimple/img/cmsmadesimple-stack-220x234.png)

### Technology Profile
CMS Made Simple is exactly what it calls itself: a simple-to-use, simple-to-manage content management system. Once you have learned the vocabulary, explored the system and the many 3rd party plugins available, you will be off and running. Written in PHP and driven by a MySQL database, CMS Made Simple can help you build smaller sites (a few hundred pages is no sweat) and semi-static websites. With over 900 modules to choose from to help extend and customize your website, CMS Made Simple may just be what you need.

### Description
The CenturyLink CMS Made Simple Blueprint provides a click-through solution to install and configure CMS Made Simple on the Linux platform.

For more information, please visit [http://www.cmsmadesimple.org/](http://www.cmsmadesimple.org/)

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Blueprint technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
To access your application from a machine outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443

### Deploying CMS Made Simple on a New Server
The CMS Made Simple is available as a Blueprint for deployment on a new server.

#### Steps to Deploy Blueprint
1. **Locate the CMS Made Simple Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “CMS Made Simple” in the keyword search on the right side of the page.
  3. Locate the 'Install CMS Made Simple on Linux x64' Blueprint

2. **Choose and Deploy the Blueprint.**
  1. Click the “Install CMS Made Simple on Linux” Blueprint.
  2. Click on "Deploy Blueprint"

3. **Customize the Blueprint**
  1. Enter server parameters
    1. Password  (must conform to password rules as shown)
    2. Re-enter password
    3. Select group
    4. Select network
    5. Select primary DNS
    6. Select secondary DNS (optional)
    7. Select server type (standard is recommended)
    8. Select service level

  2. **Customize server name**
    You may select a set of characters to customize your server name

  3. **Enter Installation Parameters**
    Complete the information below
    1. Leave Specify Credentials set to "no"
    2. Apache Web Server Port, default is 80
    3. SSL Port, default is 443
    4. Web Server domain, enter your domain name or 127.0.0.1
    5. MySQL Server port, default 3306
    6. Login, e.g. "joeuser"
    7. Your real name, e.g. 'Joe User'
    8. Email Address, e.g. joe.user@example.com
    9. Password
    10. Do you want to configure mail support?, yes/no
    11. Default email provider:, gmail/custom
    12. SMTP User, the username to send mail from
    13. SMTP Password, the password for the above account
    14. SMTP Port, default 587
    15. SMTP Host, your email host
    16. Secure connection, e.g. none/tls/ssl

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy CMS Made Simple to an existing server (alternate option)
CMS Made Simple is available as a Script Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps to deploy CMS Made Simple to an existing server
1. **Deploy or Identify an Existing Server**
Identify the server targeted for CMS Made Simple installation.  The Operating system must be supported by the Script Package.  See the [Creating a new enterprise cloud server](../../Servers/creating-a-new-enterprise-cloud-server.md) KB for more information on completing this step.

2. **Select to Execute the Package on a Server Group**
  1. Packages can be executed on one more more servers in a Group.  Search for the public script package named **Install CMS Made Simple on Linux**.
  2. See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. **Enter Installation Parameters**
  Complete the information below
  1. Choose a value for Specify Credentials. "no" will install using thesystem administration account, "yes" will allow you to specify an account and password to use for the installation
  2. Apache Web Server Port, default is 80
  3. SSL Port, default is 443
  4. Web Server domain, enter your domain name or 127.0.0.1
  5. MySQL Server port, default 3306
  6. Login, e.g. "joeuser"
  7. Your real name, e.g. 'Joe User'
  8. Email Address, e.g. joe.user@example.com
  9. Password
  10. Do you want to configure mail support?, yes/no
  11. Default email provider:, gmail/custom
  12. SMTP User, the username to send mail from
  13. SMTP Password, the password for the above account
  14. SMTP Port, default 587
  15. SMTP Host, your email host
  16. Secure connection, e.g. none/tls/ssl

4. **Deploy the Script Package**
Once verified, click on the `execute package` button. This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

5. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your CMS Made Simple server
After your Blueprint deploys successfully, please follow these instructions to access your server:

  1. Check email to obtain Server Name
  2. Use the CenturyLink Console to obtain the server's IP address
  3. Enter the IP address in your browser address bar to access the main page of the application
  4. Log in to the server and begin work!

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support)
* For issues related to cloud infrastructure (VMs, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
