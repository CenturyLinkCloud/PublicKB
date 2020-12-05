{{{
"title": "Cloud Platform - Release Notes: June 21, 2016",
"date": "06-21-2016",
"author": "Christine Parr",
"attachments": [],
"contentIsHTML": false
}}}


### Enhancements (2)
* __Control Portal:__
	* **UI Updates -** We continue to make updates to our UI. You will see small changes to fonts, spacing and alignment to the Blueprints, Object Storage, Firewall, Account Info and Services pages.  
<p>
* __Runner UI Updates:__
	- **Public Product Whitelist:** For security and customer experience reasons Runner must provide a product whitelist. Only products whose Product ID exists in the whitelist will be presented on the Public Products page. Lumen will own the management and upkeep of the whitelist.
	- **Custom Naming Support:** Customers currently have the ability to rename their accounts with a custom name within the Control Portal.  Runner now recognizes the custom name and displays it as the customer defined name.
	- **Playbook Flag Support:** When creating a job via the Manual Jobs page, users are able to pass in a flag (not a property) to the execution.  Example flags: --list-hosts, --list-tasks, --check, --diff, etc
	- **Ansible-Runner Version Override:** In order to support the most flexibility for customers, Runner allows you to specify your runtime environment via a requirements.txt file.  This file can specify any number of dependent libraries for executing playbooks including which version of Ansible to run and which version of the clc-ansible-modules to run.

### Announcements (2)
* __Relational DB Datacenter Expansion:__  Effective 6/27, Relational DB will be expanded to the UK, Asia, Canada and an additional east coast data center.  Specific data center locations are GB3, SG1, CA3 and NY1.
<p>
* __Upcoming Enhancements to Authentication & Changes for Your SAML Configuration:__ In the coming months, Lumen Cloud will be upgrading its authentication service. Many customers will not experience any material changes as a result of this upgrade. However, customers that have enabled SAML for their Lumen Cloud accounts will be required to make configuration changes to ensure that authentication continues to function.  Please review this [FAQ](https://www.ctl.io/knowledge-base/support/authentication-updates-faq/) to understand the action required on your part, if any.

### Ecosystem (1)
* __Fortinet:__ Fortinet has integrated their high performing FortiGate platform with the Lumen Cloud. The latest Fortinet technology includes net-gen IPv4/IPv6 firewall, application control, and intrusion prevention, which deliver unmatched granular management and control of data, applications, users, and devices. The Fortinet solution also provides essential protection for remote users and offices such as VPN, endpoint protection, two-factor authentication, and vulnerability management. Click [here](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-fortinet/) to get started.  
