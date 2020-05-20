{{{
  "title": "RedHat machines report they are not registered to RHN when running 'yum'",
  "date": "11-25-2019",
  "author": "Matthew Ordman",
  "attachments": [],
  "contentIsHTML": false
}}}

### Red Hat Update Infrastructure

When running 'yum' on a RedHat Enterprise Linux (RHEL) machine deployed in the CenturyLink Cloud, you may receive the following message:

**This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.**

This message is normal and does not indicate any problem, as machines we deploy are themselves not registered to RHN; these machines connect to repositories within our Red Hat Update Infrastructure (RHUI). All base packages for the RHEL distribution in question should be available via the RHUI entitlement installed on your machine at build time.

If for some reason your machine is not able to download packages from our RHUI system, please contact our support team to investigate at help@ctl.io.
