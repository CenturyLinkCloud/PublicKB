{{{
"title": "Cloud Platform - Release Notes: June 11, 2019",
"date": "06-11-2019",
"author": "Marco Paolillo",
"keywords":["lumen", "cam", "ams", "msa", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (7)

#### [Lumen Private Cloud on VMware Cloud Foundation](https://www.ctl.io/lumen-private-cloud-on-vmware-cloud-foundation/)

##### Automated vApp Templates Catalog

All new builds will use an automated Catalog subscription model. The Default Catalog, named **(siteID) (data center) cl01 Lumen**, will come populated with various vApp Templates. For more information, please refer to the knowledge base article [Default Catalog and How to Opt Out](../../lumen-edge-private-cloud/catalog/default-catalog.md).

#### [Lumen Public Cloud](https://www.ctl.io/dedicated-cloud-compute/)

##### Windows 2008 Vulnerability

On May 14, 2019, Microsoft announced CVE-2019-0708, a critical flaw in Remote Desktop Services that enables unauthenticated remote code execution. The exploit is now publicly available and being used in campaigns across the Internet. There are a number of free automated tools that even make this exploit available to anyone who can follow a how-to.

If you have Remote Desktop Services enabled and a public IP, you are at a high risk of being compromised and need to update all machines running Windows 2008 or older ASAP. At the very least, please disable Remote Desktop Services if you can until the updates are performed.  

In all cases, Lumen recommends that you to install the updates for this vulnerability as soon as possible.  Where able, migrate applications to a newer version of Windows as Windows 2008 is going end of support Jan 2020.  For responses to FAQs regarding Windows 2008 support please see [this Knowledge Base article](../../support/windows-2008-end-of-vendor-support-faq.md).

##### Important Notice Regarding End of Sale for Lumen Cloud Managed Backup

Beginning June 25, [Lumen Cloud Managed Backup](https://www.ctl.io/managed-services/backup/) will no longer be available for purchase. There is no action necessary for current Lumen Cloud Managed Backup customers. The features and functionality of the Cloud Managed Backup offer will not change.
 
We appreciate you choosing Lumen as your Cloud Provider. At Lumen, it is our mission to offer products and services that help our customers navigate the digital transformation path; allowing them to focus on what is important &mdash; growing their business and taking care of their customers. 

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Upgraded vSphere vCenter API support

Cloud Application Manager is switching to the more recent implementation of the vSphere API in order to provide long-term support for current and upcoming releases of vCenter products. By default, new providers use the newer implementation, while existing providers will stick to the legacy implementation. We recommend all our customers to use the recent implementation for new projects, and to migrate away from the legacy implementation, as the API versions it uses will not be maintained in the future. A toggle labeled **Legacy Mode** is introduced in the edit provider dialog to migrate away from legacy mode, or to turn back to it, in case your vCenter environment does not support newer versions of the API.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Standard timeout for event execution

Application Lifecycle Management has implemented a procedure to automatically abort events that have been processing for 72 hours (3 days). In addition to the abort event action recently added to the UI and API, an instance will now not be kept stuck forever while executing an event and the execution will be aborted automatically. Similarly to what it happens when a user aborts the event manually, the activity log will reflect when the event is automatically aborted and the instance will transition to Unavailable state.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:

"AWS::Backup::BackupPlan", "AWS::Backup::BackupSelection", "AWS::Backup::BackupVault", "AWS::PinpointEmail::ConfigurationSet", "AWS::PinpointEmail::ConfigurationSetEventDestination", "AWS::PinpointEmail::DedicatedIpPool", "AWS::PinpointEmail::Identity", "AWS::Transfer::Server", "AWS::Transfer::User", "AWS::WAFRegional::GeoMatchSet", "AWS::WAFRegional::RateBasedRule" and "AWS::WAFRegional::RegexPatternSet".

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance and Reconfigure to use them.


#### [Cloud Optimization and Analytics](https://www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Integrated Azure in Asia Pacific

Lumen has been authorized by Azure to support consolidated billing and management of accounts for customers headquartered within select countries within the Asia Pacific region. A Lumen representative should be contacted for a detailed list of geographic, sector, and feature availability.
