{{{
  "title": "How to change a server administrator or root password",
  "date": "1-4-2015",
  "author": "Nathan Young",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>This can be done quite easily through the&nbsp;<a href="https://control.ctl.io/">Lumen Cloud Control Portal</a>. It's important the Control Portal and your server's password match in order to perform certain control functions such as adding disks, IP addresses, and deploying blueprints. There are a couple of pre-requisites that you will need to be able to perform this task:</p>
<ol>
  <li>First you must have an account which has administrator or root access for your company.&nbsp;&nbsp;</li>
  <li>Next you will need to have the prior password for the server which was sent to you when your server was created. If this password has changed, please change it back within the Operating System to match the portal before proceeding.</li>
</ol>
 If you meet both the requirements then you will just need to get logged in to the Control Portal and follow the steps below:
From the left navigation menu choose **Infrastructure** > **Servers**.

<p>This will take you to the Servers page, which lists the servers in your environment. Select the server who's administrator or root password you wish to change then click on the "settings" button.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/GW8PgekfbySURoDbb1tCjIy8T/?name=Screen+Shot+2014-10-16+at+11.03.10+AM.png" alt="Screen_Shot_2014-10-16_at_11.03.10_AM.png" />
</p>

<p>This takes you to the Server Settings page where you can change the server administrator or root password. Click on the "password" field. You must enter the old password in order to change to a new password.</p>
<p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/ShEf6tn51ulDzWeYgXCFb5jjO/?name=Screen+Shot+2014-10-16+at+11.04.38+AM.png" alt="Screen_Shot_2014-10-16_at_11.04.38_AM.png" />
</p>

<p>Press the save button to save your changes and apply your new password.</p>

### Important Information for Windows Domain Controllers and mismatch of root/administrator password between control and server.
 
 Our system periodically connects to VMs in order to get partition information that can be displayed in control. It does this by attempting to use the local administrator account that is registered with it to log in and query the OS. On Domain Controllers this will most likely show periodic failed login attempts you may see in your event logs since a local administrator user does not exist. If you view your server in control, you will not see any partition information displayed, which is the result of a failure to get that information from the server's OS. This is a known control portal limitation if a server password doesn't match the control portal or if the expected administrator/root isn't available. Cloning a Domain Controller is not supported. On both Linux and Windows servers cloning and other automation will fail if passwords don't match.
