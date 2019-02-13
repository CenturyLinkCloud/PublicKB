{{{
  "title": "Best Practices and Preparation for a Virtual Machine OVA/OVF Import",
  "date": "02-11-2019",
  "author": "Christian Presley",
  "attachments": [],
  "contentIsHTML": false
}}}

#### OVERVIEW

The CenturyLink Cloud Service Task team can import images of existing physical or virtual servers directly onto the CenturyLink Cloud Platform. These images are typically used for compatibility and performance testing, or as part of an overall Cloud migration strategy.

This article outlines the recommended practices for successfully importing an image onto the CenturyLink Cloud Platform.

There are additional Knowledge Base articles that outline the steps needed to export an existing Virtual Machine (VM) from different hypervisors such as [Xen](../Servers/converting-a-xen-image-to-ovf-for-use-in-centurylinkcloud.md) or [VMware Workstation](../Servers/exporting-a-vm-to-an-ovf-from-vmware-workstation-for-import-into-the-centurylink-cloud.md)


#### Pre-requisites

This is the basic information that will be required for importing OVF or OVA files:

* Desired name for the VM, following our [CenturyLink Cloud Naming Conventions](../Servers/server-naming-convention.md))
* Root or Administrator password
* Verify that the Guest Operating System is supported on the CenturyLink Cloud Platform for import [Supported Guest Operating Systems for OVA and OVF Import](../Service Tasks/supported-guest-operating-systems-for-ovaovf-import.md)
* Determine if you want to take advantage of our [Managed Operating System Services](../Managed Services/managed-operating-system-frequently-asked-questions.md) - You cannot convert a Managed VM to Unmanaged, but you can convert an Unmanaged to Managed VM.
* Account and Group in the Control Portal that the Virtual Machine(s) will be registered in
* Verify which Virtual Network/VLAN to create the VM on, and ensure the network is already created in the Control Portal

#### Requirements and Recommendations

* The VMware hardware version in the vmx file must be 11 or greater

* If exporting multiple VMs or a collection of VMs, CenturyLink Cloud requires each VM is exported individually. Individual files provide greater flexibility and reduce the need for repeated uploads in the event of file corruption or transfer failures

**Note:** vApp import is not supported

* To reduce file transfer time and ensure file integrity, CenturyLink Cloud recommends the use of a compression or archival tool to compress the OVA/OVF. CenturyLink recommends 2-4GB increments to aid in the upload process. We recommend the open-source utility [7zip](http://www.7-zip.org/)

* Create a checksum hash of the files to be uploaded, and provide the checksum in a text file zipped with the image(s). There are several tools available on Windows and Linux, but the most common is certutil for Windows, and openssl for Linux:

  * certutil -hashfile .\filename sha1

  * openssl sha1 /path/to/filename

* Upload the OVF/OVA file to the desired datacenter. Ensure the FTP server selected to upload the OVA/OVF file(s) corresponds with the desired deployment datacenter.

**Note:** The FTP URL and username/password to upload the images will be provided to you as part of the Service Task. If you are uploading an OVF, the OVF, VMDK and MD files must reside in their own folder. Do not use the FTP information from Control Portal. This FTP service is not for OVF/OVA uploads, and is designed for scripts and packages. For more information, please reference the [KB article about Portal FTP usage](../Control Portal/ftp-users-in-control-portal.md))*

* Member servers may rely on domain controllers not present in the CenturyLink Cloud environment to properly authenticate or execute policies. Please take this into consideration when planning the upload priority, order and testing methodology. While not always possible, it is recommended to remove the machine from the domain prior to exporting, rejoin the domain after the import is complete, as the virtual hardware, SID and other descriptors will have changed

* Snapshots are available for imported templates, but note these are not considered backups and should be used for specific purposes

* Describe any necessary dependencies, application specifics, or any non-standard configurations that may need to be tested for functionality

* Contact [help@ctl.io](mailto:help@ctl.io) to initiate a Service Task for the image import(s)

Following these recommended practices will ensure successful deployment of your VM or Virtual Appliance on the CenturyLink Cloud Platform.
