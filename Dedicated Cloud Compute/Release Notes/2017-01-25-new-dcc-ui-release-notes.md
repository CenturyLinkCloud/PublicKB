{{{
"title": "New DCC UI Release Notes: Beta 3",
"date": "01-25-2017",
"author": "Scott Campbell",
"attachments": [],
"contentIsHTML": false
}}}

### Announcements

* This beta release has primarily focused on security, validation and resiliency activity to improve the overall user experience.

### New Features

* Added ability to Delete Server.

### Enhancements

* Server > Utilization. Server Utilization metrics (where available) can be accessed via the Server pages.
* Added default Order Name for Add Server and Add Storage.
* Added total cost display for multiple products in an order.
* Create Server. Expanded the supported DCC Operating System catalog to include Windows Server 2008 R2 SP1 Enterprise 64-Bit.

### Known Issues

* Delete Server
    * Access to the Server > Overview page after making a Delete Server request for the server is not fully prevented and can result in an error.
    * Making a duplicate Delete Server request will result in an error (resolved beta 4).
    * The server list pane shown on the left side of the Infrastructure pages will continue to list a server after it has been deleted.
* Server > Utilization. Data collection within the last 24 hours is unreliable and may cause missing or partial data to be displayed on the Server Overview page.

### Bug Fixes and General Updates

* Resolved: Utilization graphs may show unexpected results if there are missing data points.
* Resolved: Create Server. Only Clusters that use Utility Storage will be listed. Unified Storage is not yet supported.
* Resolved: Saved Orders. Deleting a product in a saved order is not yet supported.
* Resolved: Saved Orders. Deleting a saved order is not yet supported.
* Resolved: Edit Server. Increasing a Server vRAM configuration to a value higher than the available storage in the data store may result in it being unable to start.
