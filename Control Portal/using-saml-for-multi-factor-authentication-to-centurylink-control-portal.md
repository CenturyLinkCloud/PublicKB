{{{
  "title": "Using SAML for Multi-Factor Authentication to CenturyLink Control Portal",
  "date": "10-13-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<strong>Description</strong>
<p>As described in&nbsp;<a href="https://t3n.zendesk.com/entries/22636576-Using-SAML-for-Single-Sign-On-to-the-Tier-3-Control-Portal" target="_blank">Using SAML for Single-Sign-On</a>, CenturyLink Cloud&nbsp;supports the use of Security Assertion Markup
  Language (SAML) for exchanging user authentication data as XML between trusted parties. This industry standard protocol empowers customers to use their&nbsp;<strong>own</strong>&nbsp;SAML-supported identity management system for authenticating users
  of the CenturyLink Control Portal. Now, with the addition of the&nbsp;Require SAML for Login&nbsp;option provided by Control Portal, customers can <em>force</em> users to authenticate through their identity providers to enable additional identity management
  features like multi-factor authentication (MFA) and user provisioning. This way, the CenturyLink Cloud platform can provide flexible, standards-based capabilities while allowing&nbsp;an organization to keep&nbsp;the nuts-and-bolts of their IdM configurations
  in their pre-existing systems.</p>
<p>For more details and how SAML works in general and how to specifically setup an ADFS IdP for use with Control Portal, refer to&nbsp;<a href="https://t3n.zendesk.com/entries/22636576-Using-SAML-for-Single-Sign-On-to-the-Tier-3-Control-Portal" target="_blank">Using SAML for Single-Sign-On</a>.
  In the example below, however, we will use a separate software-as-a-service vendor as the identity provider in order to also enforce multi-factor authentication. The following steps will walk through the process of configuring the IdP to add users,
  enabling MFA and SAML, and configuring CenturyLink Control Portal's SAML settings to enforce the use of the IdP.&nbsp;</p>
Steps
<p>In this example, we will use the cloud-based identity and access management solution&nbsp;<a href="http://www.onelogin.com" target="_blank">OneLogin</a>&nbsp;as our identity provider since it is free to use as a demo, easy to setup, and supports both
  SAML and MFA.&nbsp;Though we are using OneLogin in our example here, of course the principles will apply for any IdP with support for SAML and MFA. The steps below assume you have already <a href="http://www.onelogin.com/signup" target="_blank">signed up for a OneLogin account</a>  and are able to login to its administrator interface.&nbsp;</p>
<h3>Configure IdP for SAML</h3>
<ol>
  <li>In the CenturyLink Cloud Control Portal, from the Account Settings page, navigate to the "Users" tab and the "Authentication" sub-menu.</li>
  <li>Click the "SAML 2.0 Authentication" checkbox to show all the available settings. For now, just take note of the "Relying Party Assertion Consumer Service URL" listed there. It should be in the format of <code>https://{account-alias}.tier3cloud.com/SAMLAuth/Post</code>.
    (Highlighted in the screenshot below.)<img src="https://t3n.zendesk.com/attachments/token/yilavprKs9cBa121jvVRaJmUh/?name=saml-settings-blank.png" alt="saml-settings-blank.png" />
  </li>
  <li>Now login to the OneLogin end-user dashboard.</li>
  <li>From the "Apps" menu, select "Add Apps".
    <br /><img src="https://t3n.zendesk.com/attachments/token/i68H8FdUiIs2IPN6Hgm5dJUYo/?name=onelogin-add-app.png" alt="onelogin-add-app.png" />
  </li>
  <li>In the search field, type "onelogin saml" and select the first app that shows up. It should be called "OneLogin SAML Test (IdP)".
    <br /><img src="https://t3n.zendesk.com/attachments/token/uftlkKy3ffx9O7I7V7XfWeZC2/?name=onelogin-saml-test.png" alt="onelogin-saml-test.png" />
  </li>
  <li>Rename this app to "CenturyLink Cloud Control Portal" and click the "Save" button.
    <br /><img src="https://t3n.zendesk.com/attachments/token/yr6kN4SzEHnDWwOqmcqDfcfAv/?name=onelogin-app-rename.png" alt="onelogin-app-rename.png" />
  </li>
  <li>Now, on the "Configuration" tab, enter the URL you copied from Step 2&nbsp;in the section above into the "SAML Consumer URL" field. Optionally, you may provide other values in the additional fields if you know them. (You will find the Single Logout
    URL also available on the Control Portal page from Step 2&nbsp;above.)
    <br /><img src="https://t3n.zendesk.com/attachments/token/tvbTVzku9ODIXqQu9ArwVuw9S/?name=onelogin-saml-url.png" alt="onelogin-saml-url.png" />
  </li>
  <li>&nbsp;Click the "Save" button in the upper right hand corner to save the OneLogin configuration.</li>
</ol>
<p>There are a number of other settings that OneLogin supports or that may be supported by other IdPs,&nbsp;but this is the minimal configuration required on the OneLogin side for SAML authentication to work.&nbsp;</p>
<h3>Configure Control Portal SAML Settings</h3>
<ol>
  <li>While still in the OneLogin administrator interface, click on the "SSO" tab to view SAML configuration information required to plug in to the Control Portal settings. You should see a SAML 2.0 Endpoint and a X.509 Certificate. Both of these values are
    required to configure SAML in CenturyLink Cloud Control Portal.
    <br /><img src="https://t3n.zendesk.com/attachments/token/CARDEyzoXsIGea1Y9y6juGZEb/?name=onelogin-saml-info.png" alt="onelogin-saml-info.png" />
  </li>
  <li>Back in the Control Portal Authentication settings page, check the "Require SAML for Login" option and the "Apply to all Sub Accounts" options. This will require SAML login only for this account and all sub accounts. Next, enter the SAML 2.0 Endpoint
    URL provided in the previous step into the "SSO IdP URL (required)" field and copy and paste the certificate value from OneLogin page into the "Signing Certificate Key" field in Control Portal. Optionally, you can configure the "SLO IdP URL" as well.
    Click "Save" to apply the SAML settings to control.
    <br /><img src="https://t3n.zendesk.com/attachments/token/bC279PnOmcm8KPqJqMfFxhYDq/?name=saml-settings-filled-in.png" alt="saml-settings-filled-in.png" />
  </li>
</ol>
<p>At this point, SAML is configured on both ends. All that's left is to enable MFA and begin provisioning users.</p>
<h3>Configure IdP for MFA</h3>
<ol>
  <li>From the OneLogin interface, select the "Settings" menu and go to "Authentication Factors". From this screen you will be presented with a number of available multi-factor authentication providers that can be enabled. Clicking the provider name and clicking
    the "Save" button activates it as an additional authentication factor.&nbsp;In this example we will use "Google Authenticator" since it's ubiquitous and easy to setup. (You could choose RSA SecurID or another provider of your choice.)
    <br /><img src="https://t3n.zendesk.com/attachments/token/hrWs6yHdMdBHsbqSSXn5MjiB7/?name=mfa-setup.png" alt="mfa-setup.png" />
  </li>
  <li>To complete the setup, we need to define and apply a policy that requires users to authenticate with MFA. Select "Policies" from the "Settings" menu and click on the "Default policy" to edit. (We could create a new policy to apply only to our set of
    Control Portal users if we are using OneLogin with multiple applications. Here, we will keep things simple and apply a single policy for all users and apps.)</li>
  <li>On the MFA tab, click the "OTP Auth Required" and "Google Authenticator" checkboxes. To keep things simple, we'll keep the setting to require OTP for all users at every login, but this can be adjusted as desired. Click "Save".
    <br /><img src="https://t3n.zendesk.com/attachments/token/ydSBMjv3mEoeImvl45VZtwBhJ/?name=mfa-policy.png" alt="mfa-policy.png" />
  </li>
</ol>
<p>All that's left is to provision users in the IdP and associate them with users in Control Portal.</p>
<h3>Provision User(s)</h3>
<p>There are a few different options for provisioning users to CenturyLink Cloud and no doubt the IdP you choose to use has a number of options as well. OneLogin supports both bulk user import from a flat file as well as an&nbsp;<a href="https://onelogin.zendesk.com/hc/en-us/articles/201175524-Users-API"
  target="_blank">API</a>&nbsp;for creating users. CenturyLink Cloud's API also provides the capability to programmatically create users. In this example, we will assume we already have a user in the Control Portal that we want to provision to OneLogin.
  You may have the opposite situation where you need to create users in Control that already exist in your IdP. Or you may not have users in either location. No matter how you choose to provision users, as you will see, the important thing is that the
  SAML username in Control matches the SAML username in the IdP.&nbsp;</p>
<ol>
  <li>In the Control Portal, from the "Users" page in Account Settings, click the user you will be provisioning to OneLogin. (If you need to create a new user, you can follow the instructions in <a href="https://t3n.zendesk.com/entries/21389606-Creating-Users"
    target="_self">Creating Users</a>.)
    <br /><img src="https://t3n.zendesk.com/attachments/token/rtsHZoBs57Vj4NcPFEzEZDPG8/?name=users-page.png" alt="users-page.png" />
  </li>
  <li>On the User Profile page, take note of the e-mail address, first and last name. Most importantly, click on the "saml username (single sign on)" field and enter the <em>e-mail address</em> for this user. &nbsp;(The OneLogin SAML configuration uses e-mail
    as the default username. To keep this simple in this example, we will stick with this rather than set it to a custom value. In this case, it is also the same as the user name, which is a good practice for uniqueness.)
    <br /><img src="https://t3n.zendesk.com/attachments/token/uImFdvb0cV4Lfhlfu60BMtyWu/?name=user-info-page.png" alt="user-info-page.png" />
  </li>
  <li>Back in the OneLogin configuration, navigate to "Users &gt; All Users" from the menu and click the "New User" button to create a new user. Enter the first name, last name, and e-mail address you took note of in Step 3. All of these fields are required
    and as noted above, the e-mail address must match the value entered into the SAML username field in Control. You may also fill in other fields as desired. Click "Save User".
    <br /><img src="https://t3n.zendesk.com/attachments/token/4L4d0nNF0nFvCUmG26d58e0qG/?name=onelogin-user.png" alt="onelogin-user.png" />
  </li>
  <li>Now we have to give the user access to the Control Portal SAML application. On the "Applications" tab for the user, click the "+" sign to add a new app. Select "CenturyLink Cloud Control Portal" and click "continue" then enter the user's e-mail address
    and click "save".
    <br /><img src="https://t3n.zendesk.com/attachments/token/5LvdJnCYE8QICRMg9NhscRa7a/?name=onelogin-user-application.png" alt="onelogin-user-application.png" />
    <br /><img src="https://t3n.zendesk.com/attachments/token/LnTzfzXlOP695chqbVU6tQSlE/?name=onelogin-app.png" alt="onelogin-app.png" /><img src="https://t3n.zendesk.com/attachments/token/humGfRHpEiN951I03R9slImIr/?name=onelogin-app-user.png" alt="onelogin-app-user.png"
    />
    <br />
    <br />
  </li>
  <li>Next, from the "More Actions" menu, select "Send Invitation" to send an e-mail to the user to set up a password and MFA token for the first time. This will begin the provisioning process.
    <br /><img src="https://t3n.zendesk.com/attachments/token/nmAH0bcxGX6K638cOJlZxC7r0/?name=send-invitation.png" alt="send-invitation.png" /><img src="https://t3n.zendesk.com/attachments/token/epY2CdrD4MImSj4xU93PqsjT5/?name=send-invite-dialog.png" alt="send-invite-dialog.png"
    />
  </li>
  <li>The user receives an e-mail with a link to set their password. When they follow the link, they will set their password and then, in this case since we are using Google Authenticator, will be presented with a QR code to scan using the Google Authenticator
    app to setup a token and be given a security code to enter. Once this is done, the user enters the security code and clicks "log in". This will activate the user's MFA token for use.
    <br /><img src="https://t3n.zendesk.com/attachments/token/gL6dFhnRsVPBiPIHdVJw1WuNK/?name=onelogin-qr-scan.png" alt="onelogin-qr-scan.png" />
  </li>
</ol>
<h3>Putting It All Together</h3>
<p>Now that all the configuration is complete, users must login to Control Portal using their OneLogin credentials.</p>
<ol>
  <li>From a browser, go to your SAML Login page. This is the root of the highlighted URL from the very second step above, in the format <code>https://{account-alias}.tier3cloud.com</code>. (In this example, it's https://bry2.tier3cloud.com.) If you have
    the "Require SAML for Login" setting turned on as described above, this should ultimately result in you being redirected to the OneLogin login screen.</li>
  <li>Login using the username, password, and Google Authenticator security code. You should be directed back to the Control Portal and logged in as that user. You can use the logout link as well if you have set the logout URLs appropriately.</li>
</ol>
<p>Note that the "Require SAML for Login" setting will force this user to login this way whether they access the SAML-specific login page as described in Step 1 or the primary control URL (http://control.tier3.com). If the primary URL is used, when logging
  in using the regular login screen, after entering the username (and any value for password), the user will be redirected to the SAML login page as described above.</p>