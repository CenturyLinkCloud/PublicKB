{{{
  "title": "Autoscale Tips and Tricks",
  "date": "10-13-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

<p><strong>Using Vertical and Horizontal Autoscale Together</strong></p>
<p>Although it is not generally recommended to use vertical and horizontal Autoscale in conjunction with each other as it could result in some unpredictable behavior, if users are thoughtful about how they set both policies up, it is possible to use them
  together in a constructive way.</p>
<p><strong>Different Autoscale Methods Per Application Tier</strong>
</p>
<p>One of the nicest things about having both horizontal and vertical options is that some workloads scale out better (horizontal), while others scale up easier (vertical). For example, a user may have a single instance database that will not be helped by
  adding additional servers behind a load balancer. All the data for the database in this situation lives on the single server and scaling out horizontally is not an option. Even if the database has multiple server configurations, each server will
  likely require a lot of resources allocated. For the database tier of this application, users may want to configure a vertical autoscale policy to add capacity as load increases, and scale back down when load levels drop.</p>
<p>Servers in the web tier of the same application, though, are probably better scaled by having additional servers behind a load balancer, so it would make more sense to apply a horizontal autoscale policy to this group of web servers. (Make sure to leave
  servers that should not be horizontally autoscaled out of the group that the policy is applied to.)</p>
<p><strong>Vertical Autoscale Within a Horizontal Autoscale Group</strong>
</p>
<p>It is technically possible to apply vertical autoscaling policies to servers within a horizontal autoscale group. In some cases this may result in unpredictable or undesired behavior (such as horizontally autoscaling down by powering off a server that
  at the same time is vertically autoscaling up). However, there may be legitimate cases for setting up a horizontal autoscale group with vertical autoscale servers in it. If, for example, there is one server in the group that is getting pegged, it may
  not bring the average utilization within the group high enough to warrant a scale <em>out</em> event. However, it may still be appropriate to scale <em>up</em> the resources on that single server.</p>
<p>In another case, users may choose to set a low threshold time for the vertical autoscale policy (say 5 minutes) and a longer threshold time (say 15 minutes) for the horizontal autoscale policy in an attempt to scale up problematic servers first before
  scaling out. In this example, consider different cool down times as well as part of both vertical and horizontal scaling evaluation.</p>
<p><strong>Using Horizontal Autoscale to Maintain Minimum Server Count</p></strong>
<p>One nice effect of using a horizontal autoscale policy with a group is that users can set a minimum number of servers to stay on within the group. Even if users are not interested in autoscaling up very much (or at all), they can use a horizontal autoscale
  policy to ensure that at least a certain number of servers are always kept on within the group. For example, if a user wanted to keep all four servers in the group powered on at all times, they could create a horizontal autoscale policy that has a minimum
  server number set to four, and apply that policy to the group. With only four servers in the group, the policy would never be able to scale up, but if any of the servers were powered off for any reason, the autoscale policy would take care of powering
  them back on automatically.</p>
<strong>Using Horizontal Autoscale Without a Load Balancer</strong>
<p>Though horizontal autoscale may most often be used in conjunction with a load balancer, it is <em>not</em> <em>required</em> to select a load balancer group when applying a horizontal autoscale policy. Users have the option of selecting "None" instead
  of choosing a load balancer to associate with the group. This can be useful in cases where the servers act as distributed worker nodes, asynchronously responding to messages in a queue or actively polling for new files or database records. In a
  case like this, it still makes sense to autoscale the worker nodes horizontally, but there is no need to choose a load balancer to associate with the policy, allowing the group to just expand or contract the number of running servers without worrying
  about routing traffic to them.</p>
<p>
  <a name="dedicated"></a>
</p>
<strong>Using Horizontal Autoscale With a Dedicated Load Balancer</strong>
<p>When selecting a load balancer group to use with horizontal autoscale, the Control Portal will make use of the CenturyLink Cloud's self-service shared load balancer configuration in conjunction with the autoscale policy. However, if you wish to use a
  dedicated load balancer instead, horizontal autoscale policies will support this as well, but the load balancer configuration must be set up separately. Once you have a dedicated Netscaler load balancer in your environment, you can follow these steps
  to configure a horizontal autoscale policy with the dedicated load balancer:</p>


1. Create a horizontal autoscale policy.
2. Associate the policy to the group that has the servers you wish to autoscale. Select "none" for the Load Balancer option so it will not be associated with any shared load balancer configuration.
3. Take note of the IP address for every server in the horizontal autoscale group, whether it is powered on or off.
4. Login to the dedicated load balancer's web-based management page and follow the instructions for [Dedicated Load Balancer Basic Management](../Network/dedicated-load-balancer-basic-management.md) to add each of the server's IP addresses to the configuration.
5. As long as you have "ping" and "tcp" monitors setup as described in the management article, no traffic will be routed to servers that are powered off. When the group scales out and powers on a server, traffic will begin routing to it from the load balancer until the server is powered off after a scale in event. (You may wish to set up additional monitors as well to ensure that a specific application or port is available before routing traffic to the server.)

If you remove or add servers to the group, you will need to make sure to manually remove or add their IP addresses to the dedicated load balancer configuration to keep them in sync with the horizontal autoscale group as Control will not take care of this like it would with the shared load balancer.</p>

You can also read more about [Load Balancing Comparison](../Network/load-balancing-comparison-matrix.md) to see the difference between the two load balancer types and find links to resources about configuring them.

#### Schedule-Based Horizontal Autoscale

Horizontal autoscale policies are configured to be triggered using utilization thresholds for both memory and CPU. There may be cases, however, where rather than scaling in or out due to usage, users would like to scale in or out on a schedule based on knowledge of an application's usage patterns. For example, maybe the servers are hosting a timesheet system that is overwhelmed twice a month by employees entering the hours they've worked. Rather than deploying more resources than are needed for non-peak usage or dealing with bimonthly slow performance, users can create scheduled tasks to power on servers at a specific point each day/week/month to increase application capacity, and then use another schedule task to power servers back down when the predictable spike is over. This sort of elasticity is exactly what the cloud is good at and it helps you deliver an optimized application that delights users while keeping costs down. You can read more about [Scheduled Tasks](../Servers/creating-a-scheduled-task.md).
