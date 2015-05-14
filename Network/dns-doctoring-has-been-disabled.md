{{{
  "title": "DNS Doctoring has been disabled",
  "date": "05-14-2015",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>DNS Doctoring was disabled on 5/13 at ~6 PM PST.  This means that we no longer modify DNS packets that come in or out of the edge firewall.

A more thorough definition is found in Juniper's documentation: http://www.juniper.net/techpubs/en_US/junos12.1/topics/concept/dns-alg-nat-doctoring-overview.html
</p>

<p>Some customers may have been using DNS doctoring.  Here is an example:</p>

<p>App server A: APP01, 10.5.5.12  (with public IP 8.6.6.5, which has DNS configured for Acme.app.com)</p>

<p>Web server B: WEB01, 10.5.5.13</p>

<p>Previously with DNS doctoring enabled, if WEB01 tried to access Acme.app.com, the Edge firewall would modify the incoming DNS response to 10.5.5.12 instead of 8.6.6.5.  The Web and App server would communicate via internal IP's instead of trying to Hairpin with 8.6.6.5(which we do not allow)

Now with DNS doctoring disabled, if WEB01 tried to access Acme.app.com, the firewall would NOT alter the DNS packet, and WEB01 would try and access 8.6.6.5 instead of 10.5.5.12.
</p>

<p>The easiest workaround is to utilize a host file locally on the VM's where the DNS name needs to resolve locally.  There are a lot of resources available on the web with instructions for modifying your hosts file, but here are some basic instructions.</p>  
<p>For Windows:From Start -> Run or from within an explorer window in Server 2012, type "notepad c:\windows\system32\drivers\etc\hosts"
At the bottom of the file, add a line including the internal IP , hit tab, and then input the DNS name that you want to resolve to the internal IP instead of the external IP</p>
<p>For Linux:Use ssh to login to your linux server.  Edit the /etc/hosts file with an editor such as vi, pico or emacs.  At the bottom of the file, add a line including the internal (private) IP, hit tab, and then input the DNS name that you want to resolve to the internal (private) IP instead of the external (public) IP.</p>

<p>A more robust and scalable solution is to host a local DNS server and point your servers to use that.</p> 


