{{{
  "title": "Getting Started with Acumatica ERP - Blueprint",
  "date": "1-20-2015",
  "author": "Bob Stolzberg",
  "attachments": [],
  "contentIsHTML": false
}}}

### Partner Profile
Acumatica - cloud accounting software and cloud ERP software for your small to midsize business that helps you unlock your business potential [www.Acumatica.com](http://www.Acumatica.com)

#### Acumatica Support
Please use the contact page on the Acumatica website
* Sales Inquiries - (888) 228-8300
* General Inqueries - info@acumatica.com

### Description
Acumatica has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Cloud ERP solution.

### Audience
CenturyLink Cloud Users

### Impact
After reading this article, the user should feel comfortable getting started using the Acumatica technology on CenturyLink Cloud.

### Prerequisite
Access to the CenturyLink Cloud platform as an authorized user.

### Additional Resources
Acumatica Knwoledge Base Article - [Getting Started with Acumatica ERP Blueprint](http://adn.acumatica.com/forums/topic/getting-started-acumatica-erp-centurylink/)

### Detailed Steps
Follow these step by step instructions to get started with a single-server Acumatica ERP deployment.

1. Locate the Blueprint in the Blueprint Library.
  1. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library.
  2. Search for “Acumatica” in the keyword search on the right side of the page.
  3. Click the “Install Acumatica ERP” blueprint.

2. Choose the Blueprint. Click on the "Deploy Blueprint" button.

3. Configure the Blueprint. Complete the information/fields required by the Blueprint wizard “Customize Blueprint” **IMPORTANT**: Please ensure the exact following options are configured exactly as below!
  1. Build Server
    1. Password/Confirm Password (This is the root password for the server. Keep this in a secure place).
    2. Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).
    3. Optionally set the server name prefix
  2. Add Disk
   * Keep the default options
  3. Install .NET Framework 4.5 on Windows
   * Keep the default options
  4. Install SQL Server on Windows
   1. SA Password/Confirm SA Password (This is the administrator password for the SQL server. Keep this in a secure place.  You will use it in a later step.)
   2. SQL Version (choose version and edition of the SQL server to be installed)
   3. SQL Features – select “Database Engine Services” , “Full-Text Search” , and "Management Tools" options
   4. Analysis Services Mode - Default of MultiDimensional
   5. SQL Instance Name – reset it to be blank
  5. Install IIS 8 on Windows
   * Keep the default options
  6. Install Acumatica 5.00
   1. SQL Server Name – put as “localhost"
   2. SQL Sa User Password / Confirm SQL Sa User Password – specify same password you’ve used in “SA Password” password parameter of SQL server

   ![1](https://t3n.zendesk.com/attachments/token/SzfpY0EDxNDyztCdxjf9gUgwW/?name=3a.jpg)
   ![2](https://t3n.zendesk.com/attachments/token/3PstPEmgkoEFZhC5M7dbjbHGK/?name=3b.jpg)
   ![3](https://t3n.zendesk.com/attachments/token/9uQRt7ejpG9mEUJQzSorh0gNp/?name=3c.jpg)
   ![4](https://t3n.zendesk.com/attachments/token/wK25ntXhIdg1n9Tem1gddrG9I/?name=3d.jpg)

4. Review and Confirm the Blueprint. Click “next: step 2”

5. Deploy the Blueprint.
  * Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
  * This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment. Generally, it will take 15 to 20 minutes to configure all of the components.

6. Monitor the Activity Queue.
  * Monitor the Deployment Queue to view the progress of the blueprint.
  * You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.

7. Get Busy!
  * Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the application until you have received this email notification.
  * Once the process has completed ­ you will need to determine the public IP address for the newly deployed host. You can click on the link in the email to get to the server directly or click on the server through the Control Portal to obtain the Public IP.
  * Access your Acumatica ERP instance by open following URL in your browser `http://YOUR_PUBLIC_IP/AcumaticaERP/`
  * “admin” for username and “setup” for password.

Pricing
The costs listed above in Steps 1 and 2 are for the CenturyLink Cloud infrastructure only.  There are no Acumatica license costs or additional fees bundled in.



### Frequently Asked Questions
### Where do I obtain my Acumatica License?
  * Contact Acumatica via telephone (888) 228-8300 or the [contact page](http://www.acumatica.com/contact-sales/) one their website
#### Who should I contact for support?
  * For issues related to deploying the Acumatica Blueprint on CenturyLink Cloud, or with any Install or Configuration issues while deploying, please view this Knowledge Base article or contact info@acumatica.com
  * For issues related to cloud infrastructure (VM’s, network, etc), please open a ticket using the CenturyLink Cloud Support Process.



