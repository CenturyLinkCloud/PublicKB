{{{
  "title": "Getting Started with Dynatrace - Blueprints",
  "date": "01-21-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

### Partner Profile
Dynatrace - “Dynatrace APM tools provide application monitoring for today's most challenging web, cloud, mobile, enterprise and Big Data applications worldwide.” http://www.Dynatrace.com Dynatrace makes application performance monitoring, load testing and end user experience monitoring tools for enterprises

Customer Support:
* Lumen Blueprint-[specific Support Website](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=184951236)
* General Dynatrace [Support Website](https://community.compuwareapm.com/community/display/SUPPORT/How+to+get+Support)

### Description
Dynatrace makes APM software that will provide the customer with information on how their application is performing. Dynatrace has integrated their technology with the Lumen Cloud platform and produced several Blueprints. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Cloud APM solution.

### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Dynatrace technology on Lumen Cloud.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.
* See further information in Blueprints section below.

### Blueprints
1. Dynatrace All In One Blueprint - Deploys Dynatrace Server, Dynatrace Collector, Postgres and dependencies. Requires license and configuration via client connection.
2. Dynatrace Collector Blueprint - Installs Dynatrace Collector to attach to existing Dynatrace Server.
3. Install Dynatrace Agent on Linux - Install Dynatrace Agent on Linux. Further application server configuration will be necessary after install.
4. Dynatrace Free Trial Blueprint - Deploys Dynatrace Server, Dynatrace Collector, Postgres and dependencies. Enrolls customer in FreeTrial program. Requires license and configuration via client connection. For more information, visit [this link](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=185766313).

### Detailed Steps
Follow these step by step instructions to get started with a Dynatrace deployment. We'll use the 'Install Dynatrace All In One' in the example below.

1. Locate the Blueprint in the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for “Dynatrace” in the keyword search on the right side of the page.

2. Choose and Deploy the Blueprint.
   * Click the “Install Dynatrace All In One” Blueprint.
   * Click the `deploy blueprint` button.

3. Configure the Blueprint.
   * Complete the information/fields required by the Blueprint wizard.

4. Review and Confirm the Blueprint.
   * Click `next: step 2`.
   * Verify your configuration details.

5. Deploy the Blueprint.
   * Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
   * This will kick off the Blueprint deploy process and load a page to allow you to track the progress of the deployment.

6. Monitor the Activity Queue.
   * Monitor the Deployment Queue to view the progress of the Blueprint.
   * To monitor progress, click **Queue** from the Nav Menu on the left.
   * This is what a successful deployment looks like in the queue:
   * Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification.

### Access and Configure Dynatrace on Lumen
For more information on how to access, license and configure Dynatrace, please view the [Dynatrace documentation](https://community.compuwareapm.com/community/pages/viewpage.action?pageId=184951236). Additional documentation on the Free Trial can be found here.

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no Dynatrace license costs or additional fees bundled in.

### Frequently Asked Questions
Where do I obtain my Dynatrace Licenses? Contact Dynatrace via email: isvintegrate@dynatrace.com

### Who should I contact for support?
* For issues related to deploying the Dynatrace Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the [Dynatrace Support Website](https://community.compuwareapm.com/community/display/SUPPORT/How+to+get+Support)
* For issues related to cloud infrastructure (VMs, network, etc.), please open a ticket using the Lumen Cloud Support Process.
