{{{
"title": "Cloud Platform - Release Notes: August 2, 2016",
"date": "08-02-2016",
"author": "David Gardner",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (3)
* __New CenturyLink Cloud Data Center - VA2 US (Sterling, Virginia) Now Live.__

* __Relational DB: Point in Time Restore__

	Users are now able to restore a Relational DB instance to any point in time, from as far back as one week ago (or the customers' backup retention policy, whichever is shorter) to as recent as 10 minutes ago.<p>

  ![RelationalDBLogo](../../images/rdbs/rdbs-logo-black.png)

* __Runner__

  Our [automated infrastructure management service](https://www.ctl.io/runner/) has added the following new features:
	- __Ansible Module Versions__ - Users can now specify which version of Ansible modules for CLC, Azure, and AWS as part of their Runner job definition. This will allow users to continue to use specific implementations of the modules rather than the latest release.
	- __Marketplace Search__ - Users can now search for products in the Runner marketplace by vendor name.
	- __SHA__ - The SHA value for a Product is displayed in the informational box on the right of a product install page.
	- __Deep Links__ - Users can deep link to specific vendor products. This allows users and/or vendors to share links to specific products to users. When a user enters the URL, they will first be asked to log into Runner, then they will be brought directly to the vendor product.<p>

  ![RunnerLogo](../../images/runner-logo-black-text.png)

### Enhancements (1)
* __CenturyLink Cloud Platform: Inventory Protection__

	The CenturyLink Cloud Platform has added inventory protection for our pool of available Public IP addresses. This change will help to prevent situations in which new Public IP addresses are temporarily unavailable for allocation.<p>

### EcoSystem - New Blueprints (2)
* Two new Blueprints now available on both CenturyLink Cloud and CenturyLink Dedicated Cloud (Intelligent Hosting)
    - __Apache Httpd 2.4 with PHP 5.6 now available for Red Hat Enterprise Linux 6, 7__
    - __IIS version 8.5 now available on Windows Server 2012 R2__

### Announcements (2)
* __MySQL 5.7 has been certified on RHEL 5,6, and 7__ - Now available on both CenturyLink Cloud and CenturyLink Dedicated Cloud (Intelligent Hosting)
* __Upcoming Enhancements to Authentication & Changes for Your SAML Configuration__ - In the coming months, CenturyLink Cloud will be upgrading its authentication service. Many customers will not experience any material changes as a result of this upgrade. However, customers that have enabled SAML for their CenturyLink Cloud accounts will be required to make configuration changes to ensure that authentication continues to function.  Please review this [FAQ](https://www.ctl.io/knowledge-base/support/authentication-updates-faq/)  to understand the action required on your part, if any.<p>

### Bug Fixes (1)
* __MySQL 5.5 build process for RHEL 7 is now fixed__
