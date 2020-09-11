
{{{
  "title": "Installing appsFreedom Platform - Basic Edition",
  "date": "12-31-2015",
  "author": "appsFreedom Support Team",
  "attachments": [],
  "contentIsHTML": false
}}}

![appsFreedom Logo](../../images/appsfreedom-logo.png)

### Technology Profile
This blueprint allows company's of user size 1-100 deploy appsFreedom Platform - Basic edition.

### Description
appsFreedom has integrated their technology with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this solution.

This blueprint allows company's of user size 1-100 deploy appsFreedom Platform - Basic edition.
appsFreedom is the leading provider of a Model-Driven, Enterprise App Development Platform, empowering non-professional developers to easily build Mobile and Web apps, fully integrated to IT’s core applications in days. appsFreedom drives business productivity by delivering a high-productivity platform through its appsFreedom Platform to collaborate, build, deploy and run apps in a multi-channel, multi-device environment. The basic edition includes a select set of key features of the appsFreedom Platform for small to medium businesses.

For more information, please visit appsfreedom.com.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should get a functioning Rapid Mobile App Development Platform upon which they can start developing enterprise mobile app solutions.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.
* Installation and Configuration of the appsFreedom Master Database. Please contact appsfreedom(sales@appsfreedom.com) to get a copy of the Master Database.
* Connectivity Parameters to the appsFreedom Master Database.
  * HostName
  * Schema Name (DEV, QA, PRD, CA)
  * UserId (DEV, QA, PRD, CA)
  * Password (DEV, QA, PRD, CA)
* Available, Domain and SubDomain Name to be used.
* Available, SMTP Set-up Parameters.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully.
* [Add a Public IP](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal.
* [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
  * The default ports to access the application are: `80`.

### Deploying the appsFreedom Platform - Basic edition Blueprint

#### Steps to Deploy Blueprint
1. Locate the appsFreedom Platform - Basic edition Blueprint.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “appsFreedom” in the keyword search on the right side of the page.
   * Locate the 'appsFreedom Platform - Basic edition' Blueprint.

2. Choose and Deploy the Blueprint.
   * Click the "appsFreedom Platform - Basic edition" Blueprint.

3. Customize the Blueprint.
   * Global Variables for the appsFreedom Landscape Set-up **
     * Landscape
     * Database Host Name
   * Development
     * Development DB User Id
     * Development DB Password
   * Quality
     * Quality DB User Id
     * Quality DB Password
   * Production
     * Production DB User Id
     * Production DB Password
   * Container
     * Container DB User Id
     * Container DB Password
   * DNS
     * Domain
     * Subdomain
   * Mail Setup
     * Mail SMTP Server
     * Mail SMTP Port
     * Mail UserId
     * Mail Password

   * Build the Server.
     * Password, In-case, you would like to connect via ssh.
     * Customize Server Name, if needed.

   * Installer appsFreedom on Linux v1.20.
     * No Change

   * Blueprint: Oracle JDK 1-8 For Linux**
     * Accept the JDK License

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. Build and deploy your first app for FREE. Please contact appsFreedom for more details.

### About appsFreedom
CenturyLink Cloud works with [appsFreedom Inc](http://appsfreedom.com) to provide a Model-Driven, Enterprise App Development Platform, empowering non-professional developers to easily build Mobile and Web apps, fully integrated to IT’s core applications in days. appsFreedom drives business productivity by delivering a high-productivity platform through its appsFreedom Platform to collaborate, build, deploy and run apps in a multi-channel, multi-device environment. The basic edition includes a select set of key features of the appsFreedom Platform for small to medium businesses.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the appsFreedom Inc Blueprint on CenturyLink Cloud, licensing or accessing the deployed software, please contact appsFreedom Inc. Support at 855.277.7373
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
