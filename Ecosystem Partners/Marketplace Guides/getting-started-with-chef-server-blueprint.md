{{{
  "title": "Getting Started with Chef Server - Blueprint",
  "date": "02-10-2016",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile
![chef-logo](../../images/chef/chef-logo.png)

* Chef – “Code Can.”
* https://chef.io

##### Customer Support
|Support Contact |
|:-	|
|support@chef.io |

### Description
Chef has integrated their technology with the Lumen Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Configuration Management solution.

Technology from Chef helps Lumen Cloud customers address the business challenge of Configuration Management by implementing Chef Server solution - now available as part of the Lumen Cloud Blueprint Engine.

### Audience
* Lumen Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on Lumen Cloud.

After executing the steps in this Getting Started document, the users will have a functioning Chef Server with Chef manage upon which they can start developing their configuration management solutions.

### Deploying Chef Server
1. Locate the Blueprint in the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for "Chef" in the keyword search on the right side of the page.

2. Click the `deploy blueprint` button.

3. Set Required parameters.
   * **Execute on Server** - Leave selected at `CHEF`
   * **First Name** - Administrator's first name
   * **Last Name** - Administrator's last name
   * **Email** - Administrator's email
   * **Org Short Name** - Short name for Org
   * **Org Long Name** - Long name for Org
   * **Password For Admin** - Initial password to login to web interface

4. Set Optional Parameters.
   * Password/Confirm Password (This is the root password for the server. Keep this in a secure place).
   * Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).
   * Optionally set the server name prefix.
   * The default values are fine for every other option.
   * **IMPORTANT**: You should note the two hostnames you specified above, as well as the MC password. These will be needed later to log into and configure your SUREedge instances.

5. Review and Confirm the Blueprint.

6. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details stating the Blueprint is queued for execution.

7. Deployment Complete.
   * Once the Blueprint has deployed you will receive an email confirming the newly deployed assets within a few minutes.
   * If you do not receive an email you may have had a deployment error - check the *Blueprints Queue* or review the *Blueprint Build Log* to for error messages.

9. Connect to Chef Server.
  * Connect to the server's assigned IP address.
  * Use the admin account that you created on provisioning, reset the password, and if needed create new accounts and organizations.
  * You’ll probably want to download the [starter kit](https://YOURSERVERIP/organizations/your_org_here/getting_started) to help start administering your Chef server.

### Pricing
The costs listed above in the above steps are for the infrastructure only. You receive a free 25 node license with your Chef server. If you would like more licenses please email support@chef.io to secure additional entitlements.

### Frequently Asked Questions
**Where do I obtain my license?**
You receive a free 25 node license with your Chef server. If you would like more licenses please email support@chef.io.

**Who should I contact for support?**
* For issues related to deploying Chef Server, please contact support@chef.io.
* For issues related to cloud infrastructure, please open a ticket using the [Lumen Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
