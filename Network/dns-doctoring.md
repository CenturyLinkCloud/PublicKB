{{{
  "title": "DNS Doctoring",
  "date": "10-23-2014",
  "author": "James Morris",
  "attachments": []
}}}

<p>As NAT'd public IPs on Centurylink Cloud are not accessible from within the same datacenter we do doctor internal DNS requests to allow machines to still communicate when using public DNS names. Any DNS lookups on external DNS servers that return a NAT
  IP within that datacenter will be re-written to the corresponding internal IP.</p>
<p>&nbsp;</p>
<p>If you wish to avoid this behavior, currently there are 2 workarounds:</p>
<p>1. You can use our internal DNS servers 172.17.1.26 and 172.17.1.27 (or any internal DNS server) as the DNS doctoring only happens on the packets that leave our front-end firewall.</p>
<p>2. You can create a HOSTS file entry on your machines.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>More information on this topic can be found here:&nbsp;</p>
<p><a href="http://www.juniper.net/techpubs/en_US/junos12.1/topics/concept/dns-alg-nat-doctoring-overview.html" target="_blank">http://www.juniper.net/techpubs/en_US/junos12.1/topics/concept/dns-alg-nat-doctoring-overview.html</a>
</p>