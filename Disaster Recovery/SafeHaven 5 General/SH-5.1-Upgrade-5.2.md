{{{
  "title": "Upgrade from SafeHaven 5.1 to 5.2",
  "date": "06-20-2019",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Context
With the release of [SafeHaven 5.2.0](SafeHaven5.2.0-Release-Notes.md), there is manual procedure to upgrade from previous SafeHaven-5.1.* versions.

**Please note that the procedure described in this document is for EXPERTS only**. If there is any doubt, please contact SafeHaven support by creating a ticket with help@ctl.io

#### Special Note about WAN Sync Throttle
Upon SBD upgrade, all PGs will be reset back to the default 2MB/s WAN sync throttle settings. So it is recommended to take note of the existing WAN sync throttle settings for all PGs before the upgrade so that these settings can be manully changed back to the desired settings after the SBD ugprade.

### Upgrade procedure (experts only)
#### 1. Upgrade Syntropy to 5.2.0 using GUI
Do it in the same way used in all upgrades
#### 2. Upgrade Base OS to 5.2.0 using CLI on CMS 
First, ssh to the CMS as the `root` user.

Then run the following command in the `/root/BaseImageConfigurators` folder:
```
root@ip-172-31-0-72:~/BaseImageConfigurators# ./clusterBaseUpdate 
Updating Base on all SRNs...
CMS IP is  54.218.253.206
...
```
This script will update the base os package on each SRN sequentially. It takes a couple of minutes to upgrade one SRN. If there are many SRNs, this process may take some time. Please be patient. You can also ignore the outputs.

Note that we have to re-login to the cluster using the GUI after this.

In order to confirm the change, ssh into the SRN as root and run `dpkg -l |grep safehaven` and you should see something like
```
root@localhost:~# dpkg -l |grep safehaven
ii  safehaven                          5.2.0                                      amd64        CenturyLink SafeHaven. Build 5.2.0
ii  safehaven-base                     5.2.0                                      amd64        CenturyLink SafeHaven-Base. Build 5.2.0
ii  safehaven-sbd                      9.0.2                                      amd64        CenturyLink SafeHaven-SBD. Built for kernel 4.4.0-34-generic and SafeHaven-5.0.1
ii  safehaven-scst                     3.2.0                                      amd64        Specifically built for kernel 4.4.0-34-generic
root@localhost:~# 
```
We expect to see that the `safehaven-base` package is at version `5.2.0`.

#### 3. Upgrade SBD for individual SRNs manually
SBD is the kernel module running on the SRN that is responsible for SafeHaven data replication. 
In order to upgrade it, we need to run the following 3 commands in sequence:
```
/usr/lib/datagardens/scripts/srn_fully_stop.sh 
dpkg -i /usr/lib/datagardens/packages/safehaven-sbd.deb
reboot
```
It is a good idea to check the iSCSI sessions and sbd devices before and after the upgrade/reboot to confirm that the process has worked.
After the upgrade, we should have sbd-9.0.3 which can be checked by
```
root@PD-SRN-Azure:~# sbdm version

SBD release version: 9.0.3 
    
SBD installation requirements: 
        Linux distribution: 
            (1) Ubuntu 16.04.2 LTS(recommended) 
                Supported Linux kernel:  Linux 4.8.0-44-generic(recommended), 
                                         Linux 4.4.0-34-generic 
            (2) Ubuntu 14.04.4 LTS 
                Supported Linux kernel:  Linux 3.13.0-96-generic 
        Snapshot file version: 4.4 
        Bitmap file (for ROW) version: 3.3 (recommended), 
                                       3.2 

SBD(kernel land) version:
    SBD kernel version: 5.3.2 
    SBD build tag: iteration/2019-02-12-45-g8a495ec 
 
SBDM(user interface) Version: 5.3 
```