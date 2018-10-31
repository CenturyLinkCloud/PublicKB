{{{
  "title": "Partner Cloud Integration: CenturyLink Permissions and Access for Optimized AWS Accounts",
  "date": "10-11-18",
  "author": "Benjamin Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

As discussed in the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/), CenturyLink will provide tools and Operations Staff permissions for Amazon Web Services (AWS) accounts that we harden. The Service Guide provides a high-level overview of those permissions, describing the groups requiring permissions and the type of permissions they are expected to have.

### Audience

Account users that have or are considering CenturyLink Optimization of AWS Accounts. This is for all new AWS accounts created through Cloud Application Manager and any existing account moving into CenturyLink's care.

### Prerequisites

*NOTE:* To facilitate the hardening process, the customer must enable the "CTLDeveloperRole".  Once this is enabled, the hardening process will configure the remaining roles below.

For a new AWS Account:
* The customer must have reviewed the process for creating a [new Amazon Web Services account](partner-cloud-integration-aws-new.md)

For an existing AWS Account:
* The customer must already have an AWS account that has been specifically mentioned in the AWS account transfer process. (Only approved accounts are authorized for this process.)
* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](partner-cloud-integration-aws-existing.md)


### Important Information

#### Root Level Access

CenturyLink does not provide root level access for any account. Root access should be avoided unless absolutely necessary for both Master Payer accounts owned by CenturyLink and any linked account owned by the customer.

Customers with existing accounts are asked to deliver root account credentials to CenturyLink per the Service Guide. This includes root email, root password, and MFA’s secret configuration key. You may continue to use your IAM credentials.

For Master Payers and new accounts created through Cloud Application Manager, MFA access is set up after account configuration is complete. The key is kept in an encrypted vault within a domain separated from the main CenturyLink domain.


#### Federated access
All roles described below &mdash; except for the Customer Admin &mdash; maintain a trust with CenturyLink accounts. This allows access to customer accounts to certain CenturyLink users and automated tools, which inherit the permissions and restrictions described with the roles below.

#### IAM Access
The following categories explain how CenturyLink automatically provides or restricts user access.

All policies summarized in this document result from intensive consultation with AWS MSP specialists, and are designed to be in accordance with partner requirements and suggested best practices. All policies have been reviewed and approved by the vendor and third-party auditors.

#### Hardening, Re-Hardening, Overrides, and Exceptions
The following IAM hardening roles and policies are applied at the time the account is optimized. Additionally, CenturyLink will occasionally re-apply these policies. The entire process is applied to any optimized account to which CAM still has administrative rights. Any deviations from the standard will be overwritten except where there are overrides or customizations.

Overrides can be be performed by customer users with appropriate permissions or by CenturyLink Support Staff. Where the CAMOverridePolicy and CAMOpsOverridePolicy are used, users may modify permissions of CAM, Admin Users, and CenturyLink CenturyLink Support Staff via the AWS IAM Console. These policies will not be overwritten when account hardening is re-applied. Please be aware that these polices may be applied to several roles.

Change Requests may result in exceptions to hardening. Please read the "Change Request" sections below. If you submit one and it is accepted, CAM will not be able to overwrite those changes as a result of future hardening attempts.


**Customer Role**
* **Attached Policy Names**: CTLCustomerPolicy
* **Targeted groups/tools/users**: Any customer user. This policy is applied to all customer IAM Groups.
* **Intent**: To be added to existing customer IAM groups or given to new customer groups. This policy allows the user to manipulate all services within AWS, but restricts certain views and actions that would confuse or cause conflict in an Optimized account.
* **Change Requests**: This will be applied by default, but CenturyLink can work with you to ensure that the policy does not impact existing functionality. If there are any concerns or desired exceptions regarding these policies, please submit a ticket and one of our Product Team members will be glad to discuss it with you.
* **Policy Summary**
  - Restricts the ability to link or unlink from an organization.
  - Restricts deleting CenturyLink-defined IAM policies, roles and additional sundry functions (such as MFA/SAML deletion).
  - Billing/Usage/Budgeting aspects of the portal are restricted to prevent confusion due to CenturyLink consolidated billing. (Optimized accounts have access to this data through Cloud Application Manager's Analytics tools.)

  **CenturyLink Operations Role**
  * **Attached Policy Names**: ReadOnlyAccess, CTLOperationsPolicy, CAMOpsOverridePolicy
  * **Targeted groups/tools/users**: CenturyLink Support Staff and tools
  * **Intent**: To allow Operations rights of least privilege, with flexibility
  * **Change Requests**: Both the customer and Operations can modify CAMOpsOverridePolicy to change permissions and restrictions of Operations
  * **Policy Summary**
  - ReadOnlyAccess: Allows ReadOnlyAccess
  - CTLOperationsPolicy: Allows ability to create and update most IAM concepts while preventing them from making changes to other IAM dependencies of CAM.
  - CAMOpsOverridePolicy: See "Hardening, Re-Hardening, Overrides, and Exceptions" above.




**CenturyLink Developer Role**
* **Attached Policy Names**: CTLDeveloperPolicy
* **Role Name**: CTLDeveloperRole
* **Targeted groups/tools/users**:Cloud Application Manager's Optimization tool. A limited number of CenturyLink developers have access to the tool.
* **Intent**: The Optimization tool should be able to configure customer accounts, affect IAM permissions, and swiftly remediate any issues.
* **Change Requests**: Because CenturyLink must maintain administrative access, no changes can be made at this time. Please see the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/) for details.
* **Policy Summary**:
  - Full access

**CenturyLink Lambda Role**
* **Attached Policy Names**: CTLAccountControlsLambdaPolicy
* **Targeted groups/tools/users**: Newly created IAM users that are not in IAM Groups
* **Intent**: Our hardening applies continuous auto-remediation steps to ensure your accounts are protected. IAM users who are not placed within a group will have all their permissions removed, so it is recommended that you move all IAM users to an IAM group. Once they are placed in a group, permissions can be applied again. Newly created IAM groups will automatically have the CTLCustomerPolicy applied. These steps are taken to ensure a seamless experience between Cloud Application Manager and your AWS account. This also allows CenturyLink to ensure that your account continues to meet best practice security guidelines.
* **Change Requests**: This will be applied by default, but as this policy is intended to help, not hinder you, please contact CenturyLink with a support ticket if you find it conflicts with existing functionality.
* **Policy Summary**:
  - Full control of IAM and Config


**CenturyLink Analytics Role**
* **Policy Name**: CTLCloudOptimization
* **Targeted groups/tools/users**: Cloud Optimization and Analytics tool
* **Intent**: To enable Analytics tools and allow customer users transparency into usage and best practices.
* **Change Requests**: This is not optional so no change requests can be made.
* **Policy Summary**
  - Get, List, and Describe capabilities for AWS Certificate Manager, Cloud Formation, CloudFront, Cloud HSM, CloudSearch, CloutTrail, CloudWatch, Config, Data Pipeline, Direct Connect, Dynamo DB, EC2, ECS, Elasticache, Elastic Beanstalk, EFS, ELB, Elastic Map Reduce, Elastisearch, Glacier, IAM, Kinesis, key Management Service, Lambda, RDS, Redshift, Route 53, S3, Simple Email Service, Simple DB, Support, Simple Workflow Service, Simple Notification Service, Simple Queue Service, Storage Gateway, and Workspaces.

**Cloud Application Manager Role**
* **Attached Policy Names**: CTLCAMPolicy, ReadOnlyAccess, CAMOverridePolicy
* **Targeted groups/tools/users**: Cloud Application Manager, Monitoring Service
* **Intent**: To permit Cloud Application Manager's [application lifecycle management (ALM)](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/) capabilities and to enable [Monitoring](../Monitoring/CAMMonitoringUI.md).
* **Change Requests**: While this policy is applied by default, [the standard CAM policy](../Deploying Anywhere/using-your-aws-account.md) is intended to be customizable. If you would like to alter the ALM capabilities of Cloud Application Manager, you may create custom policies under the "CAMOverridePolicy". See below.
* **Policy Summary**
  - CTLCAMPolicy: All the ability to manipulate resources as described [here](../Deploying Anywhere/using-your-aws-account.md)
  - CTLCAMPolicy: Allows governance for all EC2 functions
  - CTLCAMPolicy: Full control of typical autoscaling/Cloud Formation/RDS/S3 tasks
  - CTLCAMPolicy: Allows IAM user/policy creation, deletion, listing and modification.
  - CTLCAMPolicy: Allows core Cloud Application Manager functionality and delegation for Managed Services Anywhere assistance.
  - ReadOnlyAccess: Allows ReadOnlyAccess to enable the [Monitoring](../Monitoring/CAMMonitoringUI.md) feature on Cloud Application Manager
  - CAMOverridePolicy: See "Hardening, Re-Hardening, Overrides, and Exceptions" above.

**Cloud Integration Admin Role**
* **Attached Policy Names**: CTLCustNoSupportPolicy, CTLCAMPolicy, CAMOverridePolicy, CTLCustomerPolicy, ReadOnlyAccess
* **Targeted groups/tools/users**: Administrator users of CAM Optimized Providers.
* **Intent**: To permit these users as much freedom as possible.
* **Change Requests**: If you would like to alter the ALM capabilities of Cloud Application Manager, you may create custom permissions under the "CAMOverridePolicy".
* **Policy Summary**
  - CTLCustNoSupportPolicy: Deny support permissions (please contact CenturyLink with support requests)
  - CAMOverridePolicy: See "Hardening, Re-Hardening, Overrides, and Exceptions" above.
  - ReadOnlyAccess: Allows ReadOnlyAccess to enable the [Monitoring](../Monitoring/CAMMonitoringUI.md) feature on Cloud Application Manager
  - CTLCAMPolicy: See "Cloud Application Manager Role" above

**CAM User Read-only Role**
* **Attached Policy Names**: ReadOnlyAccess
* **Targeted groups/tools/users**: Users of CAM for whom providers are shared, but administrative access is not given. This is not specific to Optimized providers. When providers are Optimized, the Cloud Integration Read-Only Role is used.
* **Intent**: To permit these users to see but not alter any resources in the AWS Console when they click the provider's "AWS Console" button
* **Change Requests**: To avoid creating a security breach, CenturyLink will not change this role.
* **Policy Summary**
  - Read-only access.

**Cloud Integration User Read-only Role**
* **Attached Policy Names**: ReadOnlyAccess, CTLCustomerPolicy, CTLCustNoSupportPolicy
* **Targeted groups/tools/users**: Users of CAM for whom Optimized providers are shared, but administrative access is not given.
* **Intent**: To permit these users to see but not alter any resources in the AWS Console when they click the provider's "AWS Console" button
* **Change Requests**: To avoid creating a security breach, CenturyLink will not change this role.
* **Policy Summary**
  - Read-only access.
  - See "CenturyLink Developer Role" above.
  - CTLCustNoSupportPolicy: Deny support permissions (please contact CenturyLink with support requests.)

**CenturyLink Service Management Policy**
* **Policy Name**: CTLServiceManagmentPolicy
* **Role Name**: CTLServiceManagmentRole
* **Targeted groups/tools/users**: Service Management Staff
* **Intent**:This is not an immediate part of any Optimization scenario but it is enabled by Cloud Application Manager's Account Optimization. Access to a customer's account via this role is only given to a CenturyLink representative when the customer has purchased Service Management from CenturyLink.
* **Change Requests**: This policy is not currently activated by default, just created. If you need permissions changed, please submit a ticket describing the change you would like.
* **Policy Summary**:
  - Add, Change, and Delete capabilities for all services. No capabilities to edit account details or budgets.*
