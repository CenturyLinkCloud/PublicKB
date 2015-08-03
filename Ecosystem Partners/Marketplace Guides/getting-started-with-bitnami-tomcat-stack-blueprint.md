{{{
  "title": "Getting Started with Tomcat - Blueprint",
  "date": "07-30-2015",
  "author": "Bitnami and <a href='https://www.linkedin.com/in/bstolzberg'>Bob Stolzberg</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

![Tomcat logo](https://bitnami.com/assets/stacks/tomcatstack/img/tomcatstack-stack-220x234.png)

### Technology Profile
Apache Tomcat is the most widely adopted application and web server in production today. Where WildFly is full JEE stack, Tomcat is a simpler servlet container and web server. Tomcat is lightweight and agile, simple to use and has a very large ecosystem of add-ons

### Description
Through the CenturyLink Blueprint integration, the Tomcat Stack provides a click-through solution to install and configure Tomcat on the Linux platform.

For more information, please visit [http://tomcat.apache.org/](http://tomcat.apache.org/)

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Blueprint technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
- If you want to access your application over the internet, please perform the following tasks after you receive an email notifying you that the Blueprint completed successfully:

1. If you need to connect to your server via the Internet, [Add a Public IP](../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal

2. [Allow incoming traffic](../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
  * The default ports to access the application are: 80, 443

### Deploying Tomcat on a New Server
Tomcat is available as a Blueprint for deployment on a new server.

#### Steps to Deploy Blueprint
1. **Locate the Tomcat Stack Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Tomcat” in the keyword search on the right side of the page.
  3. Locate the 'Install Tomcat on Linux' Blueprint

2. **Choose and Deploy the Blueprint. Click the “Install Tomcat on Linux” Blueprint.**

3. **Configure the Blueprint** 
Complete the information below:

  1. Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
  2. Username, e.g. manager
  3. Password
  4. MySQL Server root password
  5. Apache Web Server Port, e.g. 80
  6. SSL Port, e.g. 443
  7. MySQL Server port, e.g. 3306

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

### Deploy Tomcat to an existing server (alternate option)
The Tomcat Stack is available as a Script Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps to deploy Tomcat to an existing server
1. **Deploy or Identify an Existing Server**
Identify the server targeted for Tomcat installation.  The Operating system must be supported by the Script Package.  See the [Creating a new enterprise cloud server](../Servers/creating-a-new-enterprise-cloud-server.md) KB for more information on completing this step.

2. **Select to Execute the Package on a Server Group**
  1. Packages can be executed on one more more servers in a Group.  Search for the public script package named **Install Tomcat on Linux**.
  2. See the [using group tasks to install scripts on groups](../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. **Configure the Parameters**
Set the following application parameters:

* **Username** - default manager
* **Password**
* **MySQL Server root password**
* **Apache Web Server Port** - default 80
* **SSL Port** - default 443
* **MySQL Server port** - default 3306

4. **Deploy the Script Package**
Once verified, click on the `execute package` button. This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

5. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your Tomcat server
After your Blueprint deploys successfully, please follow these instructions to access your server:

  1. Check email to obtain Server Name and IP Address Login information
  2. Log in to the server and start having fun!

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support)
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
