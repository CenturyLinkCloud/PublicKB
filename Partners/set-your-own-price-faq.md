{{{
  "title": "Set Your Own Price FAQ",
  "date": "09-30-2015",
  "author": "Mary Cadera",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

CenturyLink Cloud offers customers a way to set custom prices for their sub accounts. We call this feature Set Your Own Price, or SYOP. Using this feature does not change the prices between a customer and CenturyLink Cloud, rather, it provides the customer the opportunity to adjust the prices seen by their sub accounts for that sub account's usage. In addition, customers can leverage our v2 API to generate invoices for their sub accounts based on these custom prices.

##### Who should use the Set Your Own Price (SYOP) Feature?
The SYOP feature should be used by anyone who would like to set prices for their sub accounts that are different from the price they pay to CenturyLink Cloud. This change affects only the prices that are shown to sub accounts, and does not change the amount that customers are responsible for paying to CenturyLink Cloud for their combined accounts' usage.

##### How do I change prices for my sub accounts?
To access the SYOP functionality, navigate to https://control.ctl.io/pricingcatalog. Step-by-step instructions for [setting a default price sheet](/setting-default-prices-for-sub-accounts.md) and [setting a price sheet for a specific sub account](/setting-prices-for-sub-accounts.md) are in our Knowledge Base.

##### What prices can be adjusted?  
Prices for all products appearing in the [online Pricing Catalog](//www.ctl.io/pricing) can be changed, with the sole exception of Support. Support fees are charged as a fixed percentage of a customer's entire bill, and cannot be adjusted via Set Your Own Price at this time.

##### What roles have access to the SYOP feature?
Users with the Billing Manager and Account Admin roles can access SYOP and make changes to prices.

##### What happens when CenturyLink Cloud changes the price of a product? Does this affect the price I have set for my sub accounts?
If you've used the SYOP feature to create a price adjustment for your sub accounts, a price change made by CenturyLink Cloud will not affect that adjustment. It will remain intact, and your sub accounts will continue to recieve the price you have created for them.

If you have _not_ adjusted the price for your sub accounts, a price change by CenturyLink Cloud will automatically roll through your account hierarchy, and your sub accounts prices will be updated.

A CenturyLink Cloud price change will always affect what you owe to CenturyLink Cloud for your account and your sub accounts' usage, regardless of any price adjustments you have created for your sub accounts through the SYOP feature.

##### How do I change the prices for all of my existing subaccounts?
Changes made to the prices in the "Default Pricing Catalog" will affect all sub accounts that do not have an existing custom price adjustment in place for that product. This is true for accounts that currently exist. This default pricing is also applied to new sub accounts at the time that they are created. [You can reference these instructions](/setting-default-prices-for-sub-accounts.md) for step-by-step details on how to create a default price sheet through the Default Pricing Catalog Adjustments UI.

Your Default price sheet's default state is the same pricing that is applied to your parent account. If you do not wish to create custom default prices for your sub accounts - that is, if you wish for your sub accounts to simply inherit the same pricing as their parent account - there is nothing you need to do.

##### How do I change the price for only one of my existing subaccounts?
Customers can set custom prices for a single sub account in their account hierarchy.  Any sub accounts of that sub account will inherit their parent's pricing. [You can reference these instructions](/setting-prices-for-sub-accounts.md) for step-by-step details on how to create a price sheet for a single sub account through the price Adjustments UI.

##### Do sub accounts inherit their parent account's pricing?
Yes. Unless a special price is created for them, a sub account will automatically inherit the custom prices set for their parent. These are the prices set in the Default Pricing Catalog, unless a custom price has been created explicitly for an account through an account adjustment. The Default Pricing Catalog will default to the pricing that the parent account pays to CenturyLink Cloud (meaning that if customers do not wish to adjust their sub account's pricing, there is no action required of them).

##### Will there be a feature flags to allow parent accounts to control their sub accounts' access to SYOP?
There are no feature flags for the SYOP feature at this time. We are targeting to have this added to the Service Catalog in the future, so that users can turn this feature off for their sub accounts - and if they want they can turn it off for themselves too. Stay tuned!
