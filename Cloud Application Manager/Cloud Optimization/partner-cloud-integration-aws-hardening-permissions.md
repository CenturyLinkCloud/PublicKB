{{{
  "title": "Partner Cloud Integration: CenturyLink Permissions and Access for Optimized AWS Accounts",
  "date": "05-07-2018",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

As discussed in the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/), CenturyLink will provide tools and Operations Staff permissions for Amazon Web Services (AWS) accounts that we harden. The Service Guide provides a high-level overview of those permissions, describing the groups requiring permissions and the type of permissions they are expected to have.

### Audience

Account users that have or are considering CenturyLink Optimization of AWS Accounts. This is for all new AWS accounts created through Cloud Application Manager and any existing account moving into CenturyLink's care.

### Prerequisites

For a new AWS Account:
* The customer must have reviewed the process for creating a [new Amazon Web Services account](partner-cloud-integration-aws-new.md)

For an existing AWS Account:
* The customer must already have an AWS account that has been specifically mentioned in the AWS account transfer process. (Only approved accounts are authorized for this process.)
* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](partner-cloud-integration-aws-existing.md)


### Important Information

#### Root Level Access

CenturyLink does not provide root level access for any account. Root access should be avoided unless absolutely necessary for both Master Payer accounts owned by CenturyLink and any linked account owned by the customer.

For existing accounts, the Customer administrator is asked to set up Multi-Factor Authentication (MFA) access after configuration and keep their key in a secure location. Customers are also asked never to log in with root account access.

For Master Payers and new accounts created through Cloud Application Manager, MFA access is set up after account configuration is complete. The key is kept in an encrypted vault within a domain separated from the main CenturyLink domain.


#### Federated access
All roles described below &mdash; except for the Customer Admin &mdash; maintain a trust with CenturyLink accounts. This allows access to customer accounts to certain CenturyLink users and automated tools, which inherit the permissions and restrictions described with the roles below.

#### IAM Access
The following categories explain how CenturyLink automatically provides or restricts user access.

All policies summarized in this document result from intensive consultation with AWS MSP specialists, and are designed to be in accordance with partner requirements and suggested best practices. All policies have been reviewed and approved by the vendor and third-party auditors.

**Customer Policy**
* **Policy Name**: CTLCustomerPolicy
* **Targeted groups/tools/users**: Any customer user. This policy is applied to all customer IAM Groups.
* **Intent**: To be added to existing customer IAM groups or given to new customer groups. This policy allows the user to manipulate all services within AWS, but restricts certain views and actions that would confuse or cause conflict in an Optimized account.
* **Change Requests**: This will be applied by default, but CenturyLink can work with you to ensure that the policy does not impact existing functionality. If there are any concerns or desired exceptions regarding these policies, please submit a ticket and one of our Product Team members will be glad to discuss it with you.
* **Policy Summary**
  - Restricts the ability to link or unlink from an organization.
  - Restricts deleting CenturyLink-defined IAM policies, roles and additional sundry functions (such as MFA/SAML deletion).
  - Billing/Usage/Budgeting aspects of the portal are restricted to prevent confusion due to CenturyLink consolidated billing. (Optimized accounts have access to this data through Cloud Application Manager's Analytics tools.)


**CenturyLink Developer Policy**
* **Policy Name**: CTLDeveloperPolicy
* **Role Name**: CTLDeveloperRole
* **Targeted groups/tools/users**:Cloud Application Manager's Optimization tool. A limited number of CenturyLink developers have access to the tool.
* **Intent**: The Optimization tool should be able to configure customer accounts, affect IAM permissions, and swiftly remediate any issues.
* **Change Requests**: Because CenturyLink must maintain administrative access, no changes can be made at this time. Please see the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/) for details.
* **Policy Summary**:
  - Full access

**CenturyLink Lambda Policy**
* **Policy Name**: CTLAccountControlsLambdaPolicy
* **Role Name**: CTLAccountControlsLambdaRole
* **Targeted groups/tools/users**: Newly created IAM users that are not in IAM Groups
* **Intent**: Our hardening applies continuous auto-remediation steps to ensure your accounts are protected. IAM users who are not placed within a group will have all their permissions removed, so it is recommended that you move all IAM users to an IAM group. Once they are placed in a group, permissions can be applied again. Newly created IAM groups will automatically have the CTLCustomerPolicy applied. These steps are taken to ensure a seamless experience between Cloud Application Manager and your AWS account. This also allows CenturyLink to ensure that your account continues to meet best practice security guidelines.
* **Change Requests**: This will be applied by default, but as this policy is intended to help, not hinder you, please contact CenturyLink with a support ticket if you find it conflicts with existing functionality.
* **Policy Summary**:
  - Full control of IAM and Config


**CenturyLink Analytics Policy**
* **Policy Name**: CTLCloudOptimization
* **Role Name**: CTLCloudOptimization
* **Targeted groups/tools/users**: Cloud Optimization and Analytics tool
* **Intent**: To enable Analytics tools and allow customer users transparency into usage and best practices.
* **Change Requests**: This is not optional so no change requests can be made.
* **Policy Summary**
  - Get, List, and Describe capabilities for AWS Certificate Manager, Cloud Formation, CloudFront, Cloud HSM, CloudSearch, CloutTrail, CloudWatch, Config, Data Pipeline, Direct Connect, Dynamo DB, EC2, ECS, Elasticache, Elastic Beanstalk, EFS, ELB, Elastic Map Reduce, Elastisearch, Glacier, IAM, Kinesis, key Management Service, Lambda, RDS, Redshift, Route 53, S3, Simple Email Service, Simple DB, Support, Simple Workflow Service, Simple Notification Service, Simple Queue Service, Storage Gateway, and Workspaces.

**Cloud Application Manager Policy**
* **Policy Name**: CTLCAMPolicy, ReadOnlyAccess
* **Role Name**: CTLCAMRole
* **Targeted groups/tools/users**: Cloud Application Manager, Monitoring Service
* **Intent**: To permit Cloud Application Manager's [application lifecycle management (ALM)](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) capabilities and to enable [Monitoring](../Monitoring/CAMMonitoringUI.md).
* **Change Requests**: While this policy is applied by default, [the standard CAM policy](../Deploying Anywhere/using-your-aws-account.md) is intended to be customizable. If you would like to alter the ALM capabilities of Cloud Application Manager, please submit a ticket describing the policy you wish to apply.
* **Policy Summary**
  - All the ability to manipulate resources as described [here](../Deploying Anywhere/using-your-aws-account.md)
  - Allows governance for all EC2 functions
  - Full control of typical autoscaling/Cloud Formation/RDS/S3 tasks
  - Allows IAM user/policy creation, deletion, listing and modification.
  - Allows core Cloud Application Manager functionality and delegation for Managed Services Anywhere assistance.
  - Allows ReadOnlyAccess to enable the [Monitoring](../Monitoring/CAMMonitoringUI.md) feature on Cloud Application Manager

**CenturyLink Service Management Policy**
* **Policy Name**: CTLServiceManagmentPolicy
* **Role Name**: CTLServiceManagmentRole
* **Targeted groups/tools/users**: Service Management Staff
* **Intent**:This is not an immediate part of any Optimization scenario but it is enabled by Cloud Application Manager's Account Optimization. Access to a customer's account via this role is only given to a CenturyLink representative when the customer has purchased Service Management from CenturyLink.
* **Change Requests**: This policy is not currently activated by default, just created. If you need permissions changed, please submit a ticket describing the change you would like.
* **Policy Summary**:
  - Add, Change, and Delete capabilities for all services. No capabilities to edit account details or budgets.*
