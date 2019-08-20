{{{
"title": "Cloud Platform - Release Notes: August 20, 2019",
"date": "08-20-2019",
"author": "Christine Knobbe",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Kubernetes provider support for shared clusters

Cloud Application Manager now supports the Kubernetes provider type to be connected to s shared cluster where the user has access only to a limited set of namespaces. A list of allowed namespaces can be given on the provider configuration dialogue. Multiple namespaces can be specified as a comma-space separated list. The user should have the same permissions in all of them; the permissions that will be used for all namespaces will be retrieved from the first one on the list.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Instances page now displays CenturyLink network resources

Application Lifecycle Management Instances page will now list CenturyLink network resources, such as Virtual Networks and VPNs. These resources will be shown as unregistered instances with some basic information for each type such as subtype, data center, status, name, and description. If you have an existing CenturyLink Cloud provider already set up, you need to synchronize it for these resources to be discovered. More types of native resources from CenturyLink Cloud will come soon to the Cloud Application Manager instances page.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in Cloud Formation template boxes. These additional types are:
* "AWS::CloudWatch::AnomalyDetector"
* "AWS::CodeStar::GitHubRepository"
* "AWS::IoTEvents::DetectorModel"
* "AWS::IoTEvents::Input".

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.

#### [Cloud Optimization and Analytics](https://www.ctl.io/cloud-management/cloud-optimization/)

##### Change in Analytics Source Data

CenturyLink has been working with our Analytics vendor to change the AWS source for billing and usage data. While CenturyLink has been consuming the Cost and Usage Report for billing, our Analytics site has been consuming data from the Detailed Billing Report. Now both systems will be using the Cost and Usage report to ensure fewer discrepancies occur between the billing capabilities of CenturyLink and the budgetary and analytical capabilities of our Analytics site.  

### Announcements (1)

#### Notice of Migration for CenturyLink Cloud Shared Load Balancer Customers to Cloud Load Balancing-as-a-Service

In an effort to provide the quality service you expect from CenturyLink on the latest technology available, we will be migrating all current CenturyLink Cloud Shared Load Balancer customers to a new load balancer service; CenturyLink Cloud Load Balancing-as-a-Service. This new offer will provide added functionality, and most customers will also see a cost savings.

All affected customers have been notified via email of the impending migration. CenturyLink will perform the migration and there is no anticipated impact or downtime to the service during the migration. The CenturyLink Cloud Load Balancing-as-a-Service uses a multi-tenant, scalable, and programmable infrastructure presented to the customer as a service, and offers all of the same functionality as the previous offer, as well as additional features and/or functionality that include Health-check monitoring and port forwarding configurations.

You can learn more about the new offer and view pricing on the [Cloud Load Balancing-as-a-Service product page](https://www.ctl.io/load-balancing/). If you have additional questions, please feel free to contact [noc@ctl.io](mailto:noc@ctl.io), or read our [knowledge base article](../../General/LBaaS/LBaaSFAQ.md).
