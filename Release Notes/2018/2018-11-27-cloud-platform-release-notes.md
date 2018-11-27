{{{
"title": "Cloud Platform - Release Notes: November 27, 2018",
"date": "11-27-2018",
"author": "John Gerger",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (7)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

**Extend AWS console session timeout to 30 minutes**

Starting this release, users who logon to AWS Management Console via Cloud Application Manager can stay connected for 30 minutes. The session timeout time has been extended for the session token used to Single Sign-On into the AWS console. This will help users to perform tasks on their AWS infrastructure or applications for a longer time if logged in via Cloud Application Manager.

**Link to provider monitoring dashboard**

Cloud Application Manager now includes a Monitoring button in the provider details page to go to the provider monitoring dashboard into the Monitoring site. This new button is accessible in any AWS or Azure type providers and will open a new window or tab in your browser to display it.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**New Cloud Formation types supported**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are:

``'AWS::SecretsManager:*', 'AWS::DLM::LifecyclePolicy', 'AppSync::FunctionConfiguration', 'EC2::EC2Fleet', 'Kinesis::StreamConsumer', 'Route53Resolver::ResolverEndpoint', 'Route53Resolver::ResolverRule'``

The user can now use these new resource types in the template definition of any Cloud Formation template box, or update the template file of any existing template instance and reconfigure it to use the new resource types.

**Support for new AWS instance type**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports additional AWS instance types: m5a and r5a. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select this Instance type in your Deployment Policy boxes to provision this type of instance at deployment time.

**Custom root password for CenturyLink Cloud deployment policies**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports the ability to specify a custom root password into the CenturyLink Cloud deployment policies so that the specified value will be used at deployment time to set the password for the root account of the instance. If not specified, a random password will be generated and set for the deployed instance. This password will be accessible through the CenturyLink Cloud control portal.

**Register instances deployed through a Cloud Formation template instance**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports registering compute instances that were deployed through a Cloud Formation template instance deployment. There instances will be linked with the parent Cloud Formation template instance that created them, so that certain lifecycle operations (such as terminate or force terminate) will be only allowed to be performed through the parent instance, to avoid inconsistencies between both instances state.

**New resources tab for Cloud Formation template instances**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now provides a new tab into the Cloud Formation template instances displaying the resources that have been provisioned through the template deployment with their basic information about type and name of the resource. It will be updated whenever you reconfigure the template instance so that it will reflect the actual existing resources associated with the instance. If any resource is a virtual machine that has been registered into Cloud Application Manager, a link will be provided for that resource in the resources tab to navigate to the imported instance details page.
