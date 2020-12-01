{{{
  "title": "Managing security through OpenVPN connections",
  "date": "8-28-2013",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>OpenVPN itself does not do port limiting or any sort of security differentiation between certificates. It is simply a network bridge for its clients,&nbsp;because&nbsp;of this security has to be managed at the server and firewall levels. </p>
<p>In order to limit the ports and IP destinations that OpenVPN clients can communicate to, the OpenVPN server must reside on a&nbsp;separate&nbsp;VLAN from the machines that you wish to limit access to. Once this prerequisite is in place, access from
  the OpenVPN clients can be controlled via firewall rules applying to the OpenVPN client IP range (usually the last 32 addresses of the VLAN the OpenVPN server resides on. This will however apply to all OpenVPN clients regardless of their certificate.</p>
<p>In order to have multiple access policies, multiple OpenVPN server would be required.</p>
<p>It is recommended to use individual certificates for each VPN user. If you need to block an individual's access, simply click the Red Delete button on the Network -> VPN page for the relevant certificate. This will revoke the certificate on the VPN server and disconnect the user if they are currently connected. Once a certificate name has been revoked the same name can never be used again. If you are using a shared certificate and need to revoke an individual's access, you will have to delete the shared certificate, issue a new one, and then redistrubute the certificate to all other valid users. </p>
<p></p>
<p></p>
<p></p>
<p></p>
