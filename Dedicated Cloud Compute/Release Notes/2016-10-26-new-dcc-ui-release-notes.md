{{{
"title": "New DCC UI Release Notes: Beta 1",
"date": "10-26-2016",
"author": "Scott Campbell",
"attachments": [],
"contentIsHTML": false
}}}

### Announcements

* Dedicated Cloud Compute (DCC) is now live in Production! This public Beta release allows view only access to a number of areas currently available from Savvis Station Portal > Marketplace, details below.
* Additional functionality will be implemented over the coming months with the intention of eventually replacing the DCC functionality found in Marketplace.

### New Features

* New user interface consistent with Lumen Cloud Compute (CLC) with the ability to view your dedicated resources from the perspective of a global dashboard, an individual datacenter or a specific cluster.
* Compute tab providing view only information similar to the Marketplace > Symphony Orchestrator > Compute Dashboard.
* Storage tab providing view only information similar to the Marketplace > Symphony Orchestrator > Storage Dashboard.
* Saved Images under each datacenter providing view only information similar to the Marketplace > Symphony Orchestrator > Image Management.
* Hosts tab under each cluster providing view only information similar to the Marketplace > Symphony Orchestrator > Compute Dashboard > Details for each Virtual Hosting Instance.
* Overview tab for each Virtual Machine Instance providing view only information similar to the Marketplace > Symphony Orchestrator > Compute Dashboard > Details.

### Enhancements

* Server Operations for Start/Stop/Restart.
* Orders > Server Operations. Allows access to manage Server Operations requests.
* Cluster > Hosts > Utilization. Host Utilization metrics (where available) can be accessed via the Cluster pages.

### Limitations

* No write access. This means that it is currently not possible to: Create Server, Add Storage or edit any configuration
Create > Add Storage. Only clusters with Utility Storage will provide a price estimate.

### Known Issues

* A Virtual Machine that is Created or Deleted in Savvis Station Portal may take up to 8 hours to synchronize with DCC
Multiple duplicate Server Operations for Start/Stop/Restart can be requested and queued during the period between the first request being created and it completing (resolved beta 4).
