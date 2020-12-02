{{{
  "title": "Getting Started with SUREedge - Blueprint",
  "date": "09-30-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}

<img src="../../images/sureedge/sureline_logo.png" style="border:0;float:right;max-width: 150px;">

### Technology Profile
Sureline Systems Inc. is the provider of SUREedge, an Application Mobility Solution for Disaster Recovery (DR) and Migration that is Hardware Agnostic, Hypervisor Agnostic, and Cloud Agnostic. Sureline is the only company that fundamentally solves the problem of Any-to-Any DR and Migration, enabling seamless data migration and DR from any environment – physical or virtual – to Lumen Cloud. By partnering with Lumen, SUREedge brings your enterprise Cloud strategy to life.

Sureline provies the technology and solution for:

* **Onboarding/Migration to Lumen Cloud**
* **Disaster Recovery to the Lumen Cloud**

SUREedge technology allows Lumen customers to rapidly migrate workloads from any physical or virtual system(s) into the Lumen Cloud, or use the Lumen Cloud as a DR site.

##### Customer Support
|Sales Contact |
|:-	|
|info@surelinesystems.com |

### Description
To use SUREedge for DR or onboarding to the Cloud, you must run an instance of SUREedge both on-prem and on-Lumen Cloud. The on-prem instance provides the capability to capture and dedupe-replicate applications and data, while the on-cloud instance acts as the receiver, storage and recovery manager in the Cloud.
To create the on-Cloud instance, use either of these two Blueprints:
* SUREedge Migrator:  Use this for on boarding/migration to Lumen Cloud.
* SUREedge DR:  Use this for DR Lumen Cloud.

To download and create the on-prem instance, go to [http://www.surelinesystems.com/centurylink/](http://www.surelinesystems.com/centurylink/)

### Audience
Lumen Cloud Users desiring:
* Onboarding/Migration to Lumen Cloud
* Disaster Recovery to Lumen Cloud

### Impact
After reading this article, the user should be able to:
* Install SUREedge cloud instance within Lumen Cloud
* Download and install on-prem SUREedge instance
* Configure on-prem and on-cloud instances
* Add clients for migration or DR
* Create plans for migration and DR
* Execute migration/DR plans

### Prerequisites
* On-Prem:
 * Resources on a VM infrastructure for running the on-prem SUREedge instance. Popular VM infrastructures, such as VMware, Hyper-V or KVM are supported.
 * A Windows (Windows 8.x, Windows Server 2008 or later) VM running within the VM infrastructure described in Prerequisite 1.
* On-Lumen Cloud:
 * Access to the Lumen Cloud platform as an authorized user.
 * A license for a Windows VM in Lumen Cloud.

### Postrequisites
* None

### Deploying SUREedge
You can achieve a single-button deployment of a new SUREedge instance using Lumen Cloud Blueprints.

#### Deciding Which Blueprint to Use
There are two SUREedge Blueprints available:
* SUREedge Migrator: Use this for onboarding/migration to Lumen Cloud.
* SUREedge DR: Use this for DR to Lumen Cloud.

#### Steps to Deploy a New SUREedge Blueprint
1. Locate the Blueprint in the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.
   * Search for 'SUREedge' in the keyword search on the right side of the page.
   * Select either 'SUREedge Migrator' or 'SUREedge DR'.

2. Click the `deploy blueprint` button.

3. Set Required parameters.
   * **MC Password** - Repeat the root administrator credentials already given for the server.

4. Set Optional Parameters.
   * Password/Confirm Password (This is the root password for the server. Keep this in a secure place).
   * Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).
   * Optionally set the server name prefix.
   * The default values are fine for every other option.
   * *Make note of the two hostnames you specified above and the MC password. These will be needed later to log into and configure your SUREedge instances.*

5. Review and Confirm the Blueprint.

6. Deploy the Blueprint.
   * Once verified, click the `deploy blueprint` button.
   * You will see the deployment details stating the Blueprint is queued for execution.

7. Deployment Complete.
   * Once the Blueprint has deployed you will receive an email confirming the newly deployed assets within a few minutes.
   * If you do not receive an email you may have had a deployment error - check the *Blueprints Queue* or review the *Blueprint Build Log* to for error messages.
   * You will see two VMs running, a Windows VM and a Linux VM. The Windows VM is referred to as the `SUREedge-MC` and Linux VM as `SUREedge-Stor`.
   * Login to the [Control Portal](https://control.ctl.io) and find the public IP addresses of these two systems - you will need these later.

8. **Sizing** (optional)
   * Review the capacity planning guide available at http://www.surelinesystems.com/centurylink/ to help size the SUREedge instance correctly for your use case.

9. Complete On-Premises SUREedge Component Installation.
   * Login to the Windows VM on which you intend to install the on-prem instance of the SUREedge-MC.
   * Download the software from http://www.surelinesystems.com/centurylink/. Login to your Sureline account, or register if you are new.
   * Install the software.
   * *Note the IP address of the Windows system where you installed the on-prem SUREedge-MC module and username and password during the installation. You will need these later to login to the application.*
   * NOTE: Review the capacity planning guide to help size the SUREedge-Stor VM. Your license file will be sent by email to you by Sureline team.

10. Logging onto the on-prem instance and initiating Migration.
   * Use any browser (Firefox recommended) to connect to the IP address of the on-prem SUREedge-MC. Login using the username and password you applied during the installation.

11. Your next step is to link the two instances of the SUREedge.
   * Click on Settings → Cloud or Remote → Remote
   * Enter the Public IP/FQDN, username and password of the on-cloud SUREedge-Stor of that you noted earlier while creating the Blueprint image.
   * You are now ready to add clients and start migration. Refer to the user guide available at http://www.surelinesystems.com/resources/ on how to add clients, create plans, initiate migration, etc.

12. Logging onto the on-Cloud instance and Recovering.
   * Use any browser (Firefox recommended) to connect to the public IP address of the on-cloud SUREedge-MC instance. Login using the username and password you specified while deploying the Blueprint.
   * You will be now able to recover systems that have been replicated to Lumen Cloud.
   * Refer to the [User Guide](http://www.surelinesystems.com/resources/) on how to recover a system.

### Pricing
The costs listed above in the above steps are for the infrastructure only. After deploying this Blueprint, you may secure entitlements to the technology using the following steps:
* Email: info@surelinesystems.com

### Frequently Asked Questions

**Where do I obtain my license?**
Contact info@surelinesystems.com.

**Who should I contact for support?**
* For issues related to deploying SUREedge, visit [Sureline Support](http://www.surelinesystems.com/support/).
* For issues related to cloud infrastructure, please open a ticket using the [Lumen Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
