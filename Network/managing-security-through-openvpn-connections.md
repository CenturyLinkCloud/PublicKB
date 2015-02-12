{{{
  "title": "Managing security through OpenVPN connections",
  "date": "8-28-2013",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>OpenVPN itself does not do port limiting or any sort of security differentiation between certificates. It is simply a network bridge for its clients,&nbsp;because&nbsp;of this security has to be managed at the server and firewall levels. </p>
<p>In order to limit the ports and IP destinations that OpenVPN clients can communicate to, the OpenVPN server must reside on a&nbsp;separate&nbsp;VLAN from the machines that you wish to limit access to. &nbsp;Once this prerequisite is in place, access from
  the OpenVPN clients can be controlled via firewall rules applying to the OpenVPN client IP range (usually the last 32 addresses of the VLAN the OpenVPN server resides on. &nbsp;This will however apply to all OpenVPN clients regardless of their certificate.</p>
<p>In order to have multiple access policies, multiple OpenVPN server would be required.</p>
<p></p>
<p></p>
<p></p>
<p></p>