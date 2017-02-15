{{{
  "title": "Partner Cloud Integration: Usage Estimates for Azure",
  "date": "01-17-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Use this API operation when you want to get the estimates of month-to-date and end-of-month charges for the Azure account for which CenturyLink provides platform-level support.

### Audience

All CenturyLink customers are invited to use Cloud Integration.

### Prerequisites

* Knowledge of Cloud Application Manager's [partner cloud integration](./partner-cloud-integration.md) feature.

* An existing [ARM Provider created by Cloud Application Manager](./partner-cloud-integration-azure-new.md).

* At least one hour worth of Azure usage.

### Important Information

The estimates provided are based on the best information we have from our partner. It is possible for the estimate to be different than the total presented on a customer's invoice.

To get the estimates, users will currently need to perform an API call.

### Authentication

Reference [API Documentation about authentication](https://www.ctl.io/api-docs/v2/#authentication) to retrieve the Bearer token to include in all other requests.

### URL

**Structure**

```
Get https://cloudintegration.ctl.io/accounts/{accountAlias}/azure/billingestimate
```

**Example**

```
Get https://cloudintegration.ctl.io/accounts/CINT/azure/billingestimate
```

### URI Parameters

Just pass the Authentication and Content-Type Headers

### Response

**Name** | **Type** | **Description**
 --- | --- | ---
 mtdEstimate | float | In dollars, what CenturyLink estimates you would be billed if the month ended today. The month-to-date amount is based on information CenturyLink gets from Azure and is not intended to be 100% accurate.
 eomEstimate | float | In dollars, what CenturyLink estimates you would be billed at the end of the month. The month-end estimation formula is currently prorated based on the number of days in the month and the number of days remaining in the month. Therefore, any spikes or troughs in usage at the beginning of the month will result in inaccurate estimation. As the month progresses, the estimate should get more and more accurate.
