{{{
  "title": "Creating Cross Data Center Firewall Policies",
  "date": "1-7-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Creating Cross Data Center Firewall Policies</h3>
<p>In addition to being able to connect networks within a particular data center through&nbsp;<a href="connecting-data-center-networks-through-firewall-policies.md">Intra Data Center firewall policies</a>,
  users can also create firewall policies that span cloud data centers. This helps enterprises build sophisticated, secure network topologies that take advantage of the CenturyLink Cloud's global footprint while meeting an organization's functional needs.</p>
<h3>General Notes</h3>
<ul>
  <li>In the current iteration customers cannot apply Firewall ACL's to traffic traversing cross data center policies.</li>
  <li>Each CenturyLink Cloud Data Center location provides unique private IP networks to customers. Thus eliminating any risk of overlapping IP space that would require a NAT with this service.</li>
</ul>
<h3><strong>Detailed Steps</strong></h3>
<p><strong><br /></strong>1. <a href="https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs">Create network VLAN(s)</a>&nbsp;in each of the respective CenturyLink Cloud Data Centers.</p>
<p>2. Validate the networks are in place in your CenturyLink Cloud account using the&nbsp;<strong>Networks&nbsp;</strong>menu item and selecting the appropriate Data Center. In the sample below, networks exists in both UC1 (Santa Clara) &amp;
  DE1 (Germany). </p>
<p><img src="https://t3n.zendesk.com/attachments/token/GyMTPFj5yNAuMs8gwXVUKExEZ/?name=01.png" alt="01.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/SMHQWeIGnCKI1DxPqO05vmMM1/?name=02.png" alt="02.png" />
</p>
<p><strong>OPTIONAL: &nbsp;Perform a test ICMP ping between virtual instances private IP addresses in different Cloud Data Centers. This test should fail as no Cross Data Center Firewall Rule is in place between networks in UC1 &amp; DE1.</strong>
</p>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/7xDTkGLoXpfTOtPRF5DLFhOye/?name=09.png" alt="09.png" /></strong>
</p>
<p><strong><br /></strong>3. Navigate to the Firewall menu in Control.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/iGqdw8VdfVC7RCxCygglmXyi5/?name=03.png" alt="03.png" />
</p>
<p>4. Select&nbsp;<strong>Either</strong>&nbsp;the source or destination CenturyLink Cloud Data Center node (as policies when applied are two-way rules). Next, choose to the&nbsp;<strong>Cross Data Center</strong>&nbsp;tab.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/tGm0I9fmyLqfoSryqlOZ3ec6J/?name=04.png" alt="04.png" />
</p>
<p>5. Choose&nbsp;<strong>Add Policy, Set Local Address</strong>.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ZosfcyVHiBisY80dKQvzcvX6F/?name=05.png" alt="05.png" />
</p>
<p>6. Select the appropriate network or CIDR IP range for the local address(es). In this example, we are using the entire 10.120.69.0/24 network block for a local address in UC1.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/gwgsREn2menIBpXzip0eEN150/?name=06.png" alt="06.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/anfgznJYPCTz1bawmJIkwebMJ/?name=07.png" alt="07.png" />
</p>
<p>7. Choose&nbsp;<strong>Set Remote Address(es). </strong>Select the appropriate network or CIDR IP range for the remote address(es). In this example, we are using the entire 10.110.226.0/24 network block for a remote address in DE1.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/OegJVdmynpVnbllAXveAinPOq/?name=08.png" alt="08.png" />
</p>
<p>8. Once complete, press the&nbsp;<strong>Save</strong>&nbsp;button. Your new Cross Data Center Rule will take &lt;60 seconds to process in the Queue. You can review its progress using the Queue Menu item. </p>
<p><img src="https://t3n.zendesk.com/attachments/token/haES1hGoEFg4Zt8RznoVleB5x/?name=10.png" alt="10.png" />
</p>
<p>9. Confirm the Cross Data Center Firewall Policy is functional by performing another ICMP ping test between virtual instances located in the (2) networks in different Data Center nodes. In this example, we are able to ping a virtual instances
  in Germany (DE1) from Santa Clara (UC1). </p>
<p><img src="https://t3n.zendesk.com/attachments/token/AzjfOwBAWjigeEC82VMxAAPpU/?name=11.png" alt="11.png" />
</p>
