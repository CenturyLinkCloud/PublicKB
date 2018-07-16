{{{
"title": "Creating Cloud Application Manager Users",
"date": "05-16-2017",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

**In this article:**

* User Management page
* User Management options
* Creating Cloud Application Manager Users
* Logging in to Cloud Application Manager

### User Management page

A Cloud Application Manager administrator can access User Management page from within Management site and he can find there all the existing users in the organization with some useful data of each user such as:

* **Name** and **email**
* **Id**
* **Status** (Invited, Active, Deactivated, Password Locked)
* **Instances**, **Boxes** and **Provider** (the number of each that he owns)
* **Last Login** (date of last login, or empty if never logged in)
* **Created** (date when the user was created)

There is also a search field in the top page of the screen to look for users that matches the search term in their name, email or id fields.

### User Management options

Next to each user in the User Management page there is a gear button that provides access to an administrator to the following options, depending on the state of the user:

* **Edit User**: to change first or last name of the user
* **Resend Invitation**: to resend invitation email to an invited user who has not yet logged in
* **Reset Password**: to trigger the password reset flow, sending an email to the user to reset his password
* **Unlock Password**: to unlock the password of a password locked user (does not change it), resetting the count of failed password attempts
* **Deactivate User**: to disable an active user
* **Activate User**: to enable a deactivated user
* **Delete User**: to remove the user from the system. If the user has existing assets (instances, boxes or providers) the confirmation pop-up window will ask the administrator to select a target workspace where the user assets will be transferred to.

### Creating Cloud Application Manager Users

From the User Management page, the administrator can press the **New** button to create new users into the organization.

![Create User](../../images/cloud-application-manager/management/new-user.png)

The administrator can also selects the Cost Center the user will be associated with, so all the assets that the user creates would be billed to that Cost Center, if necessary.

Once the Administrator fills in the New User form and clicks on Save, an email will be sent to the specified email address inviting the user to access into Cloud Application Manager.

When the user clicks the "Access My Account" button located in the email received, he will be redirected to the Cloud Application Manager login page, where he would be able to create a password to log in or use any of the available login mechanisms as explained below.

### Logging In to Cloud Application Manager

You have a few options:

* Sign in to Cloud Application Manager at https://[companyname].cam.ctl.io/#/login with a username and password created using the process above.
* Log-in with an existing Google account.
* Log-in with your current GitHub credentials if your org admin has enabled GitHub sign in for Cloud Application Manager.
* Enter your company Active Directory credentials in the username, password fields if your admin enabled LDAP integration with Cloud Application Manager.
* Log-in with your company SAML credentials if your admin enabled and configured SAML integration with Cloud Application Manager.
* Log-in with your CenturyLink Cloud credentials if your admin enabled CenturyLink Cloud authentication integration with Cloud Application Manager.

**Note**: When you log in with your AD credentials, GitHub, Google, SAML or CenturyLink Cloud accounts, Cloud Application Manager does not have access to your password. We use your email to create a profile and workspace for you.

![Getting Started - Login page](../../images/cloud-application-manager/getting-started-login-1.png)

___

**Help**

Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md) for help. Or you may contact [support](mailto:incident@CenturyLink.com) from within the Cloud Application Manager interface.

![Getting Started - Support options](../../images/cloud-application-manager/getting-started-login-7.png)

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
