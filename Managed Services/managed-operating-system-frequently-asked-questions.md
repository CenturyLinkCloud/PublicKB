{{{
  "title": "Managed Operating System - Frequently Asked Questions",
  "date": "4-22-2015",
  "author": "Jacob Kenner",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Here are a few frequently asked questions for our managed OS service:</p>
<p><strong>Q: What is included in the Managed OS service? </strong>
</p>
<p>A: CenturyLink’s Managed OS service helps you spend less time on the IT tasks that don’t contribute immediately to your daily goals. To this end, here are the tasks performed on your behalf with our managed
  OS service:</p>
<ul>
  <li>Vendor Management – CenturyLink maintains ownership and management responsibility for your OS, freeing you from managing OS-level functions, SPLAs and license keys.</li>
  <li>Access Management – We take responsibility for user policies, administration and password management enforcement.</li>
  <li>Configuration Management – We confirm the initial install and basic functionality using an OS image built on vendor-recommended best-practices &amp; years of industry experience.</li>
  <li>Change Management – We provide access to OS-level change data performed by CenturyLink staff, along with robust ITIL-based internal changed control.</li>
  <li>Patch/Update Management – With support available for all critical and vendor-recommended patches, we ensure only OS vendor-recommended patches are installed.</li>
  <li>Security – We secure the OS with industry-standard anti-virus protection, regular virus and malware signature updates, and additional OS-level hardening to mitigate risk.</li>
</ul>
<p><strong>Q: How do I create a Managed VM?</strong>
</p>
<p> From the Control Portal menu, select “Create Server.”  Then, select the data center, group membership, and other VM properties.  Select a data center that supports managed services, and then click the “managed server” element to “Yes.” The operating system drop-down menu will automatically show available options. Choose your version, and then proceed with the remainder of the server creation process.</p>
<p>
After creating a managed VM, the VM will be 'Under Construction' while background processes are completed. You will not have access to the server during that time; you will receive a notification via email once the operation has completed. Please allow up to a 30 minutes. If there are any issues beyond that time, contact us via email <a href="mailto:request@centurylink.com">request@centurylink.com</a> or by phone at the following numbers. In the US: 888.638.6771; UK: +44.118.322.6100; Singapore: +65.6305.8099. Please do not email the CenturyLink Cloud NOC or raise the issue via chat - faster responses to inquiries will come from the email address and support numbers above.</p>
<p><strong>Q: What if I don’t see an option for Managed OS in the CenturyLink Cloud Control Panel?</strong>
</p>
<p>A: There could be a few causes:</p>
<ul>
  <li>Be sure you are creating the server in a data center that supports managed services.</li>
  <li>It is possible your company has not yet executed a Master Services Agreement (MSA) with CenturyLink Technology Solutions. To obtain a MSA – or if you believe you should already have one in place – please contact a CenturyLink Sales Representative
    toll free at:</li>
  <ul>
    <li>United States: 1-855-287-2541</li>
    <li>Canada: 1-877-387-3764</li>
    <li>Europe, Middle East &amp; Africa: +44 (0) 207 400 5600</li>
    <li>Japan: +81 3 5214 0180</li>
    <li>Hong Kong: +852 3079 4461</li>
    <li>Singapore: +65 6591 8824</li>
  </ul>
</ul>

<p><strong>Q: Is there anything that I cannot do in the Control Portal with a managed VM?</strong></p>
<p>A: A managed virtual machine cannot be cloned, archived, or converted to a template. Also, the "time to live" option is not available when creating a new managed server. At this time, you cannot create a managed server within a Cloud Blueprint.</p>

<p><strong>Q: How do I log into my server?</strong>
</p>
<p>A: To access your managed VM, you will need your Local Account server name and password, unless you have created a Managed Active Directory Domain or are using a CenturyLink Shared Active Directory Domain.
  The Local Account user name is the full server name, and the password credential is available in your CenturyLink Cloud Control Portal using the “<em>click to authenticate</em>” link on the server overview page. <em>Please note that the user name and password for your Server is not the same user name and password for the Cloud Control Portal.</em></p>
<p>Once you have obtained your password, you may access Windows environments using Remote Desktop and RHEL environments using SSH. For more detailed information about accessing your server for the first time, please see the articles for <a href="https://www.centurylinkcloud.com/knowledge-base/managed-services/managed-windows-server-connecting-to-your-server-with-remote-desktop/">Windows Server</a>  or <a href="https://www.centurylinkcloud.com/knowledge-base/managed-services/managed-red-hat-connecting-to-your-server-with-ssh/">RHEL</a>.<strong></strong>
</p>
<p><strong>Q: What should I do if I have trouble connecting via Remote Desktop?</strong>
</p>
<p>A: If you have difficulty connecting via RDP, be sure you are connecting from an IP that has TCP Port 3389 allowed on the <em>inbound</em> firewall. If you have a firewall at your location, you will need
  to have TCP port 3389 opened for <em>outbound</em> traffic. The firewall rule-set can be reviewed with your primary CenturyLink order contact or Consulting Engineer. <strong>Note that you should NEVER manage your remote servers through public IP address, and ONLY access servers through a secure tunnel like client VPN or site to site VPN!</strong>
</p>
<p>If you connect and find that the system disconnects you immediately, you should ensure you are using the latest Remote Desktop client and that your client machine is fully patched. For additional support, please contact the Client Service Center
  at 1-888-638-6771 and choose menu option 2.</p>
<p><strong>Q: How can I have my VM patched?</strong>
</p>
<p>A: An important component of OS administration and management is keeping the system up-to-date. This includes keeping the system current with all patches to help prevent security compromises or operational reliability
  issues. CenturyLink will, from time to time, schedule the installation of system patches as deemed appropriate by our Solution Engineers. We will schedule the installation with you in advance. This will allow both parties to prepare for the patching,
  as well as provide ample time for discussion regarding the potential impact the patch may have on specific applications within your environment.</p>
<p>In addition, you can request patching for your VM by contacting the Client Service Center at 1-888-638-6771 and choosing menu option 2.</p>
<p><strong>Q: How can I transfer files to my server using Remote Desktop?</strong>
</p>
<p>A: Files can be transferred by simply drag and drop in Windows Explorer from your remote desktop session.</p>
<ul>
  <li>Configuring Remote Desktop for files transfer:</li>
  <li>Run Remote Desktop Connection (Start Menu/All Programs/Accessories).</li>
  <li>Enter the IP Address of the server.</li>
  <li>Click Options, then select Local Resources tab.</li>
  <li>Under Local devices and resources, click on More…</li>
  <li>Click on the “+”next to Drives, then select the local drive on your client which you would like to copy files from.</li>
  <li>Click Ok when done.</li>
  <li>Click Connect to initiate the connection.</li>
  <li>After connection is established, in your remote desktop session, open Windows Explorer (Start Menu/All Programs/Accessories)</li>
  <li>Local drive will show as Driver Letter on Hostname format, e.g. C on MyPC, process to copy files to or from your local drive</li>
</ul>
<p><strong>Q: Who do I contact if I have trouble with my Managed VM?</strong>
</p>
<p>A: The CenturyLink Technology Solutions Client Service Center is available to assist you with any issues you may have 24 hours a day, 7 days a week, and 365 days a year. Simply call us at 1-888-638-6771, or send email to request@savvis.com for Managed OS issues. If there is an outage, email can be sent to incident@savvis.com.</p>
<p><strong>Q: How can I remove Managed Services from a VM?</strong>
</p>
<p>A: Currently, the only way to remove Managed Services from a VM once it has been deployed is to delete the VM and to create a new server that is unmanaged. This process should be followed for managed operating systems as well as for managed applications.</p>
<p><strong>Q: How can I tell my <em>managed</em> VMs from my <em>unmanaged</em> VMs in the CenturyLink Cloud Control portal?</strong>
</p>
<p>A: Managed VMs will be noted with an asterisk (*) in front of the server name. For example, <em>*ILMHPELCTA04</em>. This notation is intended to make it easier to locate managed VMs from within
  a list of all Cloud VMs you have created.</p>
<p>Q:    <strong>My VM shows under constructionin Control, but shows that the build has completed successfully?</strong>
</p>
<p>A:    On Managed VMs, there are additional tasks that is being processed in the background in order to fully integrate into the Managed system, once this is complete Control will reflect it as active and manageable. </p>

<p><strong>Q: Can I join Managed Servers to my own domain?</strong>
</p>
<p>A: Yes, customers may elect to join a Managed Server to their own domain instead of the CenturyLink Shared Active Directory Domain.  In order to join Managed Servers to a <em>dedicated</em> customer domain a user must deploy <a href="https://www.centurylinkcloud.com/knowledge-base/managed-services/getting-started-with-managed-active-directory">Managed Active Directory</a> in the CenturyLink Cloud.
</p>
<p><strong>Q: Can <i>un-managed</i> Servers be converted to <i>Managed</i> (or vice versa)?</strong>
</p>
<p>A: Servers <b>can</b> be converted from unmanaged to managed by executing the "Managed RHEL for CPI" (for Red Hat servers) or "Managed WIN for CPI" (for Windows servers) Blueprints in the library. Customers <b>cannot</b> go from a managed server to an unmanaged server.
</p>
<p><strong>Q: What Anti-Virus is provided for Windows Servers and how often is it updated?</strong>
</p>
<p>A: McAfee is leveraged on Managed Windows Servers and is updated daily.</p>
