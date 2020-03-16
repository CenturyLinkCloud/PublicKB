{{{
"title": "Cloud Platform - Release Notes: January 28, 2020",
"date": "01-28-2020",
"author": "John Gerger",
"keywords":["centurylink", "release notes", "cam", "alm", "msa", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (2)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Ability to search by Account ID or Subscription ID in providers' page

Cloud Application Manager has added the ability to search by AWS Account ID or Azure Subscription ID in the providers' page. These search field additions enable users to quickly find the provider or providers that are associated with certain AWS or Azure accounts just by typing the corresponding account ID or subscription ID in the search field of the providers' list page.

#### [MSA DR-Readiness](https://www.ctl.io/managed-services/disaster-recovery/)

##### Support for Linux Operating system

This feature allows a user to protect their Linux workload in CAM for DR. Azure and AWS are supported target cloud platforms to rover the instance. A Linux recovery server will be spun up at the time of disaster when a recovery operation like Test-Failover/ Failover is performed

##### Private IP support

This provides the capability to support private IPs and VPNs to replicate the data from the production site to the DR site. A user no longer has to rely on a public IP to replicate their data.
