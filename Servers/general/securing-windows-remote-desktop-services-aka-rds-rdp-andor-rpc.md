{{{
  "title": "Securing Windows Remote Desktop Services (aka RDS, RDP, and/or RPC)",
  "date": "03-31-2015",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Due to many security vulnerabilities with the Windows Remote Desktop Service, it is not recommend this remote service is allowed to communicate directly to the public Internet, and customers should utilize the multiple secure connectivity options CenturyLink Cloud offers (e.g., OpenVPN Client, IPSEC tunnels, cross connects, etc). Although, in the event a secure connectivity option is not available when accessing your Windows server via RDP, customers should strongly consider the following best practices:</p>

<ol>
<li>Deploy a Remote Desktop Gateway (RD Gateway). RD Gateways utilize the Remote Desktop Protocol over HTTPS to establish a secure, encrypted connection between remote users on the Internet and customer's Windows servers. For steps to deploy this service, please see: http://technet.microsoft.com/en-us/library/dd983949</li>

<li>If any of the previous secure solutions are not feasible options for your organization, and you need to Remote Desktop to your systems over the public Internet, you should at least restrict access to the public IP addresses you assign to each system. You can do this by enabling the "Restrict Traffic to Source IP" option within the Control Portal's configure Public IP configuration screen. For a step-by-step instructions how to perform this traffic restriction, please see: https://www.ctl.io/knowledge-base/network/how-to-add-public-ip-to-virtual-machine/</li>
<li>Keep your systems updated with the latest patches.</li>
</ol>

<p>Note: Many best practice guides for securing RDP will suggest to change the default listening port (3389) to a random unused port (e.g., 56779). Although, this is a futile mitigation attempt since many malware tools will port scan public IP addresses listening for the RDP service.</p>
