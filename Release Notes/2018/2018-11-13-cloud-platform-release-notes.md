{{{
"title": "Cloud Platform - Release Notes: November 13, 2018",
"date": "11-13-2018",
"author": "John Gerger",
"attachments": [],
"contentIsHTML": false
}}}

### Enhancements (4)

#### [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/)

**Default pricing page in CAM Management site**

[Cloud Application Manager](https://www.ctl.io/cloud-application-manager/) [Management site](https://account.cam.ctl.io/#/billing) now includes a Pricing section under the Billing page where authenticated users with administrative privileges can check the standard pricing of the different Cloud Application Manager products and services, including the billing type and the hourly or monthly price, depending on the type and the setup fee if any is required. Note that this information is the standard pricing and it does not include any custom pricing terms and/or conditions that the customer may have contracted.  We are currently working on providing those custom terms and conditions so they can be included in this section in the near future.

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

**Display ServiceNow CI value in instance details view**

[Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) now includes the ServiceNow CI value in instances page when the integration with ServiceNow CMDB is configured and the instance is successfully registered there. The CI returned by ServiceNow is stored into the instance metadata and displayed on the right side panel of the instance details view, to better map the instance into the ServiceNow database.

#### [Managed Services Anywhere](//www.ctl.io/cloud-application-manager/managed-services-anywhere/)

**Support for additional AWS metrics**

[Managed Services Anywhere's](//www.ctl.io/cloud-application-manager/managed-services-anywhere/) monitoring agent has been updated to support the collection of more AWS metrics for various services.

**Various bug fixes deployed**

#### [Public Cloud IaaS](//www.ctl.io/product-overview/#)

**WebHook TLS 1.2 Support**

[CenturyLink Cloud's WebHook](//control.ctl.io/Organization/Api/Webhooks) functionality has been upgraded to support TLS 1.2. The enablement of TLS 1.2 provides enhanced security to all consumers of the service.
