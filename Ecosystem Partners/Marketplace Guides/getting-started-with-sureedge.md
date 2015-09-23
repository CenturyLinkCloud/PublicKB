{{{
  "title": "Getting Started with SUREedge - Blueprint",
  "date": "9-24-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying the Pivotal Cloud Foundry (PCF) 1.5.5 on CenturyLink Cloud.

### Technology Profile

<img src="../../images/sureedge/sureline_logo.png" style="border:0;float:right;max-width: 150px;">

Sureline Systems Inc. is the provider of SUREedge, an Application Mobility Solution for Disaster Recovery (DR) and Migration that is Hardware Agnostic, Hypervisor Agnostic, and Cloud Agnostic. Sureline is the only company that fundamentally solves the problem of Any-to-Any DR and Migration, enabling seamless data migration and DR from any environment – physical or virtual – to CenturyLink Cloud.  By partnering with CenturyLink, SUREedge brings your enterprise Cloud strategy to life. 

Sureline provides the technology and solution for:

* **Onboarding/Migration to CenturyLink Cloud**
* **Disaster Recovery to CenturyLink Cloud **

SUREedge technology allows CenturyLink customers to rapidly migrate workloads from any physical or virtual system(s) into the CenturyLink Cloud, or use the CenturyLink Cloud as a DR site.


##### Customer Support

|Sales Contact   	|
|:-	|
|sales-clc@pivotal.io   	|


### Description

To use SUREedge for DR or onboarding to the Cloud, you must run an instance of SUREedge both on-prem and on-CenturyLink Cloud.   The on-prem instance provides the capability to capture and dedupe-replicate applications and data, while the on-cloud instance acts as the receiver, storage and recovery manager in the Cloud.

To create the in on-Cloud instance, use either of these two blueprints:

* SUREedge Migrator:  Use this for onboarding/migration to CenturyLink Cloud
* SUREedge-DR:  Use this for DR CenturyLink Cloud

To download and create the on-prem instance, go to [http://www.surelinesystems.com/centurylink/](http://www.surelinesystems.com/centurylink/)


### Audience

CenturyLink Cloud Users desiring: 
* Onboarding/Migration to CenturyLink Cloud
* Disaster Recovery to CenturyLink Cloud 


### Impact

After reading this article, the user should be able to:
* Install SUREedge cloud instance within CenturyLink Cloud
* Download and install on-prem SUREedge instance
* Configure on-prem and on-cloud instances
* Add clients for migration or DR 
* Create plans for migration and DR
* Execute migration/DR plans


### Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user
* Resources for running the on-prem SUREedge instance


### Postrequisites

* None


### Deploying SUREedge

You can achieve a single-button deployment of a new Cloud Foundry using CenturyLink Cloud Blueprints.  

#### Deciding Which Blueprint to Use

There are two SUREedge blueprints available: 
* SUREedge Migrator:  Use this for onboarding/migration to CenturyLink Cloud
* SUREedge-DR:  Use this for DR to CenturyLink Cloud


#### Steps to Deploy a New SUREedge Blueprint

1. **Create Server Groups**

  Prior to beginning the software install you must create two groups and assign a default network to them.

  * Create the group `OpenStack` and assign the network you've dedicated to PCF to this group
  * Create the group to hold your PCF environment and assign the network you've dedicated to PCF to this group

  <img src="../../images/sureedge/creating_clc_groups.gif" style="">

2. **Locate the Blueprint in the Blueprint Library**

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "Pivotal Cloud Foundry" in the keyword search on the right side of the page.

  > Note for access to this Blueprint during this early access period
  > # Email noc@ctl.io

  <img src="../../images/sureedge/cluster_blueprint_tiles.png" style="border:0;max-width:250px;">

3. **Click the Deploy Blueprint button.**

4. **Set Required parameters.**

  <img src="../../images/sureedge/deploy_cluster_parameters.png" style="max-width:450px;">

  * **Email Address** - Email address to receive build notification and PCF access information
  * **Deploy PCF** - We will automatically configure Operations Director (which manages Micro BOSH) and Elastic Runtime.  We can stop post-configuration for you to update settings or perform the full deploy on your behalf.
  * **Select Addons** (optional) - Select one or more add-on tiles to download and add.
  * **Current Control User Password** - Enter (and confirm) the password associated with your control.ctl.io account.

5. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  **Set the group to the value created in step (1).**  (Your specific group - not the OpenStack one)

  The default values are fine for every other option.

6. **Review and Confirm the Blueprint**

7. **Deploy the Blueprint**

  Once verified, click on the **deploy blueprint** button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within 50 to 75 minutes.  Take note that the Blueprint status may indicate deployment has completed but there will be a several minute delay until the cluster itself is ready for use as some backup install tasks may still be in process.

  <img src="../../images/sureedge/ops_mgr_blueprint_install_progress.png" style="border:0;width:70%;">

8. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets within a few minutes.  If you do not receive an email like the one shown below you may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <img src="../../images/sureedge/deploy_install_status1.png" style="border:1;margin-left:1em;width:70%;">

  Depending on how many components you've chosen to install and configure you'll receive several additional emails with configuration status updates.
  Follow the instruction in these messages to properly access your Operations Manager tool and deploy a PCF environment.

9. **Operations Manager**

  Once the status messages in the previous step indicate your environment is ready then access Pivotal Operations Manager via port 443 on your
  new server (point your web browser to **https://yourhost**).  Authenticate  with the username `admin` and using the same password you assign for
  the root account on this server.

  <img src="../../images/sureedge/ops_mgr_web_login.png" style="border:0;width:70%;">

10. **Validate Configuration**

  Navigate through the **Operations Director** and **Elastic Runtime** tiles to validate configuration.

  <img src="../../images/sureedge/ops_mgr_dashboard.png" style="border:0;width:70%;">

11. **Apply Changes**

  Click the **Apply Changes** button to begin building your PCF environment.

  Before long you should see the install status screen shown below to view deploy process details.

  <img src="../../images/sureedge/ops_mgr_install_progress.png" style="border:0;width:70%;">

  Once all PCF components have deployed you will see the following screen.

  <img src="../../images/sureedge/ops_mgr_install_complete.png" style="border:0;width:70%;">

12. **Enable public access** (optional)

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

Contact your Pivotal account manager or inquire via email to [sales-clc@pivotal.io](mailto:sales-clc@pivotal.io)

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For issues related to interacting with an already configured PCF environement review the [Pivotal KB](http://docs.pivotal.io/pivotalcf/getstarted/pcf-docs.html)
* For issues related to deploying the Pivotal PCF Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact sales-clc@pivotal.io or follow your existing Pivotal support process if known.

**My deploy failed, what next ?**

Resolution depends on which of the three phases errored during the deploy:

* Phase I - Preflight checklist
 * Review the Blueprint build log errors and make recommended corrective actions
* Phase II - Operations Manager bootstrap
 * You should remove the Operations Manager server and redeploy the blueprint.
* Phase III - Configuration and deployment
 * Advanced users can troubleshoot the settings or use BOSH to drill into errors
 * Beginner users may want to remove and redeploy the installation.  See below FAQ about how to safely delete an installation

Advanced troubleshooting is available using the BOSH tool from your Operations Manager server.  Perform the following to easily
access this tool:

* ssh to your Operations Manager host
* change the login shell for **tempest-web** from `/bin/false` to `/bin/bash`
* Execute the following commands:

  ```
  > su tempest-web
  > cd
  > alias bosh="BUNDLE_GEMFILE=/home/tempest-web/tempest/web/bosh.Gemfile bundle exec bosh"

  .... (Execute your bosh commands)
  ```


**How do I login to PCF for the first time?**

* Operations Manager web UI - When the environment deploy completes you will receive an email with a login link.  If you've lost this know that you can
  login with the username `admin` and using the same root password you set when building the server
* Operations Manager console - ssh as root and use the root password you set when building the server.  As needed create additional accounts or enable direct
  login to the **tempest-web** account
* PCF - Navigate to the Operations Manager web UI to gain access to the credential store


**How can I safely delete my PCF install?**

The PCF environment consistents of servers and persistent elastic block storage which both must be removed to eliminate all associated infrastructure
charges.

<img src="../../images/sureedge/ops_mgr_delete_install.png" style="border:0;width:70%;">

* If you have a fully functioning PCF environment, from your Ops Manager dashboard click the **gear** icon the select **delete this installation** (picture above)
* If you never performed a deploy or you have already performed the above deletion process - you may safely delete the Ops Manager server or the entire group containing it
* If your install encountered errors please send a ticker to **noc@ctl.io** requesting removal of all **System block storage services**


**How do I use my private IP for the system domain?**

Both hosts internal to the PCF environment and anyone who interacts with the system apps (dev console or the cf command line tool) but be able to resolve the
the system domain name.  These presents challenges if some of this system access will be across NATed public IP addresses (instead of the private IPs
directly associated with the server).

Should this split DNS be required implement the following:

* Create a DNS server for use by PCF components - this will resolve the system domain to the private IP address space.  For POCs we've seen this done
  by installing BIND on the Operations Manager host and pointing all DNS resolvers to this IP
* Edit the public DNS so the FQDN resolves to the NATed public IP for the HA proxy (.128 by default)


**IP Address Space for Larger Deployments**

CenturyLink Cloud provides class-C /24 address space on each of its networks, and with the exception of a few IPs at the top and bottom end of the range 
reserved for platform-level services, the entire subnet is available for use.  Some considerations:

* By default the IP space is cut in half - Ops Manager and CF have access to 128 and above and all lower addresses are reserved for other use.  This is
  implemented since both Ops Manager and CenturyLink Cloud believe they own IPAM responsibilities.
* Ops Manager subdivides this network and reserves a portion for each tile's use - this includes steady-state assignments as well as those used only
  during Errands testing.  In production this means the IP-range can quickly fill up even though there is actually space available
* Gain IP space by deploying initially using the following approach:
 * Set the *OpenStack* group's default network to network A.  This will move your Elastic Block Storage services onto a different network segment.
 * Set the group containing your servers to network B.  Make sure network B is not your first network defined in your primary datacenter.
 * Configure Ops Director to use from .12 all the way to .230.


**What are some known limitations?**

* Accounts requiring two-factor authentication cannoit successfully deploy PCF.  Create a new service account dedidicated to PCF.


