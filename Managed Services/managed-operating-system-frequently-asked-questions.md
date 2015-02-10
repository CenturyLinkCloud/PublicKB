{{{
  "title": "Managed Operating System - Frequently Asked Questions",
  "date": "12-2-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Here are a few frequently asked questions for our managed OS service:</p>
<p><strong>Q: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What is included in the Managed OS service? </strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; CenturyLink’s Managed OS service helps you spend less time on the IT tasks that don’t contribute immediately to your daily goals.&nbsp; To this end, here are the tasks performed on your behalf with our managed
  OS service:</p>
<ul>
  <li>Vendor Management – CenturyLink maintains ownership and management responsibility for your OS, freeing you from managing OS-level functions, SPLAs and license keys.</li>
  <li>Access Management – We take responsibility for user policies, administration and password management enforcement.</li>
  <li>Configuration Management – We confirm the initial install and basic functionality using an OS image built on vendor-recommended best-practices &amp; years of industry experience.</li>
  <li>Change Management – We provide access to OS-level change data performed by CenturyLink staff, along with robust ITIL-based internal changed control.</li>
  <li>Patch/Update Management – With support available for all critical and vendor-recommended patches, we ensure only OS vendor-recommended patches are installed.</li>
  <li>Security – We secure the OS with industry-standard anti-virus protection, regular virus and malware signature updates, and additional OS-level hardening to mitigate risk.</li>
</ul>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How do I create a Managed VM?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; From the Control Portal menu, select “Create Server.”&nbsp; You will then be prompted to select the data center, group membership, and other VM properties.&nbsp; Select a data center that supports managed services
  (an updated list is <a href="http://www.centurylinkcloud.com/managed-services" target="_blank">available here</a>), and then click the “managed server” element to “Yes.” The operating system drop-down menu will then automatically show available options.
  Choose your version, and then proceed with the remainder of the server creation process.</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What if I don’t see an option for Managed OS in the CenturyLink Cloud Control Panel?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; There could be a few causes:</p>
<ul>
  <li>Be sure you are creating the server in a data center that supports managed services.</li>
  <li>It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions.&nbsp; To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative
    toll free at:</li>
  <ul>
    <li>United States:&nbsp; 1-855-287-2541</li>
    <li>Canada:&nbsp; 1-877-387-3764</li>
    <li>Europe, Middle East &amp; Africa:&nbsp; +44 (0) 207 400 5600</li>
    <li>Japan:&nbsp; +81 3 5214 0180</li>
    <li>Hong Kong:&nbsp; +852 3079 4461</li>
    <li>Singapore:&nbsp; +65 6591 8824</li>
  </ul>
</ul>

<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is there anything that I cannot do in the Control Portal with a managed VM?</strong></p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A managed virtual machine cannot be cloned, archived, or converted to a template. Also, the "time to live" option is not available when creating a new managed server.</p>

<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How do I log into my server?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To access your managed VM, you will need your Local Account server name and password, unless you have created a Dedicated Active Directory Domain or are using a CenturyLink Shared Active Directory Domain.&nbsp;
  The Local Account user name is the full server name, and the password credential is available in your CenturyLink Cloud Control Portal using the “<em>click to authenticate</em>” link on the server overview page.&nbsp; <em>Please note that the user name and password for your Server is not the same user name and password for the Cloud Control Portal.</em>&nbsp;</p>
<p>Once you have obtained your password, you may access Windows environments using Remote Desktop and RHEL environments using SSH.&nbsp; For more detailed information about accessing your server for the first time, please see the articles for <a href="https://t3n.zendesk.com/entries/45603110-Managed-Windows-Server-Connecting-to-Your-Server-with-Remote-Desktop">Windows Server</a>  or <a href="https://t3n.zendesk.com/entries/45602910-Managed-Red-Hat-Connecting-to-Your-Server-with-SSH">RHEL</a>.<strong>&nbsp;</strong>
</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What should I do if I have trouble connecting via Remote Desktop?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; If you have difficulty connecting via RDP, be sure you are connecting from an IP that has TCP Port 3389 allowed on the <em>inbound</em> firewall.&nbsp; If you have a firewall at your location, you will need
  to have TCP port 3389 opened for <em>outbound</em> traffic.&nbsp; The firewall rule-set can be reviewed with your primary CenturyLink order contact or Consulting Engineer. <strong>Note that you should NEVER manage your remote servers through public IP address, and ONLY access servers through a secure tunnel like client VPN or site to site VPN!</strong>
</p>
<p>If you connect and find that the system disconnects you immediately, you should ensure you are using the latest Remote Desktop client and that your client machine is fully patched.&nbsp; For additional support, please contact the Client Service Center
  at 1-888-638-6771 and choose menu option 2.</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I have my VM patched?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; An important component of OS administration and management is keeping the system up-to-date. This includes keeping the system current with all patches to help prevent security compromises or operational reliability
  issues. CenturyLink will, from time to time, schedule the installation of system patches as deemed appropriate by our Solution Engineers.&nbsp; We will schedule the installation with you in advance. This will allow both parties to prepare for the patching,
  as well as provide ample time for discussion regarding the potential impact the patch may have on specific applications within your environment.</p>
<p>In addition, you can request patching for your VM by contacting the Client Service Center at 1-888-638-6771 and choosing menu option 2.</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I transfer files to my server using Remote Desktop?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Files can be transferred by simply drag and drop in Windows Explorer from your remote desktop session.</p>
<ul>
  <li>Configuring Remote Desktop for files transfer:</li>
  <li>Run Remote Desktop Connection (Start Menu/All Programs/Accessories).</li>
  <li>Enter the IP Address of the server.</li>
  <li>Click Options, then select Local Resources tab.</li>
  <li>Under Local devices and resources, click on More…</li>
  <li>Click on the “+”next to Drives, then select the local drive on your client which you would like to copy files from.</li>
  <li>Click Ok when done.&nbsp;</li>
  <li>Click Connect to initiate the connection.</li>
  <li>After connection is established, in your remote desktop session, open Windows Explorer (Start Menu/All Programs/Accessories)</li>
  <li>Local drive will show as Driver Letter on Hostname format, e.g. C on MyPC, process to copy files to or from your local drive</li>
</ul>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Who do I contact if I have trouble with my Managed VM?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year.&nbsp; Simply call us at 1-888-638-6771.</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I remove Managed Services from a VM?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Currently, the only way to remove Managed Services from a VM once it has been deployed is to delete the VM and to create a new server that is unmanaged.&nbsp;</p>
<p><strong>Q:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; How can I tell my <em>managed</em> VMs from my <em>unmanaged</em> VMs in the CenturyLink Cloud Control portal?</strong>
</p>
<p>A:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Managed VMs will be noted with an asterisk (*) in front of the server name.&nbsp; For example, <em>*ILMHPELCTA04</em>.&nbsp; This notation is intended to make it easier to locate managed VMs from within
  a list of all Cloud VMs you have created.</p>
<p>Q: &nbsp; &nbsp; &nbsp; &nbsp;<strong>My VM shows under construction&nbsp;in Control, but shows that the build has completed successfully?</strong>
</p>
<p>A: &nbsp; &nbsp; &nbsp; &nbsp;On Managed VMs, there are additional tasks that is being processed in the background in order to fully integrate into the Managed system, once this is complete Control will reflect it as active and manageable. &nbsp;</p>