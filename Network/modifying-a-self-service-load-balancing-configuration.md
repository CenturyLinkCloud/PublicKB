{{{
  "title": "Modifying a Self-Service Load Balancing Configuration",
  "date": "8-6-2013",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>In order to build highly available web applications, Tier 3 customers can use a load balancer. While customers are free to set up a dedicated load balancer with the help of the Tier 3 NOC, customers can also use a shared load balancer that is managed
  through the Tier 3 Control Portal. In this KB article, we walk through the shared load balancer and how to modify a pool of servers.</p>
<h3>Audience</h3>
<ul>
  <li>Tier 3 customers (Application developers, system administrators)</li>
</ul>
<h3>Prerequisites</h3>
<ul>
  <li>Must have Account Administrator permissions on the platform</li>
</ul>
<h3>Detailed Steps</h3>
<ol>
  <li>Navigate to the load balancer service via the "Load Balancer" item in the "Services" menu. This overview page shows each load balancer configuration including its name, description, VIP and ports.
    <br /><img src="https://t3n.zendesk.com/attachments/token/vxmg3rwhhahhdcb/?name=loadbalancer-update01.png" alt="loadbalancer-update01.png" />
  </li>
  <li>Click the row of the load balancer that you wish to configure. From the subsequent page, you can turn the entire configuration "on" or "off", view the activity history, see the billing summary, and delete the entire configuration.
    <br /><img src="https://t3n.zendesk.com/attachments/token/bixxcykzsdnltcw/?name=loadbalancer-update02.png" alt="loadbalancer-update02.png" />
  </li>
  <li>Switch to the "Settings" tab where you can view pool information and change values.
    <br /><img src="https://t3n.zendesk.com/attachments/token/chjjce0iddquzxc/?name=loadbalancer-update03.png" alt="loadbalancer-update03.png" />
  </li>
  <li>Click the row containing the pool that you wish to change. This initates "edit mode" and allows you to change VIP ports, routing method, persistence strategy, and number/status of servers in the pool.
    <br /><img src="https://t3n.zendesk.com/attachments/token/bf3wnzkzynlna9m/?name=loadbalancer-update04.png" alt="loadbalancer-update04.png" />
  </li>
  <li>Switch the persistence method to "sticky" to see how this affects the load balancer configuration.
    <br /><img src="https://t3n.zendesk.com/attachments/token/kh0iaal8cavkaj6/?name=loadbalancer-update05.png" alt="loadbalancer-update05.png" />
  </li>
  <li>Save the settings and view a multi-server web application in the browser. In the example below, notice that each browser request goes to the same server because sticky persistence was selected.
    <br /><img src="https://t3n.zendesk.com/attachments/token/2a7sde6iv9ulflg/?name=loadbalancer-update06.gif" alt="loadbalancer-update06.gif" />
  </li>
  <li>Return to the load balancer configuration and switch back to "standard" persistence. Also disable one of the servers which takes it out of rotation by the load balancer. As a result, all traffic will still be sent to a single server, but not because
    of persistence settings but because there is only a single active server.
    <br /><img src="https://t3n.zendesk.com/attachments/token/mvblm13ui4s0ag8/?name=loadbalancer-update07.png" alt="loadbalancer-update07.png" />
  </li>
  <li>Open up the web browser and see that all requests go to a single server. Note that if you kept sticky sessions and took the server out of rotation, then any existing persistent connections would&nbsp;<strong>continue to be routed</strong> to the disabled
    server. No&nbsp;<strong>new&nbsp;</strong>traffic would be routed to that server, but it would still respond to requests from existing connections.
    <br /><img src="https://t3n.zendesk.com/attachments/token/lhgpltutp59nu8x/?name=loadbalancer-update08.gif" alt="loadbalancer-update08.gif" />
  </li>
  <li>Re-enable the disabled server and immediately see that browsing the VIP results in both servers responding to requests.
    <br /><img src="https://t3n.zendesk.com/attachments/token/t51q2faqwi163mn/?name=loadbalancer-update09.png" alt="loadbalancer-update09.png" />
  </li>
</ol>