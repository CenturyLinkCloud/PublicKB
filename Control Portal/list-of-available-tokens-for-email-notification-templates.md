{{{
  "title": "List of Available Tokens for Email Notification Templates",
  "date": "2-21-2013",
  "author": "Richard Seroter",
  "attachments": []
}}}

<h3>Description (goal/purpose)</h3>
<p>Tier 3 offers resellers a way to customize and personalize the Tier 3 cloud to fit their needs. One way to do that is to modify the default email templates that are used by the Tier 3 system. Many of the email templates offer "tokens" which represent
  information about the user (e.g. "username") or resource (e.g. "blueprint name") that the email applies to. In this KB article, we'll list each email template and which tokens are available.</p>
<p>Note that to view the available tokens for a template, click inside the "message body" to switch from the Viewer interface to the Editable interface.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/xfqjfcfmzzxrmy4/?name=templates01.png" alt="templates01.png" />
</p>
<h3>Audience</h3>
<ul>
  <li>Tier 3 customers</li>
</ul>
<h3>Pre-Requisites</h3>
<ul>
  <li>Account must be enabled for full customization. Contact the Tier 3 NOC to enable your account.</li>
</ul>
<h3>Template List</h3>
<ol>
  <li><strong>Billing Invoice. </strong>There are no template-specific tokens.</li>
  <li><strong>Billing Receipt.&nbsp;</strong>
  </li>
  <ol>
    <li><strong>payment amount. &nbsp;</strong>Amount charged to your account for the billing cycle.</li>
    <li><strong>transaction code. </strong>Unique identifier for the payment transaction.</li>
    <li><strong>payment type. </strong>Indicates the payment type set for the account. Values include: Check, ACH, Credit Card.</li>
  </ol>
  <li><strong>Billing Failure.</strong>
  </li>
  <ol>
    <li><strong>payment amount. </strong>Amount charged to your account for the billing cycle.</li>
    <li><strong>payment type. </strong>Indicates the payment type set for the account. Values include: Check, ACH, Credit Card.</li>
    <li><strong>failure reason</strong>. Description of why the attempt to charge the designated payment type failed.&nbsp;</li>
  </ol>
  <li><strong>Blueprint Success.</strong>
  </li>
  <ol>
    <li><strong>blueprint name. </strong>The name given to the blueprint template.</li>
    <li><strong>server info. </strong>Information about the server(s) impacted by the blueprint.</li>
    <li><strong>warnings. </strong>Message containing details of any errors that occurred while executing the blueprint.</li>
  </ol>
  <li><strong>User Welcome.</strong>
  </li>
  <ol>
    <li><strong>base url. </strong>Home URL for accessing the Control Portal.&nbsp;</li>
    <li><strong>username. </strong>Username defined by the new user.</li>
    <li><strong>password. </strong>Temporary password for&nbsp;the new user.</li>
  </ol>
  <li><strong>User Password Reset.</strong>
  </li>
  <ol>
    <li><strong>new password. </strong>New password defined by the user.</li>
  </ol>
  <li><strong>VPN Server Confirmation. </strong>There are no template-specific tokens.</li>
  <li><strong>WebFabric Success.</strong>
  </li>
  <ol>
    <li><strong>webfabric name. </strong>Friendly name provided by the user when creating the Web Fabric environment.</li>
    <li><strong>webfabric domain name. </strong>Management API URL for the Web Fabric environment.</li>
    <li><strong>management url. </strong>Control Portal URL to manage this Web Fabric environment.</li>
  </ol>
  <li><strong>Server Lifespan Expiration.</strong>
  </li>
  <ol>
    <li><strong>server name. </strong>Name of the server that is about to expire.</li>
    <li><strong>expiration date. </strong>Date that the named server will expire.</li>
    <li><strong>expiration timezone. </strong>Timezone associated with the expiration date/time.</li>
    <li><strong>expiration action. </strong>Indicates what will happen on expiration. Options include: Archive, Delete.</li>
  </ol>
  <li><strong>Group Lifespan Expiration.</strong>
  </li>
  <ol>
    <li><strong>group name. </strong>Name of the group that is about to expire (as defined in the Scheduled Task).</li>
    <li><strong>server list. </strong>Collection of servers that are impacted by the expiration.</li>
    <li><strong>expiration date. </strong>Date that the named group will expire.</li>
    <li><strong>expiration timezone. </strong>Timezone associated with the expiration date/time.</li>
    <li><strong>expiration action. </strong>Indicates what will happen on expiration. Options include: Archive, Delete.</li>
  </ol>
</ol>