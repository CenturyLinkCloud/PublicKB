{{{
  "title": "Cloud Platform – Release Notes: October 18, 2012",
  "date": "10-19-2012",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<hr />
<ul>
  <li><strong>Firewall Policies</strong>&nbsp;&nbsp;New in this release, and <strong>currently only available for CenturyLink Cloud Administrators</strong>, firewall policies allow users to create and maintain complex intra-DC networking policies. Administrators can
    use these policies to define how network traffic should go between the vlans that exist in their primary account and various sub-accounts. <strong>In the very near future, this feature will be opened up for CenturyLink Cloud customers to use</strong>. For more
    information, please see the following Knowledge Base articles: <a href="http://help.tier3.com/entries/22196842-connecting-data-center-networks-through-firewall-policies" target="_blank">Connecting Data Center Networks Through Firewall Policies</a>    and <a href="http://help.tier3.com/entries/22210896-creating-bi-directional-firewall-policies" target="_blank">Creating Bi-Directional Firewall Policies</a>.</li>
  <li><strong>"Script" Tasks on Groups</strong>&nbsp;&nbsp;This new Task can be applied in blueprints and as part of Group-level actions. It supports the execution of user-entered script statements for Windows (PowerShell and Command) and Linux (SSH). This
    allows users to quickly and easily perform group-level activities such as turning off a service or enabling a firewall rule.</li>
</ul>
<p></p>
<p><strong>Minor Defects Fixed or Enhancements Added (4)</strong>
</p>
<hr />
<ul>
  <li><strong>Scheduled Tasks - Add Shutdown as an option</strong>&nbsp;&nbsp;In addition to pausing, powering on, and rebooting servers as part of a maintenance schedule, you can now also perform a server shutdown.</li>
  <li><strong>Web Fabric - Unable to build a web fabric in an alternate DC, switching DC results in error</strong>&nbsp;&nbsp;Corrected an issue that occurred during Web Fabric provisioning or migration between data centers.</li>
  <li><strong>Published Shared packages not appearing in the Published Software\Scripts Tab in the Account that created it</strong>&nbsp;&nbsp;Some customer-uploaded software packages weren't available for use.</li>
  <li><strong>Servers - Server quick links are not displaying servers in maintenance</strong>&nbsp;&nbsp;Servers in maintenance mode were not showing up in the "Quick Links" section of the base "Servers" page.</li>
</ul>