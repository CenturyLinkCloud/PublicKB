{{{
  "title": "Creating Bi-Directional Firewall Policies",
  "date": "10-26-2021",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>Lumen Cloud Platform firewall policies make it simple to connect networks within a given account or across accounts. Firewall policies are inherently one-way, but it is very straightforward to craft a pair of policies that enable bi-directional communication.
  This walkthrough builds upon the servers, networks and policies built in the KB article entitled <a href="connecting-data-center-networks-through-firewall-policies.md">Connecting Data Center Networks Through Firewall Policies</a>.</p>
<p><strong>Steps:</strong>
</p>
<p><strong>1. Confirm that you have two servers in two different networks.</strong>
</p>
<ul>
  <li>In the KB article reference above, there was a parent account and a sub-account, and a network and server in each. The two servers operate on different networks.
  </li>
</ul>
<p><strong>2. Build a pair of policies that enable network communication in both directions.</strong>
</p>
<ul>
  <li>Check the existing firewall policies by navigating to&nbsp;the <strong>Firewall</strong>&nbsp;menu item under the <strong>Network </strong>menu. From the previous KB article walkthrough, there should be a single firewall policy that makes it possible
    for the server in the parent account's network to ping a server in the sub-account's network.
  </li>
  <li>This traffic is one-way only. To confirm this, attempt to ping the server in the parent account from the server in the sub-account. Notice that the request times out because network traffic is not allowed from the child network to the parent.
   
  <li>In order to allow servers in the sub-account's network to communicate with servers in the parent account's network, another firewall policy must be created.</li>
  <li>Switch the <strong>Source Account </strong>and <strong>Destination Account </strong>values at the top of the page to reflect the sub-account as the source and parent account as the destination.
   
  <li>Click the <strong>add policy </strong>button and add a firewall policy that allows traffic from (restricted) IP addresses in the sub-account network to (restricted) IP addresses in the parent account network.
   
  <li>Save the firewall policy.</li>
</ul>
<p><strong>3. Confirm that the policies are working.</strong>
</p>
<ul>
  <li>From the server in the sub-account's network, once again attempt to ping the server in the parent account's network.
  </li>
  <li>As expected, the traffic is now configured to travel in both directions between the networks. So in order to create bi-directional network communication, create two firewall policies overall.</li>
</ul>
