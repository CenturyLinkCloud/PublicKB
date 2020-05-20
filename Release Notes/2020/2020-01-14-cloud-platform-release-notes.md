{{{
"title": "Cloud Platform - Release Notes: January 14, 2020",
"date": "01-14-2020",
"author": "Thomas Broadwell",
"keywords":["centurylink", "release notes", "cam", "alm", "disconnect", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Support for Portuguese and Spanish accents and special characters

Cloud Application Manager now supports the usage of Portuguese and Spanish accents and special characters. Users can now name their resources with these types of characters, and also use them in most of the providers, boxes and instance attributes such as description, readme, claims and requirements, as well as in users' first and last names.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Extended event execution audit trail

Application Lifecycle Management has extended the event execution audit trail. Apart from the event execution output results that are being already logged in the instance activity page, this feature will add the logging of all the scripts source code that is being executed on an instance, including the variable substitutions that were made before running it. This feature is not enabled by default in an organization. For that reason, an organization administrator should request the enablement of it via a support ticket.

##### Register-only instances

Application Lifecycle Management has added the ability to restrict the execution of any script in registered instances. When this feature is enabled, the instances being registered (imported) can be considered as registered-only instances, since there is no option to update nor modify the instance. If the imported instance is hosted into a managed provider, only the make managed process scripts and subsequent updates to this process will be allowed to be executed. This feature is not enabled by default in an organization. For that reason, an organization administrator should request the enablement of it via a support ticket.

##### Added bulk delete option in boxes list page

Application Lifecycle Management has added the ability to bulk delete boxes in the boxes list view. Users can select several boxes in the list and if they have the necessary permissions to delete them, they can click on the Delete Boxes option in the Bulk Actions dropdown menu to remove them.

##### Added support for Ubuntu 18 and Windows 2019 in CLC-based deployment policies

Application Lifecycle Management now supports Ubuntu 18 and Windows 2019 OS-based images to be used in CLC deployment policies. Users should synchronize their CLC providers in order to gather information about the available images for these operating system versions to allow the selection of these as templates for their deployment policies.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are: "AWS::CodeBuild::ReportGroup" and "AWS::EC2::GatewayRouteTableAssociation". Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use them.
