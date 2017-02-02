{{{
  "title": "How to configure MX Records",
  "date": "5-9-2012",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>How to configure MX Records</h3>

<p>MX records (Mail Exchanger Records) are used to tell the internet how to route email to your Exchange server or Spam filter. Most email environments use an external Spam filter that will guarantee 100% uptime and no email loss by using multiple
  MX records. The Spam filter will filter out unwanted messages and then route the email to your mail server.</p>
<p>MX records are configured in DNS. To configure MX records using the Control portal follow these steps:</p>
<ol>
  <li>Navigate to Domains -&gt; DNS. Select the DNS zone that corresponds with your email domain</li>
  <li>Select the DNS Tasks drop down and hit Add New Record</li>
  <li>Select type: MX</li>
  <li>In the Exchange field, input the MX record</li>
  <li>Preference: Select 10 for the first record, and ascend for each additional record. The lowest Preference number is used first.</li>
</ol>
<p>See below for an example of inputting an MX record for the domain mydnszone9.com using Postini’s Spam filtering.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/k9go5c3aizbyvep/?name=Input1.png" alt="Input1.png" />
</p>
<p>Below is an example of a complete configuration using Postini.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/gijwpzamcxbkihx/?name=Complete.png" alt="Complete.png" />
</p>
<h4>Additional information:</h4>
<p>MX records tell senders how to send email to your domain. When your domain is registered, it’s assigned several DNS records which enable systems on the Internet to be able to locate it. MX records are part of these records and are required
  for email to flow to your mail server(s).</p>
<h4>Example:</h4>
<p>MX record for mydnszone9.com = mydnszone9.com.s7a1.psmtp.com preference: 10</p>
<p>Mail sent to @mydnszone9.com would lookup MX record and find the above record. It would then route MX (Mail) traffic to mydnszone9.com.s7a1.psmtp.com which is a Postini address. When Postini receives it they will check it for viruses, spoofed
  information, known Spam threats, as well as run the message itself through a rigorous Spam detection process. This whole process takes less than 5 seconds. Once complete, the email will be forwarded to your mail server. Your mail server
  should be configured to ONLY receive email from Postini’s range of IP’s. Otherwise spammers could send mail directly to your servers and bypass Postini.</p>

<p>See this additional article for assistance configuring DNS: <a href="../Control Portal/how-to-use-control-dns.md">How to use Control DNS</a>
</p>

<h4>How to verify your MX records are correct from a Windows computer:</h4>
<ol>
  <li>Launch a command prompt.</li>
  <li>Type: nslookup (press enter)</li>
  <li>Type: set querytype=mx (press enter)</li>
  <li>Type your domain: mydnszone9.com (press enter)</li>
</ol>
<p>This should output your MX records that you entered at Domains -&gt; DNS. They will look like this:</p>
<p>Non-authoritative answer:</p>
<p>Mydnszone9.com MX preference = 10, mail exchanger = mydnszone9.com.s7b2.psmtp.com</p>
