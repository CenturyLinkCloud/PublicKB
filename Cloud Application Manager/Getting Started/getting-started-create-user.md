{{{
"title": "Creating Cloud Application Manager Users",
"date": "05-16-2017",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

**In this article:**

* Creating Cloud Application Manager Users
* Logging in to Cloud Application Manager
___

### Creating Cloud Application Manager Users

**Where can I create new users?**

* After buying Cloud Application Manager, browse to https://[companyname].elasticbox.com/#/signup and fill out the form. Once your have filled out the form check your email to validate your email address.

* Click the "Validate Email" button located in the email received and you will be automatically logged into Cloud Application Manager.

### Logging In to Cloud Application Manager

You have a few options:

* Sign in to Cloud Application Manager at https://[companyname].elasticbox.com/#/login with a username and password created using the process above.
* Log-in with an existing Google account.
* Log-in with your current GitHub credentials if your org admin has enabled GitHub sign in for Cloud Application Manager.

Enter your company Active Directory credentials in the username, password fields if your admin enabled LDAP integration with Cloud Application Manager.

**Note**: When you log in with your AD credentials, GitHub or Google accounts, Cloud Application Manager does not have access to your password. We use your email to create a profile and workspace for you.

![getting-started-login-1.png](../../images/cloud-application-manager/getting-started-login-1.png)

___

**Help**

Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md) for help. Or you may contact [support](mailto:cloudsupport@centurylink.com) from within the Cloud Application Manager interface.

![getting-started-login-7.png](../../images/cloud-application-manager/getting-started-login-7.png)

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.

* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
