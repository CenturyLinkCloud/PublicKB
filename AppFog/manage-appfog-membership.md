{{{
  "title": "Manage AppFog Membership",
  "date": "04-15-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Audience

Application developers

### Adding an AppFog Member from Account

Many software development efforts involve a team or teams that need access to the deployment platform. To add AppFog members they must have existing user credentials on the Control Portal Account. Please go to [this article](../Accounts & Users/creating-users.md) for creating user credentials in your Control Portal Account.

To add a member to AppFog, you must have the AppFog Admin role level permissions. If you have these permissions set for your account, go to the Members tab of your chosen region (US East or US West) and follow these steps:

1. Click the "invite member" button.
1. Enter username of user's Control Portal credentials
1. Select the level of permissions to grant this new member
  * Manager: Can invite/manage users, select/change the plan, establish spending limits
  * Billing Manager: Can edit/change the billing account info, payment info
  * Auditor: Read-only access to org info and reports
1. Click "add member" button
1. They should now be a member of your AppFog organization

### Setting an AppFog Member's Role

To update a user's AppFog role level permissions, follow these steps:

1. Click on the member's row that you want to edit
1. Select the level of permissions you want to update this member to
  * Manager: Can invite/manage users, select/change the plan, establish spending limits
  * Billing Manager: Can edit/change the billing account info, payment info
  * Auditor: Read-only access to org info and reports
1. Click "apply" button
1. Their permissions should now be updated on the row

### Managing Space Membership

Within each AppFog region (US East and US West) there are Spaces. A Space represents a container for managing Application deployments and service instances. Each Space can have its own membership. For instance, you could have specific members in a "Developer" Space that don't have access to manage the "Production" Space.

To manage membership of a Space, click on a Space from the left-side navigation or from the Spaces grid on the region view. Adding a member and updating their role in the Space is the same as managing membership to an AppFog region except the names and description of the Space roles:

* Space Manager: Can invite/manager users and view information about applications and service instances
* Space Developer: Can deploy and manage applications and service instances
* Space Auditor: Can view information about applications and service instances
