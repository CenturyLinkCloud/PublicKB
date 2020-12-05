{{{
  "title": "Monitors for Managed Operating Systems",
  "date": "02-12-2015",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview
This document provides an overview of the monitors that are enabled with Managed Operating Systems and offers some details about the monitoring process.

### Audience

Users employed by companies that have agreed to terms with [Lumen Sales](http://www.centurylink.com/) for the Lumen Cloud product.

### Prerequisites
* An understanding of the process for [making newly created servers managed](../Managed Services/created-a-managed-server-now-what.md) or for [converting pre-existing servers to managed](../Managed Services/converting-unmanaged-virtual-machines-to-managed.md)
* Review of the general platform [Services Guide's](https://www.ctl.io/legal/serviceguide/) Managed Services section, specifically Managed Operating Systems.
* Review of the [Services Guide](http://service-guides.centurylink.com/Default.aspx?ReturnUrl=%2fHandlers%2fDownloadPDF.ashx%3fid%3d{55962F17-2DA3-446D-9ED3-67DC3CF30F6F}&id={55962F17-2DA3-446D-9ED3-67DC3CF30F6F) for Managed Operating Systems

### Details

Monitoring alerts from Managed, CLC servers are enriched with your company's data, including your primary technical point of contact, and presented to the Global Operations team. After reviewing the issue, the Operations team will either resolve the issue or reach out to your primary technical contact.

You are encouraged to set up a primary technical contact by contacting Support as soon as possible. If you have not set up a primary technical contact, the default contact will be an arbitrary contact associated with your account. **The primary technical contact is NOT retrieved from the notification contacts you may have identified in Control Portal.** The notification users in the Control Portal will be recipients of alerts directly from the portal.

If you have specific or detailed contact strategies and/or remediation requirements for your servers, you are encouraged to contact Support. Your requirements will be documented and presented to Operations whenever they review alerts coming from your servers.

If you wish to set up maintenance activity, such as an update, please contact Support. During the time you schedule, alerts will be suppressed and prevent unnecessary and confusing contacts for you.

The following monitors have default settings at the time the servers are made managed, but can be adjusted by making a request with operations. If you have any questions about what other monitors are available, you are encouraged to contact support.

**Monitor** | **Description** | **Threshold** | **Frequency of Check**
---- | ---- | ---- | ---
CPU | Percentage of total CPU used | 100% average for 15 minutes (VM so can go over 100%) | 1 minute
Memory | Percentage of total Memory used | 97% (Win) 95% (Unix) average for 15 minutes | 1 minute
Disk Usage - Priority 3 | Percentage of total disk used | 90% | 1 minute
Disk Usage - Priority 2 | Percentage of total disk used | 95% | 1 minute
Port Reachable | Is it possible to reach the port? |Not reachable | 1 minute
Heartbeat | The monitoring agent on your server sends a heartbeat to a secondary system so that if there was ever a fault with the agent, we are notified. | No heartbeat | 1 minute checks (alert at 7 minutes without response)
