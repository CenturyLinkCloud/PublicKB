{{{
  "title": "Getting Started with Cloudberry Lab Backup Ultimate - Blueprint",
  "date": "12-29-2017",
  "author": "<a href='https://twitter.com/EvgenyRudinsky'>@EvgenyRudinsky<a/>",
  "attachments": [],
  "contentIsHTML": false
}}}

### Partner Profile
[CloudBerry Lab](http://www.cloudberrylab.com) - Provides data backup solutions that allow backing up to all top cloud storage services.

![CloudBerry Lab - # 1 Cross Platform Cloud Backup](../../images/cloudberrylab/cloudberrylab-logo.png)


### Contact Cloudberry lab
##### Customer Sales and Support:
* Customer support
  * Email: [support@cloudberrylab.com](mailto:support@cloudberrylab.com)
  * Telephone:  US 1 (415) 301 7773 ext 1
* Solution Architects group
  * Email: [sa-team@cloudberrylab.com](mailto:sa-team@cloudberrylab.com)
  * Telephones: US 1 (917) 720 3791; UK 44 (0) 20 7193 0300
* Sales team
  * Email: [sales@cloudberrylab.com](mailto:sales@cloudberrylab.com)
  * Telephone: US 1 (415) 301 7773 ext 2

### Description
CloudBerry Lab has integrated their backup technology with the Lumen Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Backup to Cloud Object Storage solution.

The evolution of cloud  technology saw cloud storage as a great tool to offload on premise storage economics into the cloud. Thanks to ever-increasing Internet bandwidth and declining storage prices, keeping backups in the cloud has become a viable alternative to traditional on-site data storage for SMBs. Many companies often overlook key considerations when it comes to online backup:
* Reliable Storage. When moving backup data offsite, a company should ensure the cloud storage service is reliable, cost-effective, yet high-performing.
* Data Security. Security is a top concern when business data is taken to the cloud. Company's private data could be compromised if the solution lacks the right features.
* Restore Capabilities. Backup data stored at a remote facility should be always at a recoverable state, accessible at any time, and allow point-in-time object-level restore.


### Solution Overview
CloudBerry Backup is a reliable, powerful and affordable cloud backup solutions that is fully compatible with Lumen object storage. In addition to offering real-time and/or scheduled regular backups, it allows you to:
* Store backups in a Lumen user-owned account.
* Encrypt data via 256-bit AES encryption with user-controlled password.
* Check backup consistency to ensure data is in a recoverable state.
* Free restores No need for a commercial license to restore data.

Technology from CloudBerry Lab helps Lumen Cloud customers address the business challenge of secure and easy-to-use backup-to-cloud by implementing Cloudberry Lab backup solution - now available as part of the Lumen Cloud Blueprint Engine.

### Offer
CloudBerry Labs has included a free, 15-day trial license with the Blueprint deployment. Users can try the software during that time period without restriction.

### Audience
Lumen Cloud Users, Administrators, Engineer, Backup Operators, Storage Enthusiasts

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on Lumen Cloud.

After executing the steps in this Getting Started document, the users will have a functioning backup-agent installed on a virtual server upon which they can start backing up their data to Lumen Object Storage.

### Prerequisite
* Access to the Lumen Cloud platform as an authorized user.
* Existing Windows Platform server to deploy to.
* Configure the VPN access to the virtual server.

### Deploy CloudBerry Labs Software via Blueprint
Follow these step by step instructions to deploy Cloudberry Backup Ultimate Edition on your server and connect to you Lumen Object Storage account.

1. Open the Blueprint Library.
   * Login to the Control Portal. From the Nav Menu on the left, click **Orchestration > Blueprints Library**.

2. Search for the Blueprint.
   * To search for the Blueprint, type “Cloudberry Backup Ultimate Server” under “Refine Results” in the right panel and click the `Go` button.

3. Choose the Blueprint.
   * Click on the Blueprint titled “CloudBerry Backup Ultimate Server”.

4. Deploy the Blueprint.
   * Click the `deploy blueprint` button to begin configuring your installation.

5. Configure the Blueprint.
   * On the first page, “Customize Blueprint”, ensure the following options are configured.
   * Choose the server, you would like to install Cloudberry Backup Ultimate on.
   * Then, click `next step 2`.

6. Review and Confirm the Blueprint.
   * You will come to a confirmation view of what your Blueprint looks like.
   * Verify your configuration details.
   * Then, click `deploy blueprint`.

7. Monitor the Activity Queue.
   * After clicking Deploy Blueprint, the job will be submitted into a queue and you will be taken to a monitoring page where you can see the progress of each step the Blueprint goes through.
   * To monitor progress, click **Queue** from the Nav Menu on the left.

8. Jump In! once the blueprint job completes.

### Access and use Cloudberry
Follow these steps to access and use the CloudBerry software.

1. Access the VM.
   * Please, log in to your server using the VPN Access.

2. Launch the software.
   * You will see a Cloudberry Backup Ultimate Edition Icon on the desktop.
   * Double click it to launch.
   * If you plan to leverage the trial features select the **Start Trial** button and follow the instructions. Otherwise, input your license key.

    ![Cloudberry Ultimate Backup for Windows](../../images/cloudberrylab/cloudberrylab-ultimate-backup.jpg)

3. Add an account.
   * Go to “File” > “Add new account”.

    ![Cloudberry Ultimate backup - Acc New Account](../../images/cloudberrylab/cloudberrylab-ultimate-backup-add-account.jpg)

4. Choose Lumen

    ![Cloudberry Ultimate Backup - select cloud storage Lumen](../../images/cloudberrylab/cloudberrylab-select-cloud-storage-centurylink-focused.jpg)

5. You’ll be requested to enter your Lumen Cloud Storage account credentials.

  ![Cloudberry Lab Ultimate Backup Lumen Configuration](../../images/cloudberrylab/cloudberrylab-add-new-storage-account-centurylink-access-credentials.jpg)

6. To add Lumen Cloud Storage: Via your web browser, in your Lumen Cloud Portal, navigate to “Object Storage” in the top menu.

  ![CTL control panel - select object storage](../../images/cloudberrylab/ctl-control-panel-object-storage.jpg)

7. Press “Create the bucket”, then enter the bucket name.

  ![CTL control panel create bucket](../../images/cloudberrylab/ctl-control-panel-object-storage-create-bucket.jpg)

8. Go to the bucket properties.

  ![CTL control panel bucket properties](../../images/cloudberrylab/ctl-control-panel-bucket-properties.jpg)

9. Copy the endpoint without bucket name paste it to the account credentials window in Cloudberry Backup.

  ![CTL getting bucket endpoint, control panel](../../images/cloudberrylab/ctl-control-panel-getting-bucket-endpoint.jpg)

10. Paste it to the account credentials window in Cloudberry Backup > Service point.

  ![Cloudberry Lab - service endpoint for Lumen](../../images/cloudberrylab/cloudberrylab-centurylink-endpoint.jpg)

  The list of service points are available [in our knowledgebase.](../../Storage/Object Storage/object-storage-regions-and-service-points.md)

11.	Go back to the buckets window and choose the tab “Users”.

  ![CTL - user management](../../images/cloudberrylab/ctl-control-panel-user-management.jpg)

12.	Choose the user.

  ![CTL - select user](../../images/cloudberrylab/ctl-control-panel-select-user.jpg)

13.	Copy your secret and access keys.

  ![CTL getting users credentials](../../images/cloudberrylab/ctl-user-credentials.jpg)

14.	Paste your secret and access keys to the account credentials window in Cloudberry Backup and enter any Display name you like.

  ![Cloudberry Ultimate Backup - storage account configuration (access / secret key pair)](../../images/cloudberrylab/cloudberrylab-centurylink-storage-account-configuration.jpg)

15. Now you can see all the buckets you have created through your Lumen dashboard and create new buckets.
   * Select existing bucket or create new and press "OK".

      ![Cloudberry Ultimate Backup - list and create bucket for Lumen](../../images/cloudberrylab/cloudberrylab-centurylink-list-create-bucket.jpg)

16.	To start creating your first backup plan, press the button “Files”.

    * Proceed to the second step and choose the "Lumen" option.
    * Then the connection you have created.

        ![Cloudberry Ultimate Backup - select Lumen account](../../images/cloudberrylab/cloudberrylab-backup-to-centurylink-account.jpg)

17.	All further information you can in the Help topics:

### Pricing
The costs associated with this Blueprint deployment are for the Lumen Cloud infrastructure only. There are no CloudBerry Labs license costs or additional fees bundled in.

By the first run of Cloudberry Backup you activate the free trial, which is valid for 15 days. As soon as the trial expires, you’ll be able to buy the license online using your credit card. You can also purchase it anytime through Cloudberrylab.com by visiting [this link](http://www.cloudberrylab.com/enterprise-cloud-backup-software.aspx).

### Frequently Asked Questions

#### Where do I get my full CloudBerry License?
You can purchase online by visiting [this link](http://www.cloudberrylab.com/enterprise-cloud-backup-software.aspx).

#### Who should I contact for support?
* For issues directly related to the Cloudberry lab software or licensing, please contact [support@CloudBerryLab.com](mailto:support@cloudberrylab.com) or via telephone: US 1 (415) 301 7773.
* For issues related to cloud infrastructure (VMs, network, etc.), or if you experience a problem deploying the Blueprint, please open a Lumen Cloud Support ticket by emailing [help@ctl.io](mailto:help@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new).
