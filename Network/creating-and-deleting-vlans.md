{{{
  "title": "Creating and Deleting VLANs",
  "date": "7-3-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>CenturyLink Cloud customers can create complex network topologies to securely segment application tiers or entire systems. Using the Control Portal, users can easily provision VLANs and delete unused ones. Each CenturyLink Cloud customer gets an initial
  private VLAN to use, and can add more VLANs (for a fee). In this KB article, we will show how to create and delete a VLAN.</p>
<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud customers (system administrators)</li>
</ul>
<h3>Prerequisites</h3>
<ul>
  <li>Must have Account Administrator permissions on the platform</li>
</ul>
<h3>Detailed Steps</h3>
<ol>
  <li>Navigate to the "Networks" item under the "Network" menu. From here you can see all the networks currently provisioned for this account (and available to sub-accounts if the "share parent networks" option is set for the sub-account).
    <br /><img src="https://t3n.zendesk.com/attachments/token/OVoPAmnxOTdNWTjOqy8W0wm2f/?name=networks-menu.jpg" alt="networks-menu.jpg" />
  </li>
  <li>Click the "add network" button to add a new VLAN to the account. Note that each VLAN has 217 usable addresses as blocks are reserved for OpenVPN usage and other purposes. Be aware that there is no confirmation prompt upon clicking this button as a Cloud
    Blueprint is immediately launched to provision the network. This provisioning process adds routes the VPN server for the account and ensures that this account is ready to use.
    <br /><img src="https://t3n.zendesk.com/attachments/token/evzrkdjjxpuagk4/?name=vlan-createdelete02.png" alt="vlan-createdelete02.png" />
  </li>
  <li>Once the process completes, the user can see the new network in the list. See that the "add network" button is disabled because by default, each account can have a total of 3 VLANs. If you need more than that, please contact the NOC.
    <br /><img src="https://t3n.zendesk.com/attachments/token/b8jhpm8tudvrvbl/?name=vlan-createdelete03.png" alt="vlan-createdelete03.png" />
  </li>
  <li>To delete a VLAN, click the "x" button on the row of the target VLAN. If there are no servers currently attached the VLAN, the user will see a prompt similar to the following image. This prompt notifies the user that deleting the VLAN will also remove
    all corresponding firewall policies.
    <br /><img src="https://t3n.zendesk.com/attachments/token/pxwfaitjb07rans/?name=vlan-createdelete04.png" alt="vlan-createdelete04.png" />
  </li>
  <li>If there are servers currently part of the VLAN, then the user will see a prompt like the following image. The listed servers must either (a) be deleted or (b) be disconnected from the VLAN. To do option (b), please contact the NOC to move the servers
    to a different VLAN.
    <br /><img src="https://t3n.zendesk.com/attachments/token/dxepjxewmwivz4e/?name=vlan-createdelete05.png" alt="vlan-createdelete05.png" />
  </li>
</ol>
