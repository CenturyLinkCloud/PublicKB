{{{
"title": "Enterprise Setup & Onboarding",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Enterprise Setup & Onboarding

If you have a SaaS enterprise account in ElasticBox, understand how to set up and onboard users with information in this article.

**In this article:**
* Your Enterprise in ElasticBox
* Enterprise on-Boarding Checklist

___

### Your Enterprise in ElasticBox
In ElasticBox SaaS, each enterprise is hosted as a tenant in a multi-tenanted platform architecture. ElasticBox keeps each tenant’s data secure by separating their data logically in databases. Therefore, all the users, assets, and data in your enterprise are not visible or accessible outside your organization or even to ElasticBox.

**Get an enterprise account**

To get an enterprise account, [contact sales](mailto:support@elasticbox.com). You’ll receive an enterprise domain at **yourcompanyname.elasticbox.com**. You also get a default admin account to manage the enterprise with the username as **operations+yourorgdomainnameelasticbox.com**. This default admin account lets you see and manage all users, assets, and resources in your organization from the [admin console](./admin-overview.md).

___

### Enterprise On-Boarding Checklist

If you’re a new enterprise in ElasticBox, use this checklist to set up your enterprise and make it available for others to use.

* **Secure the default admin account**: When you get an enterprise in ElasticBox, you get a default admin account with the username **operations+yourdomainname@elasticbox.com**. We recommend that you use the default admin account for emergency situations. Log in to the default admin account and change the password to keep the account secure. Then grant enterprise administrative access to other users so they can log into their accounts and manage the enterprise in ElasticBox.
* **(Optional) Request shared workspace for help with troubleshooting**: In your ElasticBox SaaS enterprise, users with admin access can request access to a workspace shared both by you and the ElasticBox admins. This shared workspace is called **yourorgname - ElasticBox**. The purpose of this workspace is troubleshooting. Since ElasticBox can’t access your data, the workspace allows you to share assets like providers, boxes, and instances so that ElasticBox admins can access them in the workspace to troubleshoot support issues. [Email us](mailto:support@elasticbox.com) if you want this workspace created for your enterprise.
* **Identify your enterprise users**: Once an enterprise account is available, [enable authentication methods](./user-authentication.md) such as Google, username/password, GitHub, or LDAP to allow others to sign up for an account. You and others can sign up for an account in your enterprise domain at ElasticBox.com with your domain credentials.
* **Migrate Developer Edition users to the enterprise**: Users who signed up for Developer Edition accounts with your company domain name before your enterprise was available are not part of your enterprise. You can see them as [unmanaged users](./manage-assets-monitor-usage.md) in the admin console under the Users > Unmanaged tab. To migrate them over to your enterprise, [Email us](mailto:support@elasticbox.com) a list of these users and we’ll port them.
  **Note**: To migrate the assets of Developer Edition accounts to their enterprise counterpart, the users must share all assets in their Developer Edition account personal workspace. Assets in workspaces outside of their personal one are not migrated to their enterprise accounts.
  **Note**: If users in your company signed up via an authentication method not currently supported by your enterprise, then those users are locked out. Contact support to delete their account and have them sign in again or [enable the authentication method](./user-authentication.md) to support their login.
* **Ask others to sign up**: To get others in your company to start using ElasticBox, send them an email or some communication notifying them about ElasticBox. Ask them to sign up for an account at **yourcompanyname.elasticbox.com** using one of the authentication methods you support for signup.

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
