{{{
  "title": "Getting Started with Appcito CAFE - Blueprint",
  "date": "9-28-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Technology Profile

<img src="../../images/appcito/appcito_logo.png" style="border:0;float:right;max-width: 150px;">

**TODO**

http://www.appcito.com


##### Customer Support

|Sales Contact   	|
|:-	|
|**TODO**@appcito.com   	|


### Description

**TODO**


### Audience

CenturyLink Cloud Users


### Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user


### Postrequisites

* A functioning account on the Appcito platform http://cafe18stage.appcito.com/#signup


### Steps to Deploy a New Appcito ADC

1. **Locate the Blueprint in the Blueprint Library**

 Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "Appcito" in the keyword search on the right side of the page.

  <img src="../../images/appcito/cluster_blueprint_tiles.png" style="border:0;max-width:250px;">

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="../../images/appcito/deploy_parameters.png" style="max-width:450px;">

  * **Cluster Name** - TODO
  * **Account Name** - TODO
  * **Control User Password** - The password associated with your control.ctl.io login

4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the **deploy blueprint** button. You will see the deployment details stating the Blueprint is queued for execution.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets within a few minutes.  If you do not receive an email like the one shown below you may have had a deployment error - review the *Blueprint Build Log* to for error messages.

8. **Complete Activation**

 * Login to your newly created server and take note of the *Appcito Activation Key* displayed on login:

   ```
   Welcome to Appcito PEP image built on Wed Sep 23 17:47:37 UTC 2015

   Appcito Activation Key:  630377EA-621B-11E5-B289-5B1EDFA4CB8D
   Please signup/login into your account at http://cafe18stage.appcito.com to activate Appcito Load balancer
   ```
 * [Login to your existing Appcito account](http://cafe18stage.appcito.com/) or [sign up for a new one](http://cafe18stage.appcito.com/#signup)
 * Click on `My Account` then click on `Activate PEP`
   ![Activate Pep]("../../images/appcito/activate_pep.png")


### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

 * Email: **TODO**@appcito.com

### Frequently Asked Questions

**Where do I obtain my license?**

Contact **TODO**@appcito.com.

**Who should I contact for support?**

* For issues related to deploying Appcito, visit **TODO**.
* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
