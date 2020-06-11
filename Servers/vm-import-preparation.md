{{{
    "title": "Preparing a VM for Import",
    "date":"06-09-2020",
    "author": "Derek Jansen",
    "attachments": [],
    "contentIsHTML": false
}}}

### Overview

There are many considerations to be made when peparing your VM for import into CenturyLink Cloud. This article will cover the following subjects.

- [Ensuring Portal Functionality](#ensuring-portal-functionality)
- [Minimum Requirements](#minimum-requirements)
- [Self-Service Import Requirements](#self-service-import-requirements)
- [Service Task Import Requirements and Recommendations](#service-task-import-requirements-and-recommendations)

### Ensuring Portal Functionality

Before importing the VM, you may want to ensure it will be fully compatible with the portal and platform automation, but this is optional and will not prevent the VM from being imported. In order to ensure these capabilities, the below requirements must be met.

- SCSI must be used, and only 1 SCSI controller is supported. Refer to this VMware article for more information: https://kb.vmware.com/s/article/1016192.
- LVM and striped Windows volumes are not supported.

Meeting the following conditions is optional when importing via a service task. **However**, a self-service import will still need these items to be met.

- The OS firewall must not block Ping.
- VMware Tools must be installed.
- For functionality with *Linux* operating systems:
    - Bash shell must be installed.
    - Direct Root access via SSH on port 22 must be enabled, and Root must be accessible with a password (access with a private key is not supported).
- For functionality with *Windows* operating systems:
    - SysPrep must be allowed to run so that the VM can be updated to use the CenturyLink Cloud Windows license. This is billed to your account.
    - The platform must have Administrator (with password) access to PowerShell on ports 5985 and 5986 using. PowerShell must be at least version 2.0, but version 3.0+ is highly recommended.

### Requirements and Recommendations

Review the following sections. There are minimum requirements which must be met, regardless of how the VM is imported, and there are lists of conditions that must be met based on the method used to import the VM.

#### Minimum Requirements

There are minimum requirements that your VM must meet. The following will apply to any import, regardless of whether it was done self-service or via a service task.

- The VM must be one of our [supported operating systems](../Support/supported-operating-systems.md).
- It must be possible to configure a static IP address. DHCP is not supported, and public IP addresses cannot be assigned directly to the VM.
- The VM must not be joined to a domain. Remove the VM from its domain before exporting it to an OVA/OVF.
- The virtual hardware version (VMX) must be 11.
- vApp imports are not supported.

#### Self-Service Importing Requirements

In order to perform a self-service import, the below minimum requirements must be met. If your VM does not meet these requirements, review the [service task requirements](#service-task-import-requirements-and-recommendations) and consider importing it via a service task.

- Review the [Ensuring Portal Functionality section](#ensuring-portal-functionality) of this article. There are conditions listed there that, while optional for service task imports, are mandatory for self-serivce imports.
- The VM files must be in OVF format. At this time, OVAs can only be imported via a service task.
- Use only alphanumeric characters in the file/folder names of your OVF because special characters may result in failure. This is normally done when exporting the OVF from the old environment.

Review our [self-service import instructions](../Servers/using-self-service-vm-import.md) for guidance on performing the import.

#### Service Task Import Requirements and Recommendations

In order to have a VM imported via a service task, the below minimum requirements must be met.

- The VM must be accessible as Administrator with a password. RDP and PowerShell access is not required, but it is highly recommended as described in other sections of this article.
- VMs are supported from other x86/x64 virtualization services, so long as the image is converted to an OVF/OVA (Xen, KVM, Hyper-V).
- VMs are not supported from virtualization services outside of the x86/x64 architecture (Intel IA64, Oracle SPARC, HPVM, Solaris containers, IBM PowerVM).
- If exporting multiple VMs or a collection of VMs, we require each VM to be exported individually. Individual files provide greater flexibility and reduce the need for repeated uploads in the event of file corruption or transfer failures.

The following items are recommended but not required.

- To reduce file transfer time and ensure file integrity, we advise the use of a compression or archival tool to compress the OVA/OVF, such as 7-Zip. We recommend 2-4 GB increments to aid in the upload process.
- Create a checksum hash of the files to be uploaded, and provide it in a text file zipped with the image(s). There are several tools available on Windows and Linux, but the most common is certutil for Windows and openssl for Linux (as shown below).
    - Windows: `certutil -hashfile .\filename sha1`
    - Linux: `openssl sha1 /path/to/filename`
