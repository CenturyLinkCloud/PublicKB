{{{
"title": "Cloud Platform - Release Notes: October 16, 2018",
"date": "10-16-2018",
"author": "Matthew Ordman",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (5)

#### Portal

**Context switching enhancements**

We have made enhancements to the context switching behavior to ease management and navigation across sites. When an administrator logs in to Management site, the default scope will be Organization scope. Typically, this role is more focused on managing organization-wide settings, so users will have all these settings accessible whenever they log in. Other user roles will still land in their default personal workspace context. Also, the current context is kept when users switch between Management and Application sites, so users will maintain the same context scope they were working on when they switch between Application site and Managed site.

#### [Cloud Optimization](https://www.ctl.io/cloud-application-manager/cloud-optimization/)

**Customizable AWS Permissions for Operations**

In Optimized AWS Accounts, Customers and CenturyLink Support now have the ability to customize permissions and restrictions for CenturyLink Support. CenturyLink will not make changes without customer consent and all changes will be logged. Please review the KB for [permissions](../../cloud-application-manager/cloud-optimization/partner-cloud-integration-aws-hardening-permissions/).

#### [Analytics](https://www.ctl.io/cloud-application-manager/)

**Read-Only Access to Analytics**

To help administrators with compliance, users may be given Visitor access to Cloud Application Manager workspaces. In addition to reviewing workspace providers, these users will have access to the Analytics site, but will not have the ability to update any resources or instances associated with that workspace.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**Filter by the Provider in Deployment Policy Boxes view**

Application Lifecycle Management now includes a new provider filter in the Deployment Policy boxes view so that users can select one or several among the available provider types, or among existing providers. This allows users to easily list and locate any Deployment Policy box belonging to any specific provider or provider type, either in the list view or in the tiles view.

**Support for new AWS instance types**

Application Lifecycle Management now supports the latest Amazon Web Services instance types: R5, R5d and T3. Once users synchronize their AWS provider in Cloud Application Manager, they will be able to select the new instances type.
