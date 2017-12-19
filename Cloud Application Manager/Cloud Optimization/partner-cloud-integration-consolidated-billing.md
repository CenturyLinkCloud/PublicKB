{{{
  "title": "Partner Cloud: Consolidated Billing",
  "date": "08-20-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Cloud Optimization offers consolidated billing to make payments easy. Standard Consolidated billing includes usage discounts and simplified invoices.

If you require more detail into your billing, that is also offered with [Analytics](../Analytics/CloudApplicationManagerAnalyticsUI.md)

### Audience

All of our customers are invited to use Cloud Optimization via Cloud Application Manager.

### Prerequisites

* An understanding of the features and benefits of [Partner Cloud Integration](partner-cloud-integration.md)

* To experience consolidated billing, the user must have enabled at least one Cloud Optimized provider.


### Important Information

When a customer migrates an existing AWS account to CenturyLink, the customer will receive 2 bills for the first month.

The customer will still receive a bill from AWS for the month that the customer was migrated. AWS will send a bill that cover the usage from the beginning of the month to the time that the account was transferred to CenturyLink. CenturyLink will send a bill from the time the account was transferred till the end of the month.

For tax purposes, CenturyLink defines most services either as IaaS or SaaS.

The patterns of estimates and billing are currently as follows:

Pattern | Description | Timing | Retrieved Data | Availability
--- | --- | --- | --- | ---
Daily Updates | Once per day, CenturyLink provides an updated estimate for all aggregated usage via Cloud Application Manager | The updates occur approximately 3pm UTC (10am Central) | AWS: All data available since the last update; Azure: All data from one day ago, 5am UTC to 4:59 UTC (12:00am to 11:59 Central). | These updates are made for Optimized Amazon Web Services and Optimized Microsoft Azure accounts.
Monthly Usage | On the last day of the month, CenturyLink will take the most updated estimate from the vendor for your Optimized accounts and apply that to your CenturyLink invoice. This will, by necessity, exclude a few hours of the month's usage. | The last update will occur at approximately 3pm UTC (10am Central). Your CenturyLink invoice is normally available on the first day of the new month. | AWS: All data available since the last update; Azure: All data from one day ago, 5am UTC to 4:59 UTC (12:00am to 11:59 Central).   | These updates are made for Optimized Amazon Web Services accounts and Optimized Microsoft Azure accounts.
Reconciliation Usage | Reconciliation charges account for any difference between what CenturyLink charged in monthly usage and what our partners show on finalized invoices. | Reconciliation charges appear on CenturyLink invoices one month in arrears.  | All usage and fees from the previous month are considered in our calculations. |These updates are made for Optimized Amazon Web Services accounts and Optimized Microsoft Azure accounts.
Arrears Usage | Instead of basing invoices off of estimates and reconciling one month later, CenturyLink waits until the vendor's invoice has been finalized before collecting the usage data and providing an invoice.  | Your entire month's usage will be will be billed one month in arrears |  All usage and fees from the previous month are considered in our calculations.  | No partners, currently

Your aggregated charges for all the services from any of your Cloud Optimized accounts  will appear as Cloud Application Manager line items, labeled as the following.

**Monthly Usage**

*AWS*
* Integrated AWS Services IaaS
* Integrated AWS Services SaaS
* Integrated AWS EC2 Services
* Integrated, AWS Reserve Instance Fees - IaaS
* Integrated, AWS Reserve Instances - IaaS

*Azure*
* Integrated Microsoft Azure Services IaaS
* Integrated Microsoft Azure Services SaaS



**Reconciliation**

*AWS*
* Update to Previous Month AWS Services IaaS
* Update to Previous Month  AWS Services SaaS
* Update to Previous Month  AWS EC2 Services
* Update to Previous Month AWS Reserve Instance Fees - IaaS
* Update to Previous Month  AWS Reserve Instances - IaaS

*AZURE* 
* Update to Previous Month Microsoft Azure Services SaaS
* Update to Previous Month Microsoft Azure Services IaaS


**Arrears**

Arrears billing will no longer be used for Azure after October 1, 2017.


  *Exchange Rates*
  
  The way CenturyLink handles Monthly Usage billing for non-US customers is obtain the current exchange rate of the day of the update, not necessarilly the rate for the day associated with the retrieved data (see table above).
  
  The way CenturyLink handles Reconciliation billing for non-US customers is to obtain the exchange rate for the first day of the month for which the Reconciliation data is available, not the rate for any day associated with the month of the retrieved data.

  The way CenturyLink temporarily handles arrears billing for non-US customers is to hold onto a record of all usage until the 27th of the month following the month of actual usage. We then use the conversion rate on the 27th to convert the usage to USD in order for it to be to processed. If you informed CenturyLink that you wanted your invoices to be in your country's currency, that charge will be converted to your currency again on the last day of the month, using that date's exchange rate. CenturyLink makes no guarantee the exchange rates will be the same on the 27th and last days of the month.
