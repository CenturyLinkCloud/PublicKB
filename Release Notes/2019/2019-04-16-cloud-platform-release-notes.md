{{{
"title": "Cloud Platform - Release Notes: April 16, 2019",
"date": "04-16-2019",
"author": "Tessa Rodriguez",
"keywords":["lumen", "cam", "OS", "aws", "analytics"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (1)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Analytics

The user experience for the Analytics site has been improved for both new and existing customers. At the time your analytics-enabled provider is created  automation will deliver correct Analytics permissions. Your CAM user will inherit those permissions simply by signing into our Analytics site or by clicking the "sync user" button. If you are an existing Analytics user and want to ensure Analytics permissions are correct, first synchronize the provider in the Management site and then navigate to the Analytics site.

### Announcements (4)

#### OS Updates

As part of our ongoing efforts to improve security and availability of all Lumen Cloud resources, the following operating systems have been patched: Windows 2012 and CentOS 6 & 7.

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Cloud Application Manager Jenkins plugin update

Cloud Application Manager Jenkins plugin (ElasticBox CI plugin) now supports the latest Jenkins available versions and abides by the latest security guidelines. Additionally, the Cloud Application Manager Jenkins plugin now includes support for proxy, this means that if a Jenkins user has configured the Jenkins server to use a proxy, the plugin will also use the proxy configuration to connect to any outbound resource, such as any Cloud Application Manager defined cloud environment.

##### Optimized AWS provider synchronization

Cloud Application Manager has optimized its AWS provider type synchronization process. Based on our internal benchmarks, the synchronization process now runs around 40% faster by gathering the account infrastructure details and unregistered resources quicker and the provider will be sooner online and ready.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Support for new AWS instance types

Application Lifecycle Management now supports the latest Amazon Web Services instance types: M5ad and R5ad. Once you synchronize your AWS provider in Cloud Application Manager, you will be able to select in your Deployment Policy boxes any flavor of these Instance types by looking them up in the search box of the Instance Type drop down.
