{{{
"title": "Cloud Platform - Release Notes: April 2, 2019",
"date": "04-02-2019",
"author": "Christine Sala",
"keywords":["centurylink", "cam", "clc", "cpc-vcf", "aws", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (6)

#### [CenturyLink Private Cloud on VMware Cloud Foundation](https://www.ctl.io/centurylink-private-cloud-on-vmware-cloud-foundation/)

All new customer builds from this point forward will include vCloud Director 9.5.

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Support for CenturyLink Master Account login method

Cloud Application Manager now supports CenturyLink Master Account as an authentication method. A new button will appear on the Cloud Application Manager login page next to your existing authentication methods. This will allow users to sign in with a CenturyLink Master Account so they can use their credentials to access Cloud Application Manager. This will also let users with additional CenturyLink products supporting this authentication method to use Single Sign-On within Cloud Application Manager and these other additional products.

##### SAML support improvements for encryption and groups

Cloud Application Manager improved its SAML support to include encryption and SAML groups. An organization administrator can now specify the service provider certificate that will be used by Cloud Application Manager to sign and encrypt messages, coming from or going to, the SAML backend. In addition, when a user logs in with SAML, user's group membership will be collected if provided by the SAML backend and these groups will then be available to be included as members in any workspace, cost-center or as administrators of the organization. All SAML group members will then get automatic access to the corresponding team workspace, cost-center or organization, and thus, to all resources pertaining to that scope.

##### EC2 instance role support in Cloud Application Manager Data Center Edition

Cloud Application Manager Data Center Edition now supports leveraging an EC2 Instance Role as an authorization mechanism for all AWS API calls the appliance performs. EC2 Instance Roles ease credential management and increase security for applications running in EC2 instances, so this feature only applies to appliances running as AWS EC2 Instances. Once set, you will only be able to configure new AWS providers using an IAM Role. For more information, refer to [Cloud Application Manager Data Center Edition with EC2 Instance Role](../../Cloud Application Manager/Appliance/camdce-with-ec2-instance-role.md)

##### Support for multiple ServiceNow instances

Cloud Application Manager now adds support to configure multiple ServiceNow instances to integrate with. The organization settings page provides the ability to set up multiple ServiceNow instance configurations within the organization. From there, every deployment of an instance in Cloud Application Manager will inform all ServiceNow instances CMDB about the new resource, will show its IDs in the instance details page, and will inform all ServiceNow instances CMDB about termination of an instance so it can be removed there as well.

##### User Interface Redesign for Provider Services

Cloud Application Manager has redesigned the user interface formerly used to enable services such as [Managed Services Anywhere](../../Cloud Application Manager/Managed Services/getting-started-with-cam-enable-managed-provider.md), [Automatic Discovery of Resources](../../Cloud Application Manager/Getting Started/register-existing-instance.md) and [Analytics](../../Cloud Application Manager/analytics/cloudapplicationmanageranalyticsui.md). The services toggles that were available in the Edit Provider dialog has been moved to a new tab called Services in the provider details page, where you can manage them and see additional details such as the status of your Managed Services Anywhere enabled locations.

### Bug Fixes (4)

#### [CenturyLink Public Cloud](https://www.ctl.io/cloud-platform/)

Fixed bug for API Endpoint /v2/servers/{accountAlias}/{serverName} which allowed the server to be retrieved when providing an incorrect accountAlias as long as it was in the same account hierarchy as the user requesting the data.

#### [Dedicated Cloud Compute (DCC)](https://www.ctl.io/dedicated-cloud-compute/)

* Updated query so users are able to view clusters with pending AIPs
* Added logic to address change tier memory calculation
* Addressed a UI load timing issue
