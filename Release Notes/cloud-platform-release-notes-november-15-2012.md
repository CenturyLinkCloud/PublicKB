{{{
  "title": "Cloud Platform – Release Notes: November 15, 2012",
  "date": "12-11-2012",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (5)</strong>
</p>
<hr />
<ul>
  <li><strong>New Data Center in Canada. </strong>CenturyLink Cloud now offers a Canadian data center in Toronto.</li>
  <li><strong>Self service server disk resize</strong>. Customers may now increase the size of their storage disks without contacting the CenturyLink Cloud NOC. Windows servers realize their updated storage capacity instantly, while Linux servers must have their volumes
    manually extended to reflect the increased storage.</li>
  <li><strong>API addition - Account management features</strong>.The CenturyLink Cloud (SOAP/HTTP) API has been extended to support a range of account management features such as: CreateAccount, SuspendAccount, DeleteAccount, UpdateAccountDetails, and GetAccounts.</li>
  <li><strong>API addition - User management features</strong>.&nbsp;The CenturyLink Cloud API now allows customers to perform user functions such as CreateUser, DeleteUser, SuspendUser, GetUserDetails, and UpdateUser.</li>
  <li><strong>API addition - Billing management features</strong>. Customers can use the CenturyLink Cloud API to view billing information through functions such as GetBillingSummary, GetBillingHistory, GetGroupEstimate, GetServerEstimate, GetGroupSummaries, GetServerHourlyCharges,
    and GetInvoiceDetails.</li>
</ul>
<p></p>
<p><strong>Minor Defects Fixed or Enhancements Added (5)</strong>
</p>
<hr />
<ul>
  <li><strong>FTP Support in all data centers.&nbsp;</strong>Every CenturyLink Cloud data center now has FTP support for users who wish to upload software packages to their blueprint library.</li>
  <li><strong>Async firewall updates</strong>. The new CenturyLink Cloud firewall policy engine now runs asynchronously so that the user can proceed to other tasks while their firewall policies are taking effect.</li>
  <li><strong>Web Fabric upgrade. </strong>The current Iron Foundry fork was incorporated into the CenturyLink Cloud Web Fabric, bringing with it updated versions of Node.js, PostgreSQL, MongoDB and Java. See <a href="http://blog.ironfoundry.org/2012/10/ironfoundry-me-environment-now-running-latest-iron-foundry-bits/"
   >this post on the Iron Foundry blog</a> for more details.</li>
  <li><strong>Update Firewall Policy UI to simplify custom port range definition</strong>. Instead of having the user view two windows to define a custom port range for a firewall policy, we've simplified the UI to address standard and custom ports all in
    one window.</li>
  <li><strong>Friendly naming of data centers.</strong>&nbsp;In the Control Portal, users no longer see names like "WA1" and "GB1", but rather, see more informative names that identify the city and country of the data center.</li>
</ul>