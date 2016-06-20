{{{
  "title": "Getting Started With Waratek AppSecurity",
  "date": "08-20-2015",
  "author": "Waratek - David Egan",
  "attachments": [],
  "contentIsHTML": false
}}}

![](http://cdn.aws.waratek.com/wp-content/themes/waratek/images/logo.png)

### Technology Profile

Waratek security solutions protect applications and data without software agents, code changes, or network devices. By placing security within the Java virtual machine, attacks from both internal and external sources can be mitigated with minimal impact on performance. - See more at: [http://www.waratek.com/solutions/](http://www.waratek.com/solutions/).

### Description

This CenturyLink Blueprint provides a simple install solution of the Waratek AppSecurity JVM on CentOS 6 and Red Hat 6 Linux platforms.

For more information, please visit [http://www.waratek.com](http://www.waratek.com).

### Audience

CenturyLink Cloud Users desiring a secure Java environment.

### Impact

After reading this article, the user should be able to install AppSecurity for Java on a  CenturyLink Cloud server.

### Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user.

### Postrequisites

* None

### Deploying Waratek JVM on a New Server

Waratek JVM is available as a Blueprint for deployment on a new server.

#### Steps to deploy to New Server Blueprint

1.  Locate the "Install Waratek JVM 3-0-2 on New Server" Blueprint

2.  Click on the blueprint. Select "Deploy Blueprint" on the resulting screen

3.  Configure the Blueprint. Complete the information below:

    1.  Enter password.
    2.  Choose your group.
    3.  Choose your network.
    4.  Choose Primary and Secondary DNS.
    5.  Choose the Server Type.
    6.  Choose Service Level.
    7.  Enter Server Name.  

4.  Review and Confirm the Blueprint

    1.  Click “next: step 2”
    2.  Verify your configuration details.

5.  Deploy the Blueprint
  *  Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  *  This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6.  Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

7.  Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

#### Steps to deploy to an existing server

1.  Deploy or Identify an existing server

2.  Locate the "Install Waratek JVM on Existing Server" blueprint in the Blueprint Library

3.  Select "Deploy Blueprint"

4.  Select the server to be deployed

5.  Select "next: step 2"

6.  Select "Deploy Blueprint"

7.  Monitor the Deployment Queue to view the progress of the blueprint. You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

8.  Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Frequently Asked Questions

#### Purchasing AppSecurity
* Contact [our sales team](mailto:sales@waratek.com).

#### Who should I contact for support?

*   For issues related to deploying Waratek JVM visit [Waratek Support](https://support.waratek.com).
*   For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
