{{{
  "title": "Configure Email Alerts",
  "date": "12-28-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article focusses on how to configure email alerts. **This is a critical step for DR solution, failing in configuring email alerts may result in customers not being notified of  SafeHaven environment issues even produstion site outrage**

### Requirements
1. Access to the SafeHaven Console (GUI).
2. Initial replication has been completed for the Protection Group.
3. Periodic checkpoints are enabled for the Protection Group.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Production servers are already protected and Periodic checkpoints for the Protection Group are enabled

### Check AWS Statistics

Before enabling the email alerts please make sure that the Protection Groups are getting clean checkpoints.

1. Click **Administration** from tools bar
2. Fill in the information of user's own SMTP server
3. Check **Use anonymous SMTP service** box (Optional)
4. Configure **Report Frequency**
5. Click **Add email address** and type the recipient email address on the pop-up window.
6. Click on **Configure and Send Report**
7. Go to recipient's mailbox and check the test email

###Video Tutorial
<iframe width="560" height="315" src="https://www.youtube.com/embed/B3FA9xy5PwY" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
**Next Step** is to [Add and Claim Storage on Production SRN in CenturyLink Cloud]