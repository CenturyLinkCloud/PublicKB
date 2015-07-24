{{{
  "title": "Recommended Security Practices for Using CenturyLink Cloud",
  "date": "01-06-2015",
  "author": "Steve White",
  "attachments": [],
  "contentIsHTML": true
}}}


<h3>Description (goal/purpose)</h3>
<p>The purpose of this article is to provide some general recommended security practices for customers using CenturyLink Cloud. These practices are based on common scenarios we have seen in customer environment, but is not an exhaustive list of all possible security considerations and is not intended to replace having a proper security risk assessment performed on the customer environment.</p>
<h3>Audience</h3>
<ul>
<li>All CenturyLink Cloud customers</li>
</ul>
<h3>Impact</h3>
<p><span data-mce-mark="1">Failure to properly secure systems and applications that are exposed to the public network can result in the systems being compromised, leakage of proprietary data, etc. In some cases, a compromised machine can be used by remote attackers as part of a botnet to attack other systems across the Internet.<br /></span></p>
<h3>Prerequisites</h3>
<p>None</p>
<h3>Detailed Steps</h3>
<ol>
<li>Do not open SSH (port 22) or RDP (port 3389) to the public network. Customers wishing to manage their servers over SSH and RDP should use the provided software-based VPN or other private connection option such as Direct Connect, IPSec VPN, etc. More information about the VPN can be found in our knowledge base [here](../Network/how-to-configure-client-vpn.md)</li>
<li>Always set strong administrator passwords that are at least 12 characters long, include at least one lowercase letter, uppercase letter, number, and special character, and do not include dictionary words, even using common substitutions like "@" instead of "a".</li>
<li>When opening an application to the public network such as HTTP or HTTPS, only open the specific port(s) needed, do not open all ports, or large ranges of ports.</li>
<li>When building a new server or installing a new application onto a server, always run a patch update to install the latest operating system and application patches on the system.</li>
<li>Regularly apply patch updates to operating systems and applications.</li>
<li>If there is a business requirement such that you absolutely must open RDP or SSH to the public network, use the "restrict source traffic" feature to restrict the traffic to that port to authorized sources only. (See [How to Add Public IP to Virtual Machine](../Network/how-to-add-public-ip-to-virtual-machine.md) for more details.)</li>
</ol><img src="https://t3n.zendesk.com/attachments/token/PhlU324nfyCW2EOiwcaj5lkO2/?name=Capture.JPG" alt="Capture.JPG" width="865" height="340" />
