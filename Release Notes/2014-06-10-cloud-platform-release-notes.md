{{{
  "title": "Cloud Platform – Release Notes: June 10, 2014",
  "date": "6-12-2014",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<hr />
<ul>
  <li><strong>New "create server" experience in Control Portal</strong>. The "create server" page has been replaced with a new-and-improved version that performs better and consolidates core actions to a single page. Users can easily choose the data center,
    Group, OS template, server class, CPU, CPU Autoscale policy, memory, disks, storage type, and time-to-live for a new server. If you are looking to do things like add a public IP or install software, go to the Group overview page after building the
    server and execute from there.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/PMEELFrBptZf2RmYqIlktR8vu/?name=release06_10_14_01.gif" alt="release06_10_14_01.gif" />
  </li>
  <li><strong>Specify valid source IP range for public IP address.&nbsp;</strong>On the create/edit public IP section of the "server details" page, you can now add source IP ranges that are allowed to access the assigned Public IP. Enter multiple ranges using
    <a href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">CIDR notation</a>.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/mG4d6IGVxTaVMbTO7ujWz5Hm3/?name=release06_10_14_02.png" alt="release06_10_14_02.png" />
  </li>
</ul>
<p><strong>Minor Enhancements (7)</strong>
</p>
<ul>
  <li><strong>"Create account" page adds country/state relationship. </strong>This page now resembles the centurylinkcloud.com signup page where choosing a Country value causes the State drop-down to show valid values for that country.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/3MHTmO1WRtTfJqc5M2Tk8K9ZF/?name=release06_10_14_04.png" alt="release06_10_14_04.png" />
  </li>
  <li><strong>Server/Group search results link to new user interface.&nbsp;</strong>The global search has been updated so that server or group results direct the user to the new user experience .</li>
  <li><strong>Updated bandwidth pricing, model.&nbsp;</strong>The new bandwidth model and pricing takes effect. This is a switch from 95th percentile bandwidth billing to a GB transferred model. The bandwidth graph on the Dashboard has been updated, and invoice
    information will show the charge for outbound GB transferred during the month. <a href="https://t3n.zendesk.com/entries/42123304-June-2014-Bandwidth-Model-Change-FAQ">See the FAQ</a> for more details.</li>
  <li><strong>Blueprint API updated to show servers a Blueprint is acting on</strong>. The GetDeploymentStatus operation in the v1 Blueprint API now returns all the servers that are part of the Blueprint, even if there isn't a "create server" task in the
    Blueprint itself..</li>
  <li><strong>Blueprint Request ID available in script context.&nbsp;</strong>Blueprint developers can now access an additional context parameter from their scripts. The T3.RequestId value is populated with the unique ID of the Blueprint being executed.</li>
  <li><strong>"Account manager" field added.&nbsp;</strong>The "Account Settings" page now contains a placeholder for each customer's account manager..</li>
  <li><strong>Labels on anti-affinity pages updated.&nbsp;</strong>To avoid confusion, the anti-affinity navigation menu item and page have been updated to reflect the fact that it only applies to Hyperscale servers.</li>
</ul>