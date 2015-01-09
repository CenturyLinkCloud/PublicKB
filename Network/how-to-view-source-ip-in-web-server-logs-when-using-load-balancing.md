{{{
  "title": "How To:  View Source IP in Web Server Logs when using Load Balancing",
  "date": "11-24-2014",
  "author": "Chris Little",
  "attachments": []
}}}

<h3>Audience</h3>
<p>CenturyLink Cloud clients who make use of our Shared Load Balancing Self-Service offering based on Citrix Netscaler.</p>
<h3>Critical Note</h3>
<p><strong>Only customers leveraging HTTP (tcp/80) load balancing can take advantage of this functionality. &nbsp;Customers using SSL-passthrough and HTTPS (tcp/443) cannot as the load balancers cannot decrypt packets. &nbsp;</strong>
</p>
<h3>Overview</h3>
<p>When using the CenturyLink Cloud platform load balancing services customers who want to view or analyze web server logs find that these logs, by default, only show the MIP (Mapped IP) of the load balancing device as the Source IP. &nbsp;With this out
  of the box configuration web statistical analysis is impossible or not useful. &nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/6xnphxpuztw5qkx/?name=logging+NLB.png" alt="logging_NLB.png" />
</p>
<h3>Solution</h3>
<p><strong>CenturyLink Cloud inserts an X-Forwarded-For&nbsp;header</strong> that can be used to filter the original source IP on a customers web server logs. &nbsp;The following knowledge base articles from Citrix provide details for various web server
  platforms on how to configure Source IP logging.</p>
<p><a href="http://support.citrix.com/article/CTX119347" target="_self">Microsoft Windows 2003</a>
</p>
<p><a href="http://support.citrix.com/article/CTX125526" target="_blank">Microsoft Windows 2008 or Windows 2008 R2 (IIS 7 or 7.5)</a>
</p>
<p><a href="http://support.citrix.com/article/CTX109350" target="_self">Apache 1.3 or 2.0</a>
</p>

