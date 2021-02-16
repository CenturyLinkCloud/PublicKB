{{{ "title": "Cloud Platform - Release Notes: April 24, 2018", "date": "04-24-2018", "author": "Shasha Zhu", "attachments": [], "contentIsHTML": false }}}

### Enhancements (2)

#### Simple Backup 

Simple Backup now supports VSS snapshots on Windows servers. VSS support allows for backing up open files and preserves files consistency for VSS supported applications and databases running on Windows servers. This has been a highly requested feature and we are excited to deliver this feature. Please see our knowledge base articles for more details. https://www.ctl.io/knowledge-base/backup/


#### Cloud Application Manager

##### Billing Usage History

Cloud Application Manager now presents the Billing > Usage history in a friendlier way. Charges related to 'Application Lifecycle Management', 'Cloud Application Manager Support' and 'Update to previous month Cloud Application Manager Support' are now grouped whenever there are more than one charge corresponding to different providers. You can find a parent line-item with the corresponding total for each one of these categories. Clicking the dropdown will expand the category into details of each individual charge.

##### Cloud Optimization and Analytics

When you provision new, Optimized, AWS providers the process is now expected to be complete within five minutes of clicking the "Save" button. Additionally, you will now automatically receive temporary credentials to your account right within the provider. Click the new "Show Credentials" button to obtain administrator username, temporary password, and login URL for your account. For your security, these credentials are temporary and you will be requested to change them at first login. Thus, we will only show them once.

### Announcements (2)

#### SafeHaven

SafeHaven 5.0.1 was released with following improvements:

* Ensured the proper vSphere library is installed in the SafeHavenAppliance-5.0.1.ova
* An improved internal messaging implementation between SafeHaven nodes to meet even more demanding scalability and security requirements.
* Simplified communication among SafeHaven nodes by not using UDP ports, making it easier to setup.
* Added disk resize funtionality for AWS PGs.
* Now supports the SRNs to be gracefully rebooted.
* Please find more details about the release [here](https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-5-general/safehaven5.0.1-release-notes/#release-notes)

#### Load Balancer as a Service 

Lumen Cloud is excited to release a new load balancer service in our VA2 and WA1 locations. We’re calling it Load Balancer as a Service (LBaaS). We added more features that allow you to focus on your business while we help service your infrastructure. You get to keep all of the features that are available in the current Shared Load Balancer service, but we’ve added a few new things to get excited about:

* TCP load balancing
* Load balance on any port 23 and up
* Configurable health checks

These new features are presently available in our AU1, CA3, DE1, DE3, GB3, IL1, NY1, SG1, UC1, VA1, VA2 and WA1 locations with plans to enable additional locations in the coming months. Be on the lookout for future announcements regarding service expansion. Please note, our Shared Load Balancer service will continue to be available in all other locations until they are LBaaS enabled.

For information on pricing for LBaaS and Shared Load Balancer, see [pricing](https://www.ctl.io/pricing).

### Bug Fixes (4)

#### Cloud Application Manager 

* Fixed issue preventing some Optimized AWS Customers from resetting passwords.
* Fixed Usage History issue that erroneously showed detail totals as double what was actually charged.
* Fixed Usage History drop-downs which did not work for some customers.
* Fixed issue with CAM returning the error to a customer who wanted to migrate an existing AWS account for Optimization and Analytics, which said "Error occurred with inviting customer to AWS."
