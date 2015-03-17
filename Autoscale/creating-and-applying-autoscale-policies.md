{{{
  "title": "Creating and Applying Autoscale Policies",
  "date": "12-22-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description</strong></p>
<p>The CenturyLink Cloud platform now supports both&nbsp;<a href="#vertical">vertical Autoscale</a>&nbsp;of CPU capacity for servers as well as&nbsp;<a href="#horizontal">horizontal Autoscale</a>&nbsp;of servers. This makes it possible to scale servers up
  and down (vertical) or out and in (horizontal) based on utilization, ensuring optimal deployment of resources for cloud environments under a variety of conditions. How does Autoscale work? For vertical Autoscale, servers that exceed a user-defined CPU
  utilization threshold will instantly scale up, and servers that go below a user-defined CPU utilization threshold will scale down (and reboot) during a user-defined window. In the case of horizontal Autoscale, groups of servers that exceed a user-defined
  CPU/RAM utilization threshold will scale out by powering on one or more additional servers in the group, and groups of servers that go below a user-defined CPU/RAM utilization threshold will scale in by powering off one or more servers in the group.</p>
<p>For example, consider a vertical Autoscale policy that sets a range of 4 to 6 CPUs for a server. The server is set to scale up by 2 CPUs if the server is running at 90% utilization for longer than 15 minutes. If the server is at 15% CPU utilization for
  longer than 15 minutes, then the policy will scale the server down IF this event occurs during the user-defined scale down window. (A similar story would apply for horizontal Autoscale using number of servers instead of number of CPUs.)</p>
<p><img src="https://t3n.zendesk.com/attachments/token/xjic66bscl4hjrt/?name=autoscale-cpu02.png" alt="autoscale-cpu02.png" />
</p>
<p>This KB article describes all of the steps for creating, applying, and testing both vertical and horizontal Autoscale policies.</p>
<p><strong>Audience</strong></p>
<ul>
  <li>CenturyLink Cloud customers (operations staff)</li>
</ul>
<p><strong>Prerequisites</strong></p>
<ul>
  <li>Must be logged into the system</li>
  <li>Must have a running server to apply an Autoscale policy to</li>
</ul>
<p>
  <a name="vertical"></a>
</p>
<p><strong>Vertical Autoscale</strong></p>
<h3>Detailed Steps</h3>
<ol>
  <li>Navigate to the&nbsp;<strong>Servers</strong>&nbsp;menu item and choose&nbsp;<strong>Policies</strong>&nbsp;from the menu. This takes you to the page where you can create and manage new policies that can later be applied to servers.
    <br /><img src="https://t3n.zendesk.com/attachments/token/NpjrhxhaizUyBxI8cWcBHgiyG/?name=policies-menu.png" alt="policies-menu.png" />
  </li>
  <li>On the left side of the screen you will see a number of policy types that you are able to define. Click&nbsp;<strong>Vertical Autoscale&nbsp;</strong>to be directed to the page where you can manage all vertical Autoscale policies.
    <br /><img src="https://t3n.zendesk.com/attachments/token/v6OEf9m3vNBKBDiP3YyRyi0Fm/?name=policies-page-menu.png" alt="policies-page-menu.png" />
  </li>
  <li>This page shows all the existing vertical Autoscale policies, the details of each, and which servers have been assigned to them. Click the&nbsp;<strong>Create Autoscale Policy&nbsp;</strong>button.
    <br /><img src="https://t3n.zendesk.com/attachments/token/0D66TIuBWwwsZtug91IfqgIpx/?name=autoscale-policy-page.png" alt="autoscale-policy-page.png" />
  </li>
  <li>Define the general policy characteristics. Provide a friendly name for the policy. Choose the&nbsp;<strong>CPU Range</strong>&nbsp;which defines the allowable minimum and maximum number of CPUs for the server attached to the policy. Specify a range
    that makes sense for the type of servers you plan to use with this policy. This range will be used for each server that the policy is applied to. (So if you have three servers each using the same policy, they will each have the capability to utilize
    the maximum number of CPUs.) Next, set the&nbsp;<strong>Threshold Period&nbsp;</strong>(5 minutes, 10 minutes, 15 minutes, 30 minutes) which defines how long a server must be at the minimum or maximum usage before an Autoscale action occurs. If a
    server is likely to have temporary spikes that don't warrant a scaling event, choose a longer period. Identify the&nbsp;<strong>Cool Down Period</strong>&nbsp;(15 minutes, 20 minutes, 30 minutes) which tells the Autoscale engine how long to wait after
    performing one Autoscale event before considering another. This setting helps prevent a rapid fire set of Autoscale events before the server has a chance to recognize the positive effects from the initial scale event.
    <br /><img src="https://t3n.zendesk.com/attachments/token/86v5pfkaMr8yHBvAHHOYJCjcQ/?name=create-autoscale-policy-top.png" alt="create-autoscale-policy-top.png" />
  </li>
  <li>Set the policy's scale up characteristics. The first value defines the upper limit of CPU utilization.&nbsp;<strong>When a server is at the upper limit for a single threshold period, a scale up event occurs (unless it occurs within a cool down period).</strong>&nbsp;Also
    set the&nbsp;<strong>Scale Up Increment&nbsp;</strong>which lets you choose how many CPUs to add (1, 2, 4) during a particular scaling event
    <br /><img src="https://t3n.zendesk.com/attachments/token/3sJa4Xxm29X6ocX0rQwcWULrU/?name=autoscale-up-setting.png" alt="autoscale-up-setting.png" />
  </li>
  <li>Set the policy's scale down characteristics. The first value determines the lower limit of CPU utilization.&nbsp;<strong>When a server is at the lower limit for a single threshold period within the scale down window, a scale down event occurs.&nbsp;</strong>The&nbsp;<strong>Scale Down Window</strong>&nbsp;is
    a UTC time that you can tolerate a reboot of the system to reduce the CPU allocation&nbsp;(for example when most users may be offline).&nbsp;&nbsp;Choose a small window if a reboot will be particularly disruptive to the system. However, make sure
    that the window is wide enough to catch periods of low utilization.
    <br /><img src="https://t3n.zendesk.com/attachments/token/kASmZlMOhcPEYA5YjObUSlXFu/?name=autoscale-down-setting.png" alt="autoscale-down-setting.png" />
  </li>
  <li>Review the notice at the bottom of the policy creation page, and then click&nbsp;<strong>Create.&nbsp;</strong>The notice tells you that if you apply a policy to a server that is outside the bounds of the policy's CPU range (e.g., a policy with a maximum
    CPU count of 6 is applied to a server that is currently using 10 CPUs), then no scale up events will occur until the first scale down event pulls the server within the policy's range.
    <br /><img src="https://t3n.zendesk.com/attachments/token/HaiJ2urEcjjRQtRL5dpmrrfca/?name=autoscale-create-button.png" alt="autoscale-create-button.png" />
  </li>
  <li>See that your policy is now part of the list of vertical Autoscale policies.
    <br /><img src="https://t3n.zendesk.com/attachments/token/z6p39slkxo9ip68/?name=autoscale-cpu08.png" alt="autoscale-cpu08.png" />
  </li>
  <li>Vertical Autoscale policies can be added to&nbsp;existing&nbsp;servers or during the server creation process. These steps will show how to apply to an existing server (but similar steps below are followed after setting the "cpu autoscale" option to
    "on" when creating a server.) Locate a Windows Server 2012 Datacenter Edition, Red Hat Enterprise Linux 5/6/7, or Ubuntu 10/12/14 x64 server to apply a vertical Autoscale policy to. (If you attempt to add a vertical Autoscale policy to a server that
    isn't based on one of the previously mentioned OSes, you will see no option available to do so. Bug in platform right now - new UI does not do this.) From the server settings page, mouseover the CPU utilization chart and click the&nbsp;<strong>EDIT&nbsp;</strong>button
    that appears.
    <br /><img src="https://t3n.zendesk.com/attachments/token/sWaYmXMfqqetZCtDvi1fVcqAL/?name=autoscale-server-settings.png" alt="autoscale-server-settings.png" />
  </li>
  <li>This will display the Edit CPU panel.
    <br /><img src="https://t3n.zendesk.com/attachments/token/tb12lRou4S0rj6VjayNsZAWVu/?name=edit-cpu-panel.png" alt="edit-cpu-panel.png" />
  </li>
  <li>Flip the Autoscale slider to&nbsp;<strong>On</strong>&nbsp;and choose an Autoscale policy. (If you flip this switch from the Create Server page, you will see a preview of all the details of the policy after you select it. From the server settings page
    as shown here, only the policy name is displayed.)&nbsp;<strong>Please read any notices next to the apply button, as if your server has not already been set up to add resources without a reboot, then the first time you assign an Autoscale policy, the server will be rebooted.</strong>
    <br
    /><img src="https://t3n.zendesk.com/attachments/token/SDANt0ExuGD1mazVTy84QF4G3/?name=edit-cpu-panel-with-autoscale.png" alt="edit-cpu-panel-with-autoscale.png" />
  </li>
  <li>After clicking&nbsp;<strong>apply&nbsp;</strong>to save&nbsp;the updated server settings, return to the Autoscale overview page and see that your server is now listed next to the associated policy.
    <br /><img src="https://t3n.zendesk.com/attachments/token/7mqX0wT6sJILDGp9KVBXFa9E1/?name=autoscale-applied.png" alt="autoscale-applied.png" />
  </li>
  <li>Create a significant amount of load on the server in order to exceed the upper threshold for a sustained period of time. In the example below, see that the CPU utilization is consistently above 88%.
    <br /><img src="https://t3n.zendesk.com/attachments/token/65l5ktv4ovnazhv/?name=autoscale-cpu13.png" alt="autoscale-cpu13.png" />
  </li>
  <li>After the threshold period has passed, note that the server has a new CPU (without rebooting) and an entry was added to the activity history. The activity history entry shows the average CPU amount that triggered the Autoscale, how long the threshold
    period was, and how many CPUs the server has now.
    <br /><img src="https://t3n.zendesk.com/attachments/token/Ja24rtmMxccCVY3LJloQ7oZyW/?name=scale-up-event.png" alt="scale-up-event.png" />
  </li>
  <li>To test the scale down experience, visit your Autoscale policy and broaden the scale down time window. This ensures that the period of low usage will coincide with the window where scale down is allowed.
    <br /><img src="https://t3n.zendesk.com/attachments/token/lMB5SMAh19upoqAH2wxA9X5Qh/?name=expand-scale-down-window.png" alt="expand-scale-down-window.png" />
  </li>
  <li>Wait until the cool down period has passed, and watch for a scale down (and reboot) to occur.&nbsp;<strong>Note that a scale down event takes the server back to the minimum number of CPUs defined in the Autoscale policy.&nbsp;</strong>The activity history
    entry shows the average CPU amount that triggered the Autoscale, how long the threshold period was, and how many CPUs the server has now.&nbsp;In this scenario, see that the server has a single CPU allocated after the scale down occurs.
    <br /><img src="https://t3n.zendesk.com/attachments/token/iqSs0wENbOb1kR6jFkVvJmeZI/?name=scale-down-event.png" alt="scale-down-event.png" />
  </li>
  <li>Autoscale policies can be changed at any time and those changes are instantly reflected on the related servers. In addition, at any point you can remove the policy from a server, and go back to manually changing CPU capacity.</li>
</ol>
<p>
  <a name="horizontal"></a>
</p>
<h3>Horizontal Autoscale</h3>
<p><strong>Detailed Steps</strong></p>
<ol>
  <li>Navigate to the&nbsp;<strong>Servers</strong>&nbsp;menu item and choose&nbsp;<strong>Policies</strong>&nbsp;from the menu. This takes you to the place to create and manage new policies that can later be applied to servers.
    <br /><img src="https://t3n.zendesk.com/attachments/token/NpjrhxhaizUyBxI8cWcBHgiyG/?name=policies-menu.png" alt="policies-menu.png" />
  </li>
  <li>On the left side of the screen you will see a number of policy types that you are able to define. Click&nbsp;<strong>Horizontal Autoscale&nbsp;</strong>to display the area where you can manage all horizontal Autoscale policies.
    <br /><img src="https://t3n.zendesk.com/attachments/token/gvU5AeGJEGUXaJUVuRgCiRNco/?name=h-autoscale-settings.png" alt="h-autoscale-settings.png" />
  </li>
  <li>Click&nbsp;<strong>Create Horizontal Autoscale Policy</strong>&nbsp;to create the policy. First, define&nbsp;the general policy characteristics. Provide a friendly name for the policy. Enter the&nbsp;<strong>Minimum Servers</strong>&nbsp;which defines
    the minimum number of for the servers to remain on at all times. The maximum number is determined by the number of provisioned servers with the group that the policy is applied to. Choose which&nbsp;<strong>metrics</strong>&nbsp;to include in the
    threshold, CPU and/or memory. This will determine what metrics the threshold can be set on when defining the scale out and scale in triggers.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/p7BY10XRRntyMGuJN9sva34xO/?name=new-h-scale-general.png" alt="new-h-scale-general.png" />
    <br />
    <br />
  </li>
  <li>Set the policy's scale out characteristics. First, set the&nbsp;<strong>Scale Out Increment&nbsp;</strong>which lets you choose how many servers to turn on (1, 2, 4) during a particular scaling event.&nbsp;The next values define the upper limit of utilization.
    You will see percentage fields for each of the metrics you set (<strong>CPU</strong>&nbsp;and/or&nbsp;<strong>RAM</strong>) and if you selected both, you will have the&nbsp;<strong>operator</strong>&nbsp;option to select whether both thresholds must
    be reached or just one of them.&nbsp;<strong>When a server is at the upper limit as defined for a single threshold period, a scale out event occurs (unless it occurs within a cool down period).</strong>&nbsp;
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/Y60b6XhF9foi3sbykBoClPE0X/?name=new-h-scale-out.png" alt="new-h-scale-out.png" />
    <br />
    <br />
  </li>
  <li>Set the policy's scale in characteristics. First, set the&nbsp;<strong>Scale In Decrement&nbsp;</strong>which lets you choose how many servers to turn off (1, 2, 4) during a particular scaling event.&nbsp;The next values define the lower limit of utilization.
    You will see percentage fields for each of the metrics you set (<strong>CPU</strong>&nbsp;and/or&nbsp;<strong>RAM</strong>) and if you selected both, you will have the&nbsp;<strong>operator</strong>&nbsp;option to select whether both thresholds must
    be reached or just one of them.&nbsp;&nbsp;<strong>When a server is at the lower limit as defined for a single threshold period within the scale down window, a scale down event occurs.&nbsp;<br /><br /><img src="https://t3n.zendesk.com/attachments/token/VHTVuxKJIqXcsUwfUh0CDEnwK/?name=new-h-scale-in.png" alt="new-h-scale-in.png" /></strong>
    <br
    />
    <br />
  </li>
  <li>Set the&nbsp;<strong>Threshold Period&nbsp;</strong>(5 minutes, 10 minutes, 15 minutes, 30 minutes) which defines how long a server must be at the minimum or maximum usage before an Autoscale action occurs. If a server is likely to have temporary spikes
    that don't warrant a scaling event, choose a longer period. Identify the&nbsp;<strong>Cool Down Period</strong>&nbsp;(15 minutes, 20 minutes, 30 minutes) which tells the Autoscale engine how long to wait after performing one Autoscale event before
    considering another. This setting helps prevent a rapid fire set of Autoscale events before the server has a chance to recognize the positive effects from the initial scale event.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/9PbZy9TkTUmcC50u9xYPtgZNT/?name=new-h-scale-timing.png" alt="new-h-scale-timing.png" />
    <br />
    <br />
  </li>
  <li>Click&nbsp;<strong>Save Policy</strong>&nbsp;to complete the creation of the policy and see that your policy is now part of the list of horizontal Autoscale policies.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/MycAvvHpHO4WZzCn1iMH9LNWC/?name=new-h-scale-list.png" alt="new-h-scale-list.png" />
    <br />
    <br />
  </li>
  <li>Note: You will need to have a load balancer group created and a pool configured in order to move on to the next step. Please follow the instructions for&nbsp;<a href="https://t3n.zendesk.com/entries/22111185-Modifying-a-Self-Service-Load-Balancing-Configuration"
   >creating and configuring a load balancer</a>&nbsp;before moving on to the next step. Ideally, you should configure the load balancer with all the IP addresses (and ports) of the servers in the group you plan on applying the autoscale
    policy to. If you don't do this, the autoscale policy will take care of it for you, but it could take up to five minutes before the load balancer configuration is updated after the autoscale policy is applied to the group. Once you have a load balancer
    group and pool created and ready to use, continue on to the next steps.
    <br />
    <br />
  </li>
  <li>Horizontal Autoscale policies are added to&nbsp;existing&nbsp;server groups and not during the group creation process.&nbsp;Go to the Group Settings page for the group where you want to apply an Autoscale policy. (This group should have at least two
    identically configured servers in it. See the Autoscale FAQ for more information on how to manage horizontal Autoscale groups of servers.)
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/FyCLZRslbSFoPQ6EgDfVpXm7M/?name=group-settings.png" alt="group-settings.png" />
    <br />
    <br />
  </li>
  <li>Select the&nbsp;<strong>Horizontal Autoscale&nbsp;</strong>tab and click&nbsp;<strong>select a horizontal autoscale policy</strong>&nbsp;to show the available policies to select.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/O6C0qSVti0kZHFTOxdGBkS0Ts/?name=apply-h-scale-link.png" alt="apply-h-scale-link.png" />
  </li>
  <li>Select the name of the policy you created in the above steps and choose the load balancer you created in step 8 along with the port on the servers that the load balancer should route traffic to (or optionally select "none" if you do not need load balancing).
    Click&nbsp;<strong>save policy</strong>&nbsp;to apply the policy immediately.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/IdJ6J19zbr8e7XvcZFoeaa3nf/?name=apply-h-scale.png" alt="apply-h-scale.png" />
    <br />
    <br />You may want to read the Autoscale FAQ for more information on how the load balancer options here are used and other additional information.
    <br />
    <br />
  </li>
  <li>Now you will see the details of your policy listed to show you that it has been applied to the group.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/K1pe4Hs3d42r5UpN1AJ6hY4oa/?name=h-policy-details.png" alt="h-policy-details.png" />
    <br />
    <br />
  </li>
  <li>To test your policy, start by creating a significant amount of load on the powered on servers in the group in order to exceed the upper threshold for a sustained period of time. In the example below, see that only two of four servers are currently powered
    on and we are using the&nbsp;<strong>stress</strong>&nbsp;tool in Linux to simulate very high&nbsp;CPU utilization on the servers.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/UBYMuGarzw7JRqAsnY6Vu7t6V/?name=two-powered-on.png" alt="two-powered-on.png" /><img src="https://t3n.zendesk.com/attachments/token/dzqfePj7MLo9HcIzCvTadiZwf/?name=linux-stress-top.png" alt="linux-stress-top.png"
    />
    <br />
    <br />
  </li>
  <li>After the threshold period has passed, note that there is an additional server in the group that is now powered on and an entry was added to the activity history. The activity history entry shows the average utilization amount that triggered the Autoscale
    and which servers were affected.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/OB9W4bEOtlxALaofQ5npEB51F/?name=three-servers-powered-on.png" alt="three-servers-powered-on.png" /><img src="https://t3n.zendesk.com/attachments/token/A8ibVZb3oNMDSUIZVFEz9o0Ov/?name=activity-log-h-scale-event.png"
    alt="activity-log-h-scale-event.png" />
    <br />
    <br />
  </li>
  <li>After the peak usage has dropped below the lower threshold, wait until the cool down period has passed, and watch for a scale in to occur.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/UBYMuGarzw7JRqAsnY6Vu7t6V/?name=two-powered-on.png" alt="two-powered-on.png" /><img src="https://t3n.zendesk.com/attachments/token/i84pV12kO2dOV7rNSIHAnw6cl/?name=activity-log-h-scale-in-event.png"
    alt="activity-log-h-scale-in-event.png" />
    <br />
    <br />
  </li>
  <li>Autoscale policies can be changed at any time and those changes are instantly reflected on the related servers. In addition, at any point you can remove the policy from a group, and all the servers will remain in the group and in the load balancer pool,
    but none will be powered on/off automatically.</li>
</ol>
