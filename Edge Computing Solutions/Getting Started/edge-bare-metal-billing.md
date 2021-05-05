{{{
  "title": "Edge Bare Metal Billing",
  "date": "3-11-2021",
  "author": "Brandy Smith",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

This article outlines how customers are billed for Edge Bare Metal.
Bare Metal servers are fully integrated into the Lumen Edge Orchestrator Portal, allowing you to self-service create and manage physical servers on-demand.
Provision Edge Bare Metal servers on and off as needed with pay-as-you go flexibility, and host a wide range of apps from a unified interface with ultra low-latency.
Ideal for compute-intensive applications like databases, analytics jobs, grid computing, and other workloads requiring consistent performance.

### How to get an Estimate of Cost for Edge Bare Metal

We have created an [Edge Price Estimator](https://www.ctl.io/estimator/) tool to provide our customers with an easy way to see estimated prices for Edge Computing Solutions.
Customers can use the Price Estimator to get estimated cost of Edge Bare Metal services based on location, OS, Network, and server configurations.
As the Edge Computing Solution platform expands and evolves, the Edge Price Estimator will allow customers to get dynamic estimates for all of their Edge Solutions in one tool.
The Price Estimator makes it easy for customers to Save, Download, and Share the estimate by clicking the **Share/Save Estimate** button.

The following options are available for sharing or saving the Estimate.
1. Download the estimate as a PDF file.
2. Download the estimate as an Excel file.
3. Share via email.
4. Share via a unique URL the Price Estimator tool creates and provides.

### How am I billed for Edge Bare Metal?

Customers are not billed for Edge Bare Metal services until a Bare Metal Server is provisioned via the Edge Orchestrator Portal.

Provisioning a Bare Metal Server has multiple cost factors which are outlined below.

**Location** The hourly cost for a Bare Metal server can vary by location. Please use the [Edge Price Estimator](https://www.ctl.io/estimator/) tool to see the various hourly price per location.
**Bare Metal Server Configurations** The hourly cost for a Bare Metal server can vary by the configuration type. Please use the [Edge Price Estimator](https://www.ctl.io/estimator/) tool to see the various hourly price per configuration type.
**Bare Metal Operating System** The licensing cost for a Bare Metal server can vary by the Operating System type and version. Please use the [Edge Price Estimator](https://www.ctl.io/estimator/) tool to see the various licensing cost per OS type.
Currently, only free Open Source Operating Systems are available, but additional Operating Systems will be made available in future releases.
**Network Type** The cost for a Bare Metal server can vary by network type and usage.
Currently, only Public Internet is available as a Network type, but additional Network types will be made available in future releases.

### Public Internet Egress Charges

For Public Internet, Egress is charged based upon total number of gigabytes transferred over the course of the month.
Bandwidth selection identifies the requested rate limit for the internet port and is selected during the provisioning of the Bare Metal server instance.
**Note:** Higher rate limits can pass more traffic, which could result in additional Internet charges.
Customers should choose the Bandwidth selection that best fits their business needs to avoid unintended Internet charge spikes.
Customers are charged for Bandwidth per GB, partial GB output is rounded up.
Below is the Public Internet egress cost table.

| Public Egress Tier | Price per GB   |
|:------------------:|:--------------:|
| 0-1 GB             | Free           |
| 2GB-10 TB          | $.07           |
| 11-50 TB           | $.06           |
| 51-150 TB          | $.05           |
| 151-500 TB         | $.04           |
| 501+ TB            | $.03           |

## How will I be invoiced for Edge Bare Metal?

Edge Bare Metal allows customers the benefit of self-service management of their costs associated with their Bare Metal instances.
Customers are automatically entered into a pay-as-you go model that allows the flexibility to spin up or delete servers on-demand, as your budget and business needs change.
Customers can also enter into a Term based billing contract with spend discounting. Customers can work with their sales account manager to discuss their Term Commit options.
Once a Bare Metal Server has been successfully provisioned billing starts.
Customers are billed based on the configuration selections outlined above for each Bare Metal Server instance created.
Customers will be invoiced monthly, in arrears for their total Edge Computing Solutions billable charges for active services during that billing period.

The power states and applicable billing for an Edge Bare Metal server are as follows:
* Provision a Bare Metal Server: Starts billing
* On/Running: Continuously bills at the hourly rate based on the server configuration and applicable services tied to the server. 
* Stop: Stops the server but does NOT stop billing. 
* Delete: Deleting a Bare Metal server will end billing for that server.

Deleted servers will be charged based on the configuration, network charges, and other applicable services tied to the server during the up time of the server during a billing cycle.

Currently, this service is only billable in USD. As this offer expands globally, the ability to bill and get estimates via the [Edge Price Estimator](https://www.ctl.io/estimator/) tool in additional currencies will be made available.

## How can I view my Edge Bare Metal bill?

You can view your Edge Bare Metal bills online. Control Center lists your previous 24 months of bills.
You can reach the Control Center portal directly via the Edge Orchestrator portal under the **Support** tab.
You can also reach the Control Center portal [here](https://www.lumen.com/login).

You can learn more about viewing your invoice [here](https://www.lumen.com/help/en-us/control-center/billing/viewing-your-bill.html).
You can learn more about your billing support options [here](https://www.lumen.com/help/en-us/control-center/billing.html).

## How do I cancel my Edge Bare Metal service?

You can stop all billing by deleting all of the Bare Metal instance, and will be charged a final bill of service for the usage on the last billing cycle.
If you want to cancel your Edge Computing Solutions account, please reach out to your sales account manager or to the Lumen Edge Customer Care team 24/7 by phone 800-536-3273 or by email at [EdgeServicesIncident@lumen.com](mailto:EdgeServicesIncident@lumen.com).
