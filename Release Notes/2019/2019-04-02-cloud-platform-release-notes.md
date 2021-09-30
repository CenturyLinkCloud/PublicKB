{{{
"title": "Cloud Platform - Release Notes: April 2, 2019",
"date": "04-02-2019",
"author": "Christine Sala",
"keywords":["lumen", "cam", "clc", "cpc-vcf", "aws", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (6)

#### [Lumen Private Cloud on VMware Cloud Foundation](https://www.ctl.io/lumen-private-cloud-on-vmware-cloud-foundation/)

All new customer builds from this point forward will include vCloud Director 9.5.

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Support for Lumen Master Account login method

Cloud Application Manager now supports Lumen Master Account as an authentication method. A new button will appear on the Cloud Application Manager login page next to your existing authentication methods. This will allow users to sign in with a Lumen Master Account so they can use their credentials to access Cloud Application Manager. This will also let users with additional Lumen products supporting this authentication method to use Single Sign-On within Cloud Application Manager and these other additional products.

##### SAML support improvements for encryption and groups

Cloud Application Manager improved its SAML support to include encryption and SAML groups. An organization administrator can now specify the service provider certificate that will be used by Cloud Application Manager to sign and encrypt messages, coming from or going to, the SAML backend. In addition, when a user logs in with SAML, user's group membership will be collected if provided by the SAML backend and these groups will then be available to be included as members in any workspace, cost-center or as administrators of the organization. All SAML group members will then get automatic access to the corresponding team workspace, cost-center or organization, and thus, to all resources pertaining to that scope.


##### Support for multiple ServiceNow instances

Cloud Application Manager now adds support to configure multiple ServiceNow instances to integrate with. The organization settings page provides the ability to set up multiple ServiceNow instance configurations within the organization. From there, every deployment of an instance in Cloud Application Manager will inform all ServiceNow instances CMDB about the new resource, will show its IDs in the instance details page, and will inform all ServiceNow instances CMDB about termination of an instance so it can be removed there as well.

##### User Interface Redesign for Provider Services

Cloud Application Manager has redesigned the user interface formerly used to enable services such as [Managed Services Anywhere](../../Cloud Application Manager/Managed Services/getting-started-with-cam-enable-managed-provider.md), [Automatic Discovery of Resources](../../Cloud Application Manager/Getting Started/register-existing-instance.md) and [Analytics](../../Cloud Application Manager/analytics/cloudapplicationmanageranalyticsui.md). The services toggles that were available in the Edit Provider dialog has been moved to a new tab called Services in the provider details page, where you can manage them and see additional details such as the status of your Managed Services Anywhere enabled locations.

### Bug Fixes (4)

#### [Lumen Public Cloud](https://www.ctl.io/cloud-platform/)

Fixed bug for API Endpoint /v2/servers/{accountAlias}/{serverName} which allowed the server to be retrieved when providing an incorrect accountAlias as long as it was in the same account hierarchy as the user requesting the data.

#### [Dedicated Cloud Compute (DCC)](https://www.ctl.io/dedicated-cloud-compute/)

* Updated query so users are able to view clusters with pending AIPs
* Added logic to address change tier memory calculation
* Addressed a UI load timing issue
