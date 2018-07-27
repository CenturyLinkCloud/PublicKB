{{{
"title": "Cloud Platform - Release Notes: July 26, 2018",
"date": "07-26-2018",
"author": "David Gardner",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (5)

#### [Public Cloud Infrastructure as a Service](//www.ctl.io/product-overview/#)

##### Control Portal Design Update

We've updated CenturyLink Cloud's control portal user interface with a new look and feel. Our new aesthetic design has been applied across all of our cloud services to give users a similar experience across products.

There are no functionality or feature changes associated with this user interface update.

##### Virtual Machine Power Operation Retries

We have improved our orchestration for Virtual Machine power operations. Customers should experience fewer scenarios where blueprint operations involving Virtual Machine power operations fail.

#### [Simple Backup Reporting](//www.ctl.io/simple-backup-service/)

We are pleased to announce the addition of reporting functionality to the Simple Backup Service. The Simple Backup reports easily enable you to view the statuses of your backups and restores. Reports are generated in a CSV format for easy consumption, and are currently available from the Simple Backup section within CenturyLink Cloud Control Portal, as well as directly from our public API's. Please read our knowledge base articles for more information on the [reporting features](//www.ctl.io/knowledge-base/backup/reports/) and [API functionality](//www.ctl.io/api-docs/v2/#simple-backup).

[//www.ctl.io/knowledge-base/backup/reports/](//www.ctl.io/knowledge-base/backup/reports/)

[//www.ctl.io/api-docs/v2/#simple-backup](//www.ctl.io/api-docs/v2/#simple-backup)

#### [Cloud Application Manager](//www.ctl.io/cloud-application-manager/cloud-optimization/)

##### Application Lifecycle Management

**Task variables improvement:** Application Lifecycle Manager now supports two additional events to associate with "Task Variables". Apart from the existing 'deploy' and 'remove' events associated with an instance, Application Lifecycle Management now supports 'post-deploy' and 'teardown' events. These two events are associated with the corresponding events (including power-on and stop) of every machine of the instance (one or many), and the script associated also executes whenever an auto-scale event occurs related to the new provisioned/disposed machine. The execution of this code script is still performed outside the VM the task variable is associated with, in a controlled environment. Users also have access to the data of the associated machine such as IP addresses, so that the values can be used inside the code. The knowledge base article has been updated to reflect this improvement: [//www.ctl.io/knowledge-base/cloud-application-manager/automating-deployments/running-code-outside-an-instance/](//www.ctl.io/knowledge-base/cloud-application-manager/automating-deployments/running-code-outside-an-instance/)

**Support for Azure Managed Disks:** Application Lifecycle Manager now includes support to configure Azure deployment policies to use Managed Disks instead of block blobs as the storage type. Managed disk types are the default recommended option from Microsoft, and Application Lifecycle Management now aligns with this recommendation by adding this support to Microsoft Azure deployment Policies.

### Announcements (1)

#### [Public Cloud Infrastructure as a Service](//www.ctl.io/product-overview/#)

We have removed the ability to provision Hyperscale servers from our "Create Server" page.

On June 20, 2018, CenturyLink Cloud announced the retirement of our Hyperscale server type. For more information, please see our [FAQ](//www.ctl.io/knowledge-base/servers/hyperscale-eol-faqs/): [//www.ctl.io/knowledge-base/servers/hyperscale-eol-faqs/](//www.ctl.io/knowledge-base/servers/hyperscale-eol-faqs/)
