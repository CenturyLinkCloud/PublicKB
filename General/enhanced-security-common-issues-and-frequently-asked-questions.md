{{{
  "title": "Enhanced Security: Common Issues and Frequently Asked Questions",
  "date": "7-9-2018",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

As part of our efforts to increase the security of your accounts using the SavvisStation Portal and Private Cloud (DCC), you will need to go through a one-time setup to create a new Master Account.  Once setup is complete, for your security, you will receive a one-time prompt to provide credentials for your services to link them to your master account; as a result, you will be able to navigate between them without re-authenticating going forward. Other security improvements include optional multi-factor authentication through your smart phone (soft token) and the ability to set up multiple security questions for account validation and retrieval purposes.

This article will walk you through some of the common issues, and what steps you can take to resolve them.  It will also discuss how to ensure you are engaging the correct support team depending on your issue.  Lastly, we will answer some of the frequently asked questions.

### Common Issues  
Registration Issues|Steps to Resolve|
:---|:---|
I cannot click next on the password creation screen.|Ensure you are creating a valid password.  If the password is not valid, follow the on screen prompts to ensure the password meets all requirements.
I did not receive the registration email with my token.|Check your spam or junk folders for the email.  Also, verify that your email provider is not blocking the email.  The registration email is sent from "noreply@ctl.io" with the subject "CenturyLink Email Validation Token".  If you are still unable to find the email with the token, [engage our customer care team for assistance.](#contacting-the-customer-care-team)
I am constantly receiving session timeouts when trying to create a master account.|Remove all cookies in the browser you are trying to register with.  Then, manually opt-in by visiting this link [https://sso.ctl.io/oxauth/enableSso](https://sso.ctl.io/oxauth/enableSso).  Lastly, go back to the service, which should redirect you back to the master account screen and try to [create your master account again.](enhanced-security-master-account-registration.md)
**Sign-In Issues**|**Steps to Resolve**
I am unable to login.|Verify which account is being requested.  For Master Accounts, you will enter in your email first, then be taken to another screen to enter your password.  If you haven't linked an account for the service you are trying to access, you will be prompted to provide credentials for that service after logging into your master account.  This process is only needed once if you check the "link my account" button.  It will state "Account Linking" at the top.  The service being linked will be stated in the information tab below that.  In either scenario, you can reset your password by clicking the "Forgot your password" link below the login button.
The multi-factor code is not working.|Double check the system clock on your phone is accurate.  If the clock on the phone is not correct, you will receive old codes.
Issues scanning the QR code for multi-factor.|Please review [this KB article regarding multi-factor authentication](managed-hosting-and-private-cloud-multi-factor-authentication-for-master-account.md).
**Account Linking Issues**|**Steps to Resolve**
I am prompted to enter my SavvisStation/Private Cloud credentials every time even though I've logged in with a master account.|The first time you log into a service after creating a master account, you will need to enter in the credentials of that service to link the accounts.  When logging into the service, check the "link my account" button to create the link.  After this is done, you will no longer need to enter in the credentials of that service when logging in with your master account.  For more information regarding linking and unlinking accounts, [please review this KB article.](enhanced-security-linking-and-unlinking-accounts.md)
I receive an error stating my username or password is incorrect when trying to link a service account.|You can reset your password by clicking the "Forgot Password" link located below the sign-in button.  If you are still receiving issues, you can [reach out to the Client Response Center for assistance.](#contacting-the-client-response-center)

If the above issues did not help you, you can reach out to our support teams, detailed below.

### Contacting the Client Response Center  
The Client Response Center can assist you with issues regarding the following applications:
* SavvisStation Portal
* Private Cloud (Dedicated Cloud Compute)
* Support (managedsupport.ctl.io)

_Note: If you are unable to reach any of the above applications due to issues with your master account or multi-factor authentication, [contact the customer care team.](#contacting-the-customer-care-team)_

If you are experiencing an issue with the above, there are two ways to open up a ticket with the Client Response Center.

First, [you can open a ticket through the support site.](https://managedservices.ctl.io/msp/support/request)
This will require that you log in with your master account and have at least one linked account.  
For assistance with creating a ticket, [this video will step you through the process.](https://www.youtube.com/watch?v=CWauPgOe4Jg)

Alternatively, if the issue you are facing doesn't allow you to open a ticket, you can send an email to incident@centurylink.com.  In the email, please provide details about what you are trying to accomplish and what error you are receiving.  You can also include screenshots of the error you are receiving in this email.  

### Contacting the Customer Care Team  
The Customer Care team can assist with issues regarding the new Enhanced Security Master Account.  If you are experiencing an issue with this account, send an email to help@ctl.io with details about what you are trying to accomplish and what error you are receiving.  You can also include screenshots of the error you are receiving in this email.  

### Frequently Asked Questions
**Q: Why are we releasing this functionality?**

A: These new features are part of an effort to increase the security of your accounts and provide a new and improved support solution.

The Master Account will enable you to only need one username and password for several of CenturyLink services.  The increased security now supports multi-factor authentication.  It is also fully self-service.

The new support solution is offering a faster and more consistent experience, including a new process to submit requests, tickets, and changes all through a single form. Additional improvements include document sharing abilities, templates for your recurring requests, and bulk upload of devices for your ticket or change requests.

**Q: What services does Enhanced Security currently work with?**

A: Currently Enhanced Security works with our Managed Hosting and Private Cloud services.  This list will be expanded in the future.

**Q: How do I create my Enhanced Security Master Account?**

A:  [Please review this KB article that will walk you through the steps of creating your enhanced security master account.](enhanced-security-master-account-registration.md)

**Q: What is multi-factor authentication?**

A: Multi-factor authentication is a security standard that requires more than one method of authentication from independent sources to verify the identity of a user. Users who opt-in to multi-factor authentication will need to enter a 6-digit One-Time Password (OTP) every time they log into their master account, in addition to the username and password they set.

**Q: What do I need to know about setting up my multi-factor authentication?**

Multi-factor authentication comes with a few caveats, all of which explained during registration:
1. A smart phone with an app store is required
2. An OTP Application on the phone is required such as Google Authenticator or OTP Authenticator
3. You will need to use this soft token OTP app every time you log into your master account
4. The system clock on the device being used to register your MFA needs to be accurate, or it will generate outdated codes.

[You can read more about setting up multi-factor authentication here.](managed-hosting-and-private-cloud-multi-factor-authentication-for-master-account.md)

**Q: Which browsers are currently supported?**

A: Below are the browsers currently supported:  

Browser|Version|
:---|---:|
Chrome|Latest Version
Firefox|Latest Version
Safari|Latest Version
Microsoft Edge|Latest Version
Internet Explorer|11

**Q: Can I link multiple SavvisStation or Private Cloud accounts to one master account?**

A: At this time, you can only link one of each type of account to a master account.  If you have multiple accounts you wish to use, simply skip checking the "Link this account" check box when logging into the service.  You will always need to use your master account credentials and ALSO enter your SavvisStation/Private Cloud credentials each time you want to log into the service under this method.

**Q: How can I remove or change a linked account?**

A:  [Please review this KB article that will walk you through the steps of managing your linked accounts.](enhanced-security-linking-and-unlinking_Accounts.md)
