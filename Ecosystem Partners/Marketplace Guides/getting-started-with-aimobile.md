{{{
  "title": "Getting Started with aiMobile - Blueprint",
  "date": "12-29-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Technology Profile
<img src="../../images/aiscaler/aiscaler-logo.png" style="border:0;float:right;max-width: 150px;">

aiScaler helps Lumen Cloud customers address the business challenge of website scalability, stability and security - now available as part of the Lumen Cloud Blueprint Engine.


##### Customer Support

|Sales Contact   	| |
|:-	| |
|support@aiscaler.com<br>+1-408-744-6078<br>+44 20 7993 4587<br>Skype: ai.scaler   	| 2 Free hours of installation support<br>Professional services available.<br>Email, skype and phone available M-F Business hours EST.|

### Description
aiScaler has integrated their technology with the Lumen Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this application delivery controller solution.


#### aiMobile
**aiMobile** increases mobile site performance, unifies your domains across desktop and mobile platforms and automates delivering content that fits the capabilities of your mobile users devices.

**aiMobile** provides per device dynamic caching to decrease the time from click to content. We do on the fly re-write and redirection to allow you to transform the incoming URL’s to arrive at the right internal resource, tagged in the manner most easily digested by your development team.

**aiMobile** can detect new mobile devices and in conjunction with UserAgent databases provide nearly 100% accurate identification of end user devices.

**aiMobile** can transform your web addresses to a unified structure across all content to users, protecting your SEO investment and making user sharing of your content seamless. We provide remote API management and real time statistics to allow you to build stable systems that alert you of issues in time to keep them from affecting users. It is easy to install and we provide 2 hours of free engineering support for test and
development. Please contact us for a free technical consult.

### Audience
Lumen Cloud Users


### Impact
After reading this article, the you should feel comfortable getting started using the aiScaler technology on Lumen Cloud.

After executing the steps in this Getting Started document, you will have a functioning virtual application delivery controller, upon which you can deploy web applications that are fast, able to handle massive traffic and secured from DDoS and other online attacks.

### Prerequisites
Prior to deploying this Blueprint please create a new server matching the below specifications:

* Server running Ubuntu 14.04, Debian 7, RHEL 7 or CentOS 7. 4CPU/8GB RAM is a good starting point
* Assigned public IP with the following open ports: 22, 80, 443


### Deploying aiScaler
You can achieve a single-button deployment of a new aiScaler instance using Lumen Cloud Blueprints.

Follow these step by step instructions to deploy aiScaler. For more details please reference
https://aiscaler.com/wiki/getting-started-centurylink.

1. Locate the Blueprint in the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for "aiMobile" in the keyword search on the right side of the page.

   <img src="../../images/aiscaler/blueprint_tile_aimobile.png" style="border:0;max-width:250px;">

2. Click the Deploy Blueprint button.

3. Set Required parameters.

   <img src="../../images/aiscaler/deploy_parameters.png" style="max-width:450px;">

   * **Execute on Server** - Select the name of the pre-existing server no which to deploy the software
   * **Edition** - Select one of aiScaler, aiProtect, or aiMobile
   * **Domain** - optionally specific the first domain
   * **Origin** - optionally specific the content origin

4. Set Optional Parameters.
   * Password/Confirm Password (This is the root password for the server. Keep this in a secure place).
   * Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).
   * Optionally set the server name prefix.
   * The default values are fine for every other option.

5. Review and Confirm the Blueprint.

6. Deploy the Blueprint.
   * Once verified, click on the **deploy blueprint** button. You will see the deployment details stating the Blueprint is queued for execution.

7. Deployment Complete.
   * Once the Blueprint has deployed you will receive an email confirming the newly deployed assets within a few minutes.
   * If you do not receive an email you may have had a deployment error - check the *Blueprints Queue* or review the *Blueprint Build Log* to for error messages.

### Pricing
The costs listed above in the above steps are for the infrastructure only. After deploying this Blueprint, you may secure entitlements to the technology using the following steps:
* aiScaler offers 30 day free trial demo licenses.
* You can find all license plans available at https://aiscaler.com/pricing. For cloud usage we recommend 1GB/s bandwidth cap.
* In order to get you license, please contact support@aiscaler.com.
* Once you obtained your license, connect over SFTP and upload the license to `/etc/aicache/license`.

  ![Install License](../../images/aiscaler/license1.png)

  ![Install License](../../images/aiscaler/license2.png)

* Either restart the server from dashboard or connect over SSH and run `service aicache restart`.

  ![Install License](../../images/aiscaler/license3.png)

  ![Install License](../../images/aiscaler/license4.png)

### Frequently Asked Questions

**Where do I obtain my license?**
aiScaler offers 30 day free trial demo licenses. You can find all license plans available at https://aiscaler.com/pricing. For cloud usage we recommend 1GB/s bandwidth cap. In order to get you license please contact support@aiscaler.com.

**Who should I contact for support?**
* For issues related to deploying aiScaler, please contact support@aiscaler.com (Skype: ai.scaler).
* For issues related to cloud infrastructure, please open a ticket using the [Lumen Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
