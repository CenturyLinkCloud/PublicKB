{{{
  "title": "Load Balancer Configuration Files and Control Portal Mapping",
  "date": "11-4-2013",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<div>CenturyLink Cloud’s self-service Load Balancer provides an intuitive interface for the management and provisioning of Load Balancer groups and policies. In migrating from the previous version of our shared Load Balancer, you may find yourself presented with a configuration
  file detailing the specifics of your deployment- translating these items may require some assistance, the aim of this article is to map the most common configuration items to the Control Portal policies and detail where they diverge.&nbsp;</div>
<div></div>
<div>The typical config file looks like this:</div>
<div></div>
<div>TIER3_DEMO_80&nbsp;</div>
<div>VIP: 129.40.168.230 &nbsp;</div>
<div>Port: 80&nbsp;</div>
<div>Protocol: HTTP&nbsp;</div>
<div>Method: Least Connection&nbsp;</div>
<div>Persistence: SOURCEIP&nbsp;</div>
<div>Time out: 2 MIN&nbsp;</div>
<div>Service Group Members&nbsp;</div>
<div>10.81.194.35 port 80&nbsp;</div>
<div>10.81.194.36 port 80&nbsp;</div>
<div>Monitors: PING,TCP</div>
<div></div>
<div>To create a new Load Balancer policy, select “Load Balancer” under the “Services” menu bar, after which a list of the load balancer policies will be displayed.&nbsp;</div>
<div></div>
<div><img src="https://t3n.zendesk.com/attachments/token/30aejxwn4en847e/?name=LB1.JPG" alt="LB1.JPG" />
</div>
<div></div>
<div>Select “Create Load Balancer Group” to create a new policy and VIP.</div>
<div></div>
<div><img src="https://t3n.zendesk.com/attachments/token/get2eswxppyhd5l/?name=LB2.JPG" alt="LB2.JPG" />
</div>
<div></div>
<div>A prompt will appear wherein the name and description for the Load Balancer can be specified, in this instance “TIER3_DEMO_80” will be used for the policy name. The VIP (Virtual IP Address) will be automatically assigned and as such the previously assigned
  VIP address can be ignored. By clicking the “gear” icon <img src="https://t3n.zendesk.com/attachments/token/s6tqwsbj2zt961q/?name=LB3.JPG" alt="LB3.JPG" />&nbsp;and then “Add Pool”, servers can be added to the pool and the policy items specified.&nbsp;</div>
<div></div>
<div><img src="https://t3n.zendesk.com/attachments/token/gwd0xdcdzkizvm5/?name=LB3.5.JPG" alt="LB3.5.JPG" />
</div>
<div><img src="https://t3n.zendesk.com/attachments/token/2r78beh6qira9d2/?name=LB3.5.JPG" alt="LB3.5.JPG" />
</div>
<div></div>
<div>In translating the configuration file contents, the port and protocol fields map to the “Virtual IP Port” in the pool config (currently, the self-service Load Balancer policies only support HTTP/80 and HTTPS/443, future release will bring custom port
  support, along with full feature parity with the NetScaler devices).&nbsp;</div>
<div>The “Method” field currently supports the options of “Least Connection” or “Round Robin”. “Least Connection” routes traffic to the server that is least utilized, or has the fewest active connections, while “Round Robin” distributes traffic in an orderly
  fashion amongst all servers, without taking into consideration server load or latency. In this instance, as we are simply migrating a configuration from the shared load balancer to the self-service instance, we simply choose the option that was previously
  being utilized.</div>
<div></div>
<div><img src="https://t3n.zendesk.com/attachments/token/paymvh3ayiixclz/?name=LB4.png" alt="LB4.png" />
</div>
<div></div>
<div>Next, we will select the Load Balancer persistence type. The choices include "standard" or "sticky" (SOURCEIP). The standard option employs no persistence and is best for stateless web applications. If an application does require server-based state, then
  choose the sticky option. The sticky choice uses source IP and destination IP address-based persistence to tie requesters to the target server. How does the load balancer method and persistence work together? If we choose round robin or least connection
  along with standard persistence, then requests are routed without any concern for where the last user's request came from. If we choose round robin or least connection along with sticky persistence, then the first request will be routed based on either
  round robin or least connection, and each subsequent request from that source IP address will return to the server that responded to the initial request.</div>
<div></div>
<div><img src="https://t3n.zendesk.com/attachments/token/oaptn1qa8vopf2g/?name=LB5.png" alt="LB5.png" />
</div>
<div></div>
<div>Next, we add the IP addresses for the servers participating in the Load Balancer pool- in this instance, we will simply enter the IP addresses as they are listed in the configuration file.</div>
<div></div>
<div>Monitors and health checks are currently not user-configurable in the shared Load Balancer setup, this article will be amended to explain the available options when released. Should there be any further questions around Load Balancer configuration, please
  contact the CenturyLink Cloud support team.</div>
<div></div>