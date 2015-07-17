{{{
  "title": "Creating a Self-Service IPsec (Site-to-Site) VPN Tunnel",
  "date": "11-5-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>IPsec is a framework of open standards for ensuring private communications over public networks. It has become the most common network layer security control, typically used to create a VPN tunnel. The CenturyLink Cloud platform enables self-service
  support to configure Site-to-Site (Point-to-Point, Gateway-to-Gateway) IPsec VPN Tunnels. This model protects communications between two specific networks, such as an organization’s main office network and a branch office network, or two business
  partner’s networks.&nbsp;<strong><br /></strong>
</p>
<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud customers (system administrators) who wish to&nbsp;extend their network and/or infrastructure to the cloud platform</li>
</ul>
<h3>Prerequisites</h3>
<ul>
  <li>Must have Account Administrator permissions on the platform</li>
  <li>Listing of the&nbsp;cloud network(s) you wish to connect to across your tunnel</li>
  <li>The make, model, and code version of the endpoint device you'll be terminating to</li>
  <li>Static IP of the peering interface on your device</li>
  <li>The network blocks you wish to have be reached on your end of the tunnel - <strong>these must be private IP blocks (RFC-1918)</strong>
  </li>
  <li><strong>You must have resources (server and a network) provisioned for the account and&nbsp;the Cloud&nbsp;data center you wish to connect to.</strong>
  </li>
</ul>
<h3>Detailed Steps</h3>
<ol>
  <li>Navigate to the Network / Site-to-Site VPN Control Portal function.</li>
</ol>
<p><img src="https://t3n.zendesk.com/attachments/token/egbq7lzxvhnuzyy/?name=s2s.PNG" alt="s2s.PNG" />
</p>
<p>2. Select the create point to point VPN button</p>
<p><img src="https://t3n.zendesk.com/attachments/token/mdyjptwvqqnnjqa/?name=ipsec+image+02.jpg" alt="ipsec_image_02.jpg" />
</p>
<p>3. Select the appropriate Cloud Data Center for the VPN Tunnel</p>
<p><img src="https://t3n.zendesk.com/attachments/token/de2loiadv00zgzc/?name=ipsec+image+03.jpg" alt="ipsec_image_03.jpg" />
</p>
<p>4. Select the the network blocks you want reachable under your account. It is permissible to supply tunnel access to specific servers or small subnets within your cloud networks.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/fjqwdjeo1wpgldw/?name=ipsec+image+04.jpg" alt="ipsec_image_04.jpg" />
</p>
<p>5. Input 'Your Site' Information:</p>
<ul>
  <ul>
    <li>Site Name (ex. Montreal Office)</li>
    <li>Device Type (ex. Cisco ASA5520 v8.3)</li>
    <li>VPN Peer IPv4 Address: &nbsp;Static IP of the peering interface on your device</li>
    <li>Tunnel Encrypted Subnets: &nbsp;The network blocks you wish to have be reached on your end of the tunnel -&nbsp;<strong>these must be private IP blocks (RFC-1918)</strong>
    </li>
  </ul>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/izbezakbvlohipc/?name=ipsec+image+05.jpg" alt="ipsec_image_05.jpg" />
</p>
<p>6. Input the Phase 1 (IKE) information</p>
<ul>
  <ul>
    <li>Protocol Mode (Main or Aggressive). We recommend 'Main' mode.</li>
    <li>Encryption Algorithm (AES-128; AES-192; AES-256; 3DES). We recommend AES-128 or better.</li>
    <li>Hashing Algorithm (SHA1 96; SHA1 256; MD5). We recommend SHA1 for most customers.</li>
    <li>Pre-Shared Key: &nbsp;The pre-shared key is a shared secret that secures the VPN tunnel. This value must be identical on both ends of the connection.</li>
    <li>Diffie-Helman Group (Group 1; Group 2; Group 5). If using AES with a cipher strength greater than 128-bit, or SHA2 for hashing, we recommend Group 5, otherwise Group 2 is sufficient.</li>
    <li>Lifetime Value (1 hour; 8 hours; 24 hours). Lifetime is set to 8 hrs for IKE - This is not required to match, as the negotiation will choose the shortest value supplied by either peer.</li>
    <li>DPD State&nbsp;(Dead-peer detection): &nbsp;Specify if you wish this enabled or disabled - check your device defaults - for example Cisco ASA defaults to "on" while Netscreen/Juniper SSG or Juniper SRX default to "off"). Our default is "off".</li>
    <li>NAT-T State: &nbsp;&nbsp;Allows connections to VPN end-points behind a NAT device. Defaults to 'off' - if you require NAT-T, you also need to provide the private IP address that your VPN endpoint will use to identify itself.</li>
    <li>Remote Identity: &nbsp;The Private IP Address that your VPN endpoint will use to identify itself. Required only when NAT-T state is on.&nbsp;</li>
  </ul>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/mw8k0nuwjpeyxbj/?name=update+nat-t.png" alt="update_nat-t.png" />
</p>
<p>7. Input the Phase 2 (IPSEC) information and select Finish to complete the tunnel configuration.</p>
<ul>
  <ul>
    <li>IPSEC Protocol (ESP or AH). ESP is&nbsp;preferred.</li>
    <li>Encryption Algorithm (AES-128; AES-192; AES-256; 3DES). We recommend AES-128 or better.</li>
    <li>Hashing Algorithm (SHA1 96; MD5). We recommend SHA1 for most customers.</li>
    <li>PFS Enabled: &nbsp;We suggest enabled, using Group 2, though Group 5 is recommended with SHA2 hasing or AES-192 or AES-256.</li>
    <li>Lifetime Value (1 hour; 8 hours; 24 hours). Lifetime is set to 1 Hour&nbsp;(and unlimited KB). This setting is not required to match, as the negotiation process will choose the shortest value supplied by either peer.</li>
  </ul>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/ufpxph5fmzyhe5o/?name=ipsec+image+07.jpg" alt="ipsec_image_07.jpg" />
</p>

<h3><strong>Standard Troubleshooting</strong></h3>
<div>Our configuration will be established based on the parameters in the Control Portal self-service interface. If you need to open a ticket reporting trouble establishing a tunnel, please also start a continuous ping with traffic interesting to the VPN configuration.
  We can validate our configuration and supply any&nbsp;relevant&nbsp;log messages indicating the source of the problem.</div>
<div>
  <br />It remains up to you, the customer, to correct your own configuration, submit new configurations with changed settings, or seek troubleshooting assistance with your own resources (for example using your equipment manufacturer's maintenance contract).
  Unfortunately due to the variety of devices and technologies, we cannot be responsible for the end-to-end VPN configuration</div>
<h3><strong>Non-standard configurations</strong></h3>
<p>If you require any additional assistance beyond the options available in self-service, that would fall into the "non-standard" configuration category.</p>
<p>We define non-standard configurations as anything deviating from the above process, or utilizing configuration options specifically listed as out-of-scope. These configurations need to be addressed as a <a href="http://www.ctl.io/products/support/service-tasks"
 ><strong>service task</strong></a> engagement. Contact your account manager with any questions.</p>
<p>Common reasons for non-standard VPN tunnels include:</p>
<ul>
  <li>Requesting an engineer to perform a live turn-up with you on a conference call</li>
  <li>Requesting CenturyLink Cloud complete your organization's VPN information, or provide network documentation beyond what is included in this article.</li>
  <li>Any requirement for an engineer to attend a live meeting or telephone call.</li>
  <li>NAT requirement (generally this is a requirement when the cloud servers need to be presented as a public IP address via the tunnel) - please note this is only for NAT on the encrypted network addresses. We fully support NAT-Traversal (NAT between gateways)
    with our standard configuration.</li>
  <ul>
    <li>Regarding the addresses used for NAT presentation - if you require less than 5 total addresses, we can assign /32 mappings from our public space for the data center-side. If you require a larger block of addresses, you (the customer) will need to
      supply the public IP address space to be used to present your data center resources.</li>
  </ul>
  <li>Using the VPN as a fail-over for direct-connect customers (ex. you want to back-up your MPLS WAN with a VPN tunnel)</li>
  <li>Certificate-based authentication</li>
  <li>Non-IP Address IKE identity (such as used with a dynamic remote peer IP address, or hostname-based identity strings)</li>
  <li>User requires assistance with their device (no technical expertise in-house) - we can provide one-time configuration assistance for most enterprise-class VPN endpoints:</li>
  <ul>
    <li>Cisco PIX / ASA</li>
    <li>Cisco IOS-based</li>
    <li>Netscreen / Juniper SSG</li>
    <li>Juniper SRX</li>
    <li>Sonicwall</li>
    <li>... and many others. For most firewall-type devices, configuration assistance can be provided. We can generally find an engineer with relevant experience within our staff.</li>
  </ul>
</ul>
<h3>&nbsp;</h3>
