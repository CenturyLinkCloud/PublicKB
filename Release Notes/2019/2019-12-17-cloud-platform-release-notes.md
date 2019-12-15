{{{
"title": "Cloud Platform - Release Notes: December 17, 2019",
"date": "12-17-2019",
"author": "Ben Stephan",
"keywords":["centurylink", "release notes", "cam", "alm"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (2)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### New Disconnect and Force Disconnect operations for Compute instances provider type

Application Lifecycle Management now supports two new operations to be performed onto registered Compute instances. The user can now use the new Disconnect or Force Disconnect operations on instances registered into a Compute Instances provider. Disconnect operation will execute the dispose event and related scripts if available, remove the agent from the machine and remove the instance from Cloud Application Manager. Force Disconnect will only remove the agent from the machine and remove the instance from Cloud Application Manager, without executing the Dispose event.

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
