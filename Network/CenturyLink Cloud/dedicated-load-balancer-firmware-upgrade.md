{{{
  "title": "Dedicated Load Balancer Firmware update",
  "date": "12-11-2015",
  "author": "Maxim Volkov",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Table of Contents

* [Introduction](#introduction)
* [Preparation](#preparation)
* [Prerequisites](#prerequisites)
* [Upgrade process (CLI)](#upgrade-process)
* [Conclusion](#conclusion)

### Introduction

To address existing bugs and bring to light set of new features periodically a new firmware for your virtual load balancer is released. To make those improvements available you would need to go through the upgrade  procedure.

### Preparation

Two options exist to perform the upgrade. Both will require to [open a support ticket](../Support/how-do-i-report-a-support-issue.md) with the CenturyLink Cloud NOC.

* First option, CenturyLink NOC performs upgrade for you.

In this case your message to the NOC can follow next format:

```
NOC,

PIN:  Your support PIN
ALIAS:  Customer ALIAS
Data Center:  Data Center Location

Please upgrade firmware on dedicated load balancer: HOSTNAME.

Version to upgrade to: VERSION.00.00
```

This is a Service task and will be [billed accordingly](//www.ctl.io/service-tasks/#Pricing).

* Second option, you perform the upgrade yourself and your message to NOC can be :

```
NOC,

PIN:  Your support PIN
ALIAS:  Customer ALIAS
Data Center:  Data Center Location

Please upload the new firmware to the dedicated load balancer: HOSTNAME. New Version: VERSION.00.00
```

This tutorial will guide through the second option.

When you upgrade HA pair no down time would be required, however the proper planning is the key. The high level preview of the upgrade process looks as follows - disconnect Secondary node from synchronization, upgrade it, convert into Primary node; disconnect original Primary node from synchronization, upgrade it, turn on synchronization, convert into Primary node again.

### Prerequisites

* you have an active account with CenturyLink
* you have HA dedicated load balancers which have been configured under your account
* you have ability to login into appliance with administrative credentials

### Upgrade process (CLI)

We are starting upgrade process with secondary dedicated load balancer.

#### Upgrading first (Secondary) dedicated load balancer.
* Log into your secondary appliance.
* Save the configuration.

##### Command
  ```
  save config
  ```

* Confirm the load balancer is indeed secondary by checking Master State.

##### Command
  ```
  show node
  ```
##### Response

        Node ID:      0
        IP:  10.111.111.102 (VA1OOONSVPX02)
        Node State: UP
        Master State: Secondary
        Fail-Safe Mode: OFF
        INC State: DISABLED
        Sync State: SUCCESS
        Propagation: ENABLED
        Enabled Interfaces : 0/1
        Disabled Interfaces : None
        HA MON ON Interfaces : None
        Interfaces on which heartbeats are not seen : None
        Interfaces causing Partial Failure: None
        SSL Card Status: NOT PRESENT
        Hello Interval: 200 msecs
        Dead Interval: 3 secs
        Node in this Master State for: 3:3:13:0 (days:hrs:min:sec)

* Disable configuration sync from the primary node

  ```
  set node -hasync disable
  ```

* Enter shell mode.

#### Command

  ```
  > shell
  # cd /var/nsinstall/
  ```

*  You are going to find a compressed file in .tgz format. You have to uncompress it and go into newly created directory.

  ```
  # tar xzvf build-11.0-63.16_nc.tgz
  cd 11.0_install
  ```

* Now we initiate the upgrade process.

  ```
  ./installns
  ```

* Follow the inline instructions and reboot your appliance.

* To verify that upgrade took place issue
##### Command
  ```
  show version
  ```
##### Response
        NetScaler NS11.0: Build 63.16.nc, Date: Oct  4 2015, 08:55:49

* Login back into secondary dedicated load balancer.

* Make secondary node a primary one by issuing

#### Command
  ```
  force failover
  ```

* At this point a your appliances change HA node priority. To confirm that do

##### Command
  ```
  show node
  ```
##### Response

        Node ID:      0
        IP:  10.111.111.102 (VA1OOONSVPX02)
        Node State: UP
        Master State: Primary
        Fail-Safe Mode: OFF
        INC State: DISABLED
        Sync State: SUCCESS
        Propagation: ENABLED
        Enabled Interfaces : 0/1
        Disabled Interfaces : None
        HA MON ON Interfaces : None
        Interfaces on which heartbeats are not seen : None
        Interfaces causing Partial Failure: None
        SSL Card Status: NOT PRESENT
        Hello Interval: 200 msecs
        Dead Interval: 3 secs
        Node in this Master State for: 3:3:13:0 (days:hrs:min:sec)

#### Upgrading second (Primary) dedicated load balancer.

* Log into your second appliance.
* Save the configuration.

##### Command
  ```
  save config
  ```

* Confirm the load balancer is indeed secondary by checking Master State.

##### Command
  ```
  show node
  ```
##### Response

        Node ID:      0
        IP:  10.111.111.102 (VA1OOONSVPX01)
        Node State: UP
        Master State: Secondary
        Fail-Safe Mode: OFF
        INC State: DISABLED
        Sync State: DISABLED
        Propagation: ENABLED
        Enabled Interfaces : 0/1
        Disabled Interfaces : None
        HA MON ON Interfaces : None
        Interfaces on which heartbeats are not seen : None
        Interfaces causing Partial Failure: None
        SSL Card Status: NOT PRESENT
        Hello Interval: 200 msecs
        Dead Interval: 3 secs
        Node in this Master State for: 3:3:13:0 (days:hrs:min:sec)

* Disable configuration sync from the primary node

  ```
  set node -hasync disable
  ```

* Enter shell mode.

#### Command

  ```
  > shell
  # cd /var/nsinstall/
  ```

*  You are going to find a compressed file in .tgz format. You have to uncompress it and go into newly created directory.

  ```
  # tar xzvf build-11.0-63.16_nc.tgz
  cd 11.0_install
  ```

* Now we initiate the upgrade process.

  ```
  ./installns
  ```

* Follow the inline instructions and reboot your appliance.

* To verify that upgrade took place issue
##### Command
  ```
  show version
  ```
##### Response
        NetScaler NS11.0: Build 63.16.nc, Date: Oct  4 2015, 08:55:49

* Login back into secondary dedicated load balancer.

* Make secondary node a primary one by issuing

#### Command
  ```
  force failover
  ```

* At this point your appliances change HA node priority. To confirm that do the following:

##### Command
  ```
  show node
  ```
##### Response

        Node ID:      0
        IP:  10.111.111.102 (VA1OOONSVPX02)
        Node State: UP
        Master State: Primary
        Fail-Safe Mode: OFF
        INC State: DISABLED
        Sync State: SUCCESS
        Propagation: ENABLED
        Enabled Interfaces : 0/1
        Disabled Interfaces : None
        HA MON ON Interfaces : None
        Interfaces on which heartbeats are not seen : None
        Interfaces causing Partial Failure: None
        SSL Card Status: NOT PRESENT
        Hello Interval: 200 msecs
        Dead Interval: 3 secs
        Node in this Master State for: 3:3:13:0 (days:hrs:min:sec)

### Issue resolution

If you encounter problems during your upgrade contact NOC for resolution.

### Conclusion

That concludes upgrade of your virtual load balancer. Your HA pair is the same Primary/Secondary state as it was before the upgrade took place.
