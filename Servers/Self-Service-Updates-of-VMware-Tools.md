{{{
  "title": "Self-Service Updates of VMware Tools",
  "date": "01-16-2016",
  "author": "Aaron LeMoine",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


**Description**

VMware Tools is a suite of services and drivers supplied by VMware.  These services facilitate communication between CenturyLink Cloud's VMware vSphere environment and your server (virtual machine).  VMware Tools also provides drivers for memory management, NICs, storage, etc.  These drivers are optimized for use in a virtualized environment.  

Please note that keeping current with VMware Tools is not mandatory in order to receive support for your server in our environment.  VMware supports a wide variety of versions of VMWare Tools with each version of vSphere.  Because of this, an installed version of VMware Tools receives support for a long time.  There are times when a version of VMware Tools contains a bug that is fixed in a later release.  If you encounter the bug condition, it is recommended to upgrade.  As we lifecycle our infrastructure, we may encounter a condition where your version of VMware Tools is so old that it is no longer supported by our current version of vSphere.  If this happens, it will be necessary for you to upgrade to a newer version.

If you would like to update the version of VMware Tools on your servers, this is now available as a self-service task.  This article will discuss the steps needed for you to complete this upgrade. 

**Prerequisites**

Administrative access to servers

**Detailed Steps**
 
Installers for VMware Tools can be found on VMware's website or on Linux vendor repositories.  Prior to upgrading VMware Tools, it is recommended to create a server snapshot if you are able to do so (certain conditions exclude a server from being able to have snapshots).  Please see this link [creating-and-managing-server-snapshots](./creating-and-managing-server-snapshots.md) for instructions on how to create snapshots.  This will give you a known good state should you encounter an issue during the upgrade and need to revert back to the last known good state.  

It is also recommended to reboot your server after installing/upgrading VMware Tools.
 
**Windows**

To update VMware Tools for Windows, you can download them from VMware's website and run the .exe installer.  You can run the installer interactively or silently.  It is recommended that you reboot after installation.

1. If possible, create a server snapshot.
2. Download the latest version from VMware's website via this link [Here](https://packages.vmware.com/tools/releases/latest/windows/x64/index.html)
3. Double-click on the downloaded .exe file to run the installer interactively.
4. Reboot the server.


**Linux**

To update them for Linux, updates should be made available through vendor repositories.  Please contact help@ctl.io for assistance if your Linux server does not connect to a repository properly.  RedHat servers will receive updates from CenturyLink Cloud's RHUI environment.  CentOS, Ubuntu and other Debian variants will receive updates from their respective vendors.

1. If possible, create a server snapshot.
2. Download and install the latest version from your vendor's repository using yum or apt-get.
3. Reboot the server.

 
