{{{
"title": "Cloud Platform - Release Notes: September 12, 2017",
"date": "9-12-2017",
"author": "Andy Watson",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (1)

* __Cloud Application Manager__

	- __TLS Upgrade__<br>
	As part of our impovements to Cloud Application Manager, we will be upgrading our product to use Transport Layer Security (TLS) 1.2 on September 12, 2017. you can find more information about it here.<br><br>Within Cloud Application Manager, when you deploy an instance, Cloud Application Manager installs an agent that is communicating with our backend services. Going forward when you deploy a new instance, the communication is going to happen using TLS 1.2 Protocol.<br><br>Please note that this will not impact any deployed instances, only new deployments will use  TLS 1.2 for agent communication.<br><br>In addition, if you wish to have all your existing instances use TLS 1.2, please contact us.

	- __Domain Change__<br>
	As part of our ongoing efforts to transform ElasticBox into Cloud Application Manager platform, we will be making changes to the user experience on how our customers access our platform.<br><br>Starting September 12th, 2017 all requests, except API and agent communications, to elasticbox.com will be redirected to cam.ctl.io. elasticbox.com will still be operative and will continue to honor API requests and agent communications to the backend services for the next 6 months.<br><br>If you are using custom domain to access Cloud Application Manager <organisation>.elasticbox.com, please note that going forward you need to access your custom domain at <organization>.cam.ctl.io<br><br>We strongly advise you to make changes to the API integrations and use the new domain, as the elasticbox.com domain will be discontinued in 6 months. We also encourage you to change bookmarks or any other reference that you may be using.<br><br>If you have additional inquiries or need more information, please do not hesitate to contact us.


* __SafeHaven 4.0.3 Released__<br>
Note: This is a patch release for SafeHaven 4.0.2

	- __Add Support for Windows Server 2016__
	- __Automatically resize storage pool when the backing storage is resized__
	- __Fully support the migration use case__
	- __Fully support servers with more than 10 disks__
	- __Improve error logging in Windows server__
	- __Added resiliency to PG resize__
	- __Better support for Windows Dynamic Disks__
	- __Better error handling of re-failover__
	- __A number of minor GUI fixes such as typos, error messages, resolution
  problems etc__
