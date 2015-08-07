{{{
  "title": "Customer Account Setup for Partners",
  "date": "6-5-2015",
  "author": "",
  "attachments": [],
  "contentIsHTML": false
}}}

### Create an Account for a New Customer

When you add a new customer, you need to setup an account for that customer. This account is called a Sub Account.  Here’s how it works:

- Your account hierarchy defines how you create Sub Accounts in the CenturyLink Cloud portal.  
  - Each Sub Account is logically isolated from other Sub Accounts within the parent account.
- Sub Accounts are hierarchical – user permissions flow down, not up or sideways.
- Sub Accounts inherit users and permissions from the parent account.
  - Additional users can be added to the Sub Account.

1. Go to the "Account" > "Settings" page.
2. Select the ‘Sub Accounts’ tab and click ‘+ create new account’.  Fill in the information as follows:
  - **Parent Account**
  - **Business Name**
  - **Account Alias**
  - **Address and Telephone**
  - **Fax**
  - **Time Zone**
  - **DNS**
  - **Bill To**
  - **Payment Type (Disregard this)**
  - **Share Parent Networks:** This allows Sub Accounts to share networks with the Parent Account. If this is set to ‘NO’ then the Sub Account will receive unique IP ranges when deploying servers/networks. “No” is the most common setting.
3. Sub Account Settings. By default, sub accounts inherit settings from its parent account.
  1. Toggle “Yes” to any of the settings in this section, will make that section editable in the Sub Account.
    - The users in that Sub Account will then be able to override inherited settings.  
    - Leaving the setting to “No” will hide the menu for that section in the Sub Account, preventing the settings from being overridden.  
  2. You can also select the data center where you want the new account to be homed.  
    - This does not limit your ability to build in any other data center.
    - Your VPN server will be created here.
  3. Click ‘create’ to commit the settings.

### Adding Users

1. In the dropdown in the top left of the portal, select the Sub Account for which you’d like to add a new user.  
2. Go to ‘Account>Sub Account’ ‘Users’ and click ‘+create a new user.’
3. Fill in the required information.
4. Click ‘create new user’ to commit changes.

### Assigning Roles and Admininstrative Permissions

Control Portal permissions are controlled by adding users to one or more roles.  Roles are simply a collection of actions a user is allowed to perform to areas within the Control Portal.  

User permissions are hierarchical so a user may access the account to which they are                                  assigned and that account’s sub accounts, but not a parent account.

1. To get started, go to ‘Account>Sub Accounts’, ‘Permissions’ tab.
2. Select a user from the dropdown menu and select the roles you wish to assign that user.
3. Click ‘Save’ to commit changes.

