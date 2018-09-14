{{{
  "title": "Using a Software-Defined Virtual NAS-SAN on CenturyLink Cloud",
  "date": "8-12-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Using a Software-Defined Virtual NAS/SAN on CenturyLink Cloud
Customers looking to operate CIFS, NFS or iSCSI services within the cloud platform can import software-defined virtual appliances via a [service task](//www.ctl.io/products/support/service-tasks). By using an **ecosystem** unified storage virtual appliance customers can deliver and implement various storage models.

* **NAS Services**-Provide CIFS or NFS services to virtual or bare metal servers across the CenturyLink Cloud.  
* **Bare Metal**-Deliver high performance storage via block iSCSI or NAS to augment local SATA storage or create shared iSCSI block storage LUNs for Oracle.
* **Object Storage**-Leverage our S3 Compatible Object Storage services to scale beyond the platform limits of virtual or bare metal servers.
* **Pool Storage**-Pool virtual disks and S3 Compatible Object Storage to create large block iSCSI or NAS volumes for virtual or bare metal servers.
* **High Availability**-Create highly available storage services in any combination of on-premise, CenturyLink Cloud or other leading Cloud vendors.  

In this Knowledge Base article we will be using our **ecosystem** [SoftNAS](//www.softnas.com) Virtual Appliance. [SoftNAS](//www.softnas.com) is a software-defined unified NAS/SAN storage solution for businesses that need powerful, frictionless and agile storage.

### Security Notes
In this sample deployment no security services were put in place around access to either iSCSI block or filesystem (CIFS, NFS) services. SoftNAS and the CenturyLink Cloud provide a wide range of authentication and security components customers can and should implement that are outside the scope of a basic functionality overview.

### Prerequisites

* A CenturyLink Cloud Account
* [Service Task for OVF Import](//www.ctl.io/products/support/service-tasks)
* [A licensed copy of SoftNAS](//www.softnas.com/wp/purchase)
* Refer to the [SoftNAS Getting Started Guide](../Ecosystem Partners/Marketplace Guides/getting-started-with-softnas-cloud-file-gateway-appliance.md) for details on how to procure and deploy the SoftNAS virtual appliance.

### Example A: Configuration of the SoftNAS Virtual Appliance using Virtual Disks

1. Once your SoftNAS virtual appliance is provisioned to the appropriate account via Service Task, login to Control, navigate to the Virtual Appliance, choose edit storage. **Provision the appropriate number of disks you wish to pool together into a larger storage pool.** In this sample we've chosen to add 4 x 1 TB Disks. NOTE: Understanding the [platform maximums](../Servers/cloud-server-instance-size-and-performance.md) by VM type is important. We recommend you import your Virtual Appliance as a **Standard VM** type if you wish to use up to the 4 TB Maximum.

    ![add disks](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-01.png)

2. Once the disks are added, login to the SoftNAS StorageCenter, select disk devices. The disks added via Control should be present. Quick Tip: use the refresh button if disks don't show up immediately.

    ![StorageCenter disk devices](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-02.png)

3. Select the Partition All button and confirm you wish to create partitions on all the devices.

    ![create partitions](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-03.png)

4. In the SoftNAS StorageCenter navigate to Storage Pools and select the create icon. Provide a friendly Pool name and choose an appropriate level of RAID you wish to use on this group of disks. In this example, we leveraged RAID0/striping, as all storage disks provisioned in CenturyLink Cloud already have data protection capabilities in the infrastructure. Select create.

    ![create new storage pool](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-04.png)

    ![storage pool created and online](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-05.png)

5. If you plan to deliver iSCSI volumes you need to establish an create an iSCSI Target on the SoftNAS. Navigate to iSCSI Lun Targets in the SoftNAS StorageCenter and create a new target. The Default option 'Don't Create new LUN' is adequate as these will be created later.

    ![create iscsi target](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-06.png)

6. In the SoftNAS StorageCenter navigate to Volumes and LUNs and select the create icon. The Create Volume dialog box allows you to choose the type of Volume/LUN you wish to deploy. Choices include CIFS, NFS and iSCSI.

    ##### NAS (CIFS or NFS)
    * Provide a volume name
    * Choose the storage pool previously provisioned
    * Select Filesystem (NFS, CIFS)
    * You can choose to export this volume as NFS, CIFS or Both
    * Choose the storage provisioning options: Thin or Thick
    * Choose the storage optimization options: Compression and/or Deduplication
    * Choose if you wish to leverage snapshots and their schedule

    ![create NFS Volume](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-07.png)

    ![set snapshot on NFS](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-08.png)

    ##### iSCSI Block Storage
    * Provide a volume name
    * Choose the storage pool previously provisioned
    * Select Block Device (iSCSI LUN) &amp; Share as iSCSI LUN
    * Choose the storage provisioning options: Thin or Thick
    * Choose the storage optimization options: Compression and/or Deduplication
    * Choose if you wish to leverage snapshots and their schedule
    * Select the iSCSI LUN Target created in Step #5

    ![create iscsi volume](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-09.png)

    ![set iscsi target](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-10.png)

7. Once completed the SoftNAS StorageCenter should show the volumes/LUNs you've created.

    ![volumes list in StorageCenter](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-11.png)

### Example B: Configuration of the SoftNAS Virtual Appliance using S3 Compatible Object Storage

1. Once your SoftNAS virtual appliance is provisioned to the appropriate account via Service Task, login to Control, navigate to the Virtual Appliance, choose edit storage. **Provision the appropriate size and number of virtual disks you wish to leverage for Block Cache File.** In this sample we've chosen to create a 500GB virtual disk for cache.

    ![add block cache file disk in control](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-19.png)

2. Once the disk(s) are added, login to the SoftNAS StorageCenter, select disk devices. The disks added via Control should be present. Quick Tip: use the refresh button if disks don't show up immediately.

3. Select the Partition All button and confirm you wish to create partitions on all the devices.

    ![create partitions on cache file disk](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-15.png)

4. In the SoftNAS StorageCenter navigate to Storage, disk devices.  Select **Add Device,** choose **CenturyLink Object Storage,** and then 'Next.'

    ![create new s3 disk](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-16.png)

5. In the **Add CenturyLink Cloud Disk Extender** screen input your Object Storage Access Key ID, Secret Access Key, Endpoint and bucket naming information.  Select the Block Cache File Device previously created and set its cache size as well as Encryption Password (for maximum security).  Finally, set your Disk Size.  Refer to the [SoftNAS documentation](//www.softnas.com/docs/softnas/v3/html-reference-guide/) for additional details and maximum sizes.

    ![add cloud disk extender](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-17.png)

6. A disk device should now be available to assign to a Storage Pool.

    ![disk available to assign to pool](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-18.png)

7.  Provision Storage Pool(s) and volumes as shown in **Example A beginning with step 4.**

### Connecting to NAS or Block Storage on Windows
The examples below are just examples of using a Windows 2012 R2 Virtual Instance to mount a CIFS and iSCSI Volume. Customers should follow standard NFS mount procedures for Linux Instances.
  * If you are leveraging a centralized Active Directory DNS we recommend you add an (A) record so the SoftNAS can be resolved via name or IP.
  * To map a CIFS share use the command line to execute (or Map Network Drive in the Desktop).

      ```
        net use * \\nasip or name\share name. In this example the command was net use * \\softnas\cifs_share.
      ```

    ![Windows UNC Share Mapped](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-12.png)

  * To mount an iSCSI block volume locate the iSCSI initiator (built into Windows 2012, download for 2008 R2) and input the IP address of the SoftNAS virtual appliance, select quickconnect. Select the volumes and devices tab and choose auto configure. Use the disk management tools in Windows to bring online, initialize and format the newly presented iSCSI LUN.

    ![iscsi initiator properties](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-13.png)

    ![iscsi initiator volumes and devices](../images/using-a-software-defined-virtual-nassan-on-centurylink-cloud-14.png)
