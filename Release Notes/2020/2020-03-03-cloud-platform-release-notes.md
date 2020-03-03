{{{
"title": "Cloud Platform - Release Notes: March 3, 2020",
"date": "03-03-2020",
"author": "Craig Wedbush",
"keywords":["centurylink", "release notes", "cam", "alm", "msa", "compute instances", "cloudformation"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (3)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Support for running ALM agent as a non-root account

Application Lifecycle Management has added support for running the ALM agent as a non-root account in Linux-based VM instances. In the configuration tab of the provider details page, there's a new option to configure it. If the user specified does not exist, it will be created during the bootstrapping of the agent for a new instance. Users can also specify the mode in which the agent will execute any event. That is, as an admin, as the specified user, or automatic (the agent will try to execute as root if it has permissions to do so, or as the current user otherwise). These settings are applied to all instances deployed into the provider and can be overridden at instance level once it has deployed. That means that every time there is a new event to execute, the agent will use the previously chosen user and mode to perform it.

##### Support for the GCP US west (Salt Lake City, Utah, USA) region

Application Lifecycle Management now supports another Google Cloud Platform (GCP) region: US west (Salt Lake City, Utah, USA) and its corresponding availability zones, with the API name of us-west3. Once you synchronize your Google Cloud provider in Cloud Application Manager, you will be able to select any of the three availability zones of the new region in your Deployment Policy boxes. This applies to the current GCP bring your own cloud support.

##### New CloudFormation types supported

Application Lifecycle Management now supports additional CloudFormation types to be used in CloudFormation template boxes.

These additional types are:

* "AWS::Config::ConformancePack"
* "AWS::Config::OrganizationConformancePack"
* "AWS::EC2::LocalGatewayRoute"
* "AWS::EC2::LocalGatewayRouteTableVPCAssociation"
* "AWS::FMS::NotificationChannel"
* "AWS::FMS::Policy"

Users can now use these new resource types in the template definition of any CloudFormation template box or update any existing template instance to use it.
