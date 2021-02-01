{{{
  "title": "Partner Cloud: AWS Customers Leaving Lumen",
  "date": "10-30-2018",
  "author": "Ben Swoboda",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

Departing AWS Customers leaving Lumen may be interested in understanding the process for gaining root account access, plus removing of non-customer IAM accounts, groups, roles, and federation.


### Audience

AWS Customers of Lumen whose contract has ended.

### Prerequisites

*  Pay off all existing invoices. See below regarding the last invoice.

* Contact with your Lumen account representative.

* Correct access to your AWS account(s). (See below.)

* Review the [Service Guide](https://www.ctl.io/legal/cloud-application-manager/service-guide/).

* Review the [Cloud Application Manager Supplemental Terms](https://www.ctl.io/legal/cloud-application-manager/supplemental-terms/)

* Understand AWS [organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html)



### Important Information

Because we bill in arrears, expect to receive at least one more invoice from Lumen after your departure.

Your departure will be aided by creating a support ticket. Please review the following information to help you create the content of that ticket. Then send in the ticket for the legal process to begin. Three parties must sign: your company, AWS, and Lumen. A template for the ticket is below. You do not need to know exactly what date you will be leaving when you create the ticket.

You should schedule time to work with Lumen to 1) leave the Lumen-governed AWS Organization 2) obtain the root account credentials from Lumen. 3) Remove Lumen access. The goal is to perform those steps on the day of your departure, but it is reasonable to expect it within two weeks.

Be certain your Accounts Payable team is aware of this transition. Immediately after leaving the Lumen organization, all usage on the account is Payable to AWS. If you leave in the middle of the month, you should expect a prorated invoice from both AWS, Lumen, and - if you are moving to another reseller - another reseller partner.

### Preparation

**Ticket Information**

You can help determine how to fill in the blanks by reading the rest of this document. We recommend you create this ticket at least two weeks prior to the end of the contract. 

```
This is a request to meet with my Lumen account representative and potentially a member of the Cloud Application Manager Product team.

Goal:
Target Date:
Lumen account representative:
Departing AWS AccountIDs:
AWS AccountIDs to which you currently do not have root access:
Secure method of delivering root credentials to you:
Who do you want to handle removing your member accounts from our AWS organization? (Lumen or your company):
If your company, identify any AWS Users needing permissions:
Do you wish to continue using CAM for ALM?:
Special Considerations:

Please direct this ticket towards the CAM_CloudIntegration group

```

**Prepare payment for accounts with expired credit cards and new accounts created with Lumen**

AWS requires all accounts that are no longer part of an AWS Organization to have a valid payment method. You should prepare to have your company credit card on hand for your departure.  

Since you received invoices through Lumen you were not required to have a credit card on accounts created with Lumen. All those accounts will not be able to leave Lumen until an administrator applies a credit card as the [payment method](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/edit-payment-method.html).

**How will you leave the Lumen-governed AWS Organization**

If you will be departing Lumen's organization to join another AWS organization, we recommend you have the other organization send invitations to you within fifteen days of your target date so that invitation will be queued up and ready when you depart. You can then handle everything at once. If that is not possible, then the most efficient way to schedule it is just to ask a Lumen admin to revoke your membership for all your accounts at once.

Allowing your accounts to depart from the Lumen-governed AWS Organization will be handled by someone with the appropriate permissions. Either someone with root access to the account or one of your IAM users with the appropriate permissions. (Having one of your IAM users do it will require Lumen to change your IAM policy before you depart.)

A Lumen administrator can remove membership from your org for all your accounts out at once.

Obtaining the root account credentials must be done with your company's security in mind.  It is best if you coordinate that transition via phone or another secure method to prevent security gaps. It will first require Lumen to remove Multi-Factor Authentication and change the email and password for the root account.



### Transition Activities

**Remove Account Membership**

If you will be joining another AWS Organization, it is recommended you have the invitations from the other organization sent to your accounts prior to departing Lumen.

If your users will be handling the process of departing, here is how to do it from the console:

* https://console.aws.amazon.com/organizations/
* Click "Leave Organization"

![Leave  AWS Organization](../../images/cloud-application-manager/CAM_COA_LeaveOrg1b.png)

* If you are then accepting invitations to another organization, you may mimic the steps you performed when your account [became a member](partner-cloud-integration-aws-existing.md) of the Lumen-governed AWS Organization after accepting Terms and Conditions.


**Address Your Data Generated by Lumen Configuration:**

Data for standard customers accounts has been saved within the accounts. Two Simple Storage Service (S3) buckets have been created by Lumen.

 * You may keep the data, archive it, or delete it as you like.
>   * config-bucket-<accountID>
>   * ctlaudit-<accountID>

**Revoke Lumen Access**

Performing the following steps will remove any federated access with Lumen employees or its tools:

* Several IAM Policies have been created by Lumen. Do a search within IAM for "CTL" and all our policies will be presented to you. If you wish to delete one, select one and click "Policy Actions" then Delete. If you wish to keep using CAM for Application Lifecycle Management, then please keep the policy that is described in the associated CAM provider intact. Lumen will need to work with you to keep the existing CAM provider, but remove the "Optimization" tags.

* Several IAM Roles have been created. Do a search within IAM for "CTL" and all our policies will be presented to you. If you wish to delete one, select one and click "Policy Actions" then Delete.
