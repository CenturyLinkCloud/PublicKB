{{{
"title": "Enterprise Setup",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

### Enterprise Setup

If you have a SaaS enterprise account in Cloud Application Manager, understand how to set up users with information in this article.

**In this article:**
* Your Enterprise in Cloud Application Manager
* Enterprise on-Boarding Checklist
___

### Your Enterprise in Cloud Application Manager
In Cloud Application Manager SaaS, each enterprise is hosted as a tenant in a multi-tenanted platform architecture. Cloud Application Manager keeps each tenant’s data secure by separating their data logically in databases. Therefore, all the users, assets, and data in your enterprise are not visible or accessible outside your organization or even to Cloud Application Manager.

**Get an enterprise account**

To get an enterprise account, [contact sales](mailto:incident@CenturyLink.com). You’ll receive an enterprise domain at **yourcompanyname.cam.ctl.io**. You also get a default admin account to manage the enterprise with the username as **operations+yourorgdomainname@cam.ctl.io**. This default admin account lets you see and manage all users, assets, and resources in your organization from the [admin console](../Administering Your Organization/admin-overview.md).

___

### Enterprise On-Boarding Checklist

If you’re a new enterprise in Cloud Application Manager, use this checklist to set up your enterprise and make it available for others to use.

* **Secure the default admin account**: When you get an enterprise in Cloud Application Manager, you get a default admin account with the username **operations+yourdomainname@cam.ctl.io**. We recommend that you use the default admin account for emergency situations. Log in to the default admin account and change the password to keep the account secure. Then grant enterprise administrative access to other users so they can log into their accounts and manage the enterprise in Cloud Application Manager.
* **(Optional) Request shared workspace for help with troubleshooting**: In your Cloud Application Manager SaaS enterprise, users with admin access can request access to a workspace shared both by you and the Cloud Application Manager admins. This shared workspace is called **yourorgname - Cloud Application Manager**. The purpose of this workspace is troubleshooting. Since Cloud Application Manager can’t access your data, the workspace allows you to share assets like providers, boxes, and instances so that Cloud Application Manager admins can access them in the workspace to troubleshoot support issues. [Email us](mailto:incident@CenturyLink.com) if you want this workspace created for your enterprise.
* **Identify your enterprise users**: Once an enterprise account is available, [enable authentication methods](../Administering Your Organization/user-authentication.md) such as Google, username/password, GitHub, or LDAP to allow others to sign up for an account. You and others can sign up for an account in your enterprise domain at Cloud Application Manager.com with your domain credentials.
  **Note**: To migrate the assets of Developer Edition accounts to their enterprise counterpart, the users must share all assets in their Developer Edition account personal workspace. Assets in workspaces outside of their personal one are not migrated to their enterprise accounts.
  **Note**: If users in your company signed up via an authentication method not currently supported by your enterprise, then those users are locked out. Contact support to delete their account and have them sign in again or [enable the authentication method](../Administering Your Organization/user-authentication.md) to support their login.
* **Ask others to sign up**: To get others in your company to start using Cloud Application Manager, send them an email or some communication notifying them about Cloud Application Manager. Ask them to sign up for an account at **yourcompanyname.cam.ctl.io** using one of the authentication methods you support for signup.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
