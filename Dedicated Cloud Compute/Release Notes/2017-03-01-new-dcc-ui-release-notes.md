{{{
"title": "New DCC UI Release Notes: Beta 4",
"date": "03-01-2017",
"author": "Scott Campbell",
"attachments": [],
"contentIsHTML": false
}}}

### New Features

* Server > Overview. Added ability to Add Disk to a Server, see limitations below.
* Infrastructure > Storage. Added ability to Delete Disk from a Datastore, see limitations below.

### Enhancements

* Create Server
    * Expanded the supported DCC Operating System catalog to include Red Hat Enterprise Linux AS v7 64 bit Managed Operating System and Red Hat Enterprise Linux AS v5 64 bit Managed Operating System.
    * Number of instances can now be configured up to 5.
* Updated confirmation behaviors and messaging.

### Known Issues

* Delete Disk. If more than 25 Datastore rows are expanded in the Infrastructure > Storage tab then the Delete Disk function will only work on the most recently expanded 25 Datastore rows.
* Add Disk. During the time the Add Disk order is processing it is possible for the Server > Overview page to show a "There are no disks under this server" message.

### Limitations

* Add Disk. Only a single disk can be added per request.
* Delete Disk. Only a single disk can be deleted per request.

### Bug Fixes and General Updates

* Resolved: Delete Server. Making a duplicate Delete Server request will result in an error.
* Resolved: Edit Server. Attempting to decrease a Server vRAM configuration to a value lower than the minimum required for the Operating System is not prevented.
* Resolved: Server > Overview. Multiple duplicate Server Operations for Start/Stop/Restart can be requested and queued during the period between the first request being created and it completing.
