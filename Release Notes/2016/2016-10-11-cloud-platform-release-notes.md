{{{
"title": "Cloud Platform - Release Notes: October 11, 2016",
"date": "10-11-2016",
"author": "Christine Naumann",
"attachments": [],
"contentIsHTML": false
}}}


### Enhancements (1)

**status.ctl.io**

We've updated our layout and made upcoming maintenances easier to find! Under our main status message, we identify when our next maintenance is scheduled. This is also a link that redirects below the grid to show the list of all scheduled maintenance events on the main page of [status.ctl.io](https://status.ctl.io/).

Take a look at [status.ctl.io](https://status.ctl.io/) to see our new layout. We will continue to send notifications for upcoming maintenance. You can subscribe to notifications that matter to you by clicking 'Manage Notifications' on the status page.

### Announcements (2)

**SAML**

Upcoming Enhancements to Authentication & Changes for Your SAML Configuration: In the coming weeks, Lumen Cloud will be upgrading its authentication service. Many customers will not experience any material changes as a result of this upgrade. However, customers that have enabled SAML for their Lumen Cloud accounts will be required to make configuration changes to ensure that authentication continues to function. Please review this [FAQ](https://www.ctl.io/knowledge-base/support/authentication-updates-faq/) to understand the action required on your part, if any.

***Network Exchange***

[Network Exchange](https://www.ctl.io/network-exchange/) has been released in SC8/9 -UC1, supporting connectivity from HAN-connected services such as IQ, DCC and others to CLC.

### Bug Fixes (1)

**Load Balancer-as-a-Service Maintenance Mode**

We resolved the following bug with our Load Balancer as a Service:

When the new Load Balancer UI was released on 8/25/2016, customers did not have the ability to take a server out of the Load Balancer config so that maintenance can be performed.  This feature has since been restored and allows for a server to be taken out of the pool temporarily while it's under maintenance.
