{{{
"title": "New DCC UI Release Notes: Beta 1 Update",
"date": "11-09-2016",
"author": "Scott Campbell",
"attachments": [],
"contentIsHTML": false
}}}

## New Features

* Added ability to edit the Server configuration for vCPU/vRAM (equivalent to Change Tier in Marketplace > Symphony Orchestrator > Compute Dashboard), see limitations below.

### Known Issues

* Increasing a Server vRAM configuration to a value higher than the available storage in the data store may result in it being unable to start (resolved beta 3).

### Limitations

* Attempting to decrease a Server vRAM configuration to a value lower than the minimum required for the Operating System is not prevented (resolved beta 4).
* Editing a Server configuration under an ESX v4.1 Host is not yet supported.
