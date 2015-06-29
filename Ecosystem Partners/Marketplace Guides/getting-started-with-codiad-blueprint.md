{{{
  "title": "Getting Started with Codiad - Blueprint",
  "date": "05-30-2015",
  "author": "Bitnami",
  "attachments": [],
  "contentIsHTML": false
}}}

![Codiad logo](https://bitnami.com/assets/stacks/codiad/img/codiad-stack-220x234.png)

### Technology Profile
Codiad is a web-based IDE framework with a small footprint and minimal requirements. Codiad was built with simplicity in mind, allowing for fast, interactive development without the  overhead of some of the larger desktop editors.

### Description
The CenturyLink Codiad Blueprint provides a click-through solution to install and configure Codiad on the Linux platform.

For more information, please visit [http://codiad.com](http://codiad.com)

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Blueprint technology on CenturyLink Cloud.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443

### Deploying the Codiad Blueprint on a New Server
The Codiad Stack is available as a Blueprint for deployment on a new server.

#### Steps to Deploy Blueprint
1. **Locate the Codiad Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Codiad” in the keyword search on the right side of the page.
  3. Locate the 'Install Codiad on Linux' Blueprint

2. **Choose and Deploy the Blueprint.**
   Click the “Install Codiad on Linux” Blueprint.

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

  3. Installation Parameters
    1. Installation credentials - leave this as "no"
    2. Apache Web Server Port, default 80
    3. SSL Port, default 443
    4. Web Server domain, e.g. "my.codiadserver.mydomain.com", or 127.0.0.1
    5. Login, e.g. user_id to run under
    6. Your real name, e.g. Display User Name
    7. Email Address, e.g. user@example.com
    8. Password

4. **Review and Confirm the Blueprint**
  1. Click “next: step 2”
  2. Verify your configuration details.

5. **Deploy the Blueprint**
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. **Monitor the Activity Queue**
  1. Monitor the Deployment Queue to view the progress of the blueprint.
  2. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  3. Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Deploy Codiad to an existing server (alternate option)
Codiad is available as a Script Package for deployment on an existing server based on your own sizing requirements or to support more advanced configurations such as customized Blueprint Workflows to repeatably deploy multiple stacks on servers.

#### Steps to deploy Codiad to an existing server
1. **Deploy or Identify an Existing Server**
  1. Identify the server targeted for Codiad installation.  The Operating system must be supported by the Script Package.  The server must be a server within your CenturyLink Cloud account.
2. **Select to Execute the Package on a Server Group**
  1. Packages can be executed on one more more servers in a Group.  Search for the public script package named **Install Codiad on Linux**.
  2. See the [using group tasks to install scripts on groups](../../Servers/using-group-tasks-to-install-software-and-run-scripts-on-groups.md) KB for more information on how to complete the next few steps.

3. **Configure the Parameters**
Set the following application parameters:

  1. **Apache Web Server Port** - default 80
  2. **SSL Port** - default 443
  3. **Web Server domain** - your domain, or default 127.0.0.1
  4. **Login** - default user
  5. **Your real name** - default User Name
  6. **Email Address** - default user@example.com
  7. **Password**

4. **Deploy the Script Package**
Once verified, click on the `execute package` button. This will kick off the deployment process and load a page where you can track the progress. Deployment will typically complete within a few minutes.

5. **Monitor the Activity Queue**
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your Codiad server
After your Blueprint deploys successfully, please follow these instructions to access your server:
  1. Create and configure a public IP address as described in the Postrequisites section above
  2. Enter the ip address in a browser, which will bring up the login page
  3. Log in to the server and begin work!

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Bitnami license costs or additional fees bundled in.

### About Bitnami
CenturyLink Cloud works with [Bitnami](http://www.bitnami.com) to provide open source software integrations to its customers.  Bitnami is a library of popular server applications and development environments that can be installed with one click, either in your laptop, in a virtual machine or hosted in the cloud. Bitnami takes care of compiling and configuring the applications and all of their dependencies (third-party libraries, language runtimes, databases) so they work out-of-the-box. The resulting packaged software (a 'stack') is then made available as native installers, virtual machines and cloud images. These Bitnami application packages provide a consistent, secure and optimized end-user experience when deploying any app, on any platform.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Bitnami Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Bitnami Support website](http://www.bitnami.com/support)
* For issues related to cloud infrastructure (VMs, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
