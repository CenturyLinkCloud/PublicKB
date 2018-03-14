{{{
  "title": "Partner Cloud Integration: CenturyLink AWS Reserved Instance Strategy",
  "date": "2-7-2018",
  "author": "Andy Watson",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

CenturyLink [Cloud Application Manager's](https://www.ctl.io/cloud-application-manager/) Cloud Optimization offers [consolidated billing](partner-cloud-integration-consolidated-billing.md)to make payments easy. Part of the consolidated billing involves CenturyLink's strategy for billing Amazon Web Services [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html).


### Audience

Users of accounts that already have or are considering CenturyLink Optimization of AWS Accounts. This is for all new standard AWS accounts created through Cloud Application Manager and any existing account moving into CenturyLink's care who have bought Amazon Web Services Reserved Instances.


### Prerequisites

For a new AWS Account:

* The customer must have reviewed the process for creating a [new Amazon Web Services account](partner-cloud-integration-aws-new.md) and is thinking about buying AWS Reserved Instances.

For an existing AWS Account:

* The customer must already have an AWS account that has been specifically mentioned in the AWS account transfer process. (Only approved accounts are authorized for this process.)

* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](partner-cloud-integration-aws-existing.md)

* The customer has purchased AWS Reserved Instances or is thinking about buying AWS Reserved Instances.


### Important Information

#### Customer Reserved Instances

Reserved Instances purchased prior to transferring to CenturyLink may still be used and must always stay with the account at which they were purchased.  If the Customer purchased Reserved Instances from a Master Payer they own, they can still use those Reserved Instances while under CenturyLink's care. Please review the process for migrating an [existing Amazon Web Services account](partner-cloud-integration-aws-existing.md), specifically the "Considerations" section.

Standard customer AWS accounts reside in one CenturyLink owned AWS Organization.

The CenturyLink AWS Organization provides safeguards to make sure the customer is getting the full benefits of the AWS Reserved Instances that they have purchased while with CenturyLink. These safeguards also apply to Reserved Instances that existed before the account was migrated to CenturyLink.

If you want to purchase Reserved Instances which exceed the limit prescribed by AWS, please contact [Cloud Application Manager Support](https://www.ctl.io/cloud-application-manager/#Support) with your request.

(Please note that Reserved Instances do not apply to the CenturyLink 5% EC2 OnDemand Discount)

#### AWS Reserved Instance Initial Purchase Fee
AWS allows customers to buy Reserved Instances and choose between three payment options: All Upfront, Partial Upfront, and No Upfront.

If you choose the Partial or All Upfront payment option, the initial purchase fee will be shown as a different line in your CenturyLink bill.

CenturyLink splits the different products that RI's can be bought into two different categories, Software as a Service(SaaS) and Infrastructure as a Service(IaaS). These monthly increments are displayed on your bill with the line item description below and will be displayed as IaaS or SaaS depending on the product category.


Line item description on your bill: Integrated, AWS Reserve Instance Fees - IaaS


Line item description on your bill: Integrated, AWS Reserve Instances - SaaS


#### Customer Reserved Instance Monthly Increments

Customers who buy an AWS Reserved Instance with the Partial or No Upfront payment options have to pay the remaining balance in monthly increments over the term of the RI. These monthly increments are displayed on your bill with the line item description below.

Line item description on your bill: AWS Monthly EC2 Reserved Instance Charges


#### Customer Reserved Instances Monthly Increments that are not EC2
AWS continues to expand the different products that are available to purchase Reserved Instances. CenturyLink accommodates this with any RI that is not an EC2 instance and receives monthly increment charges for those RI's will have the charges displayed on your bill with the line item description below.

Line item description on your bill: Integrated, AWS Reserve Instances - SaaS


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.
