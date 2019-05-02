{{{
"title": "Software as a Service (SaaS) Integration Methods",
"date": "05-01-2019",
"author": "Brandy Smith",
"attachments": [],
"contentIsHTML": false
}}}

### Overview

Software Providers that are classified as Software-as-a-Service (SaaS) will need to build out API's to integrate with the Marketplace. Below is a high level overview of the various integration paths available. The technical documentation can be found [here](./software-as-a-service-saas-api.md).

#### API

**Overview**

*The endpoint for the* ```/update-subscription/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint & expected json payload during onboarding*

##### Provision Account

The CenturyLink Cloud Marketplace will provide the user interface & collect the information that is required to provision an account on your platform. However, we do not collect Private Card Information (PCI) on your behalf. The information we are prepared to collect include:

* Username
* Password
* Company Name
* **Account Holders Name**
* **Email Address**
* Address # 1
* Address # 2
* Country
* State or Province
* Zip or Postal Code
* Phone Number
* **Reseller Key**

Only the **bold** fields are required from a CenturyLink perspective. However, you will be able to specify which data points are displayed to your perspective buyer, as well as which are required for them to complete.

We understand that there will be a need for variability with the API names among our providers but would prefer the following scheme when possible: ```/provider-name-provision-account/```.

The parameters will be passed via a json payload. The exact json message will vary between providers. We've provided an example below.

```
{
  "resellerkey": 'xxxx',
  "name": "account holder name",
  "email": "email address"
}
```

The status codes your API will need to return are:

* 201 - Account Provisioning Successful (Co ID from your platform to be returned)
* 40x - Account Provisioning Failure
* 50x - Server Side Error

##### Update Subscription


*The full endpoint for the* ```/update-subscription/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

The elements passed to the ```/update-subscription/``` API include (**bold** items are required):

* **coid** - The ID assigned to the customer from your organization.
* **expired** - True or False. The element should be set to 'true' if the customer has terminated services with your organization. Set the element to 'false' if the services are ongoing.
* expired-date - If **expired** is set to true, this element must be populated with the date the consumer terminated services.
* **sku** - The SKU ID for the product in the CenturyLink Cloud Marketplace. This will be provided to you by CenturyLink.
* count - If the subscription is based on a usage model & or the cost is based off of an incremental value, pass the aggregated usage value in this element.
* **providerkey** - The value of this element will be provided to you by CenturyLink.

An example json payload the ```/update-subscription/``` API is provided below.

```
{
	"coid": '',
    "expired": '',
    "expired-date": '',
    "sku": '',
    "count": '',
    "providerkey": ''
}
```

```/update-subscriptions/``` will return the following status codes.

* 201 - Subscription Successfully Updated
* 40x - Account Provisioning Failure
  * Required element(s) not provided
  * **expired** set to 'true' & **expired-date** not provided
* 50x - Server Side Error

Depending on how your product is billed, you may be required to call ```/update-subscription/``` multiple times per customer subscription so we can ensure the customer is appropriately billed for your services. For any questions, please contact us at [Marketplace@centurylink.com](mailto:Marketplace@centurylink.com).
