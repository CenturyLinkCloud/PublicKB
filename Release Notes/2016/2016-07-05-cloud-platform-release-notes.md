{{{
"title": "Cloud Platform - Release Notes: July 5, 2016",
"date": "07-05-2016",
"author": "Ryan Brockman",
"attachments": [],
"contentIsHTML": false
}}}


### New Features (2)
* __Runner:__
	* **Gitlab Support -** Runner now supports GitLab in addition to GitHub as a code repository for Playbooks. Users can now reference their Playbooks from any publicly accessible GitLab repository.
	* **Azure Support -** Runner now supports Microsoft Azure! Runner supports minion deployments as well as Playbook executions against Azure.


### Enhancements (2)
* __Runner:__
	* **Playbook Version Support -** Runner now supports the ability for a Playbook to directly reference a specific version of AWS Boto, Azure, or clc-ansible-modules, when executing a Playbook. This allows users to take advantage of updated features of modules or even pin a particular Playbook to a legacy version.
<p>
* __Operating Systems:__
	* **Updated OS Templates -** The following OS templates have been updated with the latest patches from the vendor:
        * RedHat Enterprise Linux 6 | 64-bit
        * RedHat Enterprise Linux 7 | 64-bit
        * CentOS 6 | 64-bit


### Announcements (2)
* __Relational DB Datacenter Expansion:__  Relational DB is now available in the UK, Asia, Canada and an additional east coast data center.  Customers can now provision new Relational DB instances to GB3, SG1, CA3 and NY1.
<p>
* __Upcoming Enhancements to Authentication & Changes for Your SAML Configuration:__ In the coming months, Lumen Cloud will be upgrading its authentication service. Many customers will not experience any material changes as a result of this upgrade. However, customers that have enabled SAML for their Lumen Cloud accounts will be required to make configuration changes to ensure that authentication continues to function.  Please review this [FAQ](https://www.ctl.io/knowledge-base/support/authentication-updates-faq/)  to understand the action required on your part, if any.
