{{{
 "title": "Software as a Service (SaaS) Integration API",
 "date": "09-26-2017",
 "author": "Jim Phillips",
 "attachments": [],
 "contentIsHTML": false
 }}}


### Overview

CenturyLink has created multiple opportunities for software vendors to integrate with the Cloud Marketplace. Each of these methods is designed for the provider to be as independent as possible as they work through the integration process.  To be included in the Cloud Marketplace, a SaaS provider must implement one of these methods. During the Marketplace Provider Onboarding Program, we will discuss which integration type is the best fit.

#### API

**Overview**

*The endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint & expected JSON payload during onboarding*

##### Provision Account

The CenturyLink Cloud Marketplace will provide the user interface & collect the information that is required to provision an account on your platform. However, we do not collect Private Card Information (PCI) on your behalf.

You will be able to specify which data points are displayed to your perspective buyer, as well as which are required for them to complete.  This is done through the [Product Provisioning Configuration](./software-as-a-service-product-provisioning.md). In addition to the user input, as configured, CenturyLink will provide the following fields which your API client must tie to the customer for recording usage-based product SKUs (see below) in the future:

* **provisioningId** - String - Unique identifier (GUID) of the provisioning event
* **productSkus** - Array of strings - provisioned product SKU ids
* **productId** - int - marketplace product id

We understand that there will be a need for variability with the API names among our providers but would prefer the following scheme when possible: ```/provider-name-provision-account/```.

The parameters will be passed via a JSON payload. The exact JSON message will vary between providers. We've provided an example below.

```
{
  "provisioningId": "9ddz0a5e-f2d5-6eb5-89b9-7a42d0fbb836",
  "productSkus": ["MRKTPLC-PROVIDER-NAME-PRODCT-NAME"],
  "productId": 123,
  "name": "some customer",
  "email": "customer-email-address@customoredomain.com"
}
```

The status codes your API will need to return are:

* 200 - Account Provisioning Successful (CustomerID from your platform to be returned)
* 40x - Account Provisioning Failure
* 50x - Server Side Error

##### Usage-Based Product SKUs

*The full endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

Some of your products may include [Usage-based billing](./usage-based-billing.md).  Upon provisioning, you are required to track each customer's usage and report it to CenturyLink by the end of each month.  You may report usage for a customer at any time during the month, but keep in mind that every usage report sent is added to the customer's billing.  As such, it is **highly recommended** that you send a single month's usage at the end of each month for each customer.

The cutoff time to bill the customer for the current month is 3:45pm (CST) on the last day of each month.  Any usages reported after 6:00pm (CST) on the last day of the month will be applied to the next month's bill for the customer.  To allow time for processing, Please do not send usage reporting between 3:45pm (CST) and 6:00pm (CST) on the last day of the month.  

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
* 40x - Invalid Input - provisioningId, customerId, providerKey, productId, and productSku required.  usageCount must be a number
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

For any questions, please contact us at [Marketplace@ctl.io](mailto:marketplace@ctl.io).
