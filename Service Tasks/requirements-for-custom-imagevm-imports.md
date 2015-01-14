{{{
  "title": "Requirements for custom image/VM imports",
  "date": "10-13-2014",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Importing custom images/appliances for customers can be done in two ways.&nbsp; In both cases the files delivered to us from the customer should be in OVF (Open Virtualization Format) preferably in an OVA (Archive).</p>
<p><strong>Case 1:</strong>&nbsp; We can import the image/appliance as a one off import.&nbsp; The VM is manually configured to work with the customer environment and registered on the control site however any control site functions other then power on/off
  will most likely not work.&nbsp;This machine will not be able to be cloned, archived, or used as a template, and in most cases you will only be able to add a public IP to existing internal IPs without manual intervention. Drive expansions will most
  likely not complete successfully, at least not without manual intervention.</p>
<p><strong>Case 2</strong>:&nbsp; We can import the image and prep it to have full control site support.&nbsp; In most case with specialized appliances we will not be able to do this as they are too custom for us to support.</p>

<p><strong>In order to have full control site functionality the following conditions must be met:</strong>
</p>
<p>1. The machine must be one of our supported operating systems.</p>
<p>2. We must know the Administrator or root password on the machine.</p>
<p>3. We must be able to update the Administrator or root password on the machine.</p>
<p>4. We must be able to remotely administrator the machine</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; On windows machines RDP and remote powershell (version 2.0 or newer) must be enabled.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; On&nbsp;Linux machines we must be able to SSH(No public&nbsp;key authentication)&nbsp;and execute bash scripts remotely</p>
<p>5. We must be able to reconfigure multiple NICs (Static and DHCP IP addresses both must be supported)</p>
<p>6. Ping can not be blocked on the firewall.</p>
<p>7. Must be able to enable and configure SNMP if monitoring is to be functional.</p>
<p>8. Linux machines must use a bash shell.</p>
<p>9. We must be able to successfully run sysprep on windows machines.</p>
<p>10.&nbsp;Virtualized file systems (LVM, striped&nbsp;Windows volumes)&nbsp;on both Windows and Linux will not work with our automatic disk expansions (but we can still import)</p>
<p>11. Virtual machine disks should be exported as SCSI, not IDE. &nbsp;If they are IDE disk based automation will not work in control. &nbsp;See this vMware kb:&nbsp;http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1016192&nbsp;</p>
<p>12. We must be able to install VMware tools on the machine.</p>
<p>&nbsp;13.&nbsp;Windows machines cannot be domain joined (breaks clones)</p>
<p>Meeting these requirements is not always a guarantee that we will be able to have full control site support (or even import the machine at all), however missing any of them is a guarantee that we will not be able to give the image full functionality.</p>


