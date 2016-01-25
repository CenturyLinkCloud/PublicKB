{{{
  "title": "Dedicated Load Balancer Basic Management",
  "date": "12-15-2014",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description&nbsp;</h3>
<p>This KB will go over the basics of creating a Load Balancer VIP and Service Group when using dedicated Load Balancers</p>
<h3>Prerequisites</h3>
<ul>
  <li>Must have a dedicated Netscaler available in your environment</li>
  <li>Must have an Admin login to your netscaler</li>
  <li>Must have Java installed and configured correctly. See KB: <a href="../General/how-to-configure-java-settings-to-access-web-user-interfaces.md"> How-to-Configure-Java</a>
      <br />
    </a>
  </li>
  <li>Understand the basic architecture of how a Netscaler works. See KB:<a href="./load-balancing-dedicated-vs-shared.md">Load Balancing Dedicated vs Shared</a>
      <br />
    </a>
  </li>
</ul>
<h3>Notes</h3>
<ul>
  <li>Traffic destined to the Load Balancer will hit the <strong>Virtual Server(VIP)</strong> first. From there it will determine which <strong>member</strong> of the attached <strong>Service Group</strong> to send traffic too based on the <strong>Load Balancing Method.</strong>
  </li>
</ul>
<h3>Detailed Steps</h3>
<ol>
  <li>Log into the Netscaler web interface using http://netscalerManagementip with an Admin account</li>
</ol>
<h3>Create Service Group</h3>
<ol>
  <li>Expand the menu Load Balancing, select Service Groups, and click Add. (Version 10.1 and later this is within Traffic Management)</li>
  <ul>
    <li>Description of each required field</li>
    <ul>
      <li>Service Group Name: The name we reference when attaching the Service Group to the VIP</li>
      <li>Protocol: This should match the type of traffic that will be used between the Load Balancer and the members of the Service Group. Note: If you are doing SSL offloading, then the Service Group type will be HTTP while the VIP type is SSL. (Since
        traffic between the Load Balancer and members will not be re-encrypted.)</li>
      <li>Members: Specify the IP and port that should be used for each member of the Load Balanced pool. You can add additional optional parameters if necessary</li>
    </ul>
  </ul>
  <li>Select the Monitors tab and add ping and tcp at a minimum. You can add additional Monitors if necessary
    <br />
    <br />The below example shows a Service Group with name "website1_servicegroup", protocol of HTTP, and 5 members of the Load Balanced Pool, 10.10.10.4, 10.10.10.5,&nbsp;10.10.10.6,&nbsp;10.10.10.7,&nbsp;10.10.10.8 all using Port 80.</li>
</ol>
<p><img src="https://t3n.zendesk.com/attachments/token/rmi96fsg1g5cx2x/?name=ServiceGroup1-70.png" alt="ServiceGroup1-70.png" />
</p>

<h3>&nbsp;Create Virtual Servers</h3>

<ol>
  <li>Expand the menu Load Balancing, select Virtual Servers, and click Add.&nbsp;(Version 10.1 and later this is within Traffic Management)</li>
  <li>Input a descriptive name, select the correct protocol, and input the IP address of the VIP. Note: For dedicated Load Balancers the VIP will always be an internal IP. This internal IP can be used internally or over a vpn, or a public NAT
    can be established as well to allow load balancing of an external site.</li>
  <li>Select the Service Groups tab, and locate the Service Group you configured in the previous section "Create Service Group". Mark the checkbox next to the Service Group you wish to apply to this VIP.
    <br /><img src="https://t3n.zendesk.com/attachments/token/ipq8zkbvtqz1fjp/?name=VIP1_70.png" alt="VIP1_70.png" />
    <br />
  </li>
  <li>Select the Method and Persistence tab. Choose the LB Method of your choice, as well as Persistence settings(sticky sessions).&nbsp;</li>
  <li>If you are doing SSL offloading, go to the SSL Settings tab and apply/install the SSL certificate of your choice.</li>
</ol>
<h3>Additional Notes</h3>
<ul>
  <li>In order for the Load Balancer to function correctly , the Management and RNAT IPs need to be able to reach each member of the Service Groups. You can view the RNAT IP by going to Network -&gt; IPs and finding the "Mapped IP". By default,
    all IPs can talk to all other IPs within the same VLAN. However if you begin to add additional networks to your environment, you will need to create Firewall rules via the portal to allow the traffic. You will also need to add a route
    on the Load Balancer. You can do this by going to Network -&gt; Routes -RNAT via the Netscaler UI. Contact the NOC if you need additional help with this.</li>
  <li>When Load Balancing websites, its recommended to setup additional monitors on the Service Group instead of just Ping/TCP. An http-ecv monitor will verify each member of the Service Group is responding correctly before sending traffic to it. You
    can find assistance with this monitor here:&nbsp;http://support.citrix.com/article/CTX120921</li>
</ul>
<h3>&nbsp;</h3>
