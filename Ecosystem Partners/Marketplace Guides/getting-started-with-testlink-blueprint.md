{{{
  "title": "Getting Started with TestLink - Blueprint",
  "date": "10-01-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

![TestLink Logo](../../images/testlink-stack-logo.png)

### Technology Profile
TestLink is your one-stop-shop for test plan management, managing builds and getting reports and stats on your projects. It facilitates software quality assurance. From the first time you login, you can start your first test project, write your requirements, link requirements to test cases, or create test plans.

### Description
Through the CenturyLink Blueprint integration, TestLink provides a click-through solution to install and configure TestLink on the Linux platform.

For more information, please visit http://www.testlink.org.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Blueprint technology on CenturyLink Cloud.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
* If you want to access your application over the internet, please perform the following tasks after you receive an email notifying you that the Blueprint completed successfully.

* If you need to connect to your server via the Internet, [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.

* [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
  * The default ports to access the application are: `80`, `443`.

### Deploying TestLink on a New Server
TestLink is available as a Blueprint for deployment on a new server.

#### Steps to Deploy Blueprint
1. Locate the Bitnami TestLink Blueprint.
   * Starting from the CenturyLink Control Portal, navigate to the Blueprints Library.
   * Search for “TestLink” in the keyword search on the right side of the page.
   * Locate the 'Install Bitnami TestLink on Linux' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the “Install Bitnami TestLink on Linux” Blueprint.

3. Configure the Blueprint.
   Complete the information below:

   * Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
   * Apache Web Server Port, e.g., 80
   * SSL Port, e.g., 443
   * Web Server domain, e.g., 127.0.0.1
   * MySQL Server port, e.g., 3306
   * Login, e.g., user
   * Your real name, e.g., User Name
   * Email Address, e.g., user@example.com
   * Password
   * Do you want to configure mail support?, e.g., 0
   * Default email provider:, e.g., custom
   * SMTP User
   * SMTP Password
   * SMTP Port, e.g., 587
   * SMTP Host
   * Secure connection, e.g., tls

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy TestLink to an existing server (alternate option)

Bitnami TestLink is available as a Script Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps
1. Deploy or Identify an Existing Server.
   * Identify the server targeted for TestLink installation.
   * The Operating system must be supported by the Script Package.
   * See the [Creating a new enterprise cloud server](../../Servers/creating-a-new-enterprise-cloud-server.md) KB for more information on completing this step.

2. Select to Execute the Package on a Server Group.
   * Packages can be executed on one more more servers in a Group.
   * Search for the public script package named **Install Bitnami TestLink on Linux**.
   * See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. Configure the Parameters. 
   Set the following application parameters:

   * **Apache Web Server Port** - default 80
   * **SSL Port** - default 443
   * **Web Server domain** - default 127.0.0.1
   * **MySQL Server port** - default 3306
   * **Login** - default user
   * **Your real name** - default User Name
   * **Email Address** - default user@example.com
   * **Password**
   * **Do you want to configure mail support?** - default 0
   * **Default email provider:** - default custom
   * **SMTP User**
   * **SMTP Password**
   * **SMTP Port** - default 587
   * **SMTP Host**
   * **Secure connection** - default tls

4. Deploy the Script Package.
   * Once verified, click on the `execute package` button.
   * This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

5. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your TestLink server
After your Blueprint deploys successfully, please follow these instructions to access your server:
1. Check email to obtain Server Name and IP Address Login information.
2. Log in to the server and start having fun!

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers. Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, licensing or accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
