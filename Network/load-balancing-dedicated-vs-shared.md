{{{
  "title": "Load Balancing - Dedicated vs Shared",
  "date": "8-6-2013",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<div>
  <ul>
    <li>Shared Load Balancers are now <a href="creating-a-self-service-load-balancing-configuration.md">configurable in a self-service fashion</a>.</li>
    <li>Customers can log in directly to their Dedicated Load Balancers.</li>
    <li>With the Shared Load Balancers the External IP sits directly on the Load Balancer.</li>
    <li>With a Dedicated Load Balancer the VIP is an internal IP. In order to provide external access a MIP/NAT must be added to the firewall which points to the internal VIP.</li>
    <li>If a customer wants to use a Load Balancer to access an internal VIP over their site to site VPN they must use a dedicated Load Balancer. It is not possible to access an internal VIP on the the Shared Load Balancer over a site to site VPN.</li>
    <li>All shared Load Balancers are in a High Availability pair. If either node goes down there will be no downtime. Dedicated Load Balancers can be put in a HA pair by request.</li>
    <li>MIP's are not accessible from within the datacenter. If you need to reach a public IP from both inside and outside the datacenter, you need to use the Shared Load Balancer.</li>
  </ul>
</div>

<p><strong>Definitions in regards to this article</strong>:
  <br />VIP - The IP used for the Virtual Server. A VIP includes both an IP and a port. Separate VIP's are required for multiple ports used with the same IP.
  <br />Internal VIP - A VIP on a dedicated Load Balancer. This will always be an internal IP
  <br />External VIP - A VIP on a shared Load Balancer. This will always be an external IP and is accessible from outside of the datacenter or within
  <br />MIP/NAT - A one to one IP translation. In regards to this article, it is a Public IP that points to an Internal IP. Example: 66.150.99.235 -&gt; 10.90.250.250</p>
