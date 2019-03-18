{{{
"title": "Cloud Platform - Release Notes: March 19, 2019",
"date": "03-19-2019",
"author": "Guillermo Sanchez",
"keywords":["centurylink", "cam", "clc", "kubernetes", "aws", "gcp", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (6)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) 

##### Kubernetes support improvements

Cloud application Manager recently released the new Kubernetes provider type. This new feature has now been improved to support token-based authentication, report errors and additional messages in instance logs from deployed resources, new Jinja variable to refer to the namespace, support for hostnames in load-balancer, etc. For more information see [Setting up a Kubernetes provider](../../Cloud Application Manager/Deploying Anywhere/kubernetes.md) and [Using Kubernetes](../../Cloud Application Manager/Automating Deployments/using-kubernetes.md).

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Add link to resource in AWS console from instance details page

Application Lifecycle Management now includes a link in the instances details page that points to the resource in the AWS console. This link will appear next to the Provider Instance ID value in the instance details page if the user has enough rights to access the AWS console (the user has write access to the provider). If the instance has multiple machines, the link will display all those machine list in AWS console through a filter. If the instance is a Cloud Formation template, the link will display the Cloud Formation stack in the AWS console.

##### Support for new Google Cloud Platform region

Application Lifecycle Management now supports a new Google Cloud Platform region: Europe West 6 (europe-west6) and its corresponding zones. Once you synchronize your Google Cloud provider in Cloud Application Manager, you will be able to select in your Deployment Policy boxes the zones corresponding to the new region.

##### New Cloud Formation types supported

Application Lifecycle Management now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are all related to AWS IoT GreenGrass: 
"AWS::Greengrass::ConnectorDefinition", "AWS::Greengrass::ConnectorDefinitionVersion", "AWS::Greengrass::CoreDefinition", "AWS::Greengrass::CoreDefinitionVersion", "AWS::Greengrass::DeviceDefinition", "AWS::Greengrass::DeviceDefinitionVersion", "AWS::Greengrass::FunctionDefinition", "AWS::Greengrass::FunctionDefinitionVersion", "AWS::Greengrass::Group", "AWS::Greengrass::GroupVersion", "AWS::Greengrass::LoggerDefinition", "AWS::Greengrass::LoggerDefinitionVersion", "AWS::Greengrass::ResourceDefinition", "AWS::Greengrass::ResourceDefinitionVersion", "AWS::Greengrass::SubscriptionDefinition" and "AWS::Greengrass::SubscriptionDefinitionVersion". The user can now use these new resource types in the template definition of any Cloud Formation template box or update the template file of any existing template instance and reconfigure it to use the new resource types.

#### [Analytics](https://www.ctl.io/knowledge-base/cloud-application-manager/analytics/#1)

Users of Advanced Analytics may now set cost and security event Alerts for AWS and Azure. These permissions will be provided by default for new users and accounts. Existing customer permissions will be updated by request.

#### [Public Cloud IaaS](//www.ctl.io/product-overview/#)

As a part of our ongoing efforts to improve CenturyLink Cloud's offerings, we are pleased to announce that Ubuntu 18 is now available within Control. Within Control you are now able to go to create => server => operating system and select "Ubuntu 18 | 64-bit".