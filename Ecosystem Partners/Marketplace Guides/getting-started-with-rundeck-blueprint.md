{{{
  "title": "Getting Started with RUNDECK PRO - Blueprint",
  "date": "10-31-2015",
  "author": "SimplifyOps",
  "attachments": [],
  "contentIsHTML": false
}}}

![Rundeck Logo](../../images/rundeck-logo.png)

### Technology Profile
Rundeck is a job scheduler and runbook automation for today's IT operations challenges. Rundeck helps you bring your operations under control and enable on-demand self-service, while ensure security and compliance. Rundeck features fine-grain access controls, centralized logging and notifications, an extensible plugin framework, and the ability to define workflows that dispatch commands and scripts to your nodes.

### Description
Through the CenturyLink Blueprint integration, RUNDECK PRO provides a click-through solution to install and configure RUNDECK on the Linux platform.

For more information, please visit http://www.rundeck.org.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the RUNDECK on CenturyLink Cloud.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisite
If you want to access your application over the internet, please perform the following tasks after you receive an email notifying you that the Blueprint completed successfully:
* If you need to connect to your server via the Internet, [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal

* [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through the Control Portal and configuring appropriately.
   * The default ports to access the application are: `80`, `443`.

### Deploying RUNDECK on a New Server
RUNDECK is available as a Blueprint for deployment on a new server.

#### Steps to Deploy Blueprint
1. Locate the RUNDECK Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “RUNDECK” in the keyword search on the right side of the page.
   * Locate the 'RUNDECK PRO' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the “RUNDECK PRO” Blueprint.

3. Configure the Blueprint.
   Complete the information below:
   * Execute on Server: Select a Linux x64 server to deploy the Blueprint on.
   * Admin password. This is the password you will use to login to the Rundeck instance.
   * SMTP Relay. Rundeck notification emails will be forwarded to your relay.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access your RUNDECK server
After your Blueprint deploys successfully, please follow these instructions to access your server:
1. Check email to obtain Server Name and IP Address Login information.
2. The RUNDECK PRO server URL will be https://{YOUR_IP}/rundeckpro.
3. Log in to the server as 'admin' using the Password you set earlier.
4. Create your first project.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. There are no Bitnami license costs or additional fees bundled in.

### About SimplifyOps
CenturyLink Cloud works with [SimplifyOps](http://www.simplifyops.com) to provide an automated operations environment to handle routine tasks, deployment, NOC support and incident management.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the RUNDECK PRO, Licensing or Accessing the deployed software, please visit the [SimplifyOps Support website](http://support.simplifyops.com/).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
