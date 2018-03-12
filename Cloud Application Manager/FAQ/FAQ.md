{{{
"title": "FAQ",
"date": "05-18-2017",
"author": "",
"attachments": [],
"contentIsHTML": false,
"sticky": true
}}}

###FAQ

Here you will find any frequently asked questions for different topics.

**In this article:**
* Costs
* Support
* Invoice
___

### Costs
##### When is a customer charged with Application Lifecycle Management charges?
When an instance is deploy and running using one of the following.

-Application box<br>
-Script box<br>
-Template<br>
-Container<br>
-Deployment Policy<br>

##### What if an Application box has multiple script boxes?
Each instance representing a script box or a template within an application box is considered its own instance from a billing perspective.

##### If a customer deploys a script box on an existing instance will there be any additional charge?
No. There will not be any additional charge if the customer deploys a script box on an existing instance that was deployed using a deployment policy.

##### Is the platform support fee optional?
No.

##### How is an instance defined?
An instance is the output of execution of one of the following box types. Application box may
have more than one instance. In terms of billing, an instance is charged only for the uptime of the instance.

-Application box<br>
-Script box<br>
-Template<br>
-Container<br>
-Deployment Policy<br>

##### A Template Box can be used to deploy a collection of virtual machines along with more than one cloud native service. Is it still a single instance from billing perspective?
Yes, an execution of a Template Box is considered a single instance from billing perspective even though the template can be used to deploy several virtual machines or cloud native services.

##### When does a brown-field instance starts billing?
After registering an auto-discovered instance, all brown-field instances will start charging according to the Application Lifecycle Management pricing.

##### When a user buys Managed OS on Azure OR AWS, is the user charged on Application Lifecycle Management?
User is charged on Application Lifecycle Management for the life of the instance. When they buy Managed OS on Azure OR AWS on that instance, the additional charge for Managed OS is levied on the instance starting from the time of applying that service. The collective charges are $ 0.13 per instance- hour managed.

##### How are charges represented on the invoice?
Cloud Application Manager charges are represented on the invoice as one or more of the following line items
Product/Service<br>
• Cloud Application Manager<br>
• Cloud Application Manager Appliance<br>
• AWS Services IaaS<br>
• AWS Services SaaS<br>
• Microsoft Azure Services SaaS<br>
• Microsoft Azure Services IaaS<br>
• Cloud Application Manager Support<br>

#####  What is included in calculating Platform Support charges?
Platform Support charges are calculated on the combined spend of the following charges<br>
• Application Lifecycle Management<br>
• AWS Services<br>
• Azure Services<br>

___

### Support

##### What is included as part of Platform Support?
Platform Support constitutes<br>
• Application Lifecycle Management support (https://www.ctl.io/cloud-application-manager/support/)<br>
• Azure platform support comparable to Azure Professional Direct (https://azure.microsoft.com/en-us/support/plans/prodirect/)<br>
• AWS platform support comparable to AWS Business Support (https://aws.amazon.com/premiumsupport/business-support/)<br>
• Managed Services
Full details of Platform Support are published at https://www.ctl.io/legal/cloud-application-manager/service-guide/<br>


##### What if the customer has an existing Enterprise Support with AWS or Premier Support with Azure?
Customers can keep their plan by upgrading the Platform Support for additional charges.

___

### Invoice

##### How are Cloud Application Manager charges represented on my invoice?
Charges on your CenturyLink invoice are represented by an alias. Cloud Application Manager currently has three different types of alias' including Billing Account Alias, Cost Center Account Alias and Account Alias.



##### What is a Billing Account Alias?
A billing account alias represents any charges directly associated to the organization level. Currently no charges are applied directly to the billing account alias.

Cloud Application Manager Billing Account Alias
![Billing Account Alias](../../images/cloud-application-manager/cam-organization-alias.png)



##### What is a Cost Center Account Alias?
A cost center account alias represents any charges directly associated to the cost center. Currently no charges are applied directly to the cost center alias.

Cloud Application Manager Cost Center Alias
![Cost Center Account Alias](../../images/cloud-application-manager/cam-costcenter-alias.png)




##### What is a Account Alias?
An account alias represents any charges directly associated to a provider. Currently, all charges of Cloud Application Manager are directly associated to each provider.

Each provider is associated to a cost center and is shown as such in the bill.

Cloud Application Manager Account Alias
![Account Alias](../../images/cloud-application-manager/cam-provider-alias.png)

Invoice Example
![Bill Example](../../images/cloud-application-manager/cam-customer-bill-example.png)


#### Where can I see more detail for my bill?
Customers can login to their Cloud Application Manager account for a [Detailed Billing Report](../Cloud Optimization/partner-cloud-integration-detailed-billing-report.md).  

Customers can also check out our knowledge base for more billing information for [Cloud Optimization charges](../Cloud Optimization/partner-cloud-integration-consolidated-billing.md).

##### What if I have more questions about the bill?
If you have any other questions about your bill please contact [Cloud Application Manager Support](https://www.ctl.io/cloud-application-manager/#Support).
