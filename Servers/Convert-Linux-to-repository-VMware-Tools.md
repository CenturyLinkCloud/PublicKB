{{{
  "title": "Convert Linux to use repository installed VMware Tools",
  "date": "01-16-2016",
  "author": "Aaron LeMoine",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

On Linux machines that have had their VMware Tools installed via the tools installer in vSphere, installing distribution or kernel updates can cause the VMware Tools to fail.  The solution to this problem is to remove the vSphere installed version and use a repository based version, which should not be affected by subsequent updates.

**Detailed Steps**

We first need to remove the existing vSphere installed version of VMware Tools.  This is done by executing the following script that should exist if the vSphere installed version of VMware Tools is present.

`vmware-uninstall-tools.pl`

If any other versions of VMware Tools have been installed (including open-vm-tools older than 9.4.0 series), they must be removed. 

**RHEL / CentOS:**

`yum remove vmware*`

**Ubuntu:**

`apt-get remove vmware*`
Import the following keys

**RHEL / CentOS:**

`rpm --import http://packages.vmware.com/tools/keys/VMWARE-PACKAGING-GPG-DSA-KEY.pub`
`rpm --import http://packages.vmware.com/tools/keys/VMWARE-PACKAGING-GPG-RSA-KEY.pub`

**Ubuntu:**

`wget http://packages.vmware.com/tools/keys/VMWARE-PACKAGING-GPG-DSA-KEY.pub -O - | apt-key add -`
`wget http://packages.vmware.com/tools/keys/VMWARE-PACKAGING-GPG-RSA-KEY.pub -O - | apt-key add -`

**Create the config file for the new repository:**

**RHEL/CentOS 5:**

`echo -e "[vmware-tools]\nname=VMwareTools\nbaseurl=http://packages.vmware.com/tools/releases/latest/rhel5/\$basearch\nenabled=1\ngpgcheck=1" > /etc/yum.repos.d/vmware-tools.repo`

**RHEL/CentOS 6:**

`echo -e "[vmware-tools]\nname=VMwareTools\nbaseurl=http://packages.vmware.com/tools/releases/latest/rhel6/\$basearch\nenabled=1\ngpgcheck=1" > /etc/yum.repos.d/vmware-tools.repo`

**Ubuntu 14:04:**

`echo "deb http://packages.vmware.com/packages/ubuntu trusty main" > /etc/apt/sources.list.d/vmware-tools.list`

**Install VMware Tools**

**RHEL/CentOS 6:**

`yum install vmware-tools-esx-kmods vmware-tools-esx-nox`

**RHEL/CentOS 7:**

`yum install open-vm-tools`

**Ubuntu 12.04:**

`apt-get update && apt-get install vmware-tools-esx-kmods-$(uname -r) vmware-tools-esx-nox`

**Ubuntu 14:04:**

`apt-get update && apt-get install open-vm-tools open-vm-tools-deploypkg`


Additional Information

If you receive a message that vmware-tools-esx-kmods-<kernel version> doesn't exist, look for the one with the closest kernel version and install it.
aptitude search vmware-tools-esx-kmods
