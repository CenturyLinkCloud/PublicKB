{{{
"title": "Getting Started with Halon SMTP Software - Partner Template",
"date": "12-12-2015",
"author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
"attachments": [],
"contentIsHTML": false
}}}

### Overview
After reading this article, the reader should feel comfortable deploying the Halon SMTP platform on CenturyLink Cloud.

### Partner Profile
<img src="../../images/halon/halon_logo.png" style="border:0;float:right;max-width: 150px;">

Halon Security – “The SMTP software for your business”

https://halon.io

#### Contact Halon
|Sales Contact      | Customer Support	|
|:- |:-	|
|sales@halonsecurity.com       | support@halonsecurity.com	|


### Description
Halon is the scriptable SMTP (email security) software that provides anti-spam, routing, API integration, task automation, encryption and signing for today’s businesses. Halon’s SMTP email security software is now available on the CenturyLink Cloud Platform for customers to download and install. This article is to help end-users to quickly take advantage of this integration to maximize their investment and immediately protect their infrastructure.

### Solution Overview
Halon’s scriptable SMTP software is designed to give each business to have a full range of solutions to managing business email. Customers find savings through a reduced need for servers and hardware as well as by nearly eliminating task management through automation features. In addition to this customers can leverage Halon’s expertise and best-in-class service to its customers.

### Offer
The end-user initiates their relationship with Halon through their CenturyLink Cloud account but pay for their services directly to Halon on a monthly basis. This Virtual Appliance, called a Partner Template, is deployed to your CenturyLink Cloud account via a Service Task. Although Service Tasks are ordinarily billed to the end-user’s account, CenturyLink will provide a refund for costs associated with the Service Task for deploying the Partner Template. Please follow the process below to request credit. In order to purchase your license (AKA entitlement), please email sales@halonsecurity.com or click here for a list of international contacts for Halon Security Sales.

### Audience
CenturyLink customers that manage an email infrastructure.

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud. After executing the steps in this document, end-users will have a functioning and more-secure email infrastructure.

### Minimal System Requirements
Halon’s end-user console is a browser based portal and does not require extensive system resources to operate. The Halon email gateway software is highly efficient, and can handle incredible amounts of e-mail traffic. For performance benchmarks and optimizations, please see http://wiki.halon.se/Performance.

* CPU: 1 CPU (Minimum), 2 CPU (Recommended)
* RAM: 2 GB (Minimum), 4 GB (Recommended)
* Storage: 10 GB (Minimum)

### Howe to Deploy the Partner Image
1. Create an email to ServiceTasks@ctl.io.

2. Copy and paste the information below into the body of the email.

3. Edit the information as needed and send.

   ```
   TO: ServiceTasks@ctl.io

   EMAIL SUBJECT:   Ecosystem Partner Template Import Request

   CLC Support Team,

   Please create a ticket to import the Ecosystem Partner Template image  referenced below to my CenturyLink Cloud Account:

   - Import CenturyLink Ecosystem Partner Source Image: Halon Security
   - My CenturyLink Cloud Account Alias: ####
   - My CenturyLink Cloud Account PIN:  ######
   - Data Center to import image to: ###
   - Server Name to import image as: ##########
   - VLAN in the account to add the Server to: ########
   - Additional Notes or work to be done: ########

   Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.

   Thank you very much,

   Your_Name_Here
   ```

### Accessing and Configuring your Halon virtual appliance
Once the Service Task team deploys your virtual appliance, you will get an email notification with details on your new devices. Follow these instructions to access and configure your virtual appliance:

1. Add a public IP to the virtual appliance and open the following ports:
   * HTTPS (443) for management
   * single port TCP 25 (For SMTP traffic)
   * (optional) SSH/SFTP (22) for management over SSH

2. Connect to the public IP over HTTPS using your web browser.

3. You will now be presented with a login screen, use the default admin/admin credentials to login.

4. Now you can begin configuring your Halon appliance. For more information about this, see the following link: http://wiki.halon.se/Getting_started.

If a customer has any questions or complications, we provide free technical support. Feel free to email Halon at [support@halonsecurity.com](mailto:support@halonsecurity.com).

### Pricing
The costs listed above in Steps 1 and 2 are for the infrastructure only.

After deploying this Partner Template, the end-user can email Halon at [sales@halonsecurity.com](mailto:sales@halonsecurity.com) to start using this service.

#### Process to request credit for Service Task fee
Follow this process to request credit on your account to reimburse any expense to deploy the Partner Template.

* Please copy and paste the email below and send it to [Ecosystem Partner](mailto:ECOSystem@centurylink.com).

  ```
  TO: ECOSystem@centurylink.com

  EMAIL SUBJECT:   Requesting Credit for Halon Partner Template Deployment

  CLC Ecosystem Team,

  I am requesting a credit be placed on my account to cover the fees associated with deploying the Halon Partner Template to my account under the Service Task deployed on MM/DD/YYYY. My CenturyLink Cloud username or account alias the credit needs to be placed on is ######

  Thank you very much, your_name_here
  ```

### Frequently Asked Questions

#### Where do I obtain my Halon License?
* Please contact [Halon Sales](mailto:sales@halonsecurity.com).

#### Who should I contact for support?
* For issues related to deploying the Halon partner template on CenturyLink Cloud, please contact [support@halonsecurity.com](mailto:support@halonsecurity.com).
* For issues related to cloud infrastructure, please open a ticket using the CenturyLink Cloud [Support Process](../../Support/how-do-i-report-a-support-issue.md).
