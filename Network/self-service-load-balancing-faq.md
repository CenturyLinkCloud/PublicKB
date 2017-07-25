{{{
  "title": "Self Service Load Balancing FAQ",
  "date": "8-12-2013",
  "author": "jw@tier3.com",
  "attachments": [],
  "contentIsHTML": true
}}}

Self Service Load Balancing FAQ
<h3>Question:&nbsp;What is the default time out value ?</h3>
<p>Answer: The default time out value for client persistence is 2 minutes. For client idle timeout it is 3 minutes.</p>
<h3>Question:&nbsp;When port 443 is selected SSL Offloading is off?</h3>
<p>Answer: At this time there is no SSL offloading of the self service load balancer and all traffic is passed back to the machines being load balanced where the certificate will need to be installed.</p>
