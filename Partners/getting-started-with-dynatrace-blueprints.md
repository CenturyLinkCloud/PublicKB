{{{
  "title": "Getting Started with Dynatrace - Blueprints",
  "date": "1-21-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}


### Partner Profile
Dynatrace - “Dynatrace APM tools provide application monitoring for today's most challenging web, cloud, mobile, enterprise and Big Data applications worldwide.” http://www.Dynatrace.com Dynatrace makes application performance monitoring, load testing and end user experience monitoring tools for enterprises

Customer Support:
* CenturyLink Blueprint-[specific Support Website](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=184951236)
* General Dynatrace [Support Website](https://community.compuwareapm.com/community/display/SUPPORT/How+to+get+Support)

### Description
Dynatrace makes APM software that will provide the customer with information on how their application is performing.  Dynatrace has integrated their technology with the CenturyLink Cloud platform and produced several Blueprints.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Cloud APM solution.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Dynatrace technology on CenturyLink Cloud.

### Prerequisite
* Access to the CenturyLink Cloud platform as an authorized user.
* See further information in Blueprints section below.

### Blueprints
1. Dynatrace All In One Blueprint - Deploys Dynatrace Server, Dynatrace Collector, Postgres and dependencies. Requires license and configuration via client connection.
2. Dynatrace Collector Blueprint - Installs Dynatrace Collector to attach to existing Dynatrace Server.
4. Install Dynatrace Agent on Linux - Install Dynatrace Agent on Linux. Further application server configuration will be necessary after install.
5. Dynatrace Free Trial Blueprint - Deploys Dynatrace Server, Dynatrace Collector, Postgres and dependencies. Enrolls customer in FreeTrial program. Requires license and configuration via client connection.  For more information, visit [this link](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=185766313).

### Detailed Steps
Follow these step by step instructions to get started with a Dynatrace deployment.    We'll use the 'Install Dynatrace All In One' in the example below.

1. Locate the Blueprint in the Blueprint Library.
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Dynatrace” in the keyword search on the right side of the page.

2. Choose and Deploy the Blueprint.
  1. Click the “Install Dynatrace All In One” blueprint.
  2. Click on the "Deploy Blueprint" button.
   ![2.jpg](https://t3n.zendesk.com/attachments/token/JkyvaCSCSeVyVnpDqRMRlrl4q/?name=2.jpg)

3. Configure the Blueprint.
   Complete the information/fields required by the Blueprint wizard.
   ![3.jpg](https://t3n.zendesk.com/attachments/token/XBgBCt3A0l4XNDm7A0JXGE2cG/?name=3.jpg)

4. Review and Confirm the Blueprint.
  1. Click “next: step 2”
  2. Verify your configuration details.
   ![4.jpg](https://t3n.zendesk.com/attachments/token/0H4w5DKq1hv1u8FojXWoFD6Dg/?name=4.jpg)

5. Deploy the Blueprint.
  1. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  2. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
  * This is what a successful deployment looks like in the queue:
   ![queue](https://t3n.zendesk.com/attachments/token/20v6ABIQPsXP4Eb92429rpStU/?name=5.jpg)
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.

### Access and Configure Dynatrace on CenturyLink
For more information on how to access, license and configure Dynatrace, please view the [Dynatrace documentation](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=184951236).  Additional documentation on the Free Trial can be found here.

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Dynatrace license costs or additional fees bundled in.

### Frequently Asked Questions
Where do I obtain my Dynatrace Licenses? Contact Dynatrace via email: isvintegrate@dynatrace.com

### Who should I contact for support?
* For issues related to deploying the Dynatrace Blueprint on CenturyLink Cloud, Licensing or Accessing the deployed software, please visit the [Dynatrace Support Website](https://community.compuwareapm.com/community/display/SUPPORT/How+to+get+Support)
* For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.
