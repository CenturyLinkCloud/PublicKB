{{{
"title": "New DCC UI Release Notes: MVP Release",
"date": "05-03-2017",
"author": "Anthony Hakim",
"attachments": [],
"contentIsHTML": false
}}}

### Announcements

Dedicated Cloud Compute (DCC) is now fully live in Production! This release provides most functionality currently available from Savvis Station Portal > Marketplace:

Dashboard

* Overview: Global dedicated resource summary with ability to access datacenter specific Infrastructure information
* Compute: Global dedicated compute dashboard similar to Marketplace > Symphony Orchestrator > Compute Dashboard
* Storage: Global dedicated storage dashboard similar to Marketplace > Symphony Orchestrator > Storage Dashboard

Create

* Add Server: Configure and price virtual servers similar to Marketplace > Add > Symphony Dedicated
* Add Storage: Configure and price storage similar to Marketplace > Add > Storage

Infrastructure (A searchable navigation with ability to access datacenter, cluster, server or saved images specific information)

* Overview:
  * Datacenter: Datacenter specific dedicated resource summary with ability to access cluster specific information
  * Cluster: Cluster specific dedicated resource summary with ability to access host specific information
  * Server: Virtual Intelligent Hosting Instance resource management tools and summary similar to Marketplace > Symphony Orchestrator > Compute Dashboard > Details
* Compute: Datacenter or cluster specific dedicated compute dashboard
* Storage: Datacenter or cluster specific dedicated storage dashboard
* Hosts: Virtual Intelligent Hosting Node summary similar to Marketplace > Symphony Orchestrator > Compute Dashboard > Details
* Utilization: Host or server specific utilization information similar to Marketplace > Symphony Orchestrator > Compute Dashboard > Details > Service Utilization
* Saved Images: Datacenter specific image management tool similar to Marketplace > Symphony Orchestrator > Image Management

Orders

* Saved Orders: Manage your open and locked orders similar to Marketplace > Shopping Cart > My Cart and Marketplace > Shopping Cart > Locked Carts
* Order Provisioning: View your queued provisioning requests for dedicated resources similar to Marketplace > Shopping Cart > Submitted Orders
* Server Operations: View your queued operations requests for actions such as Stop/Start/Restart etc.


### New Features

Create > Add Storage
* Storage products for both Utility and Unified storage types may now be ordered and deployed (equivalent to Marketplace > Add > Storage)

### Enhancements

Create
* When adding a product to an order the resource reservation processing will now occur asynchronously allowing you to continue to other tasks instead of waiting. The Order Details page will show progress and any errors

Saved Orders
* If you are the creator of a locked order you may now delete products from the order without first unlocking it

Notify Purchaser
* When an order is automatically locked (to prevent an order containing mixed product types that have been determined to be incompatible) a notify purchaser email is NOT sent. You may use the Notify action on a locked order to send or resend a notify purchaser email

### Known Issues

Server > Utilization
* Metrics related to disk size/space/utilization may show incorrect data
* Data collection within the last 24 hours is unreliable and may cause missing or partial data to be displayed

Add Disk
* During the time the Add Disk order is processing it is possible for the Server > Overview page to show a "There are no disks under this server" message

Delete Server
* Access to the Server > Overview page after making a Delete Server request for the server is not fully prevented and can result in an error
* The server list pane shown on the left side of the Infrastructure pages will continue to list a server after it has been deleted

Create > Add Server
* Only Clusters that already contain a server will be listed. Use SSP to create the first server if necessary
* Selections for Datacenter, Cluster and Billing Account Number will all be read only when adding a server to an Unlocked order. An order currently only supports products in a single Cluster
* A cluster with ESX v4.1 Hosts will not support all the Operating Systems listed (avoid all versions of Windows Standard Edition 2012 and RedHat Linux Advanced Server 7 if listed)

Saved Orders
* Products from multiple Clusters or Billing Account Numbers is not yet supported

### Limitations

Saved Images
* The ability to create and deploy a Saved Image are not included in this release

Server Operations
* If a Server Operation request (e.g. stop/start/restart/edit/add disk etc.) is made at a time that coincides with a CenturyLink scheduled management task then the request may be delayed and/or the result of the request may not be shown correctly until the scheduled management task completes. This may take up to 30 minutes

Clone Server
* The server being cloned will not accept any configuration change (e.g. edit/add disk/delete disk) until the Clone request completes, is deleted or the request expires (after 8 days)

Add Disk
* Only a single disk can be added per request

Delete Disk
* Only a single disk can be deleted per request

General
* Editing a Server configuration under an ESX v4.1 Host is not yet supported
* A Virtual Machine that is Created or Deleted in Savvis Station Portal may take up to 8 hours to synchronize with DCC

### Bug Fixes and General Updates

Resolved - Clone Server
* Attempting to delete a Clone Server order will fail if the lock that prevents configuration changes to the server being cloned has expired (after 8 days)
