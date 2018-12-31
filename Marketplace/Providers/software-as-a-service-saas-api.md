{{{
 "title": "Software as a Service (SaaS) Integration API",
 "date": "01-01-2018",
 "author": "Jim Phillips",
 "attachments": [],
 "contentIsHTML": false
 }}}


### Overview

CenturyLink has created multiple opportunities for software vendors to integrate with the Cloud Marketplace. Each of these methods is designed for the provider to be as independent as possible as they work through the integration process.  To be included in the Cloud Marketplace, a SaaS provider must implement one of these methods. During the Marketplace Provider Onboarding Program, we will discuss which integration type is the best fit.

#### API

**Overview**

*The endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint & expected JSON payload during onboarding*

##### Dependencies

To build out the APIs, the SKUs must be created. The process for SKU creation is as follows:
* Provider submits pricing information to Marketplace team representative.
* Marketplace team representative formats the SKUs and submits them to the CenturyLink Platform billing team to create the SKUs in staging.
* Once created the Marketplace team representative will assign the SKUs to the provider's alias and associated products in the Provider Portal.
* Provider can then use the SKUs to build out the API calls.


##### Deploy Software or Services

The CenturyLink Cloud Marketplace will provide the user interface & collect the information that is required to deploy the software or services to an account on your platform. However, we do not collect Private Card Information (PCI) on your behalf.

You will be able to specify which data points are displayed to your perspective buyer, as well as which are required for them to complete.  This is done through the [Product Deployment Configuration](software-as-a-service-product-provisioning.md). In addition to the user input, as configured, CenturyLink will provide the following fields which your API client must tie to the customer for recording usage-based product SKUs (see below) in the future:

* **provisioningId** - String - Unique identifier (GUID) of the provisioning event
* **productSkus** - Array of strings - provisioned product SKU ids
* **productId** - int - marketplace product id

The parameters will be passed via a JSON payload. If you do not add a required field with "email" in the name, a required "Contact Email" field will be added to the form.  The exact JSON payload will vary between providers, based on configuration of the product. At a minimum, all fields in the example below **always** will be sent in the payload delivered to your API.  

```
{
  "provisioningId": "9ddz0a5e-f2d5-6eb5-89b9-7a42d0fbb836",
  "productSkus": ["MRKTPLC-PROVIDER-NAME-PRODCT-NAME"],
  "productId": 123,
  "contactEmail": "customer-email-address@customerDomain.com",
  "userAlias": "ABCD"
}
```

The status codes your API will need to return are:

* 200 - Success (CustomerID from your platform to be returned)
* 40x - Invalid inputs - The error message (body or string) will be displayed to the user
* 50x - Server Side Error - A generic error message will be displayed to the user

**Note**

Return payload to CenturyLink upon completed registration must return the customerId:

```
{ “customerId”: “YOUR-CUSTOMERID-STRING” }  
```

YOUR-CUSTOMERID-STRING can be a number, but you must pass it as a string.
While customerId is the only required field, you can return any other information you wish.
All returned data will be stored for future reference.

##### Delayed Billing Start

Some providers require manual work before a customer begins use of the products.  To accommodate this, we have implemented delayed billing options, available for each defined SKU. You must notify a CenturyLink Marketplace representative of which billing model you want assigned to each SKU.

The options are to start billing are:
 * Immediately
 * Expected Delay -- Billing starts with the set delay. The provider will be able to adjust the actual billing start date through the 'Deployments' page.
 * Scheduled Next Month -- Billing starts on the 1 of the month following the purchase date. The provider will be able to adjust the actual billing start date through the 'Deployments' page.
 * Manually -- The provider must proactively start billing manually through the 'Deployments' page, or an API call.

SKUs with a delayed timeframe (e.g. 3 days or 1 week), will automatically start billing at the scheduled time.  You will be able to update the scheduled time through the provider portal in case you experience delays.

SKUs implementing the manual start billing option will not start billing until you report the software or service has been started for the customer.  You can report this manually through the provider portal, within the **Deployments** tab, or by making an API call, detailed below.  You may also include SKUs that were set to start billing at a specified time.

*The full endpoint for the* ```/start-billing/``` *API is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

The elements passed to the ```/start-billing/``` API must include the following items:

* **providerKey** - String - Your unique identifier, provided by CenturyLink.
* **customerid** - String - The ID assigned to the customer from your organization, returned by your API in the provisioning API call.
* **provisioningId** - String - Unique identifier (GUID) of the provisioning event
* **productId** - int - The product id for the product in the CenturyLink Cloud Marketplace. This is provided in the provisioning API call.
* **productSkus** - Array - A list of SKUs for which to start billing.

An example JSON payload the ```/start-billing/``` API is provided below.

```
{
  "providerKey": "SOME-UNIQUE-IDENTIFIER",
  "customerId": "1234",
  "provisioningId": "9ddz0a5e-f2d5-6eb5-89b9-7a42d0fbb836",
  "productId": 123,
  "productSkus": [
    "MRKTPLC-PROVIDER-NAME-PRODCT-NAME-1",
    "MRKTPLC-PROVIDER-NAME-PRODCT-NAME-2"
  ]
}
```

```/start-billing/``` will return the following status codes.

* 200 - Billing has started for the given product SKUs.
* 40x - Invalid Input - provisioningId, customerId, providerKey, productId, and productSkus required.  productId must be an integer
* 50x - Server Side Error

##### Usage-Based Product SKUs

Some of your products may include Usage-based billing.  Upon provisioning, you are required to track each customer's usage and report it to CenturyLink by the end of each month.  You may report usage for a customer at any time during the month, but keep in mind that every usage report sent is added to the customer's billing.  As such, it is **highly recommended** that you send a single month's usage at the end of each month for each customer.

The cutoff time to bill the customer for the current month is 3:45pm (CST) on the last day of each month.  Any usages reported after 6:00pm (CST) on the last day of the month will be applied to the next month's bill for the customer.  To allow time for processing, Please do not send usage reporting between 3:45pm (CST) and 6:00pm (CST) on the last day of the month.  

*The full endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

The elements passed to the ```/saas-usage/``` API must include the following items:

* **providerKey** - String - Your unique identifier, provided by CenturyLink.
* **customerid** - String - The ID assigned to the customer from your organization, returned by your API in the provisioning API call.
* **provisioningId** - String - Unique identifier (GUID) of the provisioning event
* **productSku** - String - The SKU id associated to the product in the CenturyLink Cloud Marketplace. This is provided as one of the array values in the provisioning API call.
* **productId** - int - The product id for the product in the CenturyLink Cloud Marketplace. This is provided in the provisioning API call.
* **usageCount** - double - the amount

An example JSON payload the ```/saas-usage/``` API is provided below.

```
{
  "providerKey": "SOME-UNIQUE-IDENTIFIER",
  "customerId": "1234",
  "provisioningId": "9ddz0a5e-f2d5-6eb5-89b9-7a42d0fbb836",
  "productSku": "MRKTPLC-PROVIDER-NAME-PRODCT-NAME",
  "productId": 123,
  "usageCount": 100.5
}
```

```/saas-usages/``` will return the following status codes.

* 200 - Usage Successfully Added
* 40x - Invalid Input - provisioningId, customerId, providerKey, productId, and productSku required.  productId must be an integer and usageCount must be a number (float | decimal | integer)
* 50x - Server Side Error

##### Software Termination

*The full endpoint for the* ```/saas-usage/end``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

When a customer terminates his or her service through your website, you will need to notify us so we can stop billing the customer.  We have created an API endpoint.  The inputs are nearly identical to the ```/saas-usage``` endpoint detailed above, except the productSKUs is an array instead of a string and there is no usage count.

The elements passed to the ```/saas-usage/end``` API must include the following items:

* **providerKey** - String - Your unique identifier, provided by CenturyLink.
* **customerid** - String - The ID assigned to the customer from your organization, returned by your API in the provisioning API call.
* **provisioningId** - String - Unique identifier (GUID) of the provisioning event
* **productSkus** - Array of Strings- The list of SKU ids associated to the product in the CenturyLink Cloud Marketplace for which the customer has terminated services.
* **productId** - int - The product id for the product in the CenturyLink Cloud Marketplace. This is provided in the provisioning API call.

An example JSON payload the ```/saas-usage/end``` API is provided below.

```
{
  "providerKey": "SOME-UNIQUE-IDENTIFIER",
  "customerId": "1234",
  "provisioningId": "9ddz0a5e-f2d5-6eb5-89b9-7a42d0fbb836",
  "productSkus": [
    "MRKTPLC-PROVIDER-NAME-PRODUCT-NAME",
    "MRKTPLC-PROVIDER-NAME-SECOND-PRODUCT"
  ],
  "productId": 123
}
```

```/saas-usages/end``` will return the following status codes.

* 200 - Termination notification received
* 40x - Invalid Input - provisioningId, customerId, providerKey, productId, and productSkus required.
* 50x - Server Side Error

For any questions, please contact us at [Marketplace@centurylink.com](mailto:Marketplace@centurylink.com).
