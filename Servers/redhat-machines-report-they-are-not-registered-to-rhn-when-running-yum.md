{{{
  "title": "RedHat machines report they are not registered to RHN when running 'yum'",
  "date": "11-25-2014",
  "author": "James Morris",
  "attachments": [],
  "contentIsHTML": false
}}}

###Red Hat Update Infrastructure

When running 'yum' on a RedHat Enterprise Linux (RHEL) machine deployed in the CenturyLink Cloud, you may receive the following message:

**This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.**

This message is normal and does not indicate any problem, as machines we deploy are themselves not registered to RHN; these machines connect to repositories within our Red Hat Update Infrastructure (RHUI). All base packages for the RHEL distribution in question should be available via the RHUI entitlement installed on your machine at build time.

If for some reason your machine is not able to download packages from our RHUI system, please contact our support team to investigate.

###Bring Your Own Red Hat Network Subscription

You also have the option to bring your own RHN Subscriptions.  If you you choose to use your own RHN Subscriptions, you will need to remove your RHEL machines from our RHUI repositories first before adding your own subscriptions.

#####Remove RHUI Entitlement

yum erase RHEL(version)-(Data Center)T3N*

Examples:

* yum erase RHEL5-WA1T3N*
* yum erase RHEL6-DE1T3N*
* yum erase RHEL7-CA3T3N*
