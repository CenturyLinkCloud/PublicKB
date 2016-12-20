{{{
  "title": "Operating System Template Retirement Policy",
  "date": "1-19-2015",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": false
}}}

As we add new operating system templates to the Platform, we also remove older templates from the Platform.

To this end, CenturyLink Cloud has established an OS retirement policy.  Details listed below.

* Given equal price, the premium version of an OS will be supported over other alternatives.
* Given equal price, the 64-bit version of an OS will be supported over other alternatives.
* The two most recent major versions of a supported OS will be available.  Other operating systems may have more versions supported, at CenturyLink's discretion.
* A 120-day sunset window will be provided for each retiring template as new OS versions come online.  A notification in this knowledge base repository initiates this window.
* Customers with virtual machines based on retired templates will see functionality change during this 120-day window.
* After 60 days from the initial notification, the template will be removed from the "Create Server" function in the Control Portal and the API.  In addition, the NOC team will no longer perform OS-level troubleshooting or maintenance for VMs using these templates.
* After 120 days from the initial notification, the VMs based on these templates will no longer have the capability for "Clone", "Convert to Template" or "Add Public IP."  Power operations, snapshot, and archive will still be available.  In addition, the development team will no longer perform OS-level troubleshooting or maintenance for VMs using these templates.
* This policy only applies to unmanaged OS images.

### LIST OF NOTICES FOR RETIRED OPERATING SYSTEMS

Feb 3, 2015 - [see article](../Servers/operating-system-retirement-notice-feb-3-2015.md)
