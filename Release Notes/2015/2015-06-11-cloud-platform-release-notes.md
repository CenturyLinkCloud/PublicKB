{{{
"title": "Cloud Platform - Release Notes: June 11, 2015",
"date": "6-11-2015",
"author": "Mary Cadera",
"attachments": [],
"contentIsHTML": false
}}}


### New Features (3)

* __Managed OS.__ Clients can leverage our deep expertise in infrastructure and application management and offload critical IT functions for important applications. Managed servers are regularly patched and monitored, so the risks from viruses and other threats are reduced. __Managed OS are now available in three new locations: Singapore (SG1), Toronto (CA3), and Chicago (IL1).__

  Managed OS continue to be available in Virginia (VA1), Santa Clara (UC1) and London (GB3).

### Minor Enhancements (3)

* __Database as a Service.__ Certified Managed MySQL now works with RHEL6 and 7. You can [read more about Managed MySQL in our KB](../../Managed Services/getting-started-with-managed-mysql.md).

* __UI improvements.__ The Control Portal continues to get easier on the eye. We've made some light improvements to the UI that we think you'll appreciate.

* __CenturyLink Cloud Status.__ [status.ctl.io](//status.ctl.io/) provides real-time updates on the status of CenturyLink Cloud services, and upcoming maintenance notifications. Notifications surrounding Compute, Network, and Storage are now based on what servers an account has in a specific data center, allowing our customers to get the information they need - and only the information that they need.

  Our KB has more [information about the CenturyLink Cloud Status service.](../../General/CenturyLinkCloud/centurylink-cloud-status-faq.md)


### Notifications (2)

* __New Domains.__ Effective March 5, the default CenturyLink Cloud domain was updated to control.ctl.io. The URL for SAML users has also been updated to https://[`account-alias`].cloudportal.io (where `account-alias` is your four-letter account identifier). __Please update any code that leverages the CenturyLink Cloud API to ensure that it uses the supported endpoint.__ The legacy domains will continue to operate until July 15.

* __AppFog Limited Beta.__ Beta access for AppFog continues to be available. Based on Cloud Foundry v2, this new platform for applications makes it easier for developers to build and scale cloud-native applications. To sign-up, visit [the AppFog product page](//www.ctl.io/appfog/).


### Bug Fixes (4)

* __Roles: Server Scheduler.__ A user with this role can schedule a power op, but they cannot perform a power op from server details. Now, when a user confirms the action, the user is redirected to the queue request and the request is processed.

* __Intra DC Firewall Additions.__ This experimental API has been updated with improved error messaging. When a user attempts to use this process to create a cross DC firewall, a 400 error is provided. The page loads faster too!

* __Billing for Monthly Recurring Charges.__ We have made updates to ensure that previously omitted additional charges for services such as Dedicated Load Balancers and Cross Connects are included on monthly invoices.

* __OVF Import Timeout.__ Importing cross DC OVF files can sometimes take more than 60 minutes. To ease any pain around this, timeouts have been increased from 60 minutes to 120 minutes.
