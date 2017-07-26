{{{
	"title": "Updating CLC-Managed RHUI RPM",
	"date": "04-19-2017",
	"author": "Derek Jansen",
	"attachments": [],
	"related-products" : [],
	"contentIsHTML": false,
	"sticky": false
}}}

### Description
Moving or cloning a RHEL server [across data centers](https://www.ctl.io/service-tasks/#vm-transfer) can cause issues with its ability to use CLC-managed RHUI servers. This's because each data center homes its own RHUI. When a RHEL server is cloned or moved to a new data center, RPM will still target the RHUI in the old one. Below is an example error that can indicate this issue:

```
Could not contact CDS load balancer GB1T3NRHCDS02.t3n.dom, trying others.
Could not contact any CDS load balancers: GB1T3NRHCDS02.t3n.dom, GB1T3NRHCDS01.t3n.dom.
```

It's also possible, although rare, for the RHUI entitlement to expire. Here are two example errors that may be seen if this is the case:

```
https://gb3t3nrhcds01.t3n.dom/pulp/repos/content/dist/rhel/rhui/server/6/6Server/x86_64/extras/os/repodata/repomd.xml:">https://GB3T3NRHCDS01.t3n.dom/pulp/repos///content/dist/rhel/rhui/server/6/6Server/x86_64/extras/os/repodata/repomd.xml: [Errno 14] PYCURL ERROR 22 - "The requested URL returned error: 401 Authorization Required"
```

```
Error: Cannot retrieve repository metadata (repomd.xml) for repository: rhui-rhel-6-server-rhui-rh-common-rpms. Please verify its path and try again
```

The steps outlined in this article will provide instructions on using a script package already available on CLC. This will  ensure RPM is targeting the correct RHUI servers and its entitlement is up to date.

### Detailed Steps
1. Navigate to the server's page in Control.
1. Create a snapshot of it as a back-out plan.
1. Click on the group name containing the server. Select **execute package**.
   - You may need to select the **more...** dropdown menu before seeing that option.
1. Enter "RHUI" in search box under **PACKAGE LIBRARY**. Ensure either the **all** or **public** radio buttons are selected.
1. Select the target server.
   - You'll only be able to select RHEL servers. Others will display **Not Applicable**.
1. Execute the package on that server and monitor the job until completion.
1. Log into the server and verify RPM/Yum is updating properly.

If you're still experiencing errors, please notify us by [submitting a ticket](../Support/zendesk-login-help-for-helpdesk-ticketing-and-kb-access.md). You can also email us at help@ctl.io.
