{{{
  "title": "Applying Data Center Preferences",
  "date": "3-11-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

Lumen Cloud customers can choose which data centers to make available to the users of an account. **Changing these settings has implications on the user experience, and how new data centers are exposed to the account.** Read the steps below to learn how to enable/disable data centers, and the implications on the API.

### Audience

[Account administrators and security managers](role-permissions-matrix.md)

### Detailed Steps

1. Log-in to the Control Portal.
1. From the menu, go to Settings > Account Profile.
![Navigation Menu](../images/data-center-nav-menu.png)
1. Choose the **Data Center** sub tab.
![Data Center Menu](../images/data-center-tab.png)
1. Select the data center you wish to enable or disable and click the slider. (To enable, the slider will be in the right position with “YES” highlighted in green).
![Data Center Enable](../images/data-center-enable.png)
1. Confirmation of your new settings will be provided in the upper right-hand corner of the page.
![Data Center Change Confirmation](../images/data-center-change-confirmation.png)
1. Once a data center is disabled (in this example, CA1), it no longer appears on the dashboard overview.
![Dashboard](../images/data-center-dashboard.png)
1. A disabled data center (in this example, CA1) is also excluded from the **Create Server** page.
![Create Server](../images/data-center-create-server.png)
1. A disabled data center is also unavailable for any API operations that use a data center parameter (e.g. [Get Data Center List](http://www.ctl.io/api-docs/v2#data-centers-get-data-center-list)).

**Note:** If you apply data center preferences to your account, than any **new** Lumen Cloud data centers will **NOT** automatically show up in the Control Portal for you. You will need to come into the Data Center preferences page and manually enable the new data center. This behavior is in place to respect your conscious choice to show specific data centers.
