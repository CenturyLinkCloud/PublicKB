{{{
  "title": "Getting Started with XtremeData dbX - Blueprint",
  "date": "3-6-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/xtremedata/xtremelog_wht.png" style="max-width:200px;border:0;float:right;">

XtremeData – “On-Demand Big Data Analytics with real-time ingest."

http://www.xtremedata.com/

#####Customer Support

|Sales Contact      |
|:- |
|centurylinkcloud-sales@xtremedata.com       |


### Description

XtremeData has integrated their dbX technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this XtremeData solution.

XtremeData delivers high performance, full-featured ANSI SQL database engine designed for performance at all scales, up to 100s of terabytes. ANSI SQL. Simple to deploy, simple to administer, simple to scale up. Any data schema any data location.

Learn more from our discussion with Ravi Chandran, XtremeData's CTO:

<iframe width="560" height="315" src="https://www.youtube.com/embed/1LO2TIOvJGw" frameborder="0" allowfullscreen style="margin-left:1em;"></iframe>


### Audience

CenturyLink Cloud Users


### Deploying a New Cluster

Single button deploy of a new cluster including a master host, a standby master for failover, and two nodes.  For best performance these should be deployed on Hyperscale servers.

#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Determine whether you will be building a test cluster with small nodes or a production cluster whose nodes that have increased CPU and RAM available.

  <img src="/knowledge-base/images/xtremedata/dbx_blueprint_tile.png" style="margin-left:1em;border:0;max-width:250px;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for `dbX Cluster` in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="/knowledge-base/images/xtremedata/dbx_deploy_parameters.png" style="margin-left:1em;max-width:450px;">

  * **Head Server** - Select the first option `DBXHD`
  * **Cluster Name** - set unique identifier for all hosts in this cluster
  * **Notification Email** - Email address to receive build notification and dbX access information
  * **SMTP server info** (optional) Send messages through specific mail server
  * **Debug** (optional) Use under XtremeData support guidance


4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment times may very - wait the build queue for up to date deployment status.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* for error messages.

  <img src="/knowledge-base/images/xtremedata/dbx_deploy_success_email.png" style="border:0;">

8. **Access Web xdAdmin Console**

  Access the xdAdmin web console via https on port 2400.  Authenticate using your root user and associated credentials.

  <img src="/knowledge-base/images/xtremedata/web_gui_screenshot.png" style="border:0;">

9. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For access from the Internet at large add a public IP to your master server.

  <a href="../../Network/how-to-add-public-ip-to-virtual-machine.md">
    <img style="border:0;width:50px;vertical-align:middle;" src="../../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>



### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

 * Email: centurylinkcloud-sales@xtremedata.com

### Frequently Asked Questions

**Where do I obtain my license?**

*More to come soon*

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For issues related to deploying the XtremeData dbX Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact centurylinkcloud-sales@xtremedata.com or follow your existing XtremeData support process if known.


**How do I learn more about the application?**

View XtremeData's [documentation and other support resources](http://www.xtremedata.com/support).
