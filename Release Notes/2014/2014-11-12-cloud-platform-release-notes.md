{{{
  "title": "Cloud Platform - Release Notes: November 12, 2014",
  "date": "11-12-2014",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong>New Role-Based Access Control Services.&nbsp;</strong>CenturyLink Cloud has launched an upgraded user security model that cascades throughout the UI and v2 API. These 8 roles map to unique personas within an organization and help customers apply
    a least-privilege approach to their cloud environment. A user can be part of multiple roles, and the Control Portal user interface recognizes which role(s) a customer has and adjusts accordingly. For a deep dive description of the permissions assigned
    to each role, view the <a href="https://t3n.zendesk.com/entries/57974910-Role-Permissions-Matrix">Permission Matrix KB</a>. Also, review the <a href="https://t3n.zendesk.com/entries/57600424-Roles-FAQ">Roles FAQ</a>    and <a href="https://t3n.zendesk.com/entries/58057670-Roles-Migration-Guide">migration guide</a> for more details. Below is a brief description of each role:</li>
  <ul>
    <li><strong>Account Administrator</strong> can perform any provisioning and management tasks available in the cloud platform.&nbsp;
      <br /><img src="https://t3n.zendesk.com/attachments/token/Iqi4kDC1ck7t58vqxpyIbyLWZ/?name=release11_12_14_01.png" alt="release11_12_14_01.png" />
    </li>
    <li><strong>Server Administrator&nbsp;</strong>cannot change account-level settings or some networking services, but has full permission to create and manage virtual server infrastructure.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/BfrBnp8b7mspElMu2KpH4eO3s/?name=release11_12_14_02.png" alt="release11_12_14_02.png" />
    </li>
    <li><strong>Server Operator&nbsp;</strong>has day-to-day management permissions but cannot add public IPs, create load balancer pools, or change policies.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/4diaEtJJAEPMHGUOVjlXfwbo2/?name=release11_12_14_03.png" alt="release11_12_14_03.png" />
    </li>
    <li><strong>Security Manager&nbsp;</strong>can change account settings, user permissions, and firewall policies, but cannot build or manage virtual resources.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/jJoPB2EKkWwGQmTJ6Yf7aFJA9/?name=release11_12_14_04.png" alt="release11_12_14_04.png" />
    </li>
    <li><strong>Network Manager&nbsp;</strong>can configure and maintain network settings like DNS, VPNs, vLANs, and firewall policies.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/OIXO59C9nMnLU12xicqjv875D/?name=release11_12_14_05.png" alt="release11_12_14_05.png" />
    </li>
    <li><strong>DNS Manager&nbsp;</strong>has permission to manage DNS zones.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/xQZwASi8HmkTENYFKYsqk6ZiT/?name=release11_12_14_06.png" alt="release11_12_14_06.png" />
    </li>
    <li><strong>Billing Manager&nbsp;</strong>has access to billing history and payment information.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/ss81Dp3Spg6XGVY9P3cnO3E96/?name=release11_12_14_07.png" alt="release11_12_14_07.png" />
    </li>
    <li><strong>Account Viewer</strong>&nbsp;has read-only access to all aspects of the cloud platform, and cannot initiate changes or create resources.
      <br />
      <br /><img src="https://t3n.zendesk.com/attachments/token/f62HihkbXtcmEVm13AxnuZFbo/?name=release11_12_14_08.png" alt="release11_12_14_08.png" />
    </li>
  </ul>
  <li><strong>Feature Flags.&nbsp;</strong>The platform now supports data center-level "feature flags" that make it possible to turn capabilities on and off on a per-DC basis. This helps private cloud customers (and potentially public cloud customers) control
    which capabilities are available to their users. Initial feature flags exist for: premium storage, shared load balancer, site to site VPN, client VPN, and public IP addresses.</li>
</ul>
<p><strong>Minor Enhancements (5)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong>Server (Beta) out of Beta.&nbsp;</strong>The classic groups/server page is now retired in favor of the new Servers user interface. The page URL has changed as well, but all existing server links will seamlessly redirect.
    <br /><img src="https://t3n.zendesk.com/attachments/token/4iKXLmRWKUNtRGUkAiW46rv0N/?name=release11_12_14_09.png" alt="release11_12_14_09.png" />
  </li>
  <li><strong>Global Search index changed.</strong> The Global Search has been further tuned, and we have temporarily removed the following items from the results: group name, group description, VLAN name, public IP addresses, blueprint name, blueprint package
    name.</li>
  <li><strong>Payment details available via v1 API</strong>. The v1 API was updated to return the payment details on the new GetResponsibleBillingAccount&nbsp;call.</li>
  <li><strong>Create users with new roles via v1 API.</strong> Customers who currently provision users automatically via the v1 API <a href="https://t3n.zendesk.com/entries/22441967-CreateUser">can set values related to the newly released roles</a>.</li>
  <li><strong>Get public IP from server details page only.&nbsp;</strong>We've retired the "add public IP" button from the "IP Addresses" page and now have a consolidated place to set and manage public IP addresses. Visit the details page for a given server
    and easily set and change public IP address settings.</li>
</ul>