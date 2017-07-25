{{{
  "title": "Requirements for custom image/VM imports",
  "date": "10-13-2014",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": false
}}}

Importing custom images/appliances for customers can be done in two ways. In both cases the files delivered to us from the customer should be in OVF (Open Virtualization Format) preferably in an OVA (Archive).

**Case 1** We can import the image/appliance as a one off import. The VM is manually configured to work with the customer environment and registered on the control site however any control site functions other then power on/off will most likely not work. This machine will not be able to be cloned, archived, or used as a template, and in most cases you will only be able to add a public IP to existing internal IPs without manual intervention. Drive expansions will most likely not complete successfully, at least not without manual intervention.

**Case 2** We can import the image and prep it to have full control site support. In most case with specialized appliances we will not be able to do this as they are too custom for us to support.

**In order to have full control site functionality the following conditions must be met:**

1. The machine must be one of our supported operating systems.
1. We must know the Administrator or root password on the machine.
1. We must be able to update the Administrator or root password on the machine.
1. We must be able to remotely administrator the machine
  On windows machines RDP and remote powershell (version 2.0 or newer) must be enabled.
  On Linux machines we must be able to SSH(No public key authentication) and execute bash scripts remotely
1. We must be able to reconfigure multiple NICs (Static and DHCP IP addresses both must be supported)
1. Ping can not be blocked on the firewall.
1. Must be able to enable and configure SNMP if monitoring is to be functional.
1. Linux machines must use a bash shell.
1. We must be able to successfully run sysprep on windows machines.
1.  Virtualized file systems (LVM, striped Windows volumes) on both Windows and Linux will not work with our automatic disk expansions (but we can still import)
1.  Virtual machine disks should be exported as SCSI, not IDE.  If they are IDE disk based automation will not work in control.  See this vMware kb: http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1016192 
1.  We must be able to install VMware tools on the machine.
1. Windows machines cannot be domain joined (breaks clones)
  Meeting these requirements is not always a guarantee that we will be able to have full control site support (or even import the machine at all), however missing any of them is a guarantee that we will not be able to give the image full functionality.
1.  Only one SCSI controller is allowed to be configured. 


