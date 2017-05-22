{{{
"title": "Software as a Service (SaaS) v1 API",
"date": "04-02-2017",
"author": "Rich DuBose",
"attachments": [],
"contentIsHTML": false
}}}

### Overview

*New integrations with the v1 API are not permitted after April 8, 2017. All providers should should reference the [SaaS v2 API documentation](./software-as-a-service-saas-v2-api.md)*

CenturyLink has created multiple opportunities for software vendors to integrate with the Cloud Marketplace. Each of these methods is designed for the provider to be as independent as possible as they work through the integration process.  To be included in the Cloud Marketplace, a SaaS provider must implement one of these methods. During the Marketplace Provider Onboarding Program, we will discuss which integration type is the best fit.
### Integration Types


#### v1 API

*New integrations with the v1 API are not permitted after April 8, 2017. All providers should should reference the SaaS v2 API documentation*

**Overview**

*The endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint & expected json payload during onboarding*

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

*The full endpoint for the* ```/saas-usage/``` *is not published in this article for security reasons. Your organization will be provided documentation for the endpoint during onboarding*

The elements passed to the ```/saas-usage/``` API include (**bold** items are required):

* **userId** - The ID assigned to the customer from your organization.
* **expired** - **JP - NOT USED - we only have add /JP** True or False. The element should be set to 'true' if the customer has terminated services with your organization. Set the element to 'false' if the services are ongoing.
* expired-date - **JP - see above /JP** If **expired** is set to true, this element must be populated with the date the consumer terminated services.
* **productSku** - The SKU ID for the product in the CenturyLink Cloud Marketplace. This will be provided to you by CenturyLink.
* usageCount - If the subscription is based on a usage model & or the cost is based off of an incremental value, pass the aggregated usage value in this element.
* **providerkey** - **JP - we use partnerId (alias) - we can change it /JP** The value of this element will be provided to you by CenturyLink.

An example json payload the ```/saas-usage/``` API is provided below.
** JP - if we want to terminate subscriptions, we need a new api /JP**

```
{
  "partnerId": ''
	"userId": '',
  "expired": '', // not used
  "expired-date": '', // not used
  "productSku": '',
  "usageCount": '',
  "providerkey": '' // partnerId, currently
}
```

```/saas-usages/``` will return the following status codes.

* 201 - Subscription Successfully Updated
* 40x - Account Provisioning Failure - invalid input
  * Required element(s) not provided
  * **expired** set to 'true' & **expired-date** not provided
* 50x - Server Side Error

If your product bills by usage, you will be required to call ```/saas-usage/``` each month per customer subscription so we can ensure the customer is appropriately billed for your services. For any questions, please contact us at [Marketplace@ctl.io](mailto:marketplace@ctl.io).
