{{{
"title": "Cloud Platform - Release Notes: August 7, 2018",
"date": "08-07-2018",
"author": "Ben Swoboda",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (5)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

#### [Cloud Optimization](//www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Intra-Organization Adjustments

More details of how CenturyLink distributes credits between Optimized AWS Accounts is now represented in Usage History. It represents pre-invoice adjustments for customers who would otherwise have a negative balance on a particular line item because of shifting RI discounts. For more detail, visit the [Knowledge Base](../../Cloud Application Manager/Cloud Optimization/partner-cloud-integration-detailed-billing-report.md).

#### [Application Lifecycle Management](//www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Integration with ServiceNow CMDB

Application Lifecycle Management now supports integration with the ITSM product ServiceNow as configuration management database (CMDB). An instance will be registered into ServiceNow CMDB when it's deployed, and it will be removed from ServiceNow CMDB whenever it's terminated. This allows you to have a synchronized view of your CAM deployments into ServiceNow CMDB module.

##### Support for Azure Availability Sets

Application Lifecycle Management now supports enabling high availability in Microsoft Azure deployment policies with more than one machine. Once you increase the number of instances (machines) that a Microsoft Azure deployment policy will provision to a value higher than one in the UI, a new toggle appears below that allows you to enable High availability. When you enable this option and deploy an instance with this policy, Application Lifecycle Management will make use of Microsoft Azure Availability Sets to provide the high availability requirement.

#### [Managed Services Anywhere](//www.ctl.io/cloud-application-manager/managed-services-anywhere/)

##### Watcher Agent Dashboards now Live!

Cloud Application Manager customers can now see the metric data collected by the Watcher agent on the new dashboard landing page. Information about their VM’s OS and Applications can be viewed in an easy-to-read dashboard.

Product highlights include:

* Users will be able to list & switch between their agents within a Workspace.
* With a single click, each individual metric graph on the dashboard will allow the user to do a deep dive on our more detailed graph page.

##### Support for Edge Gateway on CPC on vCF

CenturyLink Private Cloud on vCloud Foundation (CPC on vCF) customers’ Edge Gateways can now be monitored and managed via Managed Services Anywhere

Watcher Monitors coming soon:

* Edge Gateway Load Balancer
* Edge Gateway Load Balancer Pools
* Edge Gateway Load Balancer Pool Members
* Edge Gateway VPN
