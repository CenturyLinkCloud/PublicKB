{{{
  "title": "Customer Account Setup for Partners",
  "date": "06-05-2015",
  "author": "",
  "attachments": [],
  "contentIsHTML": false
}}}

### New Customer Accounts and Sub Accounts
When you add a new customer, you need to setup an account for that customer. This account is called a Sub Account. Your account hierarchy defines how you create Sub Accounts in the Control Portal.  
* Each Sub Account is logically isolated from other Sub Accounts within the parent account.
* Sub Accounts are hierarchical – user permissions flow down, not up or sideways.
* Sub Accounts inherit users and permissions from the parent account.
* Additional users can be added to the Sub Account.

### Creating a New Customer Account
There are three sections when setting up a new account.
* Company Information - General information to create an account.
* Settings - The sub account's ability to view/modify settings. Disabling a setting hides the link entirely in this sub account.
* Data Center - The primary data center that this account will be used on.

1. From the Navigation Menu, click **Settings > Account Settings**.

2. Click the **Sub Accounts** tab .

3. Click **create new account**.  

4. In the Company Info section, enter the information requested.
   * Note: Share Parent Networks allows Sub Accounts to share networks with the Parent Account.
   * If the option is set to **NO** (the most common setting), then the Sub Account receives unique IP ranges when deploying servers/networks.

5. In the Settings section, Sub Account Settings. By default, sub accounts inherit settings from its parent account.
   * Toggling any of the settings in this section to **YES** makes that section editable in the Sub Account.
   * Users in that Sub Account are then able to override inherited settings.  
   * Leaving the setting to **NO** hides the menu for that section in the Sub Account, thereby preventing the settings from being overridden.  

6. In the Data Center section, indicate the primary data center to which you want the new account homed.  
   * This does not limit your ability to build in any other data center.
   * Your VPN server is created here.

7. Click **create**.

### Adding Users
Basically, you select the Sub Account to which you’d like to add a new user.  
1. From the Navigation Menu, click **Settings > Sub Accounts**.

2. Click the **Users** tab.

3. Click **Create New User**.

4. Fill in the required information.

5. Click **Create New User**.

### Assigning User Permissions
Control Portal permissions are controlled by adding users to one or more roles. Roles are simply a collection of actions a user is allowed to perform in specific areas within the Control Portal.

User permissions are hierarchical. A user may access the account to which the user is assigned and and sub accounts associated with that account, but not a parent account.
1. From the Navigation Menu, click **Settings > Sub Accounts**.

2. Click the **Permissions** tab.

2. Select a user from the drop-down menu and select the permissions you want the user to have by adding or removing the check mark.

3. Click **Save**.
