{{{
"title": "Cloud Platform - Release Notes: March 17, 2020",
"date": "03-17-2020",
"author": "Guillermo Sanchez",
"keywords":["centurylink", "release notes", "cam", "alm", "msa", "export", "disconnect", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (3)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

#### Unregistered instances export feature

Application Lifecycle Manager has improved the feature to export the instances list by also enabling the export of unregistered resources. The export will include 'All', 'Registered' or 'Unregistered' instances, depending on the left menu option selected when clicking on the export button. This action will provide users with a list of the instances that are available in the current scope in CSV file format.

#### Support force disconnect operation when registering instances

Application Lifecycle Manager now supports the force disconnect operation while an instance is being registered. There were some use cases where the instance started the registration process but was not able to successfully complete it due to connectivity issues or any other impediment. The force disconnect operation allows users to cancel the registration process and remove the instance from the Cloud Application Manager. Whenever the issue is fixed, the registration process can be started from scratch again.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:

* "AWS::GroundStation::Config"
* "AWS::GroundStation::DataflowEndpointGroup"
* "AWS::GroundStation::MissionProfile"

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
