{{{
  "title": "Securing Windows Remote Desktop Services (aka RDS, RDP, and/or RPC)",
  "date": "12-30-2013",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Due to many security vulnerabilities with the Windows Remote Desktop Service, it is not recommend this remote service is allowed to communicate directly to the public Internet, and customers should utilize the multiple secure connectivity options Tier
  3 offers (e.g., OpenVPN Client, IPSEC tunnels, cross connects, etc). Although, in the event a secure connectivity option is not available when accessing your Windows server via RDP, customers should strongly consider the following best practices:</p>
<p>#1 - Deploy a Remote Desktop Gateway (RD Gateway). RD Gateways utilize the Remote Desktop Protocol over HTTPS to establish a secure, encrypted connection between remote users on the Internet and customer's Windows servers. For steps to deploy this service,
  please see:
  <br />http://technet.microsoft.com/en-us/library/dd983949</p>

<p>#2 - Ensure you are utilizing strong passwords. Most RDP compromises are due to weak passwords. See the following URL to test the strength of your password(s):
  <br />https://www.microsoft.com/security/pc-security/password-checker.aspx</p>

<p>#3 - Restrict users who can log in using RDP</p>
<p>
  <br />#4 - Keep your systems updated with the latest patches.</p>
<p>
  <br />Note: Many best practice guides for securing RDP will suggest to change the default listening port (3389) to a random unused port (e.g., 56779). This can be effective against certain malware that targets RDP (e.g., https://www.microsoft.com/security/portal/threat/encyclopedia/entry.aspx?Name=Worm%3AWin32%2FMorto.A
  ), yet these ports can be easily discovered via a port scanner.</p>