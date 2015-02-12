{{{
  "title": "CenturyLink Cloud IDS / IDP Platform FAQ",
  "date": "6-29-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3><strong>Question:</strong>&nbsp; What technology is used for the CenturyLink Cloud IDS/IDP services?</h3>
<p><strong>Answer:</strong>&nbsp; CenturyLink Cloud&nbsp;has both IDS and IPS in place using features in our chosen edge firewall product (Juniper SRX) – this software component fulfills both the IDS (detection &amp; logging) and IPS (prevention) roles.</p>
<h3><strong>Question:</strong>&nbsp; What type of traffic do the IDS/IDP services filter/log?</h3>
<p><strong>Answer:</strong>&nbsp; The CenturyLink Cloud&nbsp;platform uses '”screens” to look for specific and common attack traffic.&nbsp; The complete list of supported “screens” can be found at <a href="https://www.juniper.net/techpubs/en_US/junos12.1x44/topics/reference/general/security-feature-attack-detection-prevention-support.html">https://www.juniper.net/techpubs/en_US/junos12.1x44/topics/reference/general/security-feature-attack-detection-prevention-support.html</a></p>
<h3><strong>Question:</strong>&nbsp; Can I receive reports and alerts for my specific environment from the IDS/IDP platform?</h3>
<p><strong>Answer:</strong>&nbsp; Client specific reports and alerts are not available today</p>
<h3><strong>Question:</strong>&nbsp; How frequently are the IDS/IDP “screens” updated?</h3>
<p><strong>Answer:</strong>&nbsp; Bi-Annual</p>
<h3><strong>Question:</strong>&nbsp; If a specific attack or event is detected in my environment what remediation and notification steps are taken by Tier 3?&nbsp;</h3>
<p><strong>Answer:</strong>&nbsp; The remediation activities for attacks or events vary greatly depending on the source, target, number of customers affected&nbsp;and type of exploit. &nbsp;CenturyLink Cloud resources will work closely with our customer
  base to take appropriate steps to resolve these events in a timely manner. &nbsp;This includes, but is not limited to, isolating a specific Virtual Machine to blocking IP addresses of attack sources. &nbsp; &nbsp;Customers are encouraged to review the
  following KB: &nbsp;<a href="https://t3n.zendesk.com/entries/21918740-What-can-you-expect-from-Tier-3-on-a-Security-Issue" target="_blank">https://t3n.zendesk.com/entries/21918740-What-can-you-expect-from-Tier-3-on-a-Security-Issue</a>
</p>
<h3><strong>Question:</strong>&nbsp; Does CenturyLink Cloud offer deep content inspection from its built in IDS/IDP platform?</h3>
<p><strong>Answer:</strong>&nbsp; No, Clients looking for in depth deep content inspection should contact a CenturyLink Cloud&nbsp;sales resource to review add-on security products.</p>
<h3>Question: &nbsp;What DDoS mitigation services are included in the CenturyLink Cloud&nbsp;platform?</h3>
<p><strong>Answer:</strong>&nbsp; CenturyLink Cloud&nbsp;uses signature-based DDoS mitigation technology (Juniper Screens). With a signature-based approach, attacks are automatically dropped by the Juniper SRX cluster when an attack’s unique fingerprint
  is identified, similar to how viruses are detected on PC’s using virus definition files.</p>