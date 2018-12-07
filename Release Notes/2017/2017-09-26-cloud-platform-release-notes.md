{{{
"title": "Cloud Platform - Release Notes: September 26, 2017",
"date": "9-26-2017",
"author": "Anthony Hakim",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (4)
* __Cloud Application Manager__

  __Unified User Login__

  As part of our continued efforts to improve the user experience of Cloud Application Manager platform, we are transforming the login experience into a unified user login.

  Cloud Application Manager’s unified login can be accessed by visiting https://cam.ctl.io/login

  This new login flow brings several improvements to user experience:

  - Responsive design for mobiles
  - Email is not a required field on organization login screen
  - An error message is displayed on non existent organization domains
  - Login animations and error messages have been enhanced
  - Support for new Operating System flavors in AWS, and performance improvements and fixes

  __Monitoring Enhancements__

  All Cloud Application Manager customers can now see all AWS CloudWatch metrics as part of the Watcher Graphs for free.

  While adding an AWS Provider if users add the additional AWS ReadOnlyAccess IAM Policy they will now start seeing their AWS providers along with the Servers in the Graph filter list. Once the AWS provider is selected, users can select from a wide range of AWS Cloud Watch metrics and see graphs related to those metrics for the entire time, data is available with AWS.

  Existing users can update their AWS Provider to add the additional AWS ReadOnlyAccess IAM Policy to start seeing the AWS Cloud Watch metrics.

  __Cloud Optimization and Analytics__

  One benefit of public cloud offerings is consumers are only charged for what they use. However, this usage-based model requires monitoring your environment, which many not have been a concern in a private cloud environment, in order to manage to one’s budget. Cloud Application Manager customers with Optimized AWS providers can now see a cost dashboard of their monthly spend with a breakdown of cost across services and regions in order to operate their environment efficiently.

  Customers can access this new functionality as part of the Analytics site of Cloud Application Manager and select 'Cost Dashboard' from the Left-hand Navigation bar.

  __Managed Services Anywhere__

  Cloud Application Manager’s Managed Services Anywhere now includes support for MS SQL, the foundation of Microsoft’s comprehensive data platform.  By selecting to deploy a Managed MS SQL server to AWS or Microsoft Azure - (CenturyLink Private Cloud on VMware Cloud Foundation) - customers get all the features of a managed server along with management of the SQL Server instance.  Simply Delegate Management to CenturyLink and receive Monitoring, Alerting, Ticketing, Remote Administration and Patching for both the VM and the SQL Server instance.

  Supported Versions
  - Microsoft SQL Server 2008 R2
  - Microsoft SQL Server 2012
  - Microsoft SQL Server 2014

  Supported Editions
  - Standard Edition
  - Enterprise Edition

  Supported Operating Systems
  - Managed Microsoft Windows Server 2008 R2
  - Managed Microsoft Windows Server 2012

  Supported Cloud Providers
  - AWS
  - Microsoft Azure
  - CenturyLink DCC-Foundation (coming soon)

### Enhancements (1)

* __Bare Metal - New Operating Systems__

  Customers now have the ability to deploy the following new Operating Systems on Bare Metal Servers:

  - CentOS 7
  - RHEL 7
  - Ubuntu 16

### Announcements (1)

* __Cloud Application Manager__

  Since introducing Cost Optimization and Analytics to Cloud Application Manager in January 2017, we have constantly improved the way we handle [consolidated billing]( https://www.ctl.io/knowledge-base/cloud-application-manager/cloud-optimization/partner-cloud-integration-consolidated-billing/). Our latest update affects [Optimized, Azure customers](https://www.ctl.io/knowledge-base/cloud-application-manager/cloud-optimization/partner-cloud-integration/). Instead of doing our billing in arrears, we will be gathering usage data daily. The benefit to our customers will be more timely charges on invoices plus usage estimates, visible through Cloud Application Manager.

  As a result of this transition, the next invoice from CenturyLink will include both arrears charges and charges from the most recent month for Optimized Azure. This means that on the next invoice (scheduled to go out October 1), some customers may see charges for August Azure usage and September usage in the same invoice. The charges will be represented as different line items.

  We are sorry about the inconveniences that this may cause and we encourage you to plan in advance. In Following October 1, estimates for your next bill will be included in Cloud Application Manager’s [billing dashboard](https://cam.ctl.io/#/billing).
