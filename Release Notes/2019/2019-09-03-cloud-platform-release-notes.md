{{{
"title": "Cloud Platform - Release Notes: September 3, 2019",
"date": "09-03-2019",
"author": "Christine Knobbe",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (1)

#### [Managed Services Anywhere](https://www.ctl.io/managed-services-anywhere/)

##### Monitoring checks updates for AWS RDS

Updated Watcher checks for AWS services in order to allow monitoring of newer AWS RDS instances through Watcher.

### Announcements (2)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Discover our new branding styles in the portal!

The Cloud Application Manager user interface has been updated with the latest CenturyLink branding styles. Users will be delighted with the new modern design in all Cloud Application Manager sites, such as the inverse, black-colored top navigation bar, CenturyLink mint green highlights, and updated action button colors, among others.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Enable self-register instances in AWS or CLC providers

Self-register feature allow customers to enable instances to self-register once they are deployed externally on an AWS or CLC provider already set up in Cloud Application Manager. This new feature can be enabled through a new option in the provider details page dropdown menu. Once enabled, a new button will show a snippet to be added to the machine startup process in order to trigger the self-register process. Any instance deployed from outside of Cloud Application Manager including this snippet will be self-registered and will be shown in the instances page as any other manually registered instance. This feature supports either single virtual machines or auto-scaling groups and it is available for AWS and CLC provider types for now. More provider types will come later on.

##### Instances page now displays CenturyLink database and load balancer resource types

Application Lifecycle Management Instances page will now list the CenturyLink database and load balancer resource types. These resources will be shown as unregistered instances with some basic information for each type such as subtype, data center, status, name, and description. If you have an existing CenturyLink Cloud provider already set up, you will need to synchronize it for these resources to be discovered. These resources have been added to the already displayed CLC virtual networks and VPNs recently included into the instances list.

##### Filter by Service Type in Instances Page

Application Lifecycle Management now includes a new filter in the instances page and users can select one or several of the Service Types that are available, such as Linux Compute, Windows Compute, Azure Resource Manager Service, CloudFormation Service, etc. This new feature help users to easily display and locate the group of instances that have a specific service type in any of the available instances views.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in Cloud Formation template boxes. 

Thee additional types include: 
*	"AWS::CodeBuild::SourceCredential"
*	"AWS::Glue::MLTransform"
*	"AWS::LakeFormation::DataLakeSettings"
*	"AWS::LakeFormation::Permissions"
*	"AWS::LakeFormation::Resource"
*	"AWS::ManagedBlockchain::Member"
*	"AWS::ManagedBlockchain::Node"
*	"AWS::SageMaker::Workteam"

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.