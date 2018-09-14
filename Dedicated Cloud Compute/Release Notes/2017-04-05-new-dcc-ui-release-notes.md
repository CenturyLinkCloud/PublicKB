{{{
"title": "New DCC UI Release Notes: BETA 5",
"date": "04-05-2017",
"author": "Anthony Hakim",
"attachments": [],
"contentIsHTML": false
}}}

### New Features

Server > Overview

* Added ability to Clone Server, see limitations below

### Enhancements

Create Server

* Network IP Address Assignment can now be switched between Automatic and Manual modes on a per interface basis. Manual mode allows the IP Address for any/all instances to be specified (any blank values are treated as Automatic mode).
* Expanded the supported DCC Operating System catalog to include Windows Server 2012 R2 Standard 64 bit Managed Operating System 4 CPU, Windows Server 2008 R2 SP1 Enterprise 64 bit Managed Operating System 4 CPU and Windows Server 2003 R2 Enterprise 64 bit Managed Operating System 4 CPU

Saved Orders

* During the order creation process an existing unlocked order may be automatically locked and a new order created. This is to prevent an order containing mixed product types that have been determined to be incompatible. An alert appears on the Create page when this happens.

User interface color scheme updated

* To be consistent with CenturyLink Cloud Application Manager (CAM)
* To include colored Operation System icons
* To include utilization gauges that change color based on their value

### Known Issues

Server Operations

* If a Server Operation request (e.g. stop/start/restart/edit/add disk etc.) is made at a time that coincides with a CenturyLink scheduled management task then the request may be delayed and/or the result of the request may not be shown correctly until the scheduled management task completes. This may take up to 30 minutes

Clone Server

* Attempting to delete a Clone Server order will fail if the lock that prevents configuration changes to the server being cloned has expired (after 8 days)

Server > Utilization

* Metrics related to disk size/space/utilization may show incorrect data

### Limitations

Clone Server

* The server being cloned will not accept any configuration change (e.g. edit/add disk/delete disk) until the Clone request completes, is deleted or the request expires (after 8 days)

### Bug Fixes and General Updates

Resolved: Create Server

* The boot disk capacity for some Operating Systems is incorrect and prevents deployment

Resolved: Delete Disk

* If more than 25 Datastore rows are expanded in the Infrastructure > Storage tab then the Delete Disk function will only work on the most recently expanded 25 Datastore rows
