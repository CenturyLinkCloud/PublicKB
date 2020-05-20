{{{
"title": "Cloud Platform - Release Notes: April 28, 2020",
"date": "04-28-2020",
"author": "Madhu Pavanraj",
"keywords":["centurylink", "release notes", "cam", "alm", "cloud"],
"attachments": [],
"contentIsHTML": false
}}}

### Announcements (1)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Deprecation of VMware vCloud provider legacy mode

Cloud Application Manager has deprecated the legacy mode of the VMware vCloud provider. This mode allowed customers to use old versions of vCenter as providers in Cloud Application Manager while they planned for the upgrade of their vCenter environments to newer versions. We have confirmed that no customers are still using the legacy support, so we are removing it from Cloud Application Manager. Customers can continue using vCenter with the current and newer supported versions.

### Enhancements (1)

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Allow variables and events to be added to deployment policies deployed instances

Application Lifecycle Management now allows adding variables and events into instances that have been deployed through a Deployment Policy Box, instead of a Script Box. Users can now use the Life-Cycle Editor on these instances to add any event or variable if they have the corresponding write permissions. This feature is only available for newly deployed instances; the previously existing instances will not allow adding events or variables.
