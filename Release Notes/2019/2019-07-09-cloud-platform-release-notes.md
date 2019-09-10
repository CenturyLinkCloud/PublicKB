{{{
"title": "Cloud Platform - Release Notes: July 9, 2019",
"date": "07-09-2019",
"author": "Joseph Nguyen",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Optimization](https://www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Integrated Azure in Latin America

CenturyLink has been authorized by Azure to support consolidated billing and management of accounts for customers headquartered within select countries within Latin America. A CenturyLink representative should be contacted for a detailed list of geographic, sector, and feature availability.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Script event execution timeout

Application Lifecycle Management now supports setting up a timeout at event script level at both box or instance level. Users can specify the timeout in a box event by clicking on the "Timeout" column next to the script event on the box code view. A dialog will provide predefined timeout values to choose from, but timeouts can also be customized between 10 and 1440 minutes (1 day). All instances deployed with this box will inherit the event script timeout value.

In addition, it's possible to specify the timeout for an instance. This can be done by going to the lifecycle editor on the instance details page, opening the context menu for the corresponding event script and clicking on the option *Set timeout*. This will only affect the current instance. When a timeout is set, the script event will show a clock icon next to it. If the timeout is reached when executing the script code, the script execution will be aborted.

##### Terraform template boxes on VMware vCenter providers

Application Lifecycle Management now extends its Terraform template support to the VMware vCenter provider type. In addition to the existing support for AWS, Azure, Google Cloud, CenturyLink Cloud, vCloud and CenturyLink Private Cloud on vCloud Foundation provider types, the VMware vCenter provider type is now eligible for deploying a Terraform template box when configuring a Terraform deployment policy box.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:

"AWS::Config::RemediationConfiguration", "AWS::MediaLive::Channel", "AWS::MediaLive::Input", "AWS::MediaLive::InputSecurityGroup", "AWS::SecurityHub::Hub" and "AWS::ServiceCatalog::StackSetConstraint".

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
