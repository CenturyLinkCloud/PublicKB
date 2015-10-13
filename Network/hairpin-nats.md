{{{
  "title": "Hairpin NATs",
  "date": "10-9-2015",
  "author": "Justin Lentz",
  "attachments": [],
  "contentIsHTML": false
}}}

### Hairpin NATs

This article discusses what a Hairpin NAT is and whether it is supported within CLC.

### Information

**Q - What is a hairpin NAT?**

A - Also referred to as "hairpinning", hairpinning describes a communication between two hosts behind the same NAT device using their mapped endpoint. 

**Q- Does CenturyLink Cloud allow hairpinning or Hairpin NATs?**

A - No.

### Workarounds

**Q - What workarounds are available?**

A - There are three solutions which are outlined below.

Option 1.(easiest) - Utilize a host file locally on the VM's where the DNS name needs to resolve locally.  There are a lot of resources available on the web with instructions for modifying your hosts file, but here are some basic instructions.

Windows
- From Start -> Run or from within an explorer window in Server 2012, type notepad c:\windows\system32\drivers\etc\hosts. At the bottom of the file, add a line including the internal IP, hit tab, and then input the DNS name that you want to resolve to the internal IP instead of the external IP.

Linux
- Use SSHto login to your Linux server. Edit the /etc/hosts file with an editor such as vi, pico or emacs. At the bottom of the file, add a line including the internal (private) IP, hit tab, and then input the DNS name that you want to resolve to the internal (private) IP instead of the external (public) IP. Save the /etc/hosts file.

Option 2.(situational) - Utilize the Shared Load Balancer for the public address.  Because the Load Balancer sits in a DMZ zone, the public addresses used here are available from within the same data center.  The Shared Load Balancer only supports traffic on port 80 and 443, and does not support SSL Offloading.  Instructions for utilizing the Shared Load Balancer are found here:  https://www.ctl.io/knowledge-base/network/creating-a-self-service-load-balancing-configuration/

Option 3. Configure a local DNS server and point your servers to use that.  This DNS server will have A records to direct traffic as required and use Root Hints to perform all other external record lookups.
