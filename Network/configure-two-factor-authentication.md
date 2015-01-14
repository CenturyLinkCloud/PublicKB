{{{
  "title": "Configure Two Factor Authentication",
  "date": "8-11-2014",
  "author": "jw@tier3.com",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Creating two factor authentication is very easy to do with Client VPN Service. Here are the steps to take when needing to configure it:</p>
<p><em><strong>WARNING:&nbsp;if you enable ad authentication all existing users will need to re-download their vpn certificates as their existing certificates will no longer function.</strong></em>
</p>
<ol>
  <li>Go to Network &gt; VPN</li>
  <li>From the Client VPN Main screen go to the <em><strong>VPN Tasks</strong></em> drop down and click <em><strong>Edit VPN.</strong></em>
  </li>
</ol>
<div><strong><em><img src="https://t3n.zendesk.com/attachments/token/cbwjrkakv5cekwj/?name=Screen_Shot_2012-02-01_at_1.18.28_PM.png" alt="Screen Shot 2012-02-01 at 1.18.28 PM.png" /></em></strong>
</div>
<div><strong><em>&nbsp;</em></strong>
</div>
<div>Now lets go and set the settings:</div>
<div>&nbsp;</div>
<div>
  <ol>
    <li>Max Connections: Just set it to the maximum as you are not billed by connections.</li>
    <li>Primary DNS and Secondary DNS: Set this to the DNS Servers (usually your Active Directory servers). NOTE: these need to be in the isolated network provided to you.</li>
    <li>AD Authentication: Make sure that is checked.</li>
    <li>Domain Controller IP: Specify the domain controller to do authentication on.</li>
    <li>Binding User DN: Specify the user to do the ldap query for authentication. Example: "CN=openvpn_user,CN=Users,DC=domainname,DC=local" which will allow the openvpn_user to do the authentication.</li>
    <li>Binding Password: This is the password of the user used in Binding User DN.</li>
    <li>User Location DN: Location of the domain to do the query on. Example: "DC=domainname,DC=local"</li>
    <li>User Group DN: This is the group location of the users to do the query on. Example: "CN=ManagedVPN,CN=Users,DC=domainname,DC=dom" this is the group where any user in this group has access to logon to the VPN service.</li>
  </ol>
  <div><img src="https://t3n.zendesk.com/attachments/token/8vmptjc3or8v3p8/?name=Screen_Shot_2012-02-01_at_3.48.39_PM.png" alt="Screen_Shot_2012-02-01_at_3.48.39_PM.png" />
  </div>
</div>