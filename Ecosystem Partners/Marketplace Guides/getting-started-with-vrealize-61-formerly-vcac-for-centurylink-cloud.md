{{{
  "title": "Getting Started with vRealize 6.1 (formerly vCAC) for CenturyLink Cloud",
  "date": "12-16-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><em>Updated 17 Dec 2014 by David Shacochis</em></p>
<h3>vRealize &amp; CenturyLink Cloud</h3>
<p><a href="http://www.vmware.com/products/vrealize-suite/">vRealize</a> (formerly vCloud Automation Center, or vCAC) is a cloud management platform that enables users to perform functions against VMware vSphere, other hypervisors, and select public clouds.&nbsp;vRealize
  gives IT pros:</p>
<ul>
  <li>A self-service portal for building and managing virtual infrastructure</li>
  <li>An orchestration tool for designing multi-tier applications</li>
  <li>Policy-based controls for permissions, approvals, and capacity management</li>
  <li>Auditing and logging of management activities</li>
  <li>Cross-environment visibility from a single user interface</li>
</ul>
<p>With its most recent release, VMware has built a vRealize “endpoint” to CenturyLink Cloud. This endpoint uses the CenturyLink Cloud API to provide basic creation and “day 2” management activities. Specifically vRealize offers the following capabilities
  for CenturyLink Cloud:</p>
<ul>
  <li>
    <p><strong>VM Creation.</strong> Create VMs using host reservations. Host reservations allow you to create VMs while taking into account per data center OS templates, networks and capacity limits.</p>
  </li>
  <li>
    <p><strong>Data Collection.</strong> Retrieves the list of data centers, available networks, available OS templates, public IP addresses in use, Server Groups, and virtual machines.</p>
  </li>
  <li>
    <p><strong>Display Inventory and Day 2 Operations.</strong> Show servers and their current run state and power commands like power on, power off, reboot, reset, and shutdown.</p>
  </li>
  <li>
    <p><strong>Connect via RDP/SSH.</strong> Connect to servers via private IP address.</p>
  </li>
</ul>
<p>For CenturyLink customers who have built custom private clouds using VCE or hybrid solutions with vCloud air, vRealize provides a seamless integration point for extending deployments to the CenturyLink Cloud. Likewise, VMware customers looking to
  extend their hybrid footprint into the CenturyLink Cloud can leverage vRealize to manage their CenturyLink Cloud virtual machines.</p>
<p>The vRealize endpoint for CenturyLink Cloud was created by VMware. As such, VMware will perform all ongoing support related to the integration. vRealize has a plug-in architecture that supports 3rd party “<a href="http://www.vmware.com/files/pdf/vrealize/vmware-vrealize-operations-management-packs-wp-en.pdf">management packs</a>.”</p>
<p>To enable the CenturyLink Cloud endpoint within vRealize, please reach out to your VMware sales representative.</p>
<h3>FAQs – vRealize Endpoint</h3>
<p><strong>Q: What are the capabilities of the endpoint?</strong>
</p>
<p><strong>A: </strong>The vRealize endpoint can do the following operations in the CenturyLink Cloud:</p>
<ul>
  <li><strong>Data Collection</strong>. The endpoint interrogates the platform and retrieves the list of data centers, available networks, available OS templates, public IP addresses in use, Server Groups, and virtual machines.</li>
  <li><strong>Host Reservations. </strong>Create reservations per DC that take into account OS templates, networks, and capacity limits.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/R0SXOihf2hmop4do35148ifEJ/?name=vRealize_1.png" alt="vRealize_1.png" />
</p>
<ul>
  <li><strong>Display Inventory. </strong>Show servers and their current run state.</li>
  <li><strong>Day 2 Operations. </strong>Includes power operations like power on, power off, reboot, reset, and shutdown.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/Ot3WIG5DNMCX6Jd52KllVQRCX/?name=vRealize_2.png" alt="vRealize_2.png" />
</p>
<ul>
  <li><strong>Connect via RDP/SSH</strong>. Connect to servers via private or public IP address (not recommended).</li>
  <li><strong>VM Creation. </strong>Create new, unmanaged VMs using host reservations and the vRealize concept of Blueprints.</li>
</ul>
<p><strong>Q: How do I get this installed in my vRealize environment?</strong>
</p>
<p>A: CenturyLink will provide customers the installation components, and customers either partner with VMware or follow their instructions for installing the endpoint into their vRealize environment.</p>
<p><strong>Q: What version of vRealize does this work with?</strong>
</p>
<p><strong>A: </strong>This endpoint only works with vRealize 6.1.</p>
<p><strong>Q: How do customers authenticate vRealize with the CenturyLink Cloud?</strong>
</p>
<p><strong>A</strong>: Customers use API credentials from the Control Portal.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/0mL8504ZMVG2j9utv2NCL6eKG/?name=vRealize_3.png" alt="vRealize_3.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/izpethrQ01xBGb1dsrwCeIFKw/?name=vRealize_4.png" alt="vRealize_4.png" />
</p>
<p><strong>Q: How does the endpoint show up for CenturyLink Cloud customers?</strong>
</p>
<p><strong>A: </strong>The endpoint appears under “cloud endpoints” in the management portal.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/1VE8XVNGgsCfKKnlVFbMEbZVQ/?name=vRealize_5.png" alt="vRealize_5.png" />
</p>
<p><strong>Q: Does the vRealize adapter work across a CenturyLink Cloud account hierarchy?</strong>
</p>
<p><strong>A: </strong>A vRealize “endpoint” is tied to a specific account. Customers can create multiple endpoints to map to each of their sub-accounts.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/Imyy55LLryKhAXvUKREJAxLWl/?name=vRealize_6.png" alt="vRealize_6.png" />
</p>
<p><strong>Q: Can customers execute CenturyLink Cloud Blueprints using the endpoint?</strong>
</p>
<p><strong>A: </strong>No, the endpoint has no knowledge of CenturyLink Cloud Blueprints, and the vRealize system has their own concept of orchestration capabilities (which is also named Blueprints). A vRealize Blueprint uses reservations to define a build
  process for customers.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/a9pV6n7tSr4prRjgNllNvuPF8/?name=vRealize_7.png" alt="vRealize_7.png" />
</p>
<p><strong>Q: How do vRealize Blueprints pick which data center to deploy a server to?</strong>
</p>
<p>By default, a Blueprint will use an algorithm to choose which reservation (identified by an OS template and data center) to apply. If the customer wants to pin the server to a particular data center, they define a Reservation Policy and apply that to
  the Blueprint.</p>
<p><strong>Q: Can I create a managed server using this endpoint?</strong>
</p>
<p><strong>A: </strong>No, this endpoint uses the CenturyLink Cloud v1 API that has no awareness of managed servers.</p>
<p><strong>Q: Does the endpoint let me manage servers that I created outside of the vRealize interface?</strong>
</p>
<p><strong>A: </strong>No, vRealize just knows about – and manages – the servers that it has created.</p>
<p><strong>Q: Can I use a custom template with vRealize, or just the out of the box OS templates?</strong>
</p>
<p><strong>A: </strong>vRealize retrieves all the available templates for an account and data center, including custom ones.</p>
<p><strong>Q: Can I resize a server using the vRealize interface?</strong>
</p>
<p><strong>A: </strong>No, servers cannot be resized using this version of the endpoint.</p>
<p><strong>Q: Can customers choose which operations they want to let administrators perform on a server?</strong>
</p>
<p><strong>A: </strong>Yes, the vRealize Blueprint lets the designer choose the available actions.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/fOcnoUnraPbTkbDdXbBPbmZAI/?name=vRealize_8.png" alt="vRealize_8.png" />
</p>

<p><strong>Q: How do customers provision new machines?</strong>
</p>
<p><strong>A: </strong>Once a Blueprint is created and published in vRealize, users can access them via a Service Catalog. At deploy time, the user may have some choices about the size and storage of a server.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/iAKbEzk4fjrlKB2orKKHsRNpW/?name=vRealize_9.png" alt="vRealize_9.png" />
</p>
<p><strong>Q: What does Control look like when a server has been provisioned by vRealize?</strong>
</p>
<p><strong>A: </strong>Control shows the server as always, but puts each server into its own Group that vRealize knows about.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/LjxpOo3Z137st6Z19tT8LJbGj/?name=vRealize_10.png" alt="vRealize_10.png" />
</p>
<p><strong>Q: What vRealize-specific features help CenturyLink Cloud customers?</strong>
</p>
<p><strong>A: </strong>vRealize adds some policy management that the Control Portal doesn’t have. For instance, certain operations can be set up for an approval workflow to prevent accidental or unauthorized activities. vRealize also supports the concepts
  of “leases” where a server is discarded after a certain period of time, and, through configurable archive properties, can remain available for a few remaining days. This encourages proper IT-as-a-Service thinking, while providing an escape valve for
  mistakenly deleted machines.</p>