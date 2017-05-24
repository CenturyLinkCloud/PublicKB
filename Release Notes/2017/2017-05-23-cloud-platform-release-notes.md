 {{{
"title": "Cloud Platform - Release Notes: May 23, 2017",
"date": "5-23-2017",
"author": "Bob Jackson",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (1)

 __Cloud Application Manager__

* **Bulk Import of auto discovered instances**
Cloud Application Manager now allows users to register auto discovered instances in bulk. Full instructions on how to use this new feature are available in the Knowledge Base section on our website.

* **Microsoft Azure Resale available for U.K. based customers**
Azure resale to companies based in the United Kingdom is Live! From the Azure Provider, users whose main registered address with CenturyLink is in the United Kingdom, will be permitted to automatically provision new Azure accounts for consolidated billing and platform level support. The capabilities that CenturyLink Resell will still be the same as [defined here](../../Cloud Application Manager/Cloud Optimization/partner-cloud-integration-azure-capabilities.md).

### Enhancements (3)

 __Load Balancer as a Service__

Load Balancer as a Service has added URI as a supported load balancing method. This new capability is now available in addition to Least Connection, Round Robin, and Source IP support.

 __Managed Applications__

Application Product Engineering has tested and certified Apache Tomcat 7.0.77, 8.0.43 and 8.5.14 on RHEL  6 and 7.

The Software Policies to use for RHEL 6 and 7 have been combined into a single policy. The script which installs the package is now able to detect which major version of RHEL is targeted for the install, and uses the appropriate RHN channel for the installation.

 __Safe Haven__

This is a patch release for SafeHaven 4.0.1.

The following 3 features/bug-fixes have been introduced:

1. Improving CMS performance under certain conditions by reducing file writes.
2. Allowing the deletion of a protection group in a "Failover" state.
3. Slight improvement of the Test Failover temporary space allocation policy.
   * There is a bare minimum temporary space requirement of 2GB.
   * GUI will suggest a default of 5GB temporary space.
   * Automatic deletion of the test failover instance when there is less than 1GB of free space left.
