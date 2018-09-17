{{{
"title": "Cloud Platform - Release Notes: September 18, 2018",
"date": "09-18-2018",
"author": "Andy Watson",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (1)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/)

#### [Application Lifecycle Management](//www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Instances Page Redesign

Application Lifecycle management has a new redesigned instances page where, apart from the existing (registered) instances, now you can see the unregistered instances in a separate view, or both types combined in a single view. These unregistered instances are the virtual machines from any provider that can be registered into Cloud Application Manager to enable lifecycle management. In addition, for AWS providers the Instances page will now list native services instances, classified by Compute, Storage, Network, Database and Other types. These instances will display basic information for each type, such as subtype, region, status, name and description. A great advantage for users is that they will see at a glance all AWS instances in Cloud Application Manager user interface.
The unregistered instances tab in the provider details page remains unchanged for convenience since the user can do a bulk import of unregistered instances from there as they belong to a single provider. Users can also import unregistered compute instances from the new Instances view but is limited to doing an import one instance at a time.
