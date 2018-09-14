{{{
  "title": "Managed Windows Server - Connecting to Your Server with Remote Desktop",
  "date": "10-17-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>This document provides guidance for working with your CenturyLink-managed Windows Server Operating System.</p>
<p>CenturyLink provides overall management for your Windows Server OS, including the primary Admin user privileges.&nbsp;&nbsp; Designated customer user(s) will receive access privileges for new user account creation, user deletion, and other administrative
  tasks. CenturyLink will maintain the primary administrative user account which allows us to effectively monitor and maintain your server OS.</p>
<p><strong>Connecting to Your Server with Remote Desktop</strong>
</p>
<p>When your managed server is initially configured, both a server-specific <strong><em>Local Account</em></strong> user name and password <strong><em>AND</em></strong> a <strong><em>Shared Domain</em></strong> user account and password are created, and
  both credentials can be used to access the machine for administrative purposes via Remote Desktop. The <em>Shared Domain</em> user account information can only be obtained from the CenturyLink Customer Response Center via Trouble
  Ticket. If you already have your Shared Domain credentials, you may use them instead of the Local Account credentials detailed below.</p>
<p>1. To access your server via Remote Desktop using your <strong><em>Local Account</em></strong> user name and password for your Remote Desktop session. Access your server password in the CenturyLink Cloud Control by choosing the ‘<em>click to authenticate</em>’
  link illustrated below<em>.&nbsp;&nbsp; Note:&nbsp; If you have obtained your Shared Domain credentials or created a Dedicated Domain, you may use the appropriate domain user name and password. Your Local Account, Shared Domain, or Dedicated Domain user names and passwords are different from your CenturyLink Cloud Control user name and password.</em>
</p>

<p><img src="https://t3n.zendesk.com/attachments/token/6tfHYCovnaybmZj7pDxCakmxX/?name=Screen+Shot+2014-06-19+at+10.56.00+AM.png" alt="Screen_Shot_2014-06-19_at_10.56.00_AM.png" />
  <br />&nbsp;
  <br />2 Ensure that you have started a VPN session (either client VPN, or through a persistent VPN connection). <strong>Do NOT manage your servers via public IP address!.</strong>
</p>
<p> Start Remote Desktop by clicking <em>Start\All Programs\Accessories\Remote Desktop Connection</em> and type your server’s IP address into the Server test box.
  <br />3. On the Display tab, select a screen resolution that is less than or equal to your current desktop resolution. (for example, 640 x 480, 800 x 600, 1024 x 768)
  <br />4. Press the Connect button. Once a connection has been established to the machine, you will be presented with a security warning. Press the OK button to move to the login screen.
  <br />5. Enter the username and password provided to you in Cloud Control, and select your domain.</p>
<p>NOTE: &nbsp;Your user account information is very powerful. Complex passwords are a key element to keeping your server, and potentially your sensitive company data, secure so please follow these guidelines:</p>
<ul>
  <li>Your password should be a minimum of 8 characters.</li>
  <li>Your password should contain a combination of upper- and lower-case letters.</li>
  <li>Your password should contain at least one number (0-9).</li>
  <li>Your password should contain at least one symbol, such as the # or % signs.</li>
  <li>Your password should not contain your username, known information about you (i.e. your children’s or spouse’s name(s), dates, addresses, etc….) or anything else that could be easily guessed.</li>
</ul>
