{{{
"title": "Cloud Platform - Release Notes: February 18, 2020",
"date": "02-18-2020",
"author": "Daniel Stephan",
"keywords":["lumen", "release notes", "cam", "alm", "msa", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (4)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### New provider type for Lumen DEC 3

Cloud Application Manager has added the support for the Lumen DEC 3 provider type. Any existing DEC 3 (Dynamic Enterprise Computing v3) environment can now be registered as a provider in Cloud Application Manager Provider. This will enable the deployment of new instances as well as the discovery and register of existing instances already available in the DEC 3 environment. For more information see [Using Lumen DEC 3](../../Cloud Application Manager/Deploying Anywhere/using-centurylink-dec3.md)

##### User list export feature

Cloud Application Manager now includes a button in the top right corner of the Users list page of the Management site to get an export of the list of all the organization users in a CSV or PDF file format. All columns in the user list will be displayed in the exported file along with the cost center the user belongs to. This will ease reporting and auditing tasks by providing a convenient file format to be consumed as required.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Support for the GCP Asia North East (Seoul) region

Application Lifecycle Management now supports another Google Cloud Platform (GCP) region: Asia North East (Seoul) and its corresponding availability zones, with the API name of `asia-northeast3`. Once you synchronize your Google Cloud provider in Cloud Application Manager, you will be able to select any of the three availability zones of the new region in your Deployment Policy boxes.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are: "AWS::ACMPCA::Certificate", "AWS::ACMPCA::CertificateAuthority", "AWS::ACMPCA::CertificateAuthorityActivation", "AWS::AppConfig::Application", "AWS::AppConfig::ConfigurationProfile", "AWS::AppConfig::Deployment", "AWS::AppConfig::DeploymentStrategy" and "AWS::AppConfig::Environment". Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
