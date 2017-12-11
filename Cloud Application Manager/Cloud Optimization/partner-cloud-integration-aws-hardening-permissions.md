{{{
  "title": "Partner Cloud Integration: CenturyLink Permissions for Hardened AWS Accounts",
  "date": "08-30-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Amazon Web Services Accounts that are hardened by CenturyLink will provide our tools and Operations Staff  permissions as discussed in the Service Guide. The Service Guide provides a high-level overview of those permissions. The goal of this is to provide some more detail (without posting the specific AWS JSON files used). The groups requiring the permissions will be described along with the type of permissions they are expected to have.

### Audience

Users of accounts that already have or are considering full hardening. This is for all new AWS accounts created through Cloud Application Manager and any existing account moving into CenturyLink's care which [opts for full hardening](./partner-cloud-integration-connect-aws.md).

### Prerequisites

For a new AWS Account:
* The customer must have reviewed the process for creating a [new Amazon Web Services account](./partner-cloud-integration-aws-new.md)

For an existing AWS Account:
* The customer must already have an AWS account that has been specifically mentioned in the AWS account transfer process. (Only approved accounts are authorized for this process.)
* The customer must have reviewed the process for transferring an [existing Amazon Web Services account](./partner-cloud-integration-aws-existing.md)


### Important Information

**Root Level Access**

Root level access is not provided to CenturyLink users for any account.

For existing accounts, the Customer administrator is asked to set up MFA access after configuration and keep their key in a secure location.

For new accounts created through Cloud Application Manager, MFA access is set up after configuration of the account is complete. The key is kept in an encrypted vault.

**CenturyLink Account Access by Role**

CenturyLink or Customer Role | Type of User | Optimization scenario | IAM Permissions and Restrictions
--- | --- | --- | ---
Customer Admin (see below) | Customer-defined | Full Hardening | Add, Change, and Delete capabilities for all services. No capabilities to review or usage, billing, payment methods, or budgets.
Cloud Application Manager Account Optimization | Automated Tool | Full Hardening | Administration
Cloud Application Manager Application Lifecycle Management | Automated Tool |Full Hardening | All the ability to manipulate resources as described [here](https://www.ctl.io/knowledge-base/cloud-application-manager/deploying-anywhere/using-your-aws-account/).
CenturyLink Operations | Operations Staff | Full Hardening | View-only capabilities for all products and services
*CenturyLink Service Management* | *Service Management Staff* | *This is not an immediate part of any Optimization scenario but it is enabled by the Cloud Application Manager Account Optimization. This role is only applied when customer has purchased Service Management support from CenturyLink* |  *Add, Change, and Delete capabilities for all services. No capabilities to edit account details or budgets.*

* For customers with Existing accounts, the Customer Admin Role does not have much impact as the customer will already have their own users prior to moving into CenturyLink's care.
* Restrictions to review usage, billing, payment methods, or budgets are in place because the data there will become misleading once the account in moved into CenturyLink's care. This is one of the reasons we provide our Cloud Application Manger Analytics.
