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

#### Export Unregistered Instances

Application Lifecycle Manager now allows users to export instance data with additional filters.  Users can now export unregistered instances as well. The export option now includes 'All', 'Registered' or 'Unregistered' instances, depending on the current selected view.  This action will provide users with a list of the instances that are available in the current scope in CSV file format.

#### Support force disconnect operation when registering instances

Application Lifecycle Manager now supports the force disconnect operation while an instance is being registered. There were some use cases where the instance started the registration process but was not able to successfully complete it due to connectivity issues or any other impediment. The force disconnect operation allows users to cancel the registration process and remove the instance from the Cloud Application Manager. Whenever the issue is fixed, the registration process can be started from scratch again.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:

* "AWS::GroundStation::Config"
* "AWS::GroundStation::DataflowEndpointGroup"
* "AWS::GroundStation::MissionProfile"

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.

### Enhancements (2)

#### [Cloud Application Manager - DRaaS](https://www.ctl.io/managed-services/disaster-recovery/)

##### Support for Physical Provider (compute instances) for DR to AWS/Azure

With this feature, customers can protect their VMs in any cloud that is natively not supported as a provider type in CAM. The VM can be replicated either to AWS or Azure and failed over at the time of Disaster.

##### Private IP support for replication

A user can replicate their workload over a VPN, such as IPSec or MPLS, instead of relying on replication over the internet.
