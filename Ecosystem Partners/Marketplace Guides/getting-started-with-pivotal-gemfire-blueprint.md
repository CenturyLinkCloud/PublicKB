{{{
  "title": "Getting Started with Pivotal GemFire - Blueprint",
  "date": "3-17-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying the Pivotal GemFire in-memory database on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/pivotal_gemfire/product-pivotal-gemfire.png" style="border:0;float:right;">

Pivotal GemFire – “in-memory distributed database for high scale custom applications”

http://pivotal.io/big-data/pivotal-gemfire

#####Customer Support

|Sales Contact   	|
|:-	|
|sales-clc@pivotal.io   	|


### Description

Pivotal has integrated their GemFire technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this GemFire solution.

Pivotal GemFire is an in-memory distributed database for high scale custom applications. GemFire provides in-memory access for all operational data spread across hundreds of nodes with a “shared nothing” architecture. This enables GemFire to provide low latency data access to applications at massive scale with many concurrent transactions involving terabytes of operational data. Designed for maintaining consistency of concurrent operations across its distributed data nodes, Pivotal GemFire can support ACID transactions for massively scaled applications such as stock trading, financial payments and ticket sales in proven customer deployments of more than 10 million user transactions a day.


### Audience

CenturyLink Cloud Users


### Deploying on an existing server

The GemFire Blueprint is designed to be successfully deployed on an existing server.  This let's you choose the exact server size needed to suit your deployment use case.  

#### Steps


1. **Deploy or Identify an Existing Server**

  Identify the server targeted for GemFire installation.  Pivotal requires the server be CentOS or RHEL 5, 6, or 7.

  See the [Creating a new enterprise cloud server](../../Servers/creating-a-new-enterprise-cloud-server.md) KB for more information on completing this step.

2. **Locate the Blueprint in the Blueprint Library**

  Determine whether you will be building a test cluster with small nodes or a production cluster whose nodes are configured with increased CPU and RAM.

  <img src="/knowledge-base/images/pivotal_gemfire/gemfire_blueprint_tile.png" style="border:0;max-width:250px;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for “Pivotal GemFire in the keyword search on the right side of the page.

3. **Click the Deploy Blueprint button.**

4. **Set Required parameters.**

  <img src="/knowledge-base/images/pivotal_gemfire/deploy_parameters.png" style="max-width:450px;">

  * **EULA** - Click to accept the software end user license agreement
  * **Email Address** - Email address to receive build notification and GemFire access information
  * **Start Locator and Server** - Start an initial locator and server on this host.  Skip this if you'd prefer to create your own configuration

  <img src="/knowledge-base/images/pivotal_gemfire/deploy_parameters_server.png" style="max-width:450px;">

  * **Execute on Server** - Select the server on which to execute the Blueprint

5. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  It is also used to identify the `gemfire` user for Web Control Center access.

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

6. **Review and Confirm the Blueprint**

7. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within five minutes.

8. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <img src="/knowledge-base/images/pivotal_gemfire/deploy_complete_email.png" style="border:0;width:70%;">

9. **Pulse Web Tool** (optional)

  If you elected start the initial locator and server then you will also have immediate access to the Pulse web tool via http on port 7070.  Authenticate using the `admin`/`admin` credentials

  <img src="/knowledge-base/images/pivotal_gemfire/web_pulse.png" style="border:0;">

10. **gfsh Access** (optional)

  Access the server with the user `gemfire` and your administrative credentials.  The environment has been configured so you can execute `gfsh` immediately.  New to GemFire? Review [Pivotal GemFire in 15 minutes or Less](http://gemfire.docs.pivotal.io/latest/userguide/index.html#getting_started/15_minute_quickstart_gfsh.html) to get started.

  ```
  [gemfire@localhost ~]$ gfsh
    _________________________     __
       / _____/ ______/ ______/ /____/ /
         / /  __/ /___  /_____  / _____  /
          / /__/ / ____/  _____/ / /    / /
          /______/_/      /______/_/    /_/    v8.1.0

  Monitor and Manage GemFire
  gfsh>
  ```

11. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For access from the Internet at large add a public IP to your master server.

  <a href="../../Network/how-to-add-public-ip-to-virtual-machine.md">
    <img style="border:0;width:50px;vertical-align:middle;" src="../../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>



### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

 * Email: sales-clc@pivotal.io

### Frequently Asked Questions

**Where do I obtain my license?**

Contact your Pivotal account manager or inquire via email to [centurylinkcloud-sales@pivotal.io](mailto:centurylinkcloud-sales@pivotal.io)

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For issues related to interacting with a GemFire cluster review the [Pivotal KB](https://support.pivotal.io/hc/en-us/categories/200072748-Pivotal-GemFire-Knowledge-Base)
* For issues related to deploying the Pivotal GemFire Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact sales-clc@pivotal.io or follow your existing Pivotal support process if known.


**How do I learn more about the application?**

View [Pivotal GemFire in 15 minutes or Less](http://gemfire.docs.pivotal.io/latest/userguide/index.html#getting_started/15_minute_quickstart_gfsh.html) to get started.

**How do I login to my cluster for the first time?**

Access your new Pivotal GemFire cluster via ssh as the `gemfire` user using the server default administrative credentials.
