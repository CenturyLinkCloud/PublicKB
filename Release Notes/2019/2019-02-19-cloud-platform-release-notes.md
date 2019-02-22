{{{
"title": "Cloud Platform - Release Notes: February 19, 2019",
"date": "02-19-2019",
"author": "Daniel Stephan",
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (7)

#### CenturyLink Cloud

##### SAML Certificate Update - *Action may be required!*
If you are using SAML authentication you will need to update the signing certificate for use with your IdP as of February 9, 2019. You can find the updated certificate within our [SAML knowledge base article](../../Control Portal/using-saml-for-single-sign-on-to-the-centurylink-platform-control-portal.md). Please update the certificate in order to continue SAML authentication.

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### New Kubernetes Provider Type

Cloud Application Manager now includes support for a new type of [Provider](https://www.ctl.io/knowledge-base/cloud-application-manager/core-concepts/providers/) which enables management of Instances on a Kubernetes cluster. With this new Kubernetes Provider type, you can create and manage any Kubernetes resource, either native or custom, using declarative YAML configuration files that can be included in the new Kubernetes template box type. The new Kubernetes [Template Box](https://www.ctl.io/knowledge-base/cloud-application-manager/automating-deployments/template-box/) type also supports variables with the typical [Jinja](http://jinja.pocoo.org) syntax that can be used into the template files to access their values. The existing Kubernetes resources in any newly configured Kubernetes provider will also be discovered and allowed to be registered in Cloud Application Manager. Both the deployed templates and the registered resources will be shown in the Instances page and can be managed like any other template Instance.

##### Removed Google+ API OAuth Dependency

Cloud Application Manager was using certain Google+ API on its OAuth integration. Google announced that Google+ APIs will be shut down on March 7, 2019, including Google+ Sign-in and OAuth token requests with Google+ scopes. Cloud Application Manager has removed Google+ API OAuth dependencies so that the Google OAuth support is not affected by the Google+ service shut down.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Support for Proxy in Agent Connection

Application Lifecycle Management now supports configuring a proxy for the agent to contact back to Cloud Application Manager. The user will have the ability to set up the proxy address and port values in any deployment policy configuration. These values will be used by the agent installed on the machine to contact Cloud Application Manager back, so it enables certain network restricted use cases to be supported and managed by Cloud Application Manager. The new proxy support in agent connection feature will be available for all provider types, such as AWS, Azure, CenturyLink Cloud, CenturyLink Private Cloud on VMWare Cloud Foundation, CenturyLink DCC, Google Cloud, IBM Cloud, vCloud and vCenter environments, etc.

##### Manual Terminate and Shutdown protection

Application Lifecycle Management now allows users to prevent the manual **shutdown** or **termination** of an instance.  Users can enable manual termination protection in any deployment policy box, set it at deployment time for the instance, or change its values through the Lifecycle Editor of any deployed instance. Once enabled, the user will not be allowed to manually shut down or terminate the instance unless the protection toggle is disabled. The instance will still be affected by *scheduled termination or shutdown* configured values.

##### Link To Provider Details Page

Cloud Application Manager now includes a link to the provider details page on the Instances page, view by provider. The user can now go through this link to the provider details page while browsing the instances in the view by provider. This view of the instances page already presented the instances grouped by the provider, with a dropdown to collapse or expand each provider instances. Now it includes an icon after the provider name that will navigate to the provider details page when clicked.

##### New Cloud Formation Types Supported

Application Lifecycle Management now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are:  
"AWS::ApiGatewayV2::Api", "AWS::ApiGatewayV2::Authorizer", "AWS::ApiGatewayV2::Deployment", "AWS::ApiGatewayV2::Integration", "AWS::ApiGatewayV2::IntegrationResponse", "AWS::ApiGatewayV2::Model", "AWS::ApiGatewayV2::Route", "AWS::ApiGatewayV2::RouteResponse", "AWS::ApiGatewayV2::Stage", "AWS::FSx::FileSystem", "AWS::KinesisAnalyticsV2::Application", AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption", 
"AWS::KinesisAnalyticsV2::ApplicationOutput" and "AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource".  
The user can now use these new resource types in the template definition of any Cloud Formation template box or update the template file of any existing template instance and reconfigure it to use the new resource types.

##### Support For New AWS Instance Types

Application Lifecycle Management now supports additional Amazon Web Services bare-metal instance types: m5d.metal, m5.metal, r5d.metal, r5.metal, z1d.metal. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select in your Deployment Policy boxes this Instance types by searching for them in the search box of the Instance Type drop down.
