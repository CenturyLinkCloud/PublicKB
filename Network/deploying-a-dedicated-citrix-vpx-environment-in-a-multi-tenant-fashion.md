{{{
  "title": "Deploying a Dedicated Citrix VPX Environment in a Multi-tenant Fashion",
  "date": "12-27-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Deploying a Dedicated Citrix VPX Environment in a Multi-tenant Fashion</h3>
<p>While the CenturyLink Cloud platform provides a <a href="https://t3n.zendesk.com/entries/22110695-Creating-a-Self-Service-Load-Balancing-Configuration" target="_blank">self-service load balancing service</a> for public facing web applications there may
  be times in which this model does not meet a customers use case or technical requirements. &nbsp;CenturyLink Cloud customers can license Citrix VPX dedicated virtual load balancers on a monthly use basis. &nbsp;Internal IT personnel, partners, resellers
  and other ISV's may wish to deploy dedicated Citrix VPX load balancers for consumption across their application portfolio or client base in a multi-tennant fashion. &nbsp;Using the Citrix VPX platform in a multi-tenant fashion can avoid costs of deploying
  devices for every application or customer and reduce administrative overhead. &nbsp;</p>
<h3>Use Case</h3>
<p>This KB will provide a sample use case in which a highly available pair of Citrix VPX dedicated load balancers are deployed into multi-tier account hierarchy using CenturyLink Cloud Parent &amp; Sub-accounts. &nbsp;The end state will deliver load balancing
  services to a sub-account of the parent providing account isolation while delivering secure load balancing services.</p>
<h3>Prerequisites</h3>
<ul>
  <li>A CenturyLink Cloud Account</li>
  <li>Hands-On experience deploying Dedicated VPX Appliances and configuration</li>
  <li>Hands-On experience working with Parent &amp; Sub-Account hierarchies&nbsp;and Firewall self-service&nbsp;</li>
</ul>
<h3>Building a Parent &amp; Sub-Account Hierarchy</h3>
<ul>
  <li>Each CenturyLink Cloud client will receive an initial account, this is the Parent Account. &nbsp; This is the top level of a larger account&nbsp;hierarchy&nbsp;that can be created based on business needs. &nbsp;In this sample we will construct a simple
    set of 'Client' sub-accounts to the parent to simulate delivery of services to various unique customers of an ISV using CenturyLink Cloud to deliver their own unique service portfolio. &nbsp;The Account Structure will be as follows:</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/eFb91tZdRgxU6ykxOSNBetgkY/?name=01.png" alt="01.png" />
</p>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/34202514-Creating-a-subaccount" target="_blank">Steps to create a sub-account can be found in our knowledge base</a>.&nbsp;</li>
  <li><a href="https://t3n.zendesk.com/entries/58057320-Practical-Guide-for-Using-Roles" target="_blank">A Practical Guide for Using Roles </a>can also be used to gain additional understanding of roles &amp; account hierarchies</li>
</ul>
<h3>&nbsp;Deploy the Dedicated Citrix VPX Appliances</h3>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs" target="_blank">Deploy a dedicated Network VLAN</a> in your parent account within the appropriate data center. &nbsp; Costs for VLANs can be found in our <a href="http://www.centurylinkcloud.com/estimator"
    target="_blank">Online Estimator</a> or your CenturyLink Cloud MSA. &nbsp;Once this job completes we recommend you <a href="https://t3n.zendesk.com/entries/26388584-Add-a-User-Friendly-Name-to-VLANs" target="_blank">apply a friendly name to this VLAN</a>.
    &nbsp;In the sample below in CA3 we have a network created and named NLB_10.100.97.0/24. &nbsp;<strong>TIP: &nbsp;We recommend the VPX reside in a dedicated VLAN which allows for maximum Firewall security control and scalability of VIPs.</strong>
  </li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/jnNGDnyT5uv6MQuX5yT52LFxA/?name=02.png" alt="02.png" />
</p>
<ul>
  <li>Request a <a href="http://www.centurylinkcloud.com/service-tasks" target="_blank">Service Task</a> to Deploy your Citrix VPX devices. &nbsp;Optionally, you can do single instance virtual appliances if high availability is not a requirement. &nbsp;(Tip:
    <a href="https://t3n.zendesk.com/entries/37871764-Requesting-Service-Tasks-on-CenturyLink-Cloud" target="_blank">How to Request a Service Task</a>). &nbsp;Include the following in your request:</li>
  <ol>
    <li>The Account alias of the Parent Account you wish to deploy the VPX(s) into. &nbsp;The alias is found on the Account, Info page</li>
    <li>The Data Center in which you which the VPX(s) to be deployed</li>
    <li>The Network into which the VPX(s) should be deployed. &nbsp;In this example NLB_10.100.97.0/24 was leveraged as we want to deploy the appliances into a parent network.</li>
    <li>The Group you'd like the VPX(s) deployed into</li>
    <li>Note how many VIP's you'd like reserved in the network for load balancing. &nbsp;The support team can later reserve more via a ticket. &nbsp;Generally, our team will reserve 10 VIPs out of the box unless stated otherwise. &nbsp;</li>
    <li>Indicate which of the (4) dedicated load balancer types you wish to purchase. &nbsp;See&nbsp;<a href="http://www.centurylinkcloud.com/load-balancing" target="_blank">http://www.centurylinkcloud.com/load-balancing</a>
    </li>
    <li><a href="https://t3n.zendesk.com/entries/21714594-PIN-Authentication-for-Support-Requests" target="_blank">Provide your pin</a>
    </li>
  </ol>
  <li>Once the Service Task team deploy's your VPX appliance(s) you will get a notification with details on your new devices. &nbsp;This list will include:</li>
  <ol>
    <li>The VM name of the VPX(s)</li>
    <li>The Management IP of the VPX(s): &nbsp;In this example the IP is 10.100.97.100</li>
    <li>The RNAT IP of the VPX: &nbsp;In this example the RNAT IP is 10.100.97.101</li>
    <li>Username &amp; Password to perform administration of your new appliances</li>
    <li>The list of VIP's reserved for the VPX: &nbsp;In this example the reserved pool is 10.100.97.103-113</li>
  </ol>
  <li>Citrix VPX Appliances will be shown in Control</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/OitSGuuLvfmVGYBvyDpRP1us6/?name=09.png" alt="09.png" />
</p>
<h3>Deploy Sub-Account Virtual Instances</h3>
<p>With a sub-account named 'Client A' deployed under the Parent Account, its now time to deploy virtual instances you wish to load balance in this sub-account. &nbsp; In this example, we are going to deploy (2) Windows 2012 R2 Data Center Web Servers running
  IIS. &nbsp;We will also build a test HTML page to show the load balancing services are functional at the end of configuration.</p>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs" target="_blank">Deploy a Web VLAN</a>&nbsp;in the 'Client A' sub-account within the appropriate data center. &nbsp; Costs for VLANs can be found in our&nbsp;<a href="http://www.centurylinkcloud.com/estimator"
    target="_blank">Online Estimator</a>&nbsp;or your CenturyLink Cloud MSA. &nbsp;Once this job completes we recommend you&nbsp;<a href="https://t3n.zendesk.com/entries/26388584-Add-a-User-Friendly-Name-to-VLANs" target="_blank">apply a friendly name to this VLAN</a>.
    &nbsp;In this sample we used WEB_10.100.187.0/24.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/4q318KazByfKgo2IxOOcXJJVo/?name=04.png" alt="04.png" />
</p>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/22603877-Creating-a-New-Enterprise-Cloud-Server" target="_blank">Create (2) Windows 2012 R2 Data Center Virtual Servers</a>&nbsp;into a Group called Web Servers. &nbsp;These VM's should be placed in the WEB_10.100.187.0/24
    VLAN.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/o8FZbtjFWjYCHWsfHvKRXkCJD/?name=03.png" alt="03.png" />
</p>
<ul>
  <li>Install IIS using the <a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups" target="_blank">Execute Package</a> function and <a href="https://t3n.zendesk.com/entries/56566374-CenturyLink-Cloud-Public-Blueprint-Packages"
    target="_blank">CenturyLink Cloud's public IIS 8 script</a>
  </li>
</ul>
<p>(<strong>QUICK TIP</strong>: &nbsp;Save Time and build a blueprint to deploy (2) Web Servers into the Web VLAN and layer on the IIS 8 packages)</p>
<ul>
  <li>Use <a href="https://t3n.zendesk.com/entries/20914433-How-To-Configure-Client-VPN" target="_blank">Client VPN</a> to RDP into the (2) newly created Web Servers and create a test page named default.htm in the IIS root folder (C:\inetpub\wwwroot). &nbsp;Sample
    basic HTML code is below: &nbsp;</li>
</ul>
<p>Web Server #1 default.htm file:</p>
<p>&lt;header&gt;Client A NLB&lt;/header&gt;
  <br />&lt;body&gt;Client A NLB Node #1&lt;/body&gt;</p>
<p>Web Server #2 default.htm file:</p>
<p>&lt;header&gt;Client A NLB&lt;/header&gt;
  <br />&lt;body&gt;Client A NLB Node #2&lt;/body&gt;</p>
<ul>
  <li>Validate the pages load locally on the Web Servers by accessing http://localhost</li>
</ul>
<h3>Configure Intra Data Center Firewall Policies</h3>
<p>Next, we must configure the parent account firewall in which the VPX(s) reside (NLB_10.100.97.0/24) to permit the appropriate HTTP(s) traffic and VPX Service Group health checks into the network in which the (2) Web Servers reside (WEB_10.100.187.0/24).</p>
<ul>
  <li>Navigate to the Firewall portion of Control on the 'Parent' Account.&nbsp;</li>
  <li>Select the Source Account to be the 'Parent' Account.</li>
  <li>Select the Destination Account to be 'Client A' Sub-Account.</li>
  <li>Add a Firewall Rule as follows</li>
</ul>
<p><strong>Add Source Address</strong>
</p>
<p>Network: &nbsp;NLB_10.100.97.0/24</p>
<p>Subnet Size: &nbsp;1</p>
<p>Starting IP: &nbsp;&lt;RNAT IP of NLB Provided by Service Tasks&gt; &nbsp;In this sample, the RNAT IP is 10.100.97.101&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/o5exOahqkQ9URyMIeBRsNeE3w/?name=06.png" alt="06.png" />
</p>
<p><strong>Add&nbsp;Destination Address</strong> &nbsp;</p>
<p>Network: &nbsp;WEB_10.100.187.0/24</p>
<p>Subnet Size: 1 (or use another size depending on # of web servers)</p>
<p>Starting IP address: &nbsp;&lt;Private IP address of your Web Servers in Client A sub-account&gt; &nbsp;In this sample, our web servers are 10.100.187.12 &amp; 13.</p>
<p>(<strong>Tip</strong>: &nbsp;select the add destination address a 2nd time in this sample to add 10.100.187.13 to the same firewall rule.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/gm54lHUyF8PTRZPpHTrcDi5ox/?name=07.png" alt="07.png" />
</p>
<p><strong>Add Ports</strong>
</p>
<p>Select HTTP(80) and PING, &nbsp;Optionally select HTTPS(443) if you plan to implement SSL</p>
<p><strong><img src="https://t3n.zendesk.com/attachments/token/rdrvqZ0wSRFDAplQt91CxDdk2/?name=08.png" alt="08.png" /></strong>
</p>
<ul>
  <li>Validate your new Firewall Rule and save it. &nbsp;We now have a Firewall Rule in place permitting tcp/80 and PING from the VPX RNAT IP (in a parent account) to (2) Virtual Web Servers in the Client A sub-account.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/y5rx2VVHZnW6Ip9A7MugA9ExH/?name=05.png" alt="05.png" />
</p>
<h3>Configure Citrix VPX Load Balancers</h3>
<p>We now need to configure the VPX load balancer(s) to deliver services to 'Client A' web servers. &nbsp;In this phase we will build service groups, virtual servers (VIP) and update the VPX routes to appropriately route traffic to the networks in 'Client
  A' sub-account. &nbsp;<strong>NOTE: &nbsp;This is not meant to be an all encompassing guide to configuring a Citrix VPX but just a basic sample use case to balance (2) web servers over HTTP in another sub-account and network.</strong> &nbsp;</p>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/27216280-Dedicated-Load-Balancer-Basic-Management" target="_blank">Use the Dedicated Load Balancer Basic Management KB</a> to configure a Service Group, Virtual Server and health checks for PING &amp; TCP. &nbsp;
    In this sample use case we built the following configuration using the admin interface (10.100.97.100):</li>
</ul>
<p><strong>Service Group</strong>
</p>
<p>Service Group Name: &nbsp;CLIENT_A</p>
<p>IP Members: &nbsp;10.100.187.12 &amp; 10.100.187.13 on Port 80</p>
<p>Monitors: &nbsp;TCP &amp; PING</p>
<p><img src="https://t3n.zendesk.com/attachments/token/cA9JDXtJr6NQA4pgZMvXnJy7t/?name=20.png" alt="20.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/d3htA7CIO4hbo8bTkvT31wJ8L/?name=21.png" alt="21.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/tmmVmRelqXoopOTQWqosjkFnD/?name=22.png" alt="22.png" />
</p>
<p><strong>Virtual Servers</strong>
</p>
<p>Virtual Server Name: &nbsp;CLIENT_A_PROD_WEBSITE</p>
<p>IP Address: &nbsp;&lt;IP from the reserved list during the service task portion of process&gt; &nbsp;In this example we used 10.100.97.103 from the reserved pool of VIPs</p>
<p>Service Groups: &nbsp;CLIENT_A</p>
<p>LB Method: &nbsp;Least Connection</p>
<p>Persistence: &nbsp;None</p>
<p><img src="https://t3n.zendesk.com/attachments/token/gesJ0VAHS5T2LqPGEMXpgON4g/?name=30.png" alt="30.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/uZW1n90PGkXTYi9jeiMNiKNlf/?name=31.png" alt="31.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/kAvOa1ywV8xf0QG6lp10uPLDo/?name=32.png" alt="32.png" />
</p>
<ul>
  <li>Navigate to Network, Routes in the VPX management UI. &nbsp;Create a route to the 'Client A' sub-account WEB_10.100.187.0/24 VLAN. &nbsp;<strong>TIP</strong>: &nbsp;The gateway IP will be the same gateway IP as the existing route 0.0.0.0. &nbsp;In this
    use case we used the following configuration:</li>
</ul>
<p>Network: &nbsp;10.100.187.0</p>
<p>Netmask: 255.255.255.0</p>
<p>Gateway: 10.100.97.1 (Gateway of the NLB_10.100.97.0/24 VLAN in which VPX Resides)</p>
<p>RNAT IP: &nbsp;10.100.97.101</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/Ydb7TSt11bOasYDWJOFUWeWoT/?name=40.png" alt="40.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/LSzWrXWqNsC39dudyG3vxo4ys/?name=41.png" alt="41.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/yxQ0YCE4PcvQezzC1hWrXZhDe/?name=42.png" alt="42.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/WwuhC3wlcVopT4HQBJw7qVxQ4/?name=43.png" alt="43.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/S9dNjYhCAMhmDsZUp9sH21bBU/?name=44.png" alt="44.png" />
</p>

<h3>Add Public IP to VIP for External Access</h3>
<p>Finally, as this use case is a public facing website we will use the <a href="https://t3n.zendesk.com/entries/49195400-How-To-Add-Public-IP-to-Virtual-Machine" target="_blank">Add Public IP</a> function of Control to perform a 1 to 1 NAT public IP to
  the VIP (Virtual Server) created previously on 10.100.97.103. &nbsp;</p>
<ul>
  <li>Navigate to the VPX in Control (TIP: if you have an HA pair the VIPs will be assigned to the primary VPX). &nbsp;Choose Add Public IP. &nbsp;Choose the VIP 10.100.97.103 (previously built in the VPX configuration). &nbsp;Lastly, we want to expose HTTP(80).</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/ibXZgkLMARihUw3CacpN7rHyD/?name=50.png" alt="50.png" />
</p>
<ul>
  <li>The Public IP for this new NAT can be found in the Servers Portion of the Control UI. &nbsp;In this example the Public IP is 206.152.32.226</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/O73UrfngTcsCRZbIY6S2HOxIB/?name=51.png" alt="51.png" />
</p>
<ul>
  <li>Validate the (2) Virtual Web Servers for Client-A sub-account are delivering the Test Page created previously. &nbsp;Use the refresh button a few times to see the page is being delivered by a unique web server and the services are functional. &nbsp;</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/TUOX5yKMphrCidcUsL9oWtWAP/?name=60.png" alt="60.png" />&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/AOgNNYegdbkoUnCX9Pg6Nr87k/?name=61.png" alt="61.png" />
</p>