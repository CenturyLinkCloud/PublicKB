{{{
"title": "Cloud Platform - Release Notes: February 19, 2019",
"date": "03-05-2019",
"author": "John Gerger",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (6)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

**Track logins via google analytics**

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) has added a Google Analytics tag to track logins into the system. This new tracking method enhances the analytics data we use to have better insights on how Cloud Application Manager is being used by our customers and our support staff

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**Exclude Lifecycle Management option on Deployment Policy Boxes**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports a new Exclude Lifecycle Management toggle in Virtual Machine type Deployment Policy Boxes for all major cloud providers. When the user enable this toggle, the Cloud Application Manager agent will not be installed into the deployed machine, so the instance will be free of any foreign code. The user will be only able to stop/start or terminate these instances, but will also have the option to later enable lifecycle management on this type of instances that will install the agent and allow full management features.

**Display box version in activity log**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now displays the version of the box in the activity log of an instance when executing an event. The user is now able to identify which version of a box has been used when executing an inner box event in the instance. This will help troubleshoot any issue in the even execution by knowing exactly the version that was used and hence the event code version that was used for it.

**Auto-register ARM VM resources in managed providers**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now includes the feature to auto-register VM instances that were deployed as part of a Azure ARM template deployment. The compute instances and ScalingSets included into the template box will be automatically registered in Cloud Application Manager and the make managed process will be executed on them.

**New Cloud Formation types supported**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now supports additional Cloud Formation types to be used in Cloud Formation template boxes. These additional types are:
"AWS::RAM::ResourceShare", "AWS::RoboMaker::Fleet", "AWS::RoboMaker::Robot", "AWS::RoboMaker::RobotApplication", AWS::RoboMaker::RobotApplicationVersion", "AWS::RoboMaker::SimulationApplication" and "AWS::RoboMaker::SimulationApplicationVersion". The user can now use these new resource types in the template definition of any Cloud Formation template box or update the template file of any existing template instance and reconfigure it to use the new resource types.

#### [Public Cloud IaaS](//www.ctl.io/product-overview/#)

**Simple Backup Restore Enhancements**

We are pleased to announce enhancements to the restore functionality of the [Simple Backup Service](https://backup.ctl.io/). We have added restore capability directly to our Simple Backup control portal application, allowing you to now perform restores from one central place. We also added the ability to restore files from one server to any other registered server in your infrastructure. Please see our knowledge base articles for more information on restore features.

https://www.ctl.io/knowledge-base/backup/restores
https://www.ctl.io/knowledge-base/backup/

### Bug Fixes (2)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) Usage History Updates

**AWS RI Validation Reports**

For our AWS resale customers, a bug that delivered a blank .csv with RI Validation Information between the fist and ninth of every month in usage history has been fixed. The option to run the report will only be available on the tenth of each month, when we are certain we have finalized invoices from our vendors.

**Line Items**

Details regarding Promo Codes, AWS SaaS RI purchases which had not previously been shown will be visible.
