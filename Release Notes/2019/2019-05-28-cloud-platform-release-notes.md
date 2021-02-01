{{{
"title": "Cloud Platform - Release Notes: May 28, 2019",
"date": "05-28-2019",
"author": "Christine Parr",
"keywords":["lumen", "cam", "ams", "msa", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

#### Cloud Integration

##### Re-Hardening of Integrated, AWS Accounts

Because AWS has added multiple, new regions since accounts were created, integrated accounts have been updated to ensure all regions gain the full benefit of security and compliance logging, per [this Knowledge Base article](../../Cloud Application Manager/Cloud Optimization/partner-cloud-integration-aws-hardening-permissions.md).

#### [Managed Services Anywhere](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/)

##### Monitoring UI enhancements

* Monitoring Policies now display the Policy Name and Scope of extended policies on child (Extended to) policies.  This allow a user to identify the origin, Parent Policy, of checks within a child policy.

* Improved Event Suppression visualization to make the identification of suppressed events more obvious.  Added hashed status bar for suppressed events.  The status bar color remains and allows for the identification of the status of the check and the hash indicates that the event is suppressed.

* All event dashboard times have been "fuzzified" in order to display event times in a "some time ago" format, i.e. "Event x occurred 2 hours ago."  This allows a more quickly consumable view while also offering detail Date/Time stamp upon hover over of the "fuzzified" time.

* Content pane scrolling now maintains header position allowing users to more easily determine the data being viewed.

* The Monitoring UI now offers real-time searches.  When data is input into the UI Search box, the text will be actively matched with the data on the page and highlighted.

##### Latin America (LATAM) Customer identification

Alerts for customers in the LATAM region are identifiable and will be forwarded to the appropriate LATAM support desk.  This enables future CAM MSA customers in the LATAM region the ability to communicate with Lumen support for MSA enabled providers in their local language.  

##### Support for VMs built ephemeral storage

Managed Services Anywhere has been updated to handle VMs built with ephemeral storage.  When the server is brought back online after a shutdown, by nature of being on ephemeral storage, all state is lost.  MSA now recognizes that the VM has been previously registered with a monitoring agent and upon restart, the historic monitoring data will be associated with the new agent instance.  

### Announcements (4)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Improve auditability for AWS console access from the instance details page

Application Lifecycle Management will enhance log trace for each access to the AWS console through the recently added Provider Instance ID link on the instance details page. This type of access was already been registered in the Provider activity log, but it has been improved with the instance id that is being accessed, as well as including it into the instance activity log. This way any AWS console access will be displayed either by instance activity log or by provider activity log, improving auditability and facilitating any issue troubleshooting.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:
"AWS::Glue::DataCatalogEncryptionSettings", "AWS::Glue::SecurityConfiguration", "AWS::MediaStore::Container", "AWS::ApiGatewayV2::ApiMapping" and "AWS::ApiGatewayV2::DomainName".  The user can now use these new resource types in the template definition of any CloudFormation template box or update the template file of any existing template instance adding any of these types of resource and reconfigure the instance to use it.

##### Support for new AWS instance types

Application Lifecycle Management now supports two new Amazon Web Services instance types: I3en, T3a. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select in your Deployment Policy boxes any flavor of these Instance types by looking them up in the search box of the Instance Type drop down.

#### [Lumen Public Cloud](https://www.ctl.io/dedicated-cloud-compute/)

#### OS Templates

RHEL 6 & 7 have been updated and the latest revisions are now available on the CLC Platform.  RHEL 6 in now on revision 6.8 and RHEL 7 is on 7.2.  This update was completed as part of our ongoing efforts to improve security and availability of all Lumen Cloud resources.

### Bug Fixes (2)

#### [Analytics](https://www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Issues with Syncing Analyzed Providers

Issues preventing existing, analyzed providers from syncing because of Analytics conflicts have been resolved.

#### Cloud Integration

##### Layout of Azure Providers

The layout of integrated, Azure providers has been fixed within the UI.
