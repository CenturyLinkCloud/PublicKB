{{{
  "title": "Configure Two Factor Authentication for Client VPN",
  "date": "8-11-2014",
  "author": "jw@tier3.com",
  "attachments": []
}}}

Creating two factor authentication is very easy to do with Client VPN Service. Here are the steps to take when needing to configure it:

_WARNING: if you enable AD authentication, all existing users will need to re-download their VPN certificates as their existing certificates will no longer function._

1. Go to Network > VPN from the Control Portal menu.
  ![](../images/vpn-menu.png)

2. From the VPN Configuration page, click the "edit settings" button. The VPN Settings popup will be displayed.
  ![](https://t3n.zendesk.com/attachments/token/cbwjrkakv5cekwj/?name=Screen_Shot_2012-02-01_at_1.18.28_PM.png)

3. In the VPN Settings popup, set the fields as follows

  - **Max Connections** - You are not billed by number of connections, so you may set to the maximum allowed if desired.
  - **Primary DNS and Secondary DNS** - Set this to the DNS Servers (usually your Active Directory servers). NOTE: these need to be in the isolated network provided to you.
  - **AD Authentication** - Make sure this is checked.
  - **Domain Controller IP** - Specify the domain controller to do authentication on.
  - **Binding User DN** - Specify the user to do the LDAP query for authentication. Example: `CN=openvpn_user,CN=Users,DC=domainname,DC=local` which will allow  `openvpn_user` to do the authentication.
  - **Binding Password** - This is the password of the user used in the Binding User DN setting.
  - **User Location DN** - Location of the domain to do the query on. Example: `DC=domainname,DC=local
  - **User Group DN** - This is the group location of the users to do the query on. Any user in this group will have access to logon to the VPN service. Example: `CN=ManagedVPN,CN=Users,DC=domainname,DC=dom`

  ![](https://t3n.zendesk.com/attachments/token/8vmptjc3or8v3p8/?name=Screen_Shot_2012-02-01_at_3.48.39_PM.png)
