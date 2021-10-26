{{{
  "title": "Managed Windows Server - Connecting to Your Server with Remote Desktop",
  "date": "10-26-2021",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>This document provides guidance for working with your Lumen-managed Windows Server Operating System.</p>
<p>Lumen provides overall management for your Windows Server OS, including the primary Admin user privileges.&nbsp;&nbsp; Designated customer user(s) will receive access privileges for new user account creation, user deletion, and other administrative
  tasks. Lumen will maintain the primary administrative user account which allows us to effectively monitor and maintain your server OS.</p>
<p><strong>Connecting to Your Server with Remote Desktop</strong>
</p>
<p>When your managed server is initially configured, both a server-specific <strong><em>Local Account</em></strong> user name and password <strong><em>AND</em></strong> a <strong><em>Shared Domain</em></strong> user account and password are created, and
  both credentials can be used to access the machine for administrative purposes via Remote Desktop. The <em>Shared Domain</em> user account information can only be obtained from the Lumen Customer Response Center via a Trouble
  Ticket. If you already have your Shared Domain credentials, you may use them instead of the Local Account credentials detailed below.</p>
<p>1. Access your server via Remote Desktop using your <strong><em>Local Account</em></strong> user name and password for your Remote Desktop session. Access your server password in the Lumen Cloud Control by choosing the <b>Click to Authenticate</b>
  link.&nbsp;&nbsp;</b> 
  
  <p><b>Note</b>:&nbsp; If you have obtained your Shared Domain credentials or created a Dedicated Domain, you may use the appropriate domain user name and password. Your Local Account, Shared Domain, or Dedicated Domain user names and passwords are different from your Lumen Cloud Control user name and password.</p>
</p>
<p>
2. Ensure that you have started a VPN session (either client VPN, or through a persistent VPN connection). <strong>Do NOT manage your servers via a public IP address!.</strong>
</p>
<p> 3. Start Remote Desktop by clicking <em>Start\All Programs\Accessories\Remote Desktop Connection</em>, and type your server’s IP address into the Server test box.</p>
  <p>4. On the Display tab, select a screen resolution that is less than or equal to your current desktop resolution. (for example, 640 x 480, 800 x 600, 1024 x 768).</p>
  <p>5. Press the Connect button. Once a connection has been established to the machine, you will be presented with a security warning. Press the OK button to move to the login screen.</p>
  <p>6. Enter the username and password provided to you in Cloud Control, and select your domain.</p>
<p><b>NOTE</b>: &nbsp;Your user account information is very powerful. Complex passwords are a key element to keeping your server, and potentially your sensitive company data secure, so please follow these guidelines:</p>
<ul>
  <li>Your password should be a minimum of 8 characters.</li>
  <li>Your password should contain a combination of upper- and lower-case letters.</li>
  <li>Your password should contain at least one number (0-9).</li>
  <li>Your password should contain at least one symbol, such as the # or % signs.</li>
  <li>Your password should not contain your username, known information about you (i.e., your children’s or spouse’s name(s), dates, addresses, etc….), or anything else that could be easily guessed.</li>
</ul>
