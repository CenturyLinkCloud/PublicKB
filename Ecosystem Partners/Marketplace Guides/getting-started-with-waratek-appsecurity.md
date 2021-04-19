{{{
  "title": "Getting Started With Waratek AppSecurity",
  "date": "08-20-2015",
  "author": "Waratek - David Egan",
  "attachments": [],
  "contentIsHTML": false
}}}

![Waratek Logo](../../images/waratek-logo.png)

### Technology Profile
Waratek security solutions protect applications and data without software agents, code changes, or network devices. By placing security within the Java virtual machine, attacks from both internal and external sources can be mitigated with minimal impact on performance. See more at [Waratek Solutions/](http://www.waratek.com/solutions/).

### Description
This Lumen Blueprint provides a simple install solution of the Waratek AppSecurity JVM on CentOS 6 and Red Hat 6 Linux platforms.

For more information, please visit [http://www.waratek.com](http://www.waratek.com).

### Audience
Lumen Cloud Users desiring a secure Java environment.

### Impact
After reading this article, the user should be able to install AppSecurity for Java on a  Lumen Cloud server.

### Prerequisites
* Access to the Lumen Cloud platform as an authorized user.

### Postrequisites
* None

### Deploying Waratek JVM on a New Server
Waratek JVM is available as a Blueprint for deployment on a new server.

### Steps to deploy to New Server Blueprint
1. Locate the "Install Waratek JVM 3-0-2 on New Server" Blueprint.

2. Select the Blueprint.
   * Click `deploy blueprint`.

3. Configure the Blueprint. Complete the information below:

   * Enter password.
   * Choose your group.
   * Choose your network.
   * Choose Primary and Secondary DNS.
   * Choose the Server Type.
   * Choose Service Level.
   * Enter Server Name.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete.
   * Please do not use the application until you have received this email notification.

### Steps to deploy to an existing server
1. Deploy or Identify an existing server.

2. Locate the "Install Waratek JVM on Existing Server" Blueprint in the Blueprint Library.

3. Select `deploy blueprint`.

4. Select the server to be deployed.

5. Select `next: step 2`.

6. Select `deploy blueprint`.

7. Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete.
   * Please do not use the application until you have received this email notification.

### Frequently Asked Questions

#### Purchasing AppSecurity
* Contact [our sales team](mailto:sales@waratek.com).

#### Who should I contact for support?
* For issues related to deploying Waratek JVM visit [Waratek Support](https://support.waratek.com).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
