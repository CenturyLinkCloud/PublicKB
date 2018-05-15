{{{
"title": "Cloud Platform - Release Notes: November 07, 2017",
"date": "11-07-2017",
"author": "Anthony Vetter",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (3)

__Application Lifecycle Management__

   Cloud Application Manager now provides a Boxes Catalog view where you can see all available public boxes categorized as Featured, Managed Services, Plugins and Others to easily locate & deploy. More Public Boxes will be coming soon.

__Cloud Optimization and Analytics__

* __Historical Monthly Cost Dashboard__

   Building on top of our recently released (Costing Dashboard)[https://www.ctl.io/knowledge-base/release-notes/2017/2017-09-26-cloud-platform-release-notes/] and current (Month Cost Dashboard)[https://www.ctl.io/knowledge-base/release-notes/2017/2017-10-10-cloud-platform-release-notes/] Cloud Application Manager customers with Optimized AWS providers now have access to monthly reporting that provides a granular breakdown of cost by service historically in order to further understand how an environment is performing financially over time.

   Customers can access this new historical reporting functionality in the Cloud Application Manager’s Analytics site by selecting ‘Cost’ then ‘Monthly Reports’ from the left-hand navigation bar and then selecting your targeted month.

__Managed Services Anywhere__

   Cloud Application Manager’s Managed Services Anywhere now includes support for Tomcat and Apache, enabling large-scale, mission-critical web applications to be deployed on AWS or Microsoft Azure (CenturyLink Private Cloud on VMware Cloud Foundation). By selecting to deploy Managed Tomcat and/or Apache servers to AWS or Microsoft Azure - (CenturyLink Private Cloud on VMware Cloud Foundation) - customers get all the features of a managed server along with management of the Tomcat / Apache instance. Simply Delegate Management to CenturyLink and receive Monitoring, Alerting, Ticketing, Remote Administration and Patching for both the VM and the Tomcat / Apache intance.

Supported Versions:
* Tomcat 7.0, 8.0 & 8.5
* Apache (httpd) 2.4

Supported Operating Systems:
* Managed RHEL 6 or 7
* Managed AWS Linux

Supported Cloud Providers:
* AWS
* Microsoft Azure
* CenturyLink Private Cloud on VMware Cloud Foundation

### Enhancements (1)

* __SafeHaven Version: 4.0.4__

   This is a patch release for SafeHaven 4.0.3 with only ONE particular new feature:

   At the time of automatically deploying the CLC recovery proxy servers using the SafeHaven GUI, the user now has a choice to NOT create a new CLC folder. This will make it easier for the users to manage their DR infrastructure.

   Official Release Notes Link: https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/safehaven-4.0.4-release/

### Announcements (1)

* __Public Cloud IaaS__

  Default location for new web sign up customers in the United States has been switched from NY1 to VA2.

### Bug Fixes (7)

__DCC General Bug Fixes__

* __Bug fixes for Create VM:__

   Added validation error if the catalog is from a different cluster.

* __ESX Validation error handling in UI:__

   When a validation fails during add product, the API was returning a generic error code to the UI. This has been updated to return a more specific error message.

* __OS Validation bug fix:__

   Added better wording for validation error message for CPU requirement check.

__Public Cloud IaaS Bug Fixes__

Resolved a bug where some V1 API responses were being truncated before all the data was returned.

Fixed an issue where some VPN server creations were failing.

Enhanced our functionality for adding disks to Virtual Machines running a Linux distribution as an Operating System - users will experience less failures.

Resolved a bug that caused network flapping when deleting site to site VPNs in some scenarios.
