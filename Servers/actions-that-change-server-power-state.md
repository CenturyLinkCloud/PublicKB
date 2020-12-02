{{{
  "title": "Actions That Change Server Power State",
  "date": "12-01-2019",
  "author": "Matthew Ordman",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview
This guide provides a list of the Operating Systems and Control Portal actions that affect the power state of a server on the Lumen Cloud.

### Supported Operating Systems
Please see the [supported operating system KB](https://www.ctl.io/knowledge-base/support/supported-operating-systems/)

### Actions That Affect Specific Operating System Templates

**Action**|**Scale Up**|**Scale Down**
----------|------------|--------------
Change amount of RAM|CentOS 6<br>CentOS 7<br>Debian 6<br>Debian 7<br>RedHat Enterprise Linux 5<br>RedHat Enterprise Linux 6<br>RedHat Enterprise Linux 7<br>Ubuntu 12<br>Ubuntu 14<br>Ubuntu 16|CentOS 6<br>CentOS 7<br>Debian 6<br>Debian 7<br>RedHat Enterprise Linux 5<br>RedHat Enterprise Linux 6<br>RedHat Enterprise Linux 7<br>Ubuntu 12<br>Ubuntu 14<br>Ubuntu 16<br>Windows Server 2012<br>Windows Server 2012 R2<br>Windows Server 2016<br>Windows Server 2019
Change number of vCPUs|CentOS 6<br>CentOS 7<br>Debian 6<br>Debian 7<br>RedHat Enterprise Linux 5<br>Ubuntu 16|CentOS 6<br>CentOS 7<br>Debian 6<br>Debian 7<br>RedHat Enterprise Linux 5<br>RedHat Enterprise Linux 6<br>RedHat Enterprise Linux 7<br>Ubuntu 12<br>Ubuntu 14<br>Ubuntu 16<br>Windows Server 2012<br>Windows Server 2012 R2<br>Windows Server 2016<br>Windows Server 2019

### Actions That Affect **ALL** Operating System Templates

* Clone a server
* Delete a server
* Execute scripts on a server: Depends on the specific script executed
* Pause a server
* Reboot a server
* Reset a server
* Stop a server
* Turn a server off
* Turn a server on
* Archive a server
* Delete archived server
* Restore archived server
* Revert server to snapshot
* Convert a server to a template
* Convert a template to a server
* Remove storage volumes

### Actions That **Do Not** Affect Operating System Templates

* Add a public IP address for a server
* Put a server into maintenance mode
* Remove public IP address for a server
* Take a server out of maintenance mode
* Update public IP address for a server (change port or filtering)
* View a public IP address for a server
* Add alert policy to server
* Remove alert policy from server
* View alert policies applied to server
* View archived servers
* Change scheduled task
* Create scheduled task
* Delete scheduled task
* View server scheduled tasks
* Add storage volumes
* Change custom field values
* Change server description
* Change server group
* Change server password
* Change storage amount of existing volumes
* Create server snapshot: Can impact availability
* Delete server snapshot: Can impact availability
* View server snapshots
* Create a server from a template
* Delete a server template
* View server templates
* Create Alert policy
* Create Horizontal Autoscale policy
* Create Vertical Autoscale policy: May impact power state based on policy rules
* Delete Alert policy
* Delete Horizontal Autoscale policy
* Delete Vertical Autoscale policy
* Edit Alert policy
* Edit Horizontal Autoscale policy: May impact power state based on policy rules
* Edit Vertical Autoscale policy: May impact power state based on policy rules
* View Alert policy
* View Horizontal Autoscale policy
* View Vertical Autoscale policy
* Add horizontal autoscale policy to group: May impact power state based on policy rules
* Change horizontal autoscale policy of a group: May impact power state based on policy rules
* Remove horizontal autoscale policy from group
* View horizontal autoscale policy applied to group
