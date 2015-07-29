{{{
  "title": "Platform Specific: Does AppFog provide email support for my application?",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>We do not support email services. While the mail() function in PHP is not disabled, your results would be unreliable and we do not recommend usage. We do offer the Add-On options of <a href="cloudmailin.md">CloudMailin</a> or <a href="mailgun.md">Mailgun</a> which may fulfill your email requirements.</p>
<p>Additionally, if you have a <a href="custom-domain-names.md">Custom Domain</a> you can simply point your MX records to your email service provider and only point the domain name to AppFog. This subject has been popular regarding Google Apps and you may find this article helpful: <a href="https://support.google.com/a/answer/33352?hl=en&amp;topic=2683820&amp;ctx=topic">About MX Records</a>.</p>
