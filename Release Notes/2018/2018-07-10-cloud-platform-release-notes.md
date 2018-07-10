{{{
"title": "Cloud Platform - Release Notes: July 10, 2018",
"date": "07-10-2018",
"author": "Chris Meyer",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (5)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

##### Optimized Provider Updates
* Any time a CenturyLink Operations user accesses a customer's AWS account or Azure subscription via the CAM provider, the user will see a log entry of that event within the provider.

##### Application Lifecycle Management

* Import instances deployed by an AWS CloudFormation template
Cloud Application Manager now provides the ability to import AWS EC2 instances that have been deployed as part of a Cloud Formation template deployment. Only the EC2 instance will be imported, and when deleted only the instance would be affected, no other resources that might have been deployed by the same Cloud Formation template would be deleted along with the instance. In other words, this feature enables the import and later lifecycle management of these instances that were deployed as part of a Cloud Formation template, without affecting the rest of the Cloud Formation template components

* Import AWS Autoscaling groups
Cloud Application Manager now provides the ability to import AWS Auto Scaling groups or templates as a single instance. The instances belonging to an Auto Scaling Group or Template will be shown grouped under the Import Instances page in Cloud Application Manager, and they will be imported as a whole into a single instance, that will contain all the related machines. Once properly registered (either providing the certificate for Cloud Application Manager to access the machines and install the agent) or when the agent is installed manually, all the machines would be shown in Cloud Application Manager into the instance details page, and all auto-scaling events would be detected and the instance details updated to show the current machines available into the group. If you terminate the instance in Cloud Application Manager, all the machines of the group would be terminated.

#### [SafeHaven](https://www.ctl.io/managed-services/disaster-recovery/)

* Azure DR Support
  * Added support to use Microsoft Azure Cloud as a Disaster Recovery site with SafeHaven 5.1. Azure site can be selected as a DR site when the production workload is in CLC/VMWare/CPC-vCF/Hyper-V Gen1. Azure as a DR cloud offers minimum checkpoint interval of 5 mins. Azure site as a DR support is an added functionality over already existing AWS DR support which allows pre-existing version Safehaven 5.0 systems to be upgraded without any disruptions

* New Job System
  * Introduction of a completely new job system,  which makes user experience very smooth. It is easier to monitor jobs with the added sub-job feature. The overall response time is significantly reduced due to the new job system. 

