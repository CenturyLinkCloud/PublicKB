{{{
"title": "Cloud Platform - Release Notes: January 14, 2020",
"date": "01-14-2020",
"author": "Thomas Broadwell",
"keywords":["centurylink", "release notes", "cam", "alm", "disconnect", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements

#### CenturyLink Private Cloud on VMware Cloud Foundation (CPC on vCF)

##### **Multiple Cluster Support**
Customers who order multiple CPC on vCF clusters can manage these multiple clusters within a single vCD UI.

##### **GPU Add-on**
Customers can order a GPU Add-on option for CPC on vCF new or existing clusters, providing support for VDI, Digital Imaging and High Performance Gaming use cases.

#### Application Lifecycle Management

##### Azure deployment policies search field for size and image dropdowns

Application Lifecycle Management has added a search field to the size and image dropdowns of the Azure deployment policy properties. These two dropdowns have a high number of options, so it was difficult to locate a specific one among all of them. The search field allows the user to filter the displayed options so that it is easier to locate and select the required ones. Additionally, the size description has been extended with the corresponding CPU and memory values to facilitate the selection of the appropriate one.

##### Auto-register Terraform VM resources in managed providers

Application Lifecycle Management now includes the feature to auto-register VM instances that were deployed as part of a Terraform template deployment in a vCloud-based managed provider. The compute instances included into the Terraform template box resources will be automatically registered in Cloud Application Manager and the make managed process will be executed on them. This is currently supported for CenturyLink Private Cloud on vCloud Foundation and VMWare vCloud Director provider types.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. 
These additional types are: 
* "AWS::Pinpoint::EmailTemplate"
* "AWS::Pinpoint::PushTemplate"
* "AWS::Pinpoint::SmsTemplate"
* "AWS::CodeStarNotifications::NotificationRule"
* "AWS::MediaConvert::JobTemplate"
* "AWS::MediaConvert::Preset"
* "AWS::MediaConvert::Queue" 

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
