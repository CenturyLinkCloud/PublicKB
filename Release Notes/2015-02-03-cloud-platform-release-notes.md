{{{
  "title": "Cloud Platform - Release Notes: February 3, 2015",
  "date": "2-3-2015",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<div>
  <hr>
</div>
<ul>
<li><strong><strong>Self-service Virtual Machine import.</strong></strong>&nbsp;Customers can now import their existing Windows Server 2008R2, Windows Server 2012 / R2, and Red Hat Enterprise Linux 6 virtual servers into the CenturyLink Cloud. Servers can be uploaded into any cloud data center if they <a href="https://t3n.zendesk.com/entries/60156724-Self-Service-VM-Import-OVF-Requirements">meet a series of prerequisites</a>. The customer can choose the account, group, server type (standard or Hyperscale), storage level, and VLAN for the server.&nbsp;<strong><br /></strong>
<p><img src="https://t3n.zendesk.com/attachments/token/VbmsTcFXJJXEUBoMw4kgouG7H/?name=release02_03_15_06.png" alt="release02_03_15_06.png" /><br /><br >For a more detailed walkthrough of the import process, <a href="https://t3n.zendesk.com/entries/61959224-Using-Self-Service-VM-Import">please review this KB article</a>.</p>
</li>
<li><strong>Managed Backup service.&nbsp;</strong>The CenturyLink Data Protect Backup solution is now included in the CenturyLink Cloud <strong>[Available to customers by Feb 13]&nbsp;</strong>. Customers can include the managed backup capabilities on new managed servers, or existing ones. Backup data is stored for two weeks both in the same data center as the virtual machine, and in a remote data center. For new servers, the option is available after selecting the "managed server" option:<br /><img src="https://t3n.zendesk.com/attachments/token/KWAbKUNLv7bDSkw3nz6ZaNyWe/?name=release02_03_15_05.gif" alt="release02_03_15_05.gif" /><br /><br /><br />For existing managed servers, the Managed Backup service can be enabled and disabled via the Server Details view.<br /><br /><img src="https://t3n.zendesk.com/attachments/token/N9lXMwqEyFN1jApitaTiyo6cq/?name=release02_03_15_04.gif" alt="release02_03_15_04.gif" /><br /><br />To learn more about Managed Backup, <a href="https://t3n.zendesk.com/entries/62310380-Managed-Backup-Frequently-Asked-Questions">check out new new FAQ</a>!</li>
</ul>
<p></p>
<p><strong>Minor Enhancements (6)</strong></p>
<div><hr .></div>
<ul>
<li><strong>Autoscale for Red Hat Enterprise Linux 7.&nbsp;</strong>RHEL servers now support vertical CPU autoscale policies for simple, automated scale up and scale down based on utilization.</li>
<li><strong>Cost of managed servers included in running Group.Server estimates.</strong>&nbsp;Taking advantage of managed operating systems or managed applications? Associated hourly charges are now included in both the Group overview estimates, and per-server estimates.</li>
<li><strong>Site to site VPN to single data center endpoint. </strong>Site to site VPN configurations now prevent more than one configuration to the same VPN endpoint in a data center. Please contact the NOC if you'd like to set up a new VPN tunnel to an existing endpoint.</li>
<li><strong>Private Cloud isolation in Control Portal. </strong>CenturyLink Private Cloud was launched in 2014 and customers are now going live. The Control Portal (and API) will only show a private cloud data center to the relevant customer.</li>
<li><strong>CenturyLink administrator account removed from all virtual machines</strong>. In the past CenturyLink Cloud has used a local administrator account to perform activities on servers at the request of our customers. Moving forward, we've removed this&nbsp;account from all cloud servers. What this means for customers, is (a) all access to a cloud servers is done through customer-created accounts, and (b) if you forget your password (and do not have the server password synchronized with the Control Portal), the cloud team can no longer log in and reset it for you. Store those passwords carefully!</li>
<li><strong>Default NIC changed on Windows 2008.2012 templates.&nbsp;</strong>In order to offer 10g connections on all Windows Servers, we've updated the default NIC on all Windows Server 2008 and Windows Server 2012 operating system templates to use the VMware VMXnet3 network adapter.</li>
</ul>
<p></p>
<p><strong>Notifications (3)</strong></p>
<div><hr /></div>
<ul>
<li><strong>OS template retirement. </strong>CenturyLink Cloud has established an operating system template retirement rhythm in order to offer the most supported, feature-rich servers for you in the cloud. Please <a href="https://t3n.zendesk.com/entries/61762904-Operating-System-Retirement-Notice-Feb-3-2015">read the following notice for details</a>, but the first templates are <strong>scheduled for retirement in 120 days</strong>: Windows Server 2003, CentOS 5 &amp; 6 <strong>32 bit,&nbsp;</strong>Ubuntu 10, and Windows Server 2008&nbsp;<strong>32-bit</strong>. What does "retirement" mean? <a href="https://t3n.zendesk.com/entries/62177360-Operating-System-Template-Retirement-Policy">Check out this KB article for more details</a>.</li>
<li><strong>API v1 changes to Group ID value. </strong>The "GroupID" value used by the v1 API (see <a href="https://t3n.zendesk.com/entries/20979826-Get-Groups">GetGroups</a>, for example) is changing. A new field, called GroupUUID, is being added to the API payload (in THIS release), and it represents a globally unique identify for a group. <strong>For 90 days</strong>, existing groups will get back both the original Group ID and the new UUID. After 90 days, new groups will *only* have a UUID assigned and API requests that accept a Group ID will only accept the UUID value.</li>
<li><strong>API v2 changes to Group ID value<span class="copyonly"></span></strong><span>. The group ID value is changing from an integer to a long string. In the next software release, the legacy group ID is no longer available in the v2 endpoints, and the group id field returns the new value only.</span></li>
</ul>
