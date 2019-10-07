{{{
  "title": "Configure Email Alerts",
  "date": "12-28-2017",
  "author": "Weiran Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article focusses on how to configure email alerts. **This is a critical step for DR solution, failing to configure email alerts may result in customers not being notified of SafeHaven environment issues in the event of production site outage.**

### Requirements
1. Access to the SafeHaven Console (GUI).
2. Initial replication has been completed for the Protection Group.
3. Periodic checkpoints are enabled for the Protection Group.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Production servers are already protected and Periodic checkpoints for the Protection Group are enabled.

### Check AWS Statistics

Before enabling the email alerts please make sure that the Protection Groups are getting clean checkpoints.

1. Click **Administration** from tools bar at the top and select **Configure e-mail notifications...**
2. Fill in the information of your own SMTP server
3. Check **Use anonymous SMTP service** box (Optional)
4. Enter the **Reply-To Address** and **Port** number. **Use TLS encryption** if applicable
5. Configure **Report Frequency**
5. Click on **Add email address** and type the recipient email address in the pop-up window
6. Click on **Configure and Send Report**
7. Go to recipient's mailbox and check the test email

**NOTE**: If the test email is not received, please re-configure the e-mail notifications settings to work.
The procedure is same for CLC/VMWare/Manual sites as the source datacenters.

**Next Step** is to [Test Failover to AWS](Test Failover to AWS.md). User can also choose to [Create Manual Checkpoint](Create Manual Checkpoint.md)
