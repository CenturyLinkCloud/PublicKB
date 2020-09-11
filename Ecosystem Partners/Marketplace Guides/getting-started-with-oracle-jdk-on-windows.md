
{{{
  "title": "Installing Oracle JDK 1.7 on Windows",
  "date": "12-01-2015",
  "author": "CTL Ecosystem Team",
  "attachments": [],
  "contentIsHTML": false
}}}

![Java logo](../../images/Java_image.png)

### Technology Profile
This Blueprint installs the Oracle JDK 1.7 on Windows.

### Description
This is the Oracle JDK, which requires that the user agree to the license terms supplied by Oracle [here](http://www.oracle.com/technetwork/java/javase/downloads/index.html).

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should be able to install Java on an existing Linux server.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user
* An existing Windows server

### Postrequisite
* None

### Deploying the <name of the Blueprint> Blueprint

#### Steps to Deploy Blueprint
1. Locate the Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Oracle JDK” in the keyword search on the right side of the page.
   * Locate the Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "Oracle JDK 1-7 for Windows" Blueprint.

3. Customize the Blueprint.
   * Choose the server to run the install on.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. There are no Oracle license costs or additional fees bundled in.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the Oracle Blueprint on CenturyLink Cloud, licensing or accessing the deployed software, please visit the [Oracle Support website](http://www.oracle.com/technetwork/java/javase/documentation/index.html).
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
