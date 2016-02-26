{{{
  "title": "Hairpin NAT",
  "date": "2-26-2016",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This article discusses what a Hairpin NAT is and its support within CenturyLink Cloud

### What is a Hairpin NAT?
Also referred to as "hairpinning", [hairpinning](//en.wikipedia.org/wiki/Hairpinning) describes a communication between two hosts behind the same NAT device using their mapped endpoint.

### Hairpinning/Hairpin NAT support
CenturyLink Cloud now supports, as of 2/2/2016, Hairpinning/Hairpin NAT services at a platform level globally. Any [new public IP](../Network/how-to-add-public-ip-to-virtual-machine.md) added to a Virtual or Bare Metal server **after 2/2/2016** is provided this functionality.

### Enabling Hairpinning/Hairpin NAT for existing public IPs
Customers can take one of the following steps to enable services on an existing public IP address bound to a server.

  1. Modify the Firewall rule on the Public IP.  Any modification will apply a new policy that includes support for Hairpinning.
  2. Remove and add a new public IP address to your server.  This likely will result in a new public IP for your service so take caution in using this method.
  3. [Open a support ticket](../Support/how-do-i-report-a-support-issue.md) to request Hairpinning be enabled on your Public IP.  
