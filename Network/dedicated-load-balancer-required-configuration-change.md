{{{
  "title": "Dedicated Load Balancer Required Configuration Change",
  "date": "1-15-2016",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview

We've identified an issue with some versions of Citrix NetScaler that cause the NetScaler Load Balancers to stop passing traffic after some specific security patches have been applied. In order to prevent this issue from affecting any NetScalers you may have in your environment, a small change to a configuration file and a reboot is required. We have already begun remediating as many customer NetScaler devices as we can but we have not been able to fix everyone's device.

**We will begin patching our systems after February 8, 2016. In order to ensure that your NetScalers are not affected by this issue, please make sure to complete one of the options outlined below prior to February 8, 2016.**

### What options do I have?

If you have been directed to this article, it means that for whatever reason we were unable to fix your device(s). Most likely this is due to a mismatch between the actual device password and the password stored in Control. Please select one of the following options to ensure that your NetScaler(s) are successfully remediated to prevent the above issue from occurring.

- Check the admin password for your device(s) against what is stored in the Control Portal. (You can follow the article on [how to retrieve Root/Administrator password](https://www.ctl.io/knowledge-base/servers/how-to-retrieve-rootadministrator-password/) for details on how to retrieve the password from Control.) We never access your VMs without notifying you first, but if your admin credentials are properly set in Control, we can fix the issue for you. Once the credentials have been updated to match, you may update us by e-mailing [help@ctl.io](mailto:help@ctl.io) to submit a support ticket so we can schedule the work with you to fix your NetScaler device(s). There will be some downtime (estimated 3-7 minutes) associated with the reboot, so make sure to work with us to perform the reboot during a scheduled maintenance window.

- Alternatively, you may choose to [request a new NetScaler VM](https://www.ctl.io/knowledge-base/service-tasks/deploy-a-dedicated-citrix-vpx-appliance/) from our [service task engineering group](https://www.ctl.io/knowledge-base/service-tasks/requesting-service-tasks-on-centurylink-cloud/) and transition your configuration to that VM. Newer versions of Citrix NetScaler are unaffected by the bug, so getting a new NetScaler in place is an easy fix for the problem. Keep in mind that there is a cost associated with this option - find out more on our [Service Tasks page](https://www.ctl.io/service-tasks/#load-balancer-deployment).

- If you prefer not to request a new device and not to use Control to track your admin password, you may perform the fix yourself on any/all NetScalers that we were unable to remediate or replace for you. Follow the steps below to remediate your NetScaler Load Balancers so they will not be affected by the identified issue.

  1. Log in to each NetScaler box (yes, both devices in an HA pair need the fix performed).

  2. On each device you log into, create or modify the following file:

          /flash/boot/loader.conf.local

  3. At the end of this file, add the following line:

          hw.em.txd=512

  4. Reboot each NetScaler and when it comes back up this device is now protected from the bug.

    _Note: If you have an HA pair, you can ensure no downtime by rebooting the cold node first, failing over to it, then rebooting the formerly hot node, and failing over back to it. If you do **not** have an HA pair, there will be an estimated downtime of about 3-7 minutes associated with the reboot, so make sure to perform the reboot during a scheduled maintenance window._

### What do I do next?

If you have any questions please reach out to us by e-mailing [help@ctl.io](mailto:help@ctl.io).  If you have finished one of the three options above, please let us know by e-mailing [help@ctl.io](mailto:help@ctl.io) to submit a support ticket so we know your NetScaler is healthy.
