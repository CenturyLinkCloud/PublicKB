{{{
"title": "Cloud Platform - Release Notes: February 13, 2018",
"date": "02-13-2018",
"author": "Christine Parr",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (4)

#### Cloud Application Manager

###### Cost Optimization and Analytics

Going forward, the hardening process of Optimized, AWS accounts will include continuous compliance monitoring with auto-remediation steps to ensure your accounts are protected. The following scenarios will be handled in the following manners: Newly created IAM users that are not placed within a group will have all their permissions removed. Once they are placed in a group, permissions can be applied again. Newly created IAM groups will automatically have the [CTLCustomerPolicy applied](../../Cloud Application Manager/Cloud Optimization/partner-cloud-integration-aws-hardening-permissions.md). These steps are taken to ensure a seamless experience between Cloud Application Manager and your AWS account. This also allows Lumen to ensure your account continues to meet best practice security guidelines.

Optimized, AWS accounts will automatically have AWS Monitoring Dashboards enabled in Cloud Application Manager. Please review the [AWS Dashboards article](../../Cloud Application Manager/Monitoring/AWSDashboards.md) to learn how CAM automatically provides CloudWatch metrics for the AWS services you use to increase your understanding of your AWS environment. Prior to this enhancement, administrators were required to set it up manually.

###### Application Lifecycle Management

Organization Administrators can now associate a CostCenter when creating a new user within the Organization. The new user's personal workspace will be created under that Cost Center, and all the resources deployed there in, will be charged to that specific Cost Center. Prior this enhancement, all personal workspaces were created under the default Cost Center.

Cost Center administrators can now create new AWS & Azure Optimized providers within any workspace in that Cost Center, so that Lumen can provide Consolidated Billing and Cost Optimization on those accounts. Prior to this change, only Organization administrators were having such permissions.


##### Managed Services Anywhere

###### Support for Microsoft Windows 2016 Operating System

Managed Services Anywhere now includes support for Microsoft Windows 2016 Standard and Datacenter on Lumen Cloud (CLC) along with AWS and Azure. Customers deploying the Windows 2016 Standard or Datacenter Operating System now have an option to "Delegate OS Management" to Lumen. With Lumen managing their virtual machine instances, customers enjoy all the benefits of [Managed Services Anywhere](https://www.ctl.io/legal/cloud-application-manager/service-guide/).


#### Lumen Cloud

###### Support for Microsoft Windows 2016 Operating System

In addition to being available via Cloud Application Manager, Managed Windows 2016 is also available via Lumen Cloud Control portal.


### Announcements (4)

##### Trial Credit Expiration

On October 17, 2017, the trial terms and conditions were updated to notify customers trial credits will expire after 90 days. As of February 13, 2018, new customers receiving a $500 trial credit through the [trial program](https://www.ctl.io/free-trial/) will have their trial credit automatically expire after 90 days if the entire credit amount is not used prior to the expiration date. The date in which the credit will expire can be viewed in the Promotional Credits history under the Billing section of the customer's account.


##### Dedicated Cloud Compute (DCC) OS Availability

Windows Server 2003 is no longer available for new VMs (guests) in the DCC UI. Additionally, Windows Server 2003 will be removed for new VMs (guests) in SavvisStation Portal on February 17th, 2018.

##### Microsoft Gold Certification

The value of being a Cloud Application Manager Optimized Azure customer recently improved. Lumen has upgraded to a Microsoft Gold Level Cloud Platform Provider. This level is a sign of Lumen's dedication to training and experience supporting our Azure customers. Previous to this, benefits of Lumen's platform-level support included Lumen's domain knowledge and dedication to our customers. Now Lumen gains broader access to Microsoft subject-matter experts and increased training opportunities. Our customers continue to enjoy increasing benefits of trained, support resources without spending more for that change.

##### Cloud Application Manager Earns 2018 Frost and Sullivan Award

Lumen has received the [Frost & Sullivan 2018 Product Leadership Award](http://news.centurylink.com/2018-01-23-Frost-Sullivan-recognizes-CenturyLink-as-the-product-leader-in-hybrid-cloud-management-platforms-for-its-innovative-Cloud-Application-Manager-platform) for its innovative Cloud Application Manager hybrid cloud management platform, whose dynamic capabilities deliver added value by aligning IT teams around workloads and business initiatives as they pursue their digital transformation goals.
