{{{
  "title": "Self-Service VM Import and OVF Requirements",
  "date": "10-1-2015",
  "author": "Eric Schubert",
  "attachments": [],
  "contentIsHTML": false
}}}

With a new self-service VM import capability, users can now import OVFs from VMware environments into CenturyLink Cloud. However, some OVFs may still require significant prep work depending on the state of the image. Requirements for OVF images are listed below. Please keep this in mind when prepping an image for import.

### Supported Operating Systems for Self-Service Import
- Red Hat Enterprise Linux 6 | 64-Bit
- Windows 2008 R2 DataCenter Edition | 64-Bit
- Windows 2012 R2 DataCenter Edition | 64-Bit

### All OVF Requirements
Your OVF must meet the following requirements to be imported successfully.
- File must be an OVF; OVAs are not supported.
- Manifest must use the SHA1 hashing algorithm.
- The VM must pass a checksum test to ensure there was no packet loss during the FTP transfer.
- Must be less than 1 TB in total size.
- Must not include a customized or specialized appliances.
- All disks should be SCSI (not IDE).
- Only one SCSI controller is allowed.
- Must have a single NIC.
- DHCP must be disabled.
- Only a single image should be present. Multiple images (for example a vApp) are not supported. Refer to the [Open Virtualization Format White Paper](http://www.dmtf.org/sites/default/files/standards/documents/DSP2017_2.0.0.pdf) for more information.
- The OVF file name must not include a "`.`" or a "`-`".
- Ping should not be blocked on the firewall.
- The VMware hardware version (VMX) must be 8 or lower.
- The latest version of VMware Tools must be installed. You will get the error message that reads "the guest operations agent is out of date" if your version is not correct.
- The OVF must be exported from VMware. Other hypervisors are not supported.
- The current Administrator or Root password must be input during the import process.
- Avoid usage of disk type "`monolithicSparse`" for VMDK disks.
- Must have a valid DNS address.

#### Specific Requirements for Windows 2008/2012 R2 DataCenter 64-Bit OVFs
- The machine cannot be joined to a domain. **NOTE:** Customers can join their virtual machine to a domain after the import process.
- RDP needs to be available on the image.
- RDP needs to be unblocked by Windows firewall.

#### Specific Requirements for Red Hat 6 64-Bit OVFs
- Ensure SSH is enabled and not firewalled.
- Prior to uploading the OVF for import, delete the file **70-persistent-net.rules**.
  - `rm /etc/udev/rules.d/70-persistent-net.rules`
- Create a blank file named **75-persistent-net-generator.rules** to prevent the build of the persistent net rules file.
  - `touch /etc/udev/rules.d/75-persistent-net-generator.rules`
  
#### Specific Requirements for Red Hat 7 64-Bit OVFs
- Ensure Consistent Network Device Naming is enabled.

#### Specific Requirements for CentOS OVFs
- Ensure the network interface configuration follows the RHEL convention of "ens160", "ens162" etc, for compatibility with our platform automation controls (cloning, network changes, etc).

### Other Notes
- In addition, the import function will enable the following capabilities if they are not available on your OVF image:
  - For Windows: PSEXEC must not be firewalled. PS Remoting is enabled. WinRM is enabled.
  - For Red Hat: Ensure the root account’s shell is Bash.
- We assume that Windows OVFs are properly licensed under Volume Licensing. Upon successful import, the OVF is then licensed using CenturyLink's SPLA agreement with Microsoft. 
- Bring your own licensing for Windows or Red Hat is not supported.
- All OVF files will be stored in the FTP server located in your account's home data center.
- All OVF files will be deleted 5 days after initial import. Please import your images soon after completion of the FTP transfer.
- Managed Services are not available on imported VMs.
- Import failures can be caused by conflicting settings on the OVF. To assist with troubleshooting a failured OVF, try to import the OVF back into the original virtualized environment and gather logs from this activity.
