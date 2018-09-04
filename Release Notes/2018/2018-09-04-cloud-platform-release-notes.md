{{{
"title": "Cloud Platform - Release Notes: September 04, 2018",
"date": "09-04-2018",
"author": "Matt Schwabenbauer",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (6)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

#### [Application Lifecycle Management](//www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Support for Azure Scale Sets

Application Lifecycle Management now provides support to use Scale Set into a Microsoft Azure Deployment Policy box, so that the instances deployed with it would be included into a Scale Set Azure resource and enable the user to turn on the auto scaling feature by setting up the CPU thresholds and instance increments.

##### Support for Azure Load Balancers

Application Lifecycle Management now supports Azure Load Balancer and Azure App Gateway to be added to a Microsoft Azure Deployment Policy box. Once a user enables Scale Set on it, a new section appears allowing the user to enable load balancer, either by using Azure Load Balancer or by using an Azure App Gateway.

#### [SafeHaven DRaaS](//www.ctl.io/disaster-recovery/)

* Support for Linux Operating Systems : RHEL6/7, Ubuntu 14/16 for DR to Azure.
* CMS box in CAM catalogs to deploy and configure SafeHaven Console.
* Addition of Azure Statistics tab in SafeHaven Console.
* Support for Azure Managed Disks.

### Announcements (2)

#### [Public Cloud IaaS](//www.ctl.io/product-overview/#)

##### Hyperscale Servers Migrated to Standard Compute

All instances of Hyperscale servers have been migrated to standard compute clusters. On 8/21/2018, all Hyperscale servers were re-entitled as standard compute servers, and have been billing using standard compute pricing. For more information, read this [Knowledge Base article](../../Servers/hyperscale-eol-faqs.md).

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

##### Data removal from Billing Dashboard

We are currently working towards redesigning the Billing Dashboard view and as part of that, we will no longer provide “Month To Date”, “Month Estimate”, “Current Hour” and “One Time Charges” on the Billing Dashboard page. For Monthly cost information please visit our Analytics Site.
