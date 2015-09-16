{{{
  "title": "Cloud Platform – Release Notes: August 5, 2013",
  "date": "8-9-2013",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<hr />
<ul>
  <li><strong>Self-service Load Balancer.&nbsp;</strong>Customers can create, change, and delete load balancer configurations. Each configuration consists of a VIP, and pool of servers for a given port (80 and 443 at this time). Servers can be added or deleted
    from a pool, or temporarily taken out of rotation. The cost for using the shared load balancer is $0.04 per hour, and bandwidth charges remain the
    same.
    <p><img src="https://t3n.zendesk.com/attachments/token/6nhavnhfgqq16wy/?name=release08-05_01.png" alt="release08-05_01.png" />
    </p>
  </li>
  <li><strong>Self-service provisioning of site-to-site VPN.&nbsp;</strong>Users can now configure a site to site IPsec VPN tunnel from the Control Portal instead of opening a ticket with the CenturyLink Cloud NOC.
    <br />
    <p><img src="https://t3n.zendesk.com/attachments/token/t7jrwoyoufy1ojm/?name=release08-05_02.png" alt="release08-05_02.png" />
    </p>
  </li>
</ul>
<p></p>
<p><strong>Minor Enhancements (5)</strong>
</p>
<ul>
  <li><strong>Account administrators can add new VLANs.&nbsp;</strong>Customers can add new networks to their accounts without contacting CenturyLink Cloud first. Also, VLANs can be deleted via self-service (*if* there are no IPs claimed or assigned; if the VLAN is
    in use, please open a NOC ticket to have your VLAN cleaned up) and all connected resources such as firewall rules and client VPN routes are removed. Note that private VLANs have <a href="http://www.tier3.com/products/network/firewall">the same price as before</a>.
    <p><img src="https://t3n.zendesk.com/attachments/token/rhmfej5scwlv6tz/?name=release08-05_03.png" alt="release08-05_03.png" />
    </p>
  </li>
  <li><strong>Specify custom port (ranges) on edge firewall.&nbsp;</strong>Instead of being constrained to the most common ports for the public firewall, customers can now specify custom ports or port ranges for their public IP addresses. Note that this capability
    will be available for servers in all data centers EXCEPT WA1 and UT1.
    <p><img src="https://t3n.zendesk.com/attachments/token/p1fod3ppzlic3ik/?name=release08-05_05.png" alt="release08-05_05.png" />
    </p>
  </li>
  <li><strong>Account hierarchy browser.&nbsp;</strong>Customers with many sub-accounts can now view this relationship via a hierarchical interface.
    <p><img src="https://t3n.zendesk.com/attachments/token/vtff4mpyrlxtlqc/?name=release08-05_04.png" alt="release08-05_04.png" />
    </p>
  </li>
  <li><strong>Object Storage bandwidth auditing</strong>. The initial launch of the CenturyLink Cloud geo-redundant Object Storage service did not include a charge for inbound/outbound transfer, but now this is billed at $0.08/GB.</li>
  <li><strong>Users API returns user status.</strong> Both the GetUsers and GetUserDetails API operations now return a status field that indicates if the user is active or inactive.</li>
</ul>
<p><strong>For a demo of these features, please visit:&nbsp;<a href="http://www.slideshare.net/Tier3Cloud/tier-3-august-2013-release-webcast">http://www.slideshare.net/Tier3Cloud/tier-3-august-2013-release-webcast</a>&nbsp;</strong>
</p>
