{{{
  "title": "Cloud Platform – Release Notes: February 22, 2013",
  "date": "2-22-2013",
  "author": "Richard Seroter",
  "attachments": []
}}}

<p><strong>New Features (1)</strong>
</p>
<hr />
<ul>
  <li><strong>Data Center Preferences. </strong>Account administrators can now define their preferences for which data centers are available for the account's users. Data centers enabled/disabled at the parent account level are inherited to all child accounts.
    Child accounts can restrict this list further, but cannot enable data centers that were disabled by a parent. Once these preferences are set, this impacts the data centers shown in the "data centers" drop down list across the Control Portal, and is
    reflected across operations performed on the site. These preferences are also applied by the API to prevent the creation of resources (servers, accounts, blueprints, etc) in non-preferred data centers.</li>
</ul>
<p></p>
<p><strong>Minor Defects Fixed or Enhancements Added (5)</strong>
</p>
<hr />
<ul>
  <li><strong>SAML Configuration Inheritable. </strong>SAML single sign-on settings defined at the account level are automatically inherited within the account hierarchy. The SAML configuration can still be overridden by a given sub-account.</li>
  <li><strong>SAML Auto-Login Added for Reseller Scenarios. </strong>Accounts that use SAML for single sign-on and don't want their users to see a sign-in page can now check a box on the Account Authentication Settings page to enable this behavior. When auto-login
    is enabled, users who hit the http://&lt;account alias&gt;.tier3cloud.com domain will automatically be forwarded to the configured Identity Provider to initiate the SAML single sign-on process. The only time that a user will see the CenturyLink Cloud login page
    is if (a) there is an error returned by the SAML Identity Provider or (b) if the user is not configured in the CenturyLink Cloud account.</li>
  <li><strong>&nbsp;User API Update. </strong>Both the CreateUser and Update User operations support setting the SAMLUserName property for a given user. This value
    is used when the SAML single sign-on process maps a user in the SAML Identity Provider to a user in the CenturyLink Cloud.</li>
  <li><strong>SAML users do not get prompted for credentials when viewing server password. </strong>Users who log into the Control Portal with their CenturyLink Cloud credentials are asked once again for their credentials when they attempt to view the password of a
    server on the Server Details page. Since SAML users do not have (or do not know) CenturyLink Cloud credentials, their request to view credentials is still logged for auditing purposes, but they are not asked to re-authenticate when viewing server passwords.</li>
  <li><strong>Account API Update</strong>. Users can now use the API to enable a suspended account (//www.ctl.io/api-docs/v1/#account-enable-account). This is the opposite of the Suspend Account operation (//www.ctl.io/api-docs/v1/#account-suspendaccount).
    When an account is re-enabled, the account's servers are not restarted by the system, but the VPN server is restarted automatically.</li>
</ul>
