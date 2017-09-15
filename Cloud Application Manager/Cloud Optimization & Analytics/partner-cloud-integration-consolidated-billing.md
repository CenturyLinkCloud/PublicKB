{{{
  "title": "Partner Cloud: Consolidated Billing",
  "date": "08-20-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Cloud Optimization offers consolidated billing to make payments easy. Standard Consolidated billing includes usage discounts and simplified invoices.

If you require more detail into your billing, that is also offered with [Analytics](./CloudApplicationManagerAnalyticsUI.md)

### Audience

All of our customers are invited to use Cloud Optimization via Cloud Application Manager.

### Prerequisites

* An understanding of the features and benefits of [Partner Cloud Integration](./partner-cloud-integration.md)

* To experience consolidated billing, the user must have enabled at least one Cloud Optimized provider.


### Important Information

For tax purposes, CenturyLink defines most services either as IaaS or SaaS.

The patterns of estimates and billing are currently as follows:

Pattern | Description | Timing | Availability
--- | --- | --- | ---
Daily Updates | Once per day, CenturyLink provides an updated estimate for all aggregated usage via Cloud Application Manager | The updates occur approximately 3am UTC | These updates are made for Optimized Amazon Web Services accounts.
Monthly Usage | On the last day of the month, CenturyLink will take the most updated estimate from the vendor for your Optimized accounts and apply that to your CenturyLink invoice. This will, by necessity, exclude a few hours of the month's usage. | The last update will occur at approximately 5pm UTC. Your CenturyLink invoice is normally available on the first day of the new month. | These updates are made for Optimized Amazon Web Services accounts.
Reconciliation Usage | Reconciliation charges account for any difference between what CenturyLink charged in monthly usage and what our partners show on finalized invoices. Primarily, this is comprised of the last few hours between the last update for Monthly Usage and midnight. | Reconciliation charges appear on CenturyLink invoices  one month in arrears.  | These updates are made for Optimized Amazon Web Services accounts.
Arrears Usage | Instead of basing invoices off of estimates and reconciling one month later, CenturyLink waits until the vendor's invoice has been finalized before collecting the usage data and providing an invoice.  | Your entire month's usage will be will be billed one month in arrears | Microsoft Azure

Your aggregated charges for all the services from any of your Cloud Optimized accounts  will appear as Cloud Application Manager line items, labeled as the following.

**Monthly Usage**

* Integrated AWS Services IaaS
* Integrated AWS Services SaaS
* Integrated AWS EC2 Services
* Integrated, AWS Reserve Instance Fees - IaaS
* Integrated, AWS Reserve Instances - IaaS


**Reconciliation**

* Update to Last Month’s AWS Services IaaS
* Update for Last Month’s AWS Services SaaS
* Update for Last Month’s AWS EC2 Services
* Update for Last Month’s AWS Reserve Instance Fees - IaaS
* Update for Last Month’s AWS Reserve Instances - IaaS

**Arrears**

* Integrated Microsoft Azure Services IaaS
* Integrated Microsoft Azure Services SaaS

  *Exchange Rates*

  The way CenturyLink temporarily handles arrears billing for non-US customers is to hold onto a record of all usage until the 27th of the month following the month of actual usage. We then use the conversion rate on the 27th to convert the usage to USD in order for it to be to processed. If you informed CenturyLink that you wanted your invoices to be in your country's currency, that charge will be converted to your currency again on the last day of the month, using that date's exchange rate. CenturyLink makes no guarantee the exchange rates will be the same on the 27th and last days of the month.
