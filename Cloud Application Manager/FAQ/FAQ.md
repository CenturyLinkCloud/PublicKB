{{{
"title": "FAQ",
"date": "05-18-2017",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

### FAQs

This page contains answers to frequently asked questions on different topics.

**In this article:**
* Costs
* Support
___

### Costs
### When is a customer charged with Application Lifecycle Management charges?
The customer begins incurring charges when an instance is deploy and running using one of the following.

* Application Box<br>
* Script Box<br>
* Template<br>
* Container<br>
* Deployment Policy<br>

### What if an Application Box has multiple Script Boxes?
From a billing perspective, each instance representing a Script Box or a Template in an Application Box is considered its own instance.

### If a customer deploys a Script Box on an existing instance, will there be any additional charge?
No. There are no additional charges when the customer deploys a Script Box on an existing instance using a Deployment Policy.

### Is the platform support fee optional?
No.

### How is an instance defined?
An instance is the output of execution from one of the following box types. An Application Box may
have more than one instance. In terms of billing, an instance is charged only for the uptime of the instance.

* Application Box<br>
* Script Box<br>
* Template<br>
* Container<br>
* Deployment Policy<br>

### A Template Box can be used to deploy a collection of virtual machines along with more than one cloud native service. From a billing perspective, is it still considered a single instance?
Yes, an execution of a Template Box is considered a single instance from billing perspective, even though the template can be used to deploy several virtual machines or cloud native services.

### When does a brown-field instance starts billing?
After registering an auto-discovered instance, all brown-field instances start charging according to the Application Lifecycle Management pricing.

### When a user buys Managed OS on Azure OR AWS, is the user charged on Application Lifecycle Management?
The user is charged on Application Lifecycle Management for the life of the instance. When a user buys Managed OS on Azure OR AWS on that instance, the additional charge for Managed OS is levied on the instance starting from the time the service is applied. The collective charges are $ 0.13 per instance-hour managed.

### How are charges represented on the invoice?
Cloud Application Manager charges are represented on the invoice as one or more of the following line items or
Product/Service:<br>
* Cloud Application Manager<br>
* Cloud Application Manager Appliance<br>
* AWS Services IaaS<br>
* AWS Services SaaS<br>
* Microsoft Azure Services SaaS<br>
* Microsoft Azure Services IaaS<br>
* Cloud Application Manager Support<br>

###  What is included in calculating Platform Support charges?
Platform Support charges are calculated on the combined spend of the following charges:<br>
* Application Lifecycle Management<br>
* AWS Services<br>
* Azure Services<br>

___

### Support

### What is included as part of Platform Support?
Platform Support constitutes:<br>
* [Application Lifecycle Management support](https://www.ctl.io/cloud-application-manager/support/)<br>
* [Azure platform support comparable to Azure Professional Direct](https://azure.microsoft.com/en-us/support/plans/prodirect/)<br>
* [AWS platform support comparable to AWS Business Support](https://aws.amazon.com/premiumsupport/business-support/)<br>
* Managed Services
Full details of Platform Support are [published here](https://www.ctl.io/legal/cloud-application-manager/service-guide/).<br>

### What if the customer has an existing Enterprise Support with AWS or Premier Support with Azure?
Customers can keep their plan by upgrading the Platform Support for additional charges.
