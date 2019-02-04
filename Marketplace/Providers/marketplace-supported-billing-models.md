{{{
 "title": "Marketplace Supported Billing Models",
 "date": "01-01-2019",
 "author": "Brandy Smith",
 "attachments": [],
 "contentIsHTML": false
 }}}

 The CenturyLink Cloud Marketplace supports the following billing models:

 * Hourly
 * Monthly
 * Annual - The Marketplace does not support annual billing, however, we can take an annual charge and divide it by twelve and charge the customer that value monthly. Also, term commits can be implemented to a product.
 * One-Time
 * Usage Based
 * Delayed Billing -- Unless Delayed billing is assigned to a SKU, billing will invoke immediately.

 There are several options for delayed billing they are as follows:
 * Expected Delay -- Billing starts with the set delay. The provider will be able to adjust the actual billing start date through the 'Deployments' page.
 * Scheduled Next Month -- Billing starts on the 1 of the month following the purchase date. The provider will be able to adjust the actual billing start date through the 'Deployments' page.
 * Manually -- The provider must proactively start billing manually through the 'Deployments' page, or an API call.

Once a provider determines the method(s) for Billing a product, the SKUs will need to be created.

To build out the APIs and Product Provisioning, the SKUs must be created.
The process for SKU creation is as follows:

* Provider submits pricing information to Marketplace team representative.
* Marketplace team representative formats the SKUs and submits them to the CenturyLink Platform billing team to create the SKUs in staging.
* Once created the Marketplace team representative will assign the SKUs to the provider's alias and associated products in the Provider Portal.
* Provider can then use the SKUs to build out the API calls.
* Once the integration and SKUs have been successfully tested in staging, a Marketplace team representative will submit them to the CenturyLink Platform billing team to create the SKUs in production.


Should you have additional questions, please contact us at [Marketplace@centurylink.com](mailto: Marketplace@centurylink.com).
