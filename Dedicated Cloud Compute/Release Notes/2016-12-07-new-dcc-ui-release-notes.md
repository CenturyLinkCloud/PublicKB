{{{
"title": "New DCC UI Release Notes: Beta 2",
"date": "12-07-2016",
"author": "Scott Campbell",
"attachments": [],
"contentIsHTML": false
}}}

### New Features

* Added ability to Create Server (equivalent to Marketplace > Add > Symphony Dedicated), see limitations below.
* Added ability to view and manage Saved Orders, see limitations below.
* Added ability to view and manage Provisioning Orders.

### Enhancements

* Additional advanced options are now available from Cluster > Hosts > Utilization.

### Known Issues

* Utilization graphs may show unexpected results if there are missing data points (resolved beta 3).

### Limitations

* Create Server
    * Only Clusters that use Utility Storage will be listed. Unified Storage is not yet supported (resolved beta 3).
    * Only Clusters that already contain a server will be listed. Use SSP to create the first server if necessary.
    * Selections for Datacenter, Cluster and Billing Account Number will all be read only when adding a server to an Unlocked order. An order currently only supports products in a single Cluster.
    * Only a subset of the full DCC Operating System catalog is currently supported (Windows Standard Edition 2012 R2 64-Bit and RedHat Linux Advanced Server 6 64-Bit).
    * A cluster with ESX v4.1 Hosts will not support all the Operating Systems listed (avoid all versions of Windows Standard Edition 2012 and RedHat Linux Advanced Server 7 if listed).
    * Only a single instance is currently supported (resolved beta 4).

* Saved Orders
    * A saved order can contain a maximum of 35 products. Attempting to add additional products will cause the order to be Locked and a new Unlocked order to be created.
    * Editing or deleting a product in a saved order is not yet supported (resolved beta 3).
    * Deleting a saved order is not yet supported (resolved beta 3).
    * Products from multiple Clusters or Billing Account Numbers is not yet supported.
