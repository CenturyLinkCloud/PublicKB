{{{
  "title": "Lumen Master Account: Common Issues and Frequently Asked Questions",
  "date": "9-15-2020",
  "author": "Daniel Stephan",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

As part of our efforts to increase the security of your accounts using the SavvisStation and Private Cloud (DCC), you will need to go through a one-time setup to create a new Lumen Master Account.  You may also choose to use a Lumen Master Account to log into Cloud Application Manager or Public Cloud. Once setup is complete, for your security, you will receive a one-time prompt to provide credentials for your services to link them to your Lumen Master Account; as a result, you will be able to navigate between them without re-authenticating going forward. Other security improvements include optional multi-factor authentication through your smart phone (soft token) and the ability to set up multiple security questions for account validation and retrieval purposes.

This article will walk you through some of the common issues, and what steps you can take to resolve them. It will also discuss how to ensure you are engaging the correct support team depending on your issue. Lastly, we will answer some of the frequently asked questions.

### Common Issues  
Registration Issues|Steps to Resolve|
:---|:---|
I cannot click next on the password creation screen.|Ensure you are creating a valid password. If the password is not valid, follow the on screen prompts to ensure the password meets all requirements.
I am constantly receiving session timeouts when trying to create a Lumen Master Account.|Remove all cookies in the browser you are trying to register with.  Lastly, go back to the service, which should redirect you back to the Master Account screen and try to [create your Lumen Master Account again.](lumen-master-account-registration.md)
I am unable to add my phone number|Ensure you are entering in a plus sign followed by your country calling code.  Ensure the phone number after that is correct. Example for US resident: +1-555-555-5555
Sign-In Issues|Steps to Resolve
I am unable to login.|Verify which account is being requested. For Lumen Master Accounts, you will enter in your email first, then be taken to another screen to enter your password. If you haven't linked an account for the service you are trying to access, you will be prompted to provide credentials for that service after logging into your Lumen Master Account. This process is only needed once if you check the "link my account" button. It will state "Account Linking" at the top. The service being linked will be stated in the information tab below that. In either scenario, you can reset your password by clicking the "Forgot your password" link below the login button.
The multi-factor code is not working.|Double check the system clock on your phone is accurate. If the clock on the phone is not correct, you will receive old codes.
Issues scanning the QR code for multi-factor.|Please review [this KB article regarding multi-factor authentication](mlumen-master-account-multi-factor-authentication.md).
Account Linking Issues|Steps to Resolve
I am prompted to enter my Managed Hosting (SavvisStation)/Private Cloud credentials every time even though I've logged in with a Lume Master Account.|The first time you log into a service after creating a Master Account, you will need to enter in the credentials of that service to link the accounts. When logging into the service, check the "link my account" button to create the link.  After this is done, you will no longer need to enter in the credentials of that service when logging in with your Master Account.  For more information regarding linking and unlinking accounts, [please review this KB article.](lumen-master-account-linking-and-unlinking-accounts.md)
I receive an error stating my username or password is incorrect when trying to link a service account.|You can reset your password by clicking the "Forgot Password" link located below the sign-in button. If you are still receiving issues, you can [reach out to the Client Response Center for assistance.](#contacting-the-client-response-center)

If the above issues did not help you, you can reach out to our support teams for assistance.

### Email Issues
When you are registering your Lumen Master Account for the first time you will be emailed a token. This token allows us to verify that you have provided a valid email that you have access to. When you are waiting for the token to be emailed, a button labeled "Where's my email" will be presented after 3 minutes. Clicking this button will provide some information on where in the delivery process the email is. Below, we review the different responses, and provide guidance around those responses. 

The registration email is always sent from "noreply@ctl.io" with the subject "Lumen Email Validation Token".

Where's my email response|Action to take|
:---|:---|
Emails may take up to 5 minutes to show in this report. Please try again.|We were unable to report the status of your email.  Email statuses are updated every 5 minutes.  Please wait 5 minutes, and try again.
Email successfully sent at 'date/time'|Your email has been successfully sent, and we have not received a blocked or bounced reply from the receiving email server. If you cannot find the email, please check your spam/junk folder or filters. If you still cannot find the email, please provide the date, time, sender email and subject to your email administrator to diagnose. Please note that a successfully sent email may still be rejected by the destination. Once this happens, the status being reported from "Where's my email" will be updated.
Email was bounced at 'date/time' due to 'reason'|The email was sent, but the receiving email server bounced the message.  Please ensure the email address you provided is correct, as an incorrect email address can cause this error. If it is correct, please provide the date, time, sender email and subject to your email administrator to diagnose.
Email was blocked at 'date/time' due to 'reason'|The email was sent, but the receiving email server blocked the message.  Please ensure the email address you provided is correct. If it is correct, please provide the date, time, sender email and subject to your email administrator to diagnose.

If the above issues did not help you, you can reach out to our support teams, detailed below.

### Contacting the Client Response Center  
The Client Response Center can assist you with issues regarding the following applications:
* Managed Hosting (SavvisStation)
* Private Cloud (Dedicated Cloud Compute)
* Cloud Application Manager
* Support (managedsupport.ctl.io)

_Note: If you are unable to reach any of the above applications due to issues with your Master Account or multi-factor authentication, [contact the customer care team.](#contacting-the-customer-care-team)_

[If you are experiencing an issue with the above, please visit the Managed Services and Support page for contact instructions.](https://www.ctl.io/managed-services/support/)

### Contacting the Customer Care Team  
The Customer Care team can assist with issues regarding your Lumen Master Account. If you are experiencing an issue with this account, send an email to help@ctl.io with details about what you are trying to accomplish and what error you are receiving. You can also include screenshots of the error you are receiving in this email.  

### Frequently Asked Questions
**Q: Why are we releasing this functionality?**

A: These new features are part of an effort to increase the security of your accounts and provide a new and improved support solution.

The Lumen Master Account will enable you to only need one username and password for several of Lumen services. The increased security now supports multi-factor authentication. It is also fully self-service.

**Q: What services does Lumen Master Account currently work with?**

A: Currently the Lumen Master Account works with our Managed Hosting (SavvisStation), Private Cloud (Dedicated Cloud Compute), Cloud Application Manager, and Public Cloud services. This list will be expanded in the future.

**Q: How do I create my Lumen Master Account?**

A:  [Please review this KB article that will walk you through the steps of creating your Lumen Master Account.](lumen-master-account-registration.md)

**Q: What is multi-factor authentication?**

A: Multi-factor authentication is a security standard that requires more than one method of authentication from independent sources to verify the identity of a user. Users who opt-in to multi-factor authentication will need to enter a 6-digit One-Time Password (OTP) every time they log into their Lumen Master Account, in addition to the username and password they set.

**Q: What do I need to know about setting up my multi-factor authentication?**

Multi-factor authentication comes with a few caveats, all of which explained during registration:
1. A smart phone with an app store is required.
2. An OTP Application on the phone is required such as Google Authenticator or OTP Authenticator.
3. You will need to use this soft token OTP app every time you log into your Lumen Master Account.
4. The system clock on the device being used to register your MFA needs to be accurate, or it will generate outdated codes.

[You can read more about setting up multi-factor authentication here.](lumen-master-account-multi-factor-authentication.md)

**Q: Which browsers are currently supported?**

A: Below are the browsers currently supported:  

Browser|Version|
:---|---:|
Chrome|Latest Version
Firefox|Latest Version
Safari|Latest Version
Microsoft Edge|Latest Version
Internet Explorer|11

**Q: Can I link multiple Managed Hosting (SavvisStation), Private Cloud, Public Cloud or Cloud Application Manager accounts to one Lumen Master Account?**

A: At this time, you can only link one of each type of account to a Lumen Master Account. If you have multiple accounts you wish to use, simply skip checking the "Link this account" check box when logging into the service. You will always need to use your Lumen Master Account credentials and ALSO enter your Managed Hosting (SavvisStation)/Private Cloud credentials each time you want to log into the service under this method.

**Q: How can I remove or change a linked account?**

A: [Please review this KB article that will walk you through the steps of managing your linked accounts.](lumen-master-account-linking-and-unlinking-accounts.md)
