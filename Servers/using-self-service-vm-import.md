{{{
  "title": "Using Self-Service VM Import",
  "date": "11-25-2019",
  "author": "Matthew Ordman",
  "attachments": [],
  "contentIsHTML": false
}}}

**Note**: this feature only supports OVFs exported from VMware environments, and [supported operating systems](../../support/supported-operating-systems.md). Virtual appliances and OVFs from other hypervisors should be imported as a [service task](https://www.ctl.io/centurylink-public-cloud/service-tasks/).

1. Ensure your OVF meets the requirements for import that are listed here in our [Best Practices and preparation for a virtual machine OVF import KB](../../Service Tasks/best-practices-and-preparation-for-a-virtual-machineovfova-import.md).

2. Connect to your CenturyLink Cloud FTP server; [instructions detailed here](../Control Portal/ftp-users-in-control-portal.md).
  * **Note**: You can import VMs to any available data center in your account; the OVF file is simply stored in your home data center FTP account for initial processing.

3. In the root directory of your FTP account, create a folder named “import,” if it does not already exist.

4. Within the “import” folder, create another folder with a name that matches the name of your OVF.  Upload the OVF to this location (i.e. “import/sampleovfname”), using your preferred FTP client. Be sure to use only alphanumeric characters in your filename, special characters may result in errors.
  * **Note**: Your VMDK, VMX's, etc must be uploaded to the same location as well. If you export a VM from VMWare, all you need to do is upload the entire folder using the correct folder structure.
  * **Note: the VM name cannot include a "." - this will cause import failure.

5. Transfer the OVF from your local machine to the subfolder you just created in your FTP account.
  * The transfer of the OVF may take several hours, depending on the size of the file and the speed of your connection.
  * Any packet loss during the transfer may result in import failure.

6. When the upload is complete, click Import Server under Infrastructure in the CenturyLink Cloud navigation menu.
  ![menu](../images/portal/portal-import-server.png)

7. You will then see your collection of uploaded OVFs.
  ![import server](https://t3n.zendesk.com/attachments/token/uvYOmyt2Jd2E3ASHrSvrtwUpG/?name=VM_Import.png)
  * **Note**: OVFs will be automatically deleted from your FTP server after 5 days.  As such, please complete imports shortly after initial upload.

8. Select the desired OVF to import, and proceed to complete the rest of the Import form, including specifying the data center and group location of the VM. Your OVF must map to one of the operating systems shown below.
![import location](https://t3n.zendesk.com/attachments/token/HfKE7C1T1I2uTYwjLYeNO3GWJ/?name=Screen+Shot+2015-02-04+at+7.43.53+AM.png)

9. Click "Import Server" to initiate the import process.

10. Upon successful import, your VM will appear in your chosen data center and group location within a few hours.
  * **Note**: Exact timing for the availability of your new VM in the Control Portal depends on several factors, so there is not standard availability time for imported VMs.
  * **Note**:If your OVA import fails with any of the following errros: "Invalid Ovf manifest entry", "The OVF package is invalid and cannot be deployed" or "The following manifest file entry (line 1) is invalid: SHA256 (xxxxxxx.ovf)" please see the following article for resolution: https://kb.vmware.com/s/article/2151537.
