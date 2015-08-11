{{{
  "title": "Autoscale FAQ",
  "date": "12-22-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

CenturyLink Cloud supports both vertical and horizontal autoscale policies that allow for the automatic scaling of resources based on user-defined thresholds. Based on these thresholds, vertical autoscale policies will add and remove CPU allocation to and from a given server, whereas horizontal autoscale policies power on and off instances within a (load balanced) group of servers.

This FAQ addresses commonly asked questions about the service. For a walkthrough of this service, see the [Creating and Applying Autoscale Policies](creating-and-applying-autoscale-policies.md).

### General

**Why would I assign Autoscale policies to a server?**

Autoscale makes it possible for a server or group of servers to self-regulate and only have the capacity it needs at any given time, based on real-world usage. This saves you money while reducing administrative overhead. Instead of having a system administrator closely monitor and scale servers based on an increase or decrease in utilization, you can create policies that add or remove capacity automatically. This ensures that you don't have CPUs allocated or additional servers powered on (costing you money!) unless you need them.

**What's the difference between horizontal and vertical Autoscale policies?**

Vertical autoscaling (scaling up/down) adds (or removes) CPUs to (or from) an existing server based on the policy thresholds set. This policy gets applied on a server by server basis. See details below on when servers are scaled up or down for moreinformation on what triggers a vertical autoscale event. Horizontal autoscaling (scaling out/in) powers on (or off) servers within a group and adds (or removes) them from the load balancer configuration based on the thresholds set in the policy. This policy is applied at the group level and will affect every server within the group. See details below on when servers are scaled out or in for more information on what triggers a horizontal autoscale event.

**When should I use horizontal Autoscale vs. vertical Autoscale?**

Many enterprise workloads can see an increase in performance just by adding capacity to existing servers without the need for additional servers. This is often the case if the workload is purely CPU-constrained and not I/O bound. For these types of workloads, vertical autoscale may prove to be enough. If you find that your workload has very large spikes that require bigger bursts than vertical Autoscale may be able to provide, horizontal Autoscale is definitely a powerful option as well. You can always start out using vertical Autoscale, and later change to using a horizontal Autoscale policy instead if you determine that it isn't enough for you. Or, if you know your workload causes your servers to become I/O bound, you may want to use horizontal Autoscale from the start. Also, horizontal Autoscale relies on load balancers to scale the workload. If you have a workload that doesn't scale out well this way (i.e. database servers), vertical Autoscale is the better bet. Conversely, the web tier is a great candidate for horizontal Autoscale as it scales out behind a load balancer well.

**Can I use both vertical and horizontal Autoscale on the same server(s)?**

Though it is not explicitly disabled by the platform, it is not recommended that you use both options in conjunction with each other (i.e. servers with vertical Autoscale policies inside a server group with a horizontal autoscale policy). While this case should not cause anything to break, it can result in unpredictable behavior. (In one case, for example, if a horizontal Autoscale policy scales down it may turn off a server that had a vertical Autoscale policy configured on it.)

**What Operating Systems support Autoscale?**

Vertical Autoscale can be applied to any server type that supports a "hot add" of CPU resources without a reboot. Those OSes include: Windows Server 2012 Datacenter Edition, Red Hat Enterprise Linux 5/6/7 x64, and Ubuntu 10/12/14 x64. Horizontal Autoscale is applied at the group level and will work with any server types within that group.

**How often are you sampling the virtual machine for utilization data points?**

While the minimum threshold period for an Autoscale policy is 5 minutes, the CenturyLink Cloud platform collects data points far more frequently for each server. In fact, each 5 minute threshold period contains hundreds of data points. This ensures that your server scales because of an overall utilization trend, not just an isolated spike in utilization over a few seconds.

**How soon do changes to Autoscale policies take effect on any servers that use it?**

A policy takes effect instantly.

----------

### Vertical Autoscale

**When does a server scale up?**

A server scales up when its utilization meets or exceeds the user-defined threshold for a user-defined period of time. Let's consider an example. If you create a policy with a 85% utilization threshold and a threshold period of 10 minutes, this means that if the server has at least 85% utilization for a 10 minute period, then an autoscale event will occur and capacity will be immediately added. Currently, vertical Autoscale policy thresholds can only be defined for CPU utilization.

**When does a server scale down?**

Scaling down resources requires a server reboot. Thus, this requires more careful configuration than a scale up event. The customer creates a "scale down window" in UTC time that determines when it's safe for a server to reboot. Then, if the server goes below a minimum usage threshold for as long as the threshold period - and this occurs during a scale down window - the server will be rebooted and capacity removed. If a server is at a minimum usage for a threshold period but outside the scale down window, then no scale event occurs. This design prevents a server from going offline during busy periods. Currently, vertical Autoscale policy thresholds can only be defined for CPU utilization.

**Can I still manually change CPU allocation after assigning a vertical Autoscale policy?**

No, the point of adding a vertical Autoscale policy is to eliminate the need for manual CPU sizing. If you absolutely must change the CPU allocation to a fixed amount, simply remove the vertical Autoscale policy from the server and set the CPU to the desired value.

**Why don't you let me select "scale down increments" like you do for scaling up?**

When a scale down event occurs, we scale back to the minimum number of CPUs specified in the policy. Scale down occurs during periods of idleness, and thus it makes sense to jump down to the smallest allocation possible. This saves you money and still makes it easy to step up if utilization increases.

**Does the vertical Autoscale action cause my server to reboot?**

Only in two cases. First, if this is the first time you are applying a vertical Autoscale policy to a server, and it hasn't already been configured to support a "hot add" of resources, then a reboot is required. A warning appears when applying the Autoscale policy if this reboot is necessary. Secondly, a reboot is required when removing capacity from a server during a scale down event.

**How come I see a notice on my server that says it has to be rebooted one time before capacity can be added without a reboot the next time?**

While certain Operating Systems support the addition of capacity without  a reboot, the hypervisor must be configured to recognize this. During the initial reboot of a server, the CenturyLink Cloud management platform configures that server to accept additional capacity (CPU or RAM) without requiring a reboot. This is a one-time event in the life of a server.

----------

### Horizontal Autoscale

**When does a server group scale out?**

A server group will scale out when the overall average utilization of the servers within the group meets or exceeds the user-defined threshold for a user-defined period of time. Let's consider an example. If you create a policy with a 85% utilization threshold and a threshold period of 10 minutes, this means that if the server group has at least 85% utilization for a 10 minute period, then an autoscale event will occur and the number of incremental additional servers that was specified will be powered on and added to the load balancer configuration. Horizontal Autoscale policy thresholds can be defined based on a combination of CPU and/or memory utilization.

**When does a server group scale in?**

A server group will scale in when the overall average utilization of the servers within the group drops below the user-defined threshold for a user-defined period of time. Let's consider an example. If you create a policy with a 25% utilization threshold and a threshold period of 10 minutes, this means that if the server group has less than 25% utilization for a 10 minute period, then an autoscale event will occur and the number of decremental servers that was specified will be powered off and removed from the load balancer configuration. Horizontal Autoscale policy thresholds can be defined based on a combination of CPU and/or memory utilization.

**How frequently is the load balancer configuration updated with new or deleted servers?**

The load balancer pool tied to a horizontal Autoscale policy is synced to the servers in the associated group every five minutes, meaning that every five minutes the pool will be cleaned up to purge any servers that were deleted and add any new servers that were added. This is purely a housekeeping task, however, as the load balancer will not route traffic to servers that don't exist or are powered off. See the article on how to maintain servers in a horizontal Autoscale group for more information on best practices for adding or removing servers from the group.

**Why doesn't horizontal Autoscale support provisioning and deprovisioning servers instead of just powering on and off existing ones?**

We are always continuing to explore options for how to improve features and increase performance. At this time, powering on and off servers is the most efficient way for the CenturyLink Cloud platform to scale in and out based on utilization thresholds.

**Do all the servers in my horizontal Autoscale group have to be identically configured?**

Yes, it is up to you to manage the servers within the horizontal Autoscale group and make sure that they are kept up to date and in sync with each other. It is recommended that you use a subgroup underneath the Autoscale group to refresh servers before moving them back in. See the article on how to best maintain servers in a horizontal Autoscale group for more information on this topic.

**How does a horizontal Autoscale policy determine which server(s) to power on (or off) first when an Autoscale event is triggered?**

Servers will be turned off and on based on the name of the server. This is one reason why it is very important to ensure that all servers in the group are identical as mentioned above.

**What's the best way to add or remove servers from my horizontal Autoscale group?**

See the article on how to best maintain servers in a horizontal Autoscale group for more information on this topic.

**Is there a way to trigger an Autoscale event manually so that I can control specifically when servers are powered on (or off)**?
While the Control Portal does not allow you to set scheduled times for autoscaling, you do have some options for controlling the power operations of the server outside the context of the defined Autoscale policy. You can always use the Control Portal to manually power on and off any servers in the group that you'd like. You may also wish to use the API to [power on](http://www.ctl.io/api-docs/v2#power-operations-power-on-server) and [power off](http://www.ctl.io/api-docs/v2#power-operations-power-off-server) the servers if, for example, you have a separate monitoring process that can detect load as well. Additionally, you could also use [Scheduled Tasks](../Servers/creating-a-scheduled-task.md) (on a server by server level) to turn servers on or off at a specific time when you know load is high or low, potentially scaling ahead of the Autoscale events. (In all of these cases, it is important to note that these servers may be powered off or on after being manually started or stopped due to an Autoscale event triggering.)

**What happens if I want to remove a horizontal Autoscale policy from my group?**

You are free to remove the policy at any time. What will happen is that everything stays in place (server power state, load balancer configuration), but the system no longer applies scaling rules based on aggregate usage.

**Can I use an existing load balancer pool for my group's horizontal Autoscale configuration?**

Yes. However, the service will remove any server from the load balancer that is not part of the group associated with the policy. Only choose this option if you wish to apply a horizontal Autoscale policy to a group of servers that is already set up
  in the chosen load balancer pool!

**What happens if I set the load balancer option to "None" on a Autoscale policy that's applied to a group?**

If you choose to remove the load balancer from a group's horizontal Autoscale policy, then the system will remove all the servers from that load balancer pool. The servers will remain in their current power state and will continue to scale in and out based on aggregate usage. In this scenario, a scale event will NOT be accompanied by any changes to a load balancer.

**May I create managed servers in my horizontal Autoscale group?**

Yes, managed servers may be included in a horizontal Autoscale group.

**Do I have to use the load balancer as part of my horizontal Autoscale group?**

No. When applying a horizontal Autoscale policy to a group, you have the option to not select a load balancer. This scenario is a fit for "worker nodes" that pull data from a source and may scale out when the amount of work is too much for the available servers. In this case, a load balancer is not needed as each worker node pulls available work.

**Do I have to pay for servers in my horizontal Autoscale group even when they are powered off and not in use?**

You will not be charged for CPU and memory usage when the server is powered off, however you will pay for the storage attached to these servers and any software licensing costs associated with them. (Also for managed servers, the management fee will still apply even for powered off servers.)

**Can I use horizontal Autoscale policies to add servers to application clusters (i.e. caching or database clusters)?**

Currently, horizontal Autoscale leverages the use of a network load balancer to spread the load across the servers. This is ideal primarily for web-enabled applications or other types of workloads that can utilize network-based load balancing as opposed to configuration-based server clusters.
