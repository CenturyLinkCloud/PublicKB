{{{
  "title": "Account Specific: Can I change my AppFog account email address?",
  "date": "1-27-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT

This document is for users of AppFog v1. This document does not apply to the current AppFog service that is located in CenturyLink Cloud Control Portal.

### Documentation

<p>Q. Can I change the email address I use to login to my AppFog account?</p>
<p>A. No. Due to how Cloud Foundry (the open-source PaaS underlying AppFog) was designed, each account is permanently associated with a single email address. So unfortunately, we are unable to change your account's email address. However, we have a work around solution: create a new (destination) account, and copy over the source code, environment variables, and database content from your existing (original) account.</p>
<p>To do so, follow the steps oulined in our KB <a href="how-do-i-move-my-apps-and-data-to-another-account.md"<How do I move my Apps and Data to Another Account?</a></p>
