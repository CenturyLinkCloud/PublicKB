{{{
"title": "Cloud Platform - Release Notes: October 15, 2019",
"date": "10-15-2019",
"author": "Matthew Farrell",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (2)

#### [CenturyLink Private Cloud on VMware Cloud Foundation (CPC on vCF)](https://www.ctl.io/centurylink-private-cloud-on-vmware-cloud-foundation/)

##### Upgrades for CPC on vCF

We have finished the work to enable our CPC on vCF customers the option to have their environments upgraded.

Upgrade options are for both vCD 9.7 and vCF 3.5. Customers should reach out to their account team to order an upgrade for their CPC on VCF environment.

Upgrades to vCD 9.7 allow customers access to features, such as:
  - HTML5 Tenant Portal Enhancements
  - VM based metrics

Upgrades to vCF 3.5 allow customers access to features, such as:
  - ESXi 6.7
  - vSAN 6.7
  - NSX-V 6.4.4
  - vCenter 6.7

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Cloud Application Manager – Disaster Recovery (DR)

One-click DR using CAM
  - CAM customers can protect their workload from CLC to AWS, CLC to Azure, AWS to Azure or Azure to AWS.
  - Once the workload is protected, the customers are allowed to perform recovery operations, like Test-Failover/ Failover to recover their workload to the supported clouds.

DR-Readiness feature for MSA
  - DR-Readiness feature allows existing MSA customers to order white glove DR implementation
  - Customers can click on "enable DR" for their MSA enabled networks from under CAM services.
  - Once the service is order, TAM and CTAs are going to work with the customer to start the implementation of white glove DR.

### Announcements (3)

#### [Load Balancer](https://www.ctl.io/centurylink-public-cloud/load-balancing/) Migrations

##### Notice of Migration for CenturyLink Cloud Shared Load Balancer Customers to Cloud Load Balancing-as-a-Service

In an effort to provide the quality service you expect from CenturyLink on the latest technology available, we will be migrating all current CenturyLink Cloud Shared Load Balancer customers to a new load balancer service; CenturyLink Cloud Load Balancing-as-a-Service. This new offer will provide added functionality, and most customers will also see a cost savings.

All affected customers have been notified via email of the impending migration. CenturyLink will perform the migration and there is no anticipated impact or downtime to the service during the migration. The CenturyLink Cloud Load Balancing-as-a-Service uses a multi-tenant, scalable, and programmable infrastructure presented to the customer as a service; and offers all of the same functionality as the previous offer, as well as additional features and/or functionality that include Health-check monitoring and port forwarding configurations.

You can learn more about the new offer and view pricing on the [Cloud Load Balancing-as-a-Service product page](https://www.ctl.io/load-balancing/). If you have additional questions, please feel free to contact [noc@ctl.io](mailto:noc@ctl.io), or read our [knowledge base article](../../General/LBaaS/LBaaSFAQ.md).

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

##### Cloud Application Manager Platform

###### Spanish and Portuguese supported in the new branding styles emails

Following the Cloud Application Manager branding styles update, Cloud Application Manager emails (new user, reset password, sharing notification, etc.) have been also updated. These emails also show our internationalization efforts, and as a result, Spanish and Portuguese translations have been added. Users receiving emails from Cloud Application Manager will now find the translated versions below the English version of the note.

###### Upgraded VMWare vCloud API support

Cloud Application Manager has extended the vCloud API support to newer versions (v31 and v32) in order to provide long-term support for current and upcoming releases of VMWare vCloud products. CenturyLink Private Cloud on vCloud Foundation providers will also benefit from this extended support for its current 9.7 version as well as for future releases of the product.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Enable self-register instances in vCloud based providers

Application Lifecycle Management has improved self-register instances feature to support additional provider types. Both CenturyLink Private Cloud on vCloud Foundation and VMWare vCloud provider types can now enable self-register feature. A command snippet will be provided to let users add it to any compute bootstrapping process already in use. This will trigger the self-registering of the instance when deployed from outside of Cloud Application Manager.

##### Provider Instance ID is now included in the Instances list export

Application Lifecycle Manager now includes the Provider Instance ID property of each instance to the export list of instances. A new column is added to the exported file to include this value next to the instance-id column. This will improve reporting and auditing tasks by providing a convenient file format for the user to consume as required.

##### Support for new AWS instance types

Application Lifecycle Management now supports additional Amazon Web Services instance types:

 - c5.metal, c5.12xlarge, c5.24xlarge, c5n.metal
 - g4dn.2xlarge, g4dn.4xlarge, g4dn.8xlarge, g4dn.12xlarge, g4dn.16xlarge
 - i3en.metal
 - m5.8xlarge, m5.16xlarge, m5a.8xlarge, m5a.16xlarge, m5d.8xlarge, m5d.16xlarge
 - r5.8xlarge, r5.16xlarge, r5a.8xlarge, r5a.16xlarge, r5d.8xlarge, r5d.16xlarge
 - u-18tb1.metal, u-24tb1.metal

Once the AWS provider is synchronized in Cloud Application Manager, users will be able to select these instance types in their Deployment Policy boxes by searching them in the search box of the Instance Type drop down.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are:
 - "AWS::Cognito::UserPoolDomain"
 - "AWS::Cognito::UserPoolGroup"
 - "AWS::Cognito::UserPoolIdentityProvider"
 - "AWS::Cognito::UserPoolResourceServer"
 - "AWS::Cognito::UserPoolRiskConfigurationAttachment"
 - "AWS::Cognito::UserPoolUICustomizationAttachment"
 - "AWS::EC2::TrafficMirrorFilter"
 - "AWS::EC2::TrafficMirrorFilterRule"
 - "AWS::EC2::TrafficMirrorSession"
 - "AWS::EC2::TrafficMirrorTarget"
 - "AWS::Events::EventBus".

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.

#### [Managed Services Anywhere](https://www.ctl.io/managed-services-anywhere/)

##### Published list of Monitoring Checks

Managed Services Anywhere now publishes a list of all checks that can be consumed within Cloud Application Manager Monitoring.  Previously, this information was available to consumers of Cloud Application Manager, via the Monitoring Catalog.  Now, a dynamically updated Knowledgebase article provides anyone visibility into the checks that can be configured within Cloud Application Manager's Monitoring.  [Monitoring Catalog](https://watcher.ctl.io/docs/check_types/)
