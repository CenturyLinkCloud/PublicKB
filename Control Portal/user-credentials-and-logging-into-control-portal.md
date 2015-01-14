{{{
  "title": "User Credentials and Logging into Control Portal",
  "date": "7-9-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>There are [at least] two different types of user credentials that you need to maintain and be aware of as a CenturyLink Cloud Control Portal user. One set of credentials is used for you or other users in your organization to gain access to the Control
  Portal itself. These are your CenturyLink Cloud Control Portal user credentials. You may also be responsible for maintaining a number of different administrator credentials for servers you have created within your CenturyLink Cloud account. Both credentials
  should use strong and secure passwords, however <em>they are not related to each other at all and should be managed and used distinctly.</em> This article will discuss how to manage and use both types of credentials independently.</p>
<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud customers</li>
</ul>
<h3>Control Portal Credentials</h3>
<p>Control Portal credentials are maintained in your Profile, which can be accessed using the profile icon in the upper right corner of the page.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/fILw4mWa4SlmzY5tiil5tFIor/?name=control-header-profile-icon.png" alt="control-header-profile-icon.png" />
</p>
<p>After clicking on this icon, you should see your user profile information, including a hidden string representing your password.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/RMPvZjxSj4bkfKmazwv4N8YPH/?name=user-profile.png" alt="user-profile.png" />
</p>
<p>Clicking on the password field will allow you to change your password if desired.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/TQkRpHRwRwdxn7GnukrEMlZeo/?name=user-profile-pw-change.png" alt="user-profile-pw-change.png" />
</p>
<p>This is the password you use to login to Control Portal from the login page:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/BnpyvVqrODdacI4UFoWddqdPi/?name=cp-sign-in-page.png" alt="cp-sign-in-page.png" />
</p>
<p>(Note: Your account may have SAML enabled allowing for Single Sign-On capabilities. See the <a href="https://t3n.zendesk.com/entries/22636576-Using-SAML-for-Single-Sign-On-to-the-Tier-3-Control-Portal">article about enabling SAML</a> for more information.)</p>
<p>Also, if you are an Account Admin, you have the ability to see information for other users that have been created within your subaccount through the Users area under the Account menu. You cannot see a user's passwords, however you can see their username
  and information, lock the account, set permissions, delete the account, and generate a password reset e-mail for them if they have forgotten their password.</p>
<h3>Server Admin Credentials</h3>
<p>Different from your Control Portal user credentials, server admin credentials are used to gain access to a server that you have created within your account. These credentials are typically set at the time of the server creation and can be changed from
  the server details page. (The password should be secure and strong, particularly if your server is accessible via the public Internet.)</p>
<p>For more information on changing or retrieving server administrator passwords, please reference the following articles:</p>
<ul>
  <li><a href="https://t3n.zendesk.com/entries/20343057-How-to-change-a-server-administrator-password">How to Change a Server Administrator Password</a>
  </li>
  <li><a href="https://t3n.zendesk.com/entries/22289740-How-to-retrieve-Root-Administrator-password">How to Retrieve a Root/Administrator Password</a>
  </li>
</ul>