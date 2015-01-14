{{{
  "title": "How To:  Add Public IP to Virtual Machine",
  "date": "11-5-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

How To: &nbsp;Add Public IP to a Virtual Machine&nbsp;
<p>CenturyLink Cloud customers may wish to add a public IP to specific virtual machines in their cloud environment to deliver services. &nbsp; Public IP's are delivered using a 1 to 1 NAT model. &nbsp;</p>
<h3>General Notes &amp; Best Practices</h3>
<ul>
  <li>In its current iteration setting a source IP filter will secure all public ports, single ports or port ranges specified by the customer. &nbsp;Customers can leverage OS based firewall services if they wish to secure public services in a more granular
    fashion.</li>
  <li>Customers are encouraged to leverage the source IP filter unless delivering completely open public internet services to their user community. &nbsp;</li>
  <li>Customers should avoid opening RDP or SSH to their virtual machines to the public internet. &nbsp;As such the following are recommended access methods.</li>
  <ol>
    <li>Use the free OpenVPN client included in every CenturyLink Cloud Account. &nbsp;Refer to&nbsp;<a href="https://t3n.zendesk.com/entries/20914433-How-To-Configure-Client-VPN" target="_blank">https://t3n.zendesk.com/entries/20914433-How-To-Configure-Client-VPN</a>.
      &nbsp;This is the ideal solution for individuals who are mobile and not in fixed office or data center locations.</li>
    <li>Build an IPSEC VPN Tunnel from a remote office or data center location. &nbsp;Refer to&nbsp;<a href="https://t3n.zendesk.com/entries/21808029-Creating-a-Self-Service-IPsec-Site-to-Site-VPN-Tunnel" target="_blank">https://t3n.zendesk.com/entries/21808029-Creating-a-Self-Service-IPsec-Site-to-Site-VPN-Tunnel</a>.
      &nbsp;IPSEC VPN tunnels are best for remote access to Cloud Virtual Machines when administrators are in centralized offices or data centers. &nbsp;</li>
    <li>If either of the previous options are not feasible customers should at a minimum use the source IP filter service on the public IP and pair that with local OS firewall policies within the guest VM. &nbsp;</li>
  </ol>
</ul>
<h3>Add Public IP to Virtual Machine</h3>
<p>1. &nbsp;Open the Servers GUI in the Control Portal</p>
<p>2. &nbsp;Navigate to the Virtual Machine you wish to add a public IP, select Action, Add Public IP</p>
<p><img src="https://t3n.zendesk.com/attachments/token/pD4rAaJGHVHiZzXNabbgusnfs/?name=01.png" alt="01.png" />
</p>
<p>3. &nbsp;In the Add Public IP Address form customers should populate the appropriate fields that meet their business needs. &nbsp;The GUI allows customers to add multiple single port, port ranges and CIDR Source IP ranges. &nbsp;</p>
<ul>
  <li>Internal IP Address: &nbsp;by default the GUI will present the private IP address of the virtual instance currently deployed. &nbsp;As the CenturyLink Cloud leverages a 1 to 1 NAT the public IP will be mapped to this private IP. &nbsp;It is important
    to note that should a customer require more than 1 public IP on a virtual machine the same process applies <em><strong>except </strong></em><strong>&nbsp;</strong>when visiting the GUI the internal IP address field will show '<em><strong>Add new IP</strong></em><strong> address</strong>."
    &nbsp;During the provisioning of the 2nd Public IP, as we use 1 to 1 NAT, a new private IP will also be bound to the virtual machine.</li>
  <li>Public Port(s): &nbsp;A fixed, defined list of frequently used TCP ports customers can simple select from to save time. &nbsp;</li>
  <li>Single Port: &nbsp;A specific TCP or UDP port for an application service</li>
  <li>Port Range: &nbsp;A specific range of TCP or UDP ports for an application service</li>
  <li>Restrict Traffic to Source IP: &nbsp;A flag that allows customers to input a source IP filter on the public IP. &nbsp;If this is <em><strong>not</strong> </em>enabled any ports defined will be accessible by anyone on the public internet. &nbsp;</li>
  <li>Source IP (CIDR): &nbsp;The list(s) of source IP or IP Ranges, in CIDR format, a customer wishes to permit access to the defined TCP or UDP ports. &nbsp;All other traffic will be blocked. &nbsp;Please see&nbsp;<a href="http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing"
    target="_blank">http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing</a>&nbsp;or&nbsp;<a href="http://www.ipaddressguide.com/cidr" target="_blank">http://www.ipaddressguide.com/cidr&nbsp;</a>for more details on proper format of CIDR ranges
    in the interface.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/5Knyvmz71io1cpLJElYHBaXjL/?name=02.png" alt="02.png" />
</p>
<p><img src="https://t3n.zendesk.com/attachments/token/RKl4J0cEhefRQ9bEP59SQKOnv/?name=03.png" alt="03.png" />
</p>

<h3>Edit or Delete Public IP on a Virtual Machine</h3>
<p>1. &nbsp;Open the Servers GUI in the Control Portal</p>
<p>2. &nbsp;Navigate to the Virtual Machine you wish to edit or delete the public IP, select the public IP in Server Info portion of the GUI</p>
<p><img src="https://t3n.zendesk.com/attachments/token/6OJjXOHkmdK5BQbwHKWnSo2R1/?name=04.png" alt="04.png" />
</p>
<p>3. &nbsp;Make the appropriate updates to the Ports, CIDR and other configuration data and select Update IP Address <em><strong>OR</strong></em><strong>&nbsp;</strong>select the Remove Public IP button to delete the Public IP.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/jj3lCcWD7iT3Ba3zW1l4Ss769/?name=05.png" alt="05.png" />
</p>
<h3>Frequently Asked Questions</h3>
<p>1. &nbsp;What happens to my Public IP if I use the pause, power off or archive services in CenturyLink Cloud?</p>
<p>Answer: &nbsp;Public IP addresses are static and using any of these features does not remove the public IP services from the Virtual Machine. &nbsp;The only time a public IP is removed from a virtual machine is a) when the VM is deleted b) the customer
  removes the public IP in the GUI or API</p>
<p>2. &nbsp;How are customers billed for public IP addresses? &nbsp;&nbsp;</p>
<p>Answer: &nbsp;Customers are billed a nominal fee per public IP on a monthly basis. &nbsp;Public IP's are not an hourly billing service and as such using a public IP even for an hour will result in a nominal charge for the public IP address. &nbsp;</p>
