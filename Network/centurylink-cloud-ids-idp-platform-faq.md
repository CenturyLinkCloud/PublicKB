{{{
  "title": "CenturyLink Cloud IDS / IDP Platform FAQ",
  "date": "3-6-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Q: What technology is used for the CenturyLink Cloud IDS/IDP services?</strong></p>
<p>A: CenturyLink Cloud has both IDS and IPS in place using features in our chosen edge firewall product (Juniper SRX) – this software component fulfills both the IDS (detection & logging) and IPS (prevention) roles.</p>

<p><strong>Q: What type of traffic do the IDS/IDP services filter/log?</strong></p>
<p>A: The CenturyLink Cloud platform uses ”screens” to look for specific and common attack traffic.  The complete list of supported “screens” can be found on <a href="https://www.juniper.net/techpubs/en_US/junos12.1x44/topics/reference/general/security-feature-attack-detection-prevention-support.html">Juniper's Website</a></p>

<p><strong>Q: Can I receive reports and alerts for my specific environment from the IDS/IDP platform?</strong></p>
<p>A: Client specific reports and alerts are not available today.</p>

<p><strong>Q: If a specific attack or event is detected in my environment what remediation and notification steps are taken by CenturyLink Cloud Support?</strong></p>
<p>A: The remediation activities for attacks or events vary greatly depending on the source, target, number of customers affected and type of exploit.  CenturyLink Cloud resources will work closely with our customer base to take appropriate steps to resolve these events in a timely manner.  This includes, but is not limited to, isolating a specific Virtual Machine to blocking IP addresses of attack sources.    Customers are encouraged to review <a href="http://www.ctl.io/knowledge-base/support/what-can-you-expect-from-tier-3-on-a-security-issue">our KB that covers what behavior customers can expect from CenturyLink Cloud Operations in the case of a security incident.</a></p>

<p><strong>Q: Does CenturyLink Cloud offer deep content inspection from its built in IDS/IDP platform?</strong></p>
<p>A: No, Clients looking for in depth deep content inspection should contact a CenturyLink Cloud sales resource to review add-on security products.</p>

<p><strong>Q: How frequently are the IDS/IDP “screens” updated?</strong></p>
<p>A: Bi-Annual.</p>

<p><strong>Q: What DDoS mitigation services are included in the CenturyLink Cloud platform?</strong></p>
<p>A: CenturyLink Cloud uses signature-based DDoS mitigation technology (Juniper Screens). With a signature-based approach, attacks are automatically dropped by the Juniper SRX cluster when an attack’s unique fingerprint is identified, similar to how viruses are detected on PC’s using virus definition files.</p>
