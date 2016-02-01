
{{{
  "title": "Installing appsFreedom Platform - Basic Edition",
  "date": "2015-12-31",
  "author": "appsFreedom Support Team",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile

This blueprint allows company's of user size 1-100 deploy appsFreedom Platform - Basic edition.

### Description
appsFreedom has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this solution

This blueprint allows company's of user size 1-100 deploy appsFreedom Platform - Basic edition.
appsFreedom is the leading provider of a Model-Driven, Enterprise App Development Platform, empowering non-professional developers to easily build Mobile and Web apps, fully integrated to IT’s core applications in days. appsFreedom drives business productivity by delivering a high-productivity platform through its appsFreedom Platform to collaborate, build, deploy and run apps in a multi-channel, multi-device environment. The basic edition includes a select set of key features of the appsFreedom Platform for small to medium businesses.


For more information, please visit appsfreedom.com

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should get a functioning Rapid Mobile App Development Platform upon which they can start developing enterprise mobile app solutions

### Prerequisite
  - Access to the CenturyLink Cloud platform as an authorized user.
  - Installation and Configuration of the appsFreedom Master Database. Please contact appsfreedom(sales@appsfreedom.com) to get a copy of the Master Database.
  - Connectivity Parameters to the appsFreedom Master Database.
    - HostName
    - Schema Name (DEV, QA, PRD, CA)
    - UserId (DEV, QA, PRD, CA)
    - Password (DEV, QA, PRD, CA)
  - Available, Domain and SubDomain Name to be used.
  - Available, SMTP Set-up Parameters.

### Postrequisite
To access your application from a computer outside the CenturyLink Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80

### Deploying the appsFreedom Platform - Basic edition Blueprint

#### Steps to Deploy Blueprint
1. **Locate the appsFreedom Platform - Basic edition Blueprint**
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “appsFreedom” in the keyword search on the right side of the page.
  3. Locate the 'appsFreedom Platform - Basic edition' Blueprint

2. **Choose and Deploy the Blueprint.**
   Click the "appsFreedom Platform - Basic edition" Blueprint.

3. **Customize the Blueprint**
  1. **Global Variables for the appsFreedom Landscape Set-up **
    1. Landscape
    2. Database Host Name
    **Development**
    3. Development DB User Id
    4. Development DB Password
    **Quality**
    5. Quality DB User Id
    6. Quality DB Password
    **Production**
    7. Production DB User Id
    8. Production DB Password
    **Container**
    9. Container DB User Id
    10. Container DB Password
    **DNS**
    11. Domain
    12. Subdomain
    **Mail Setup**
    13. Mail SMTP Server
    14. Mail SMTP Port
    15. Mail UserId
    16. Mail Password

  2. **Build Server**
    1. Password, In-case, you would like to connect via ssh
    2. Customize Server Name, if needed

  3.** Installer appsFreedom on Linux v1.20**
    1. No Change

  4.** Blueprint: Oracle JDK 1-8 For Linux**
    1. Accept the JDK License

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

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only. Build and deploy your first app for FREE. Please contact appsFreedom for more details.

### About appsFreedom
CenturyLink Cloud works with [appsFreedom Inc](http://appsfreedom.com) to provide a Model-Driven, Enterprise App Development Platform, empowering non-professional developers to easily build Mobile and Web apps, fully integrated to IT’s core applications in days. appsFreedom drives business productivity by delivering a high-productivity platform through its appsFreedom Platform to collaborate, build, deploy and run apps in a multi-channel, multi-device environment. The basic edition includes a select set of key features of the appsFreedom Platform for small to medium businesses.

### Frequently Asked Questions

#### Who should I contact for support?
* For issues related to deploying the appsFreedom Inc Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please contact appsFreedom Inc. Support at 855.277.7373
* For issues related to cloud infrastructure (VM's, network, etc), or is you experience a problem deploying the Blueprint or Script Package, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the CenturyLink Cloud Support website](https://t3n.zendesk.com/tickets/new).
