{{{
  "title": "Managed Red Hat - Connecting to Your Server with SSH",
  "date": "10-17-2014",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>This document provides guidance for working with your Lumen-managed Red Hat Enterprise Linux Operating System.</p>
<p>Lumen provides you overall management for your server OS, including access to the primary root user privileges for new user account creation, user deletion, application installation, and other administrative tasks. Lumen will also maintain
  root access which allows us to effectively monitor and maintain your server OS.</p>
<h3><strong>Connecting to Your Server with SSH</strong></h3>
<p>When your server was initially configured, a customer account was created for your use, and the root account was configured for you to initially access the machine for administrative purposes.&nbsp;&nbsp;</p>
<p>1. You will need the Admin (root) password for your initial SSH session. Access your server password in the Lumen Cloud Control by choosing the ‘<em>click to authenticate</em>’ link illustrated below in the red box, in the upper right corner<em>.&nbsp;&nbsp; Note:&nbsp; Your Admin user name and password are different from your Lumen Cloud Control user name and password. Also, this root account password should not be changed except from within this Lumen Cloud Control interface.</em>
</p>
<p><em><img src="https://t3n.zendesk.com/attachments/token/igx4zrd8DJt6tERYiOu0CqUGt/?name=Overview.jpg" alt="Overview.jpg" /></em>
</p>

<p>2. Use any SSH version 2 compatible client. (SSH, Putty, Secure CRT, WS_FTP).</p>
<p>3. Direct your SSH client to connect to the host server IP that was provided to you by Lumen Cloud Control. This IP is a CLC private network IP. <strong>You should NEVER manage your virtual server through a public IP address but rather, always use a secure tunnel such as a client VPN or site to site VPN connection.</strong>
</p>
<p>4. Once logged in, you should immediately set the password of your non-root management account. Run the command that's <strong>bolded below</strong> and note the resulting account name (shown below in<em> italics</em>) that you can use for your
  regular server operations:</p>
<pre># <strong>passwd $(getent passwd 5000 | cut -d: -f1)</strong><br />Changing password for user <em>clc_test</em>.</pre>
<pre>New password: <strong>********</strong></pre>
<pre>Retype new password: <strong>********</strong></pre>
<pre>passwd: all authentication tokens updated successfully.</pre>

<p>5. Change your password right away, constructing your new password in a manner meaningful to you, but also secure. Please follow the password guidelines that are recommended below.</p>
<p>Linux password strength is handled by a custom <em>PAM(8)</em> configuration that enforces the following policy:</p>
<ul>
  <li>Inclusion of at least three (3) characters from each of the following character classes:
    <ul>
      <li>Digit (0-9)</li>
      <li>Upper case alphabetic</li>
      <li>Lower case alphabetic</li>
      <li>Any other “special” character (non-digit and non-alphabetic)</li>
    </ul>
  </li>
  <li>Minimum nine (9) character password.</li>
  <li>Eight (8) character password if all four (4) of the character classes are used.</li>
  <li>Maximum of two (2) repeating, consecutive characters.</li>
  <li>Five (5) characters in the new password must not be present in the old password.</li>
  <li>Username (straight or reversed) must not be present.</li>
  <li>No dictionary words.</li>
</ul>
<p>Linux password expiration adheres to the following policy:</p>
<ul>
  <li>Maximum number of days a password may be used is ninety (90) days, after which the password will be force expired.</li>
  <li>None of the last twelve (12) passwords for a specific user account may be reused.</li>
  <li>A warning is issued at login time beginning at seven (7) days before password expiration.</li>
</ul>
<p>6. Log out of the highly-privileged root account and reserve your use of it for operations you cannot do using your non-root management account and the sudo privilege escalation command.</p>
<h3><strong>Difficulty Connecting via SSH</strong></h3>
<p>If you should have difficulty connecting via SSH, be sure that you are connecting from an IP address that has port 22 allowed on the Lumen inbound firewall. The firewall rule-set can be reviewed with Lumen Support.</p>
<p>If you have a firewall at your location ensure port 22 is opened for outbound traffic. Additionally, confirm that your SSH client is configured to use port 22 (in all likelihood it is by default).</p>
<p>If you are having problems connecting to your VM, please execute the following trouble-shooting steps (and save your output), prior to contacting Support. Saving your output data will help to expedite the trouble-shooting process.</p>
<p>1. Provide a <em>traceroute(8)</em> output from your source host to the Lumen server destination IP.</p>
<ul>
  <li>Example from a UNIX or Linux source host:</li>
</ul>
<pre>$ <strong>traceroute 216.64.212.85</strong></pre>
<ul>
  <li>Example from a Windows/DOS environment:</li>
</ul>
<pre>C:\&gt;<strong>tracert 216.64.212.85</strong></pre>
<p>2. Ensure that your firewall is open for outbound connections on port 22. Provide output of a telnet to Lumen server destination IP over port 22.</p>
<ul>
  <li>From most operating systems that have the <em>telnet</em> command the following example command line would be executed to test port 22:</li>
</ul>
<pre>$ <strong>telnet 216.64.212.85 22</strong></pre>
<ul>
  <li>A successful connection will display output similar to the following:</li>
</ul>
<pre>$ <strong>telnet 216.64.212.85 22</strong></pre>
<pre>Trying 216.64.212.85...</pre>
<pre>Connected to 216.64.212.85. Escape character is '^]'.</pre>
<pre>SSH-2.0-OpenSSH_5.3</pre>
