{{{
  "title": "Requesting an OVA or OVF Import via a Service Task",
  "date": "06-09-2020",
  "author": "Derek Jansen",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Images of existing physical or virtual servers can be imported directly onto the Lumen Cloud platform. These images are typically used for either compatibility and performance testing or as part of an overall cloud migration strategy. This article outlines the steps for successfully importing an image onto the Lumen Cloud Platform as a [service task](//www.ctl.io/lumen-public-cloud/service-tasks/#169).

### Detailed Steps

1. Review our [VM import preparation article](../Servers/vm-import-preparation.md) to ensure your VM is ready to be imported.
2. Upload the OVF/OVA file to your account's FTP site. You can find instructions on retrieving the connection details in our [FTP users article](../Control Portal/ftp-users-in-control-portal.md).
3. [Open a support ticket](../Support/how-do-i-report-a-support-issue.md). Provide the following details.
    - [support PIN](../Support/pin-authentication-for-support-requests.md)
    - explict approval of [the service task charges](//www.ctl.io/lumen-public-cloud/service-tasks/#169)
    - [destination account's alias](../Support/determine-control-portal-alias.md)
    - name of the server group in the control portal under which the VM will reside
    - [desired VM name](../Servers/server-naming-convention.md)
    - network to be used by the VM as it's represented in the portal
    - login credentials needed to configure the VM, preferably Administrator (Windows) or Root (Linux), or other super user credentials as applicable
    - any other non-standard configuration details (e.g. instructions on configuring networking on a firewall appliance)
