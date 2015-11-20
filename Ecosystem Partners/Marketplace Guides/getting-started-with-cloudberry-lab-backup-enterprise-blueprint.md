{{{
  "title": "Getting Started with CloudBerry Lab Backup Enterprise - Blueprint",
  "date": "9-21-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

![CloudBerry Logo](../../images/ecosystem-CloudBerry-logo.png)

### Partner Profile
CloudBerry Lab - Provides data backup solutions that allow backing up to all top cloud storage services.
[http://www.CloudBerryLab.com](http://www.CloudBerryLab.com

#### Contact CloudBerry Lab
##### Customer Sales and Support:
- Support Email - [support@CloudBerryLab.com](mailto:support@cloudberrylab.com)
- Support Telephone - (212) 863 9918
- Sales Email - [sales@CloudBerryLab.com](mailto:sales@cloudberrylab.com)
- Sales Telephone - (212) 863 9918

### Description
CloudBerry Lab has integrated their backup technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Backup to Cloud Object Storage solution.

The evolution of cloud  technology saw cloud storage as a great tool to offload on premise storage economics into the cloud. Thanks to ever-increasing Internet bandwidth and declining storage prices, keeping backups in the cloud has become a viable alternative to traditional on-site data storage for SMBs. Many companies often overlook key considerations when it comes to online backup:
  * Reliable Storage. When moving backup data offsite, a company should ensure the cloud storage service is reliable, cost-effective, yet high-performing.
  * Data Security. Security is a top concern when business data is taken to the cloud. Company's private data could be compromised if the solution lacks the right features.
  * Restore Capabilities. Backup data stored at a remote facility should be always at a recoverable state, accessible at any time, and allow point-in-time object-level restore.


### Solution Overview
CloudBerry Backup is a reliable, powerful and affordable cloud backup solutions that is fully compatible with CenturyLink object storage. In addition to offering real-time and/or scheduled regular backups, it allows you to:
  * Store backups in a CenturyLink user-owned account
  * Encrypt data via 256-bit AES encryption with user-controlled password 
  * Check backup consistency to ensure data is in a recoverable state
  * Free restores No need for a commercial license to restore data

Technology from CloudBerry Lab helps CenturyLink Cloud customers address the business challenge of secure and easy-to-use backup-to-cloud  by implementing Cloudberry Lab backup  solution - now available as part of the CenturyLink Cloud Blueprint Engine.

### Offer
CloudBerry Labs has included a free, 15-day trial license with the Blueprint deployment.  Users can try the software during that time period without restriction.

### Audience
CenturyLink Cloud Users, Administrators, Engineer, Backup Operators, Storage Enthusiasts

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud.

After executing the steps in this Getting Started document, the users will have a functioning backup-agent installed on virtual server upon which they can start backuping their data to Centurylink Object Storage.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Existing Windows Platform server to deploy to
- Configure the VPN access to the virtual server 

### Deploy CloudBerry Labs Cloud Storage Tools Blueprint
Follow these step by step instructions to deploy Cloudberry Backup Enterprise Edition on your server and connect to you Centurylink Object Storage account. 

1.	Open the Blueprint Library.
- Access your Blueprint Library by selecting the “Blueprints Library” under the Blueprints heading from the green drop down menu.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-1.png)

2.	Search for the Blueprint.
- To search for the blueprint, type “Cloudberry Backup Enterprise for Desktop and Server” under “Refine Results” in the right panel and click the “Go” button.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-2.png)

3.	Choose the Blueprint. 
- Click on the Blueprint titled “CloudBerry Backup Enterprise for Desktop and Server”

  [CloudBerry Image](../../images/ecosystem-CloudBerry-3.png)

4.  Deploy the Blueprint.
- Click on the “Deploy Blueprint” button to begin configuring your installation.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-4.png)

5.	Configure the Blueprint. 
- On the first page, “Customize Blueprint”, ensure the following options are configured:
  - Choose the server, you would like to install Cloudberry Backup Enterprise on.
  - Enter the e-mail, which you would like to use for trial activation.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-5.png)

  - Then select "Next Step"

  [CloudBerry Image](../../images/ecosystem-CloudBerry-6.png)

6.	Review and Confirm the Blueprint. 
- You will come to a confirmation view of what your Blueprint looks like.
- Verify your configuration details.
- Then click the green “deploy Blueprint” button at the bottom.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-7.png)

7.	Monitor the Activity Queue.
- After clicking Deploy Blueprint, the job will be submitted into a queue and you will be taken to a monitoring page where you can see the progress of each step the Blueprint goes through.  

  [CloudBerry Image](../../images/ecosystem-CloudBerry-8.png)

- You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-9.png)

6.	Jump In! 
- Once the Blueprint completes successfully, you will receive an email stating that the Blueprint build is complete. Please do not use the application until you have received this email notification. 

### Access and use Nexus Chameleon
Follow these steps to access and use the CloudBerry software

1.	Access the VM
- Please, log in to your server using the VPN Access.  

2. Launch the software
- You will see a Cloudberry Backup Enterprise Edition Icon on the desktop.  Double click it to launch.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-10.png)

3. Add an account.  Go to “File” > “Add new account”:
  [CloudBerry Image](../../images/ecosystem-CloudBerry-11.png)

4. Choose S3 Compatible.  

  [CloudBerry Image](../../images/ecosystem-CloudBerry-12.png)

5. You’ll be requested to enter your CenturyLink Cloud Storage account credentials.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-13.png)

6. To add CenturyLink Cloud Storage: Via your web browser, in your CenturyLink Cloud Portal, navigate to “Object Storage” in the top menu.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-14.png)

7. Press “Create the bucket”, then enter the bucket name.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-15.png)

8. Go to the bucket properties.

  [CloudBerry Image](../../images/ecosystem-CloudBerry-16.png)

9. Copy the endpoint without bucket name paste it to the account credentials window in Cloudberry Backup:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-17.png)

10. Paste it to the account credentials window in Cloudberry Backup > Service point:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-18.png)

11.	Go back to the buckets window and choose the tab “Users”:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-19.png)

12.	Choose the user:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-20.png)

13.	Copy your secret and access keys:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-21.png)

14.	Paste your secret and access keys to the account credentials window in Cloudberry Backup and enter any Display name you like:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-22.png)

15. Now you can see all the buckets you have created through your Centurylink dashboard and create new buckets. Then press “ok”:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-23.png)

16.	To start creating your first backup plan, press the button “Files”, proceed to second step and choose the S3 Compatible connection option and then the connection you have created:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-24.png)

17.	All further information you can in the Help topics:

  [CloudBerry Image](../../images/ecosystem-CloudBerry-25.png)

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no CloudBerry Labs license costs or additional fees bundled in.    

By the first run of Cloudberry Backup you activate the free trial, which is valid for 15 days. As soon as the trial expires, you’ll be able to buy the license online using your credit card. You can also purchase it anytime through Cloudberrylab.com by visiting [this link](http://www.cloudberrylab.com/enterprise-cloud-backup-software.aspx).

### Frequently Asked Questions

#### Where do I get my full CloudBerry License?
You can purchase online by visiting [this link](http://www.cloudberrylab.com/enterprise-cloud-backup-software.aspx)

#### Who should I contact for support?
* For issues directly related to the CloudBerry software or licensing, please contact [support@CloudBerryLab.com](mailto:support@cloudberrylab.com) or via telephone: (212) 863 9918
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new) 