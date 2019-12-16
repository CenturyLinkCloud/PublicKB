{{{
"title": "Cloud Platform - Release Notes: December 17, 2019",
"date": "12-17-2019",
"author": "Ben Stephan",
"keywords":["centurylink", "release notes", "cam", "alm", "disconnect", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (3)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### User-defined data centers and networks for Compute Instances providers

Cloud Application Manager now includes support to define data centers and networks in Compute Instances providers. Customers can now add multiple data centers and networks within them for the Compute Instances provider type. This feature helps customers to organize their instances in this provider with some structure following the real setup of their environment. The self-registering scripts will vary based on the selected data center and network. For the convenience of our customers, we automatically provide a predefined "default datacenter" and a "default network" to allow registering instances without the need for additional configuration, in case it is not required. This feature also builds the foundation for instances registered in this provider to be managed by MSA which is to be released separately soon.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### New Disconnect and Force Disconnect operations for Compute instances provider type

Application Lifecycle Management now supports two new operations to be performed on registered Compute instances. The user can now use the new Disconnect or Force Disconnect operations on instances registered into a Compute Instances provider. Disconnect operation will execute the dispose event and related scripts if available, remove the agent from the machine and remove the instance from Cloud Application Manager. Force Disconnect will only remove the agent from the machine and remove the instance from Cloud Application Manager, without executing the Dispose event. Note that for older versions of the agent, it will not be removed automatically, and in Windows machines, the service will be stopped but not removed automatically.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:

* "AWS::AccessAnalyzer::Analyzer"
* "AWS::AppSync::ApiCache"
* "AWS::CloudWatch::InsightRule"
* "AWS::ECS::PrimaryTaskSet"
* "AWS::ECS::TaskSet"
* "AWS::EKS::Nodegroup"
* "AWS::EventSchemas::Discoverer"
* "AWS::EventSchemas::Registry"
* "AWS::EventSchemas::Schema"
* "AWS::GameLift::GameSessionQueue"
* "AWS::Lambda::EventInvokeConfig"
* "AWS::S3::AccessPoint"
* "AWS::WAFv2::IPSet"
* "AWS::WAFv2::RegexPatternSet"
* "AWS::WAFv2::RuleGroup"
* "AWS::WAFv2::WebACL"

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
