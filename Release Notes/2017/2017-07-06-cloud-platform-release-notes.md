{{{
"title": "Cloud Platform - Release Notes: July 06 2017",
"date": "7-06-2017",
"author": "David Gardner",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (5)

* __Cloud Application Manager__

  - __Support for Amazon Linux Operating System__

    *Cloud Application Manager – Managed Services* now includes support for Amazon Linux Operating System. The Amazon Linux AMI is a supported and maintained by Amazon Web Services for use on the Elastic Compute Cloud (Amazon EC2). More about Amazon Linux can be found here https://aws.amazon.com/amazon-linux-ami/. Customers deploying the Amazon Linux Operating System now have an option to "Delegate OS Management" to CenturyLink. With CenturyLink managing their virtual machine instances, customers enjoy all the benefits of *Managed Services Anywhere* listed [here]( https://www.ctl.io/cloud-application-manager/managed-services-anywhere/#Features). Pricing for *Managed Services Anywhere* is defined [here](https://www.ctl.io/cloud-application-manager/managed-services-anywhere/#Pricing).

  - __User Management__

    Organization Administrators can now perform user management operations from the Organization Settings section. An Organization Administrator can perform the following operations
    * View list of users with active, locked or disabled status.
    * Add or Invite users
    * Edit User Details
    * Force reset Password
    * Lock / Unlock users and
    * Delete any User in their organization<br><br>

    For Organizations that have either username/password or LDAP as their authentication mechanism, five (5) consecutive failed login attempts will automatically lock the user account.

  - __Provider Usage Reports__

    Now that all Provider Usage Reports are available in the Dashboard section, the “Reports” page within Admin Console will no longer be available.

* __Simple Backup__

  - __Simple Backup Scheduling__

    Simple Backup now provides a more flexible and customizable way to backup your servers based on a set schedule. This feature allows you to customize your backups for hourly, daily, weekly, monthly or even yearly backups as well as specify what time of the day to execute the backup at. For more information please see our [Knowledge Base FAQ](https://www.ctl.io/knowledge-base/backup/simple-backup-service-faqs/).

* __IaaS__

  - __New Public Cloud Datacenter in Germany__

    Announcing General Availability (GA) for our new DE3 Public Cloud node. Public Cloud IaaS customers now have an additional datacenter location to deploy workloads to in Germany. Learn more on our [blog]( https://www.ctl.io/blog/post/launch-centurylink-cloud-de3/).

### Enhancements (1)

* __Network Exchange__

  - __New Exchanges Available__

    Additional Network Exchanges have been added to enable backend connections between CenturyLink Datacenters. The new exchanges are:
    * SY7/AU1
    * FR6/DE1
    * SG2/SG1
    * SE2/WA1<br><br>

  - __Cloudportal.io Access__

    Enabled access for cloudportal.io accounts.

### Ecosystem Partner Integrations (2)

* __CenturyLink Marketplace Provider Integrations__

  - __[Alert Logic Threat Manager with ActiveWatch](https://www.ctl.io/marketplace/partner/PST/product/Alert%20Logic%20Threat%20Manager%20with%20ActiveWatch/)__ is a cloud-based managed network intrusion detection and vulnerability assessment solution delivered as-a-service that works in any datacenter environment, from on-premises to the cloud. It works the same way in every environment, so you can keep costs down without having to learn multiple systems and hire additional staff.

  - __[FixStream PoC](https://www.ctl.io/marketplace/partner/ZVGW/product/FixStream%20PoC/)__ deploys a FixStream Server for Proof of Concept (PoC) Evaluation. FixStream is a disruptive AIOps (Algorithmic IT Operations) platform that provides a business-centric view of hybrid IT environments to proactively manage, plan, and trouble-shoot in real-time revenue impacting business critical processes.
