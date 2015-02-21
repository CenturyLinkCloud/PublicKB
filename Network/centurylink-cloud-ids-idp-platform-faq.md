{{{
  "title": "CenturyLink Cloud IDS / IDP Platform FAQ",
  "date": "6-29-2014",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": true
}}}

**What technology is used for the CenturyLink Cloud IDS/IDP services?**

CenturyLink Cloud has both IDS and IPS in place using features in our chosen edge firewall product (Juniper SRX) – this software component fulfills both the IDS (detection and logging) and IPS (prevention) roles.</p>

**What type of traffic do the IDS/IDP services filter/log?**

The CenturyLink Cloud platform uses '”screens” to look for specific and common attack traffic. The complete list of supported “screens” can be found at https://www.juniper.net/techpubs/en_US/junos12.1x44/topics/reference/general/security-feature-attack-detection-prevention-support.html

**Can I receive reports and alerts for my specific environment from the IDS/IDP platform?**

Client specific reports and alerts are not available today

**How frequently are the IDS/IDP “screens” updated?**

Bi-Annual

**If a specific attack or event is detected in my environment what remediation and notification steps are taken by CenturyLink Cloud?**

The remediation activities for attacks or events vary greatly depending on the source, target, number of customers affected and type of exploit. CenturyLink Cloud resources will work closely with our customer base to take appropriate steps to resolve these events in a timely manner. This includes, but is not limited to, isolating a specific Virtual Machine to blocking IP addresses of attack sources. Customers are encouraged to review the following KB: [What You Can Expect from CenturyLink Cloud on an Incident](../support/what-can-you-expect-from-centurylink-cloud-on-an-incident)


**Does CenturyLink Cloud offer deep content inspection from its built in IDS/IDP platform?**

No, Clients looking for in depth deep content inspection should contact a CenturyLink Cloud sales resource to review add-on security products.

**What DDoS mitigation services are included in the CenturyLink Cloud platform?**

CenturyLink Cloud uses signature-based DDoS mitigation technology (Juniper Screens). With a signature-based approach, attacks are automatically dropped by the Juniper SRX cluster when an attack’s unique fingerprint is identified, similar to how viruses are detected on PC’s using virus definition files.
