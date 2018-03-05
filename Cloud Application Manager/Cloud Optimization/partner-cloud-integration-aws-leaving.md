{{{
  "title": "Partner Cloud: AWS Customers Leaving CenturyLink",
  "date": "08-20-2017",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Departing AWS Customers leaving CenturyLink may be interested in understanding the process for gaining root account access, plus removing of non-customer IAM accounts, groups, roles, and federation.


### Audience

AWS Customers of CenturyLink whose contact has ended.

### Prerequisites

* Administrator access to your AWS account(s).

* Understanding of the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/).

* Understanding of the [Cloud Application Manager Supplemental Terms](https://www.ctl.io/legal/cloud-application-manager/supplemental-terms/)


### Important Information

Prior to the expiration of a contract for Cloud Application Manager 1.0, you should schedule time to work with CenturyLink to both 1) leave the CenturyLink-governed AWS Organization 2) obtain the root account credentials for every accounts that CenturyLink has supported. 3) Remove CenturyLink access. The goal is to perform those steps on the day of your departure, but it is reasonable to expect it within two weeks.

1. Leaving the CenturyLink-governed AWS Organization will be handled by the CenturyLink representatives. Be certain your Accounts Payable team is aware of this transition. After that occurs, all usage on the account is Payable to AWS.

2. Obtaining the root account credentials must be done with your security in mind. Two weeks prior to the end of the contract, create a support ticket to request a meeting with a member of the Cloud Application Manager Product team. It is best if you coordinate that transition via phone to prevent security gaps. It will first require CenturyLink to remove Multi-Factor Authentication and change the email and password for the root account.

3. Removing CenturyLink Access:

As stated in the Service Guide, data for your account has been saved within the account. Two Simple Storage Service (S3) buckets have been created by CenturyLink and you may keep the data or remove it as you like.
* config-bucket-<accountID>
* ctlaudit-<accountID>

Performing the following steps will remove any federated trust with CenturyLink employees or its tools:
* Several IAM Policies have been created by CenturyLink. Do a search within IAM for "CTL" and all our policies will be presented to you. If you wish to delete one, select one and click "Policy Actions" then Delete.
* Several IAM Roles have been created. Do a search within IAM for "CTL" and all our policies will be presented to you. If you wish to delete one, select one and click "Policy Actions" then Delete.
