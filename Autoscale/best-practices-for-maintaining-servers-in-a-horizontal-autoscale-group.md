{{{
  "title": "Best Practices for Maintaining Servers in a Horizontal Autoscale Group",
  "date": "10-13-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

When using a horizontal Autoscale policy on a group, it is very important to ensure that all the servers within the group are the same, meaning that they are kept in sync from a software and configuration perspective. This is generally true for any group of servers that sit behind a load balancer since traffic can be routed to any of the servers at any time. In the case of servers in a horizontal Autoscale group, it can also be potentially challenging to perform the necessary actions to keep the servers up to date because they may be powered on or off automatically at any time by an autoscale event trigger. This article will discuss some suggested best practices around how to manage servers within a horizontal Autoscale group.</p>

#### Audience

* CenturyLink Cloud customers

#### Prerequisites

* Must be logged into the system
* Must have a group with horizontal Autoscale policy applied

### Using a Staging Area

Since servers in a horizontal Autoscale group can be automatically powered on and off due to an autoscale event occurring, you will see in the scenarios below that it can be helpful to have a staging area to keep servers in temporarily in order to keep them out of a horizontal autoscale group so you may perform actions on them or get them ready to add to the autoscale group without risk of them being powered off. Though you may also choose to use maintenance mode to achieve similar results in certain cases, having a staging area group is still recommended practice so you have complete control over which servers are part of the autoscale group and when.

You can create a staging group anywhere, but the best place is as a nested group right underneath the horizontal autoscale group itself. The autoscale policy will only affect servers that live directly under the group on which the policy has been applied, so any servers under a group that is within the autoscale policy group are unaffected. This makes it a great place to create a group to act as a safe staging area but is still closely related to the autoscale group.

#### Adding New Servers to Group

If you would like to increase the number of available servers that can be powered on for autoscaling out, you just need to add servers to the horizontal autoscale group. As indicated above, though, you want to make sure that they have the same configuration as the other servers that already exist in the group. Instead of creating servers from scratch and manually updating them with the necessary software and configuration, there are two recommended approaches:


* **Cloning.** You may wish to keep a server in the staging area that has all the software and configurations you need for all servers in your autoscale group. When you want to add new servers to the autoscale group, just clone this server and put the new server in the autoscale group. The benefit here is that you can use this source server in the staging area when performing any changes so you only need to apply updates to a single server, as described in the next section. (Learn more about [how to clone servers](../Servers/how-to-clone-a-virtual-machine-os-instance.md).)
* **Template.** Instead of keeping a powered-on server in the staging area, you may choose to convert it to a template so that you can create servers using this custom template instead of one of the pre-configured OS ones. In this case, you will not have to keep a server in the staging area, but if you want to make changes to the template, you'll have to first convert it back to a server, perform your changes, and then convert it back to a template. (Learn more about [how to create os templates](../Servers/how-to-create-customer-specific-os-templates.md))


#### Updating Software/Configuration on Existing Servers in Group

Depending on the kind of update(s) required, there are two options for updating servers in a horizontal autoscale group:

**Replace existing servers with new updated servers.**

This is the preferred method for updating servers in a horizontal autoscale group. Follow the steps above for "Adding New Servers to Group" in order to create new servers, and use these to replace the existing ones in the group.

1. Create new servers in your staging area group as previously described. You may use either the clone or template method as detailed above, whichever you prefer. If you want to keep the same number of servers as you currently have in the horizontal
      autoscale group, make sure to create that many servers in the staging group.
2. Now you must replace the existing servers with the new ones and update the load balancer configuration accordingly. The order in which you do this will require you to consider your application's tolerance for non-uniform code in the web cluster behind the load balancer.

  * If you can have some mismatched servers for a short period of time, you can move all the new servers into the group, wait for the load balancer to update within five minutes, then remove all the old servers from the group.
  * If, however, your workload cannot tolerate any variances between the servers behind the load balancers, you will want to take a more active role in bringing the new servers into the pool and retiring the old ones. To ensure uniformity across servers at all times while still avoiding interruptions, you will want to manually update the load balancer pool yourself to include only the IP addresses for the new servers while removing all addresses for the old ones.

**Update servers in place.**

This method is generally not preferred unless you have a small number of servers in a group, the updates to be made are relatively minor (small changes, easily repeatable, fast-running), and/or if you absolutely must maintain the private IP addresses for the servers. If you choose this method, be sure to read about using Blueprints scripts for [Automated Application Deployment to Multiple Servers](../Blueprints/automated-application-deployment-to-multiple-servers.md) as one approach for an easy, repeatable, and automated process.

1. Put server in maintenance mode. This step prevents the server from being powered off by a scale in event while you are patching it. (Alternatively, you could also move the server into a staging area group.)
2. Remove server IP from load balancer pool. (This will happen automatically within five minutes after completing step 1, but if you can't wait that long, you may remove it manually.)
3. Update/patch the server as required (and restart if needed). (See [Automated Application Deployment to Multiple Servers](../Blueprints/automated-application-deployment-to-multiple-servers.md) for one approach to scripting this process.)
4. Take server out of maintenance mode to re-enable being powered off/on by autoscale events. (Alternatively, you could move the server back in to the autoscale group from a staging area group if that's the method that was used.)
5. Add server IP back to load balancer pool. (This will happen automatically within five minutes after completing step 4, but if you can't wait that long, you may add it manually.)
6. Repeat first five steps for each server in the group. </li>

#### Removing Servers from Group

Removing servers from a horizontal autoscale group should require no additional action other than a regular delete server. The load balancer will not route traffic to that IP address anymore as it will be unreachable, and within five minutes, the load balancer pool should be updated to remove the address altogether.

One thing to note here, though, is that the platform will not prevent you from deleting so many servers from the autoscale group that you are left with less than then minimum number of servers you've defined in the autoscale policy. In this case, the policy will ensure that all servers in the group are powered on, but will not <em>create</em> any additional servers. You will see a warning if you actively go to the group settings where the horizontal autoscale policy is applied, but no notifications will be sent or otherwise displayed.
