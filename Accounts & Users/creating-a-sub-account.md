{{{
  "title": "Creating a Sub Account",
  "date": "11-5-2014",
  "author": "Jon McClary",
  "attachments": [],
  "contentIsHTML": false
}}}

<p>CenturyLink Cloud supports the ability to create sub accounts, which fall under a parent account. Sub accounts have many advantages:</p>

* They are hierarchal - user permissions flow down, not up nor sideways.
* They may be billed separately or to the parent account.
* They may share parent networks or have their own.
* Settings are inherited.

<h3>Audience</h3>

Customers

<h3>Creating a Sub Account</h3>

<p>In CenturyLinkCloud’s Control Portal drop down menu, select Account &gt; Sub Accounts</p>
<p>Click “+ create new account”</p>

<h3>Company Info</h3>
<p><img src="../images/createsubaccount-subalias.png" alt="subalias.png" /></p>
<p>Change parent account if desired, such as in the case that you wish for this account to be a sub account of a sub account.</p>
<p>Fill in appropriate Business name, etc.</p>
<p>Input an Account Alias of your choice. This is a string of 2-4 alphanumeric characters which is used to identify your account and relate servers to that account by naming convention. They are globally unique so there are no duplicate aliases allowed. This is a required field.

Note that an account alias cannot be reused, even after deletion of the original account with that alias.</p>
<p>Full Address and Phone fields are required.</p>

<h3>Company Info</h3>
</p>
<p><img src="../images/createsubaccount-subbilling.png" alt="sub-billing.png" />
</p>
<p>You may input a Default Primary DNS and a Default Secondary DNS IP address. This will be the DNS server value input into your IPv4 settings when building a server. You may select your own environment DNS servers, preferred public DNS servers, or the default datacenter DNS servers (172.17.1.26, 172.17.1.27) or leave it blank, in which case it will default to the aforementioned Datacenter DNS servers, which do allow for external DNS lookup.</p>
<p>Bill to: Each sub account generates an invoice. You have the option of submitting the invoice to the parent account, or bill the sub account directly.</p>
<p>Payment Type: Input the payment type for the sub account.</p>
<p>Share Parent Networks: This allows for sub accounts to share networks with the parent account. If this is set to ‘NO’ then the sub account will receive unique IP ranges when deploying servers/networks.</p>

<h3>Settings</h3>
<img src="../images/createsubaccount-subsettings.png" alt="subsettings.png" />
<p>All settings will be inherited from the parent. Toggle on to Yes any of the settings in this section will make that section visible in the sub account. The users in that sub account will then be able to override inherited settings. Leaving the sections set to off will hide the menu for that section in the sub account, preventing the settings from being overridden. In our example sub account users will be able to change the Account Logo and Account Color Scheme from what was inherited. All other menus will be hidden.</p>


<h3>Data Center</h3>

<p><img src="../images/createsubaccount-subdatacenter.png" alt="subdatacenter.png" /></p>

<p>Select the datacenter which you wish the new account to be homed to. This does not limit your ability to build in any other datacenter. Your VPN server will be created here. You will not be able to hide the Primary datacenter. Your will not be able to change the primary datacenter.</p>

<p>Click ‘Create’ to create the sub account as configured.</p>
<p>If the account is created successfully you will be returned to the parent account (the one you were logged in to) You'll need to navigate to the new sub account via the account drop down to the left of the menu.</p>
<p>If you get any errors, like the alias is in use or missed any required fields, correct them and click Create again.</p>

<p><strong>Edit Settings:</strong></p>

<p>After the sub account is created you can edit the settings. Any of these settings may be modified in the future by logging into parent account, then browsing to Account&gt;Subaccounts and click to select the subaccount for which you wish to edit
  settings. You will be sent to the “Sub Account Settings” page.</p>
<p><img src="../images/createsubaccount-subeditsettings.png" alt="subeditsettings.png" />
</p>
<p>edit settings from the parent account after the sub account has been created</p>

<p><img src="../images/createsubaccount-subhiddenmenus.png" alt="subhiddenmenus.png" /></p>
<p>Menus are hidden to the sub account</p>
<p>You can click any of these settings and toggle them between disabled (not visible) and enabled (visible and therefore editable)</p>

###Adding Users/Permissions
1. To add new users to the subaccount
2. In the dropdown in the top left, select the subaccount for which you would like to add a user.
3. Go to account &gt; users and click “+ Create New User”.
4. Fill in required information.
5. Permissions can then be administered via the Account &gt; Permissions tab.
6. Note that user permissions are hierarchical so a user may access the account to which they are assigned, and that account’s sub accounts, but not a parent account nor any other sub account on the same level.


<h3>FAQ</h3>
<p><strong>I just created my subaccount. Why do I get a permission denied error when I try to access it?</strong></p>
<p>Allow a few minutes for the new account to fully replicate and try again.</p>

<p><strong>I don’t need this subaccount any longer, how do I delete it?</strong></p>
<p>Account &gt; Info. Click on “Request to close” link at bottom right.</p>

<p><strong>I disabled a subaccount, but still see it in my subaccounts list.</strong></p>
<p>A disabled subaccount still appears in the list, so you have the option to re-enable it. Entering the subaccount via the dropdown at the top left, and going to account&gt;info and clicking the “Request to close” link will start the process to remove the account.</p>
