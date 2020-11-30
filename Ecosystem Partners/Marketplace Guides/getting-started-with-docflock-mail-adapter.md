{{{
  "title": "Installing docflock email adapter on Windows Blueprint",
  "date": "08-31-2016",
  "author": "John Baldwin",
  "attachments": [],
  "contentIsHTML": false
}}}

![docflock logo](../../images/docflock-logo.png)

### Product Profile

docflock is a cloud based, healthcare focused documentation management and health data management platform.  docflock can ingest data and documents from virtually any health information system via various adapters.  The docflock email adapter is a service that allows for email accounts to be watched/monitored.  The adapter takes in emails and attachments, formats them as a PDF document and uploads them to the docflockDM repository for future utility.  Use cases for this email adapter include lab report receipt and upload, orders receipt and upload, referrals receipt and upload.



### Audience
Lumen Cloud Users

### Impact
After reading this article, the user should be able to download and provision a docflock email adapter.


### Prerequisite
- Access to the Lumen Cloud platform as an authorized user.
- Access to [docflock.com](http://docflock.com/) as an authorized user.

### Postrequisite

To access your application from a computer outside the Lumen Cloud network, perform the following tasks after you receive the email notifying you that the Blueprint completed successfully:
  1. [Add a Public IP](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal
  2. [Allow incoming traffic](../../Network/CenturyLink Cloud/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal and configuring appropriately.
    * The default ports to access the application are: 80, 443

### Deploying the Email Adapter Blueprint v4 job

#### Steps to Deploy
1. Locate the “Email Adapter” job
  1. Log into Lumen control portal
  2. Open Orchestration > Blueprints Library
  3. Filter by Author: Simplicity Health Systems
  4. Select “Email Adapter Blueprint v4 ATB”
2. Choose and deploy the Job
  1. Click “Deploy Blueprint”
3. Complete form field values as provided by Simplicity Health Systems
  1. Enter form field value as provided by Simplicity Health Systems for our account
  2. After Step 3 of the data input wizard, click “Deploy Blueprint” to enqueuer the provisioning job
4. Monitor the queue for progress
5. Complete

### Access your Docflock Email Adapter server
After your job deploys successfully, please follow these instructions to access your server:

* Connect to your server using credentials provided by Lumen.

### Licensing/Pricing
docflock email adapters work only with active docflockDM account holders.  Contact sales@docflock.com for pricing.

### About Simplicity Health Systems
Lumen Cloud works with [Simplicity Health Systems](http://www.docflock.com) to provide HIPAA compliant health content management and health interoperability services.


### Frequently Asked Questions

**Q: What types of files can the email adapter handle?**

A: .pdf, .png, .tif, .jpg. .jpeg

**Q:Are there file size limitations for the email adapter?**

A: The adapter can handle any file size that is supported by the email system.  

**Q: Are there limitations to the type of email accounts that the email adapter can monitor?**

A: There are no limitations.


#### Who should I contact for support?
* For issues related to deploying the docflock email adapter Blueprint on Lumen Cloud, licensing or accessing the deployed software, please visit the [docflock Support Website](http://support.docflock.com)

* For issues related to cloud infrastructure (VM's, network, etc), or if you experience a problem deploying the Blueprint or Script Package, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the Lumen Cloud Support website](https://t3n.zendesk.com/tickets/new).
