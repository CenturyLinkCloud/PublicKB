{{{
  "title": "Setting Default Pricing for Sub Accounts",
  "date": "09-30-2015",
  "author": "Mary Cadera",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

CenturyLink Cloud offers customers a way to set custom prices for their sub accounts. We call this feature Set Your Own Price, or SYOP. Using this feature does not change the prices between a customer and CenturyLink Cloud; rather, it provides the customer the opportunity to adjust the prices seen by their sub accounts for that sub account's usage.

**These instructions will help users create a default price adjustment for all sub accounts in their heirarchy. Existing sub accounts that do not already have their own custom prices set will inherit the pricing. New sub accounts will inherit the default pricing too.**

Notes:

* This feature is available to users who have the following roles:
 * Account Admin
 * Billing Manager
* Be sure you are logged in to your user account at the top of your account hierarchy - only a parent account may adjust a sub account's prices. A sub account cannot change its own prices.
* A price change will affect an entire month, there is no mid-month pricing at this time
* Any account appearing in the "Adjustments" list with a dash ("-") in the "Most Recent Account Specific Adjustment" column uses default pricing.

### Process

1. Navigate to https://control.ctl.io/pricingcatalog#/pricingCatalog
2. Select "Default Pricing Catalog Adjustments" from the left navigation bar
3. To create a new price adjustment, click the "create price adjustment" button
4. Create a name for the adjustment (a detailed description, like "New contract pricing", or "September networking price update" is helpful here)
5. Select an effective billing cycle. Please note that price changes will affect the entire month selected, there is no mid-month pricing functionality at this time
6. Select a product to adjust from the drop down menu
7. If desired, select a location, otherwise leave the location set to "default"

   *Example: if you want to change list pricing for almost all data centers, but you have a set of special prices you'd like to create in a single data center, and that data center is CA2; use the "default" location to set your prices, and then create an additional set of prices, with CA2 selected as the data center. This will create one set of prices for all data centers that are _not_ CA2 and a set of prices for CA2.*
8. Enter the new product cost - the "current cost" will be displayed as a reference point - if there is a pricing adjustment already in place for this account and this product, you will see that adjusted price displayed
9. Click "add adjustment"
10. Repeat steps 6 through 9 for any additional products that need to be adjusted
11. When all desired products have been adjusted, click the "save set" button
12. You may preview the sub account's price sheet by selecting the "Default Pricing Catalog" tab in the left navigation bar. Location can be viewed here as well by selecting the data center from the "location" drop down menu.
13. You may view which sub accounts use the default pricing by navigating to the "Adjustments" tab in the left navigation bar. Any account appearing in the list with a dash ("-") in the "Most Recent Account Specific Adjustment" column will inherit the default pricing.
