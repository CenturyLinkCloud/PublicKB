{{{
"title": "Cloud Platform - Release Notes: October 1, 2019",
"date": "10-01-2019",
"author": "David Gardner",
"keywords":["lumen", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (3)

#### Application Lifecycle Management

##### Google Cloud Engine support updates 

Application Lifecycle Management (ALM) has made a major update of the Google Cloud Engine support. It now adds support for:
* Discovery of existing compute instances already deployed into Google Cloud provider type.
* Registration of discovered instances into Cloud Application Manager.
* Supports the native terminate protection feature and synchronizes its status whenever it is configured in Cloud Application Manager or when an instance is registered.
* Enablement of this type of providers to use self-register. A command snippet will be provided to let users add it to any compute bootstrapping process to perform the self-registering of the instance when deployed from outside of Cloud Application Manager.

All the above features will be available in your existing Google Cloud providers, once you synchronize them.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes. These additional types are: "AWS::QLDB::Ledger" and "AWS::Glue::Workflow". Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.

#### Cloud Optimization

##### Integrated AWS in Asia Pacific Region

Lumen has been authorized by Amazon Web Services to support consolidated billing and management of accounts for customers headquartered within select countries within the Asia Pacific Region. A Lumen representative should be contacted for a detailed list of geographic, sector, and feature availability.

#### Redhat Upgrades

##### Red Hat 6 & Red Hat 7 Upgrades

As communicated in the previous Release Notes from September, 17th 2019 and in customer email communications, the Lumen Cloud team performed an automatic update on all Red Hat 6 & Red Hat 7 machines to point to the new RHUI 3.X. This update was successfully performed on all customers designated machines without downtime or incident on October 2, 2019. This update allows customers to continue to receive crucial RedHat package updates.

