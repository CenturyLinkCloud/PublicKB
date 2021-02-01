{{{
"title": "Cloud Platform - Release Notes: August 6, 2019",
"date": "08-06-2019",
"author": "Gary Lazaroff",
"keywords":["lumen", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### Sharing notifications for instances, boxes and providers

Cloud Application Manager adds notifying users about new resources (instances, boxes or providers) they can access. When sharing a resource with a user or a team workspace, or when adding a new resource to a team workspace, a visual indicator in form of a badge will be shown for all users who are getting direct access to the resource.

The notification indicators are per workspace (individual or team). The badges are shown for the resources present in the user's currently selected workspace.

Badges with the number of new resources will be shown in the left menu (on the Instances, Boxes, Providers menu items) and in the Context Switcher (for each workspace). Badges in the form of a red dot will be shown on each new (shared or added) resource in the lists of instances, boxes, and providers.

When a user accesses a new resource, the notification will be cleared for the user. A user can clear all notifications for all the user's workspaces from a new top menu (the bell icon).

In addition to badges, it is also possible to select email notifications when sharing resources with other users. When sharing with a team workspace all members will receive an email with a description and a link to the resource.

##### Providers' list export feature

Cloud Application Manager now includes a button in the top right corner of the providers' list page to allow the user to export the list of providers that are available in the current scope in a CSV or PDF file format. All columns in the providers' list will be displayed in the exported file along with some additional ones such as creation time, cost center and organization name. This will ease reporting and auditing tasks by providing a convenient file format for the user to consume as required.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Instances list export feature

Application Lifecycle Manager now includes a button in the top right corner of the instances list page to allow the user to export the list of instances that are available in the current scope in a CSV or PDF file format. All columns in the instances list will be displayed in the exported file along with some additional ones such as instance-id, service type, hostname, creation time and organization name. This will ease reporting and auditing tasks by providing a convenient file format for the user to consume as required.

##### Instances page now displays Lumen network resources

Application Lifecycle Management's Instances page will now list Lumen network resources, such as Virtual Networks and VPNs. These resources will be shown as unregistered instances with some basic information for each type such as subtype, data center, status, name and description. If you have an existing Lumen Cloud provider already set up, you need to synchronize it for these resources to be discovered. More types of native resources from Lumen Cloud will come soon to the Cloud Application Manager instances page.
