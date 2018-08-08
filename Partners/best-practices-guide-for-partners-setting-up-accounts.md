{{{
  "title": "Best Practices Guide for Partners Setting Up Accounts in CenturyLink Cloud",
  "date": "08-17-2016",
  "author": "",
  "attachments": [],
  "contentIsHTML": false
}}}

### Best Practices
This guide is designed to educate Partners on the best ways to set up and organize accounts for CenturyLink Cloud. To begin, let’s review the commonly used terms when setting up accounts:
* **Hierarchy:** - This is the term described the manner in which accounts are organized in CenturyLink Cloud. Accounts are organized from top to bottom, not side to side or from the bottom up.

* **Parent Accounts** - These accounts are at the top of the hierarchy and are sometimes referred to as Parent (or Root Parent) Accounts.  Partner’s are at the top of the hierarchy. (need language around distributors)

* **Sub Accounts** - Sub Accounts are added under a Parent Account.

* **Trials** - Trial accounts are a sales tool for you to extend to customers the opportunity to use CenturyLink Cloud – free of charge - with a credit of $500 or $2,500.

### Getting Started
Use Sub Accounts to create your Account Hierarchy. Sub Accounts are used to create the following:
* Demo Accounts
* Internal use/workloads
* Customer Accounts and Trials

Sub Accounts have several advantages:
* They are hierarchical – user permissions flow down, not up or sideways.
* Sub Accounts may share the Parent Account networks or have their own.
* Settings are inherited from the Parent Account.
* Users in the Sub Account can override inherited settings, if desired.
* After the Sub Account is created, you can edit the settings.
* If you no longer need a Sub Account, you can close it via the “Request to close” link.

When you create a Sub Accounts you will also create an Account Alias.
* An Account Alias is a string of 2-4 alphanumeric characters that is used to identify an account and relate servers to that account by naming convention.
* An Account Alias is a required field when setting up an account.
* Account Alias’ are globally unique so duplicate aliases are not allowed.

**Note:** An Account Alias cannot be reused, even after deletion of the original account with that alias.

### Best Practices for Creating your Account Hierarchy
Now that you know the kinds of accounts you can create in CenturyLink Cloud, let’s review the best practices for creating your account hierarchy.

### The Flat Account Hierarchy
This is the most commonly used account structure. Here’s an example of how Sub Accounts are organized using this preferred hierarchy:

**ACME (Partner Main Account)**
* Acme Cloud Demo Account
* Acme Cloud Internal Account 1
* Acme Cloud Internal Account 2
* Customer 1
* Customer 2

**Note:** The bulleted items are ALL separate Sub Accounts under the Parent Account, Acme Cloud.

### Demo Accounts
Demo Accounts are designed for you to test and demo the product. Think of your Demo Account as a sandbox to play and learn the features of CenturyLink Cloud. This is also where you will demo the product for customers. The Demo Account is created as a Sub Account under the Parent Account. Partners create a Parent Demo Account using the following naming convention:
* (Parent Account Name)+Demo Account”
* For example: (Acme Cloud)Demo Account

Setting up your Demo Account this way insures you receive the **$3000 demo credit each month**.

**Note:** Make sure you do not setup Sub Accounts (including Customer Accounts) in the Parent Demo Account.

### Internal use/ workloads
Internal use/workloads Accounts are created when you are using CenturyLink Cloud within your organization.  For example, if your company uses CenturyLink Cloud in different locations or groups, you will create these accounts using the following naming convention:
* (Parent Account Name= ACME Cloud) + City.
* For example: Acme Cloud – California

**Group:**
* (Parent Account Name= ACME Cloud)+ - Group Name
* For example: Acme Cloud– Central Marketing Group

### Customer Accounts
Customer Accounts are just what the name suggests:  accounts for your customers. Customer Accounts are created as Sub Accounts as well, and are the next set of accounts in your Account Hierarchy. When you create a Sub Account, you also create an Account Alias. Customer Accounts are created using the following naming convention:
* “Customer Name”
* for example: ABC Services

### Customer Trials
Trials are Customer Accounts. Trials give customers a chance to stand up resources and see how our cloud performs on an actual project or workload. The Trial program provides a creidt of either $500 or $2,500 to new prospects.

When a Trial is converted to a regular, paying customer, the customer does not need to recreate the work they’ve done during the Trial. The cloud environment for trial customers is exactly the same as the environment for paying customers.

### Requesting a Customer Trial
To request a trial, use the following process:

1. Create a Customer Account in the Control Portal.

2. Request a Customer Trial via email to cloudpartnerhelp@centurylink.com

3. The Email Subject should read as follows:  
   * Request – Partner Name – Customer Alias

4. In the body of the email, please include the following:
   * Partner Name
   * Partner Contact
   * Partner Contact Email
   * Customer Name
   * Customer Alias (Portal Alias)
   * Amount of Credit Requested- either $500 or $2,500

5. You will receive a confirmation email from the CenturyLink Cloud team confirming the trial has been setup for the customer.

### Tips for Where to Set up a Trial in Your Hierarchy
It’s best to place your Trial Subaccount where it will ultimately reside in the hierarchy as a billable account. This helps the Partner avoid having to delete and rebuild the customer's infrastructure at the end of the trial.

###Monitor the Trial
Partners should work closely with the prospect and monitor the status of their trials. This will improve the customer experience and increase the chance of that prospect becoming a billable customer. This is important as you’ll be able to monitor how the customer is using the trial, answer questions that arise, and insure there are no surprises if the prospect uses the entire trial credit amount.

After the credit amount is depleted, CenturyLink starts billing you (the Partner) for your customer’s usage. When a trial is created, an Account Alias is also created

### End of Trial with Customer Canceling Services
If the customer does not convert to a paying customer, you must email the CenturyLink Cloud Team - cloudpartnerhelp@centurylinkcloud.com informing them of the customer’s decision to not become a paying customer and ask for the account to be closed. You need to close the account before the credit is deplted or you will be billed for that customer’s usage.

The customer account will be removed from the Control Portal by CenturyCloud Team after the request is made.

### Service Catalog
The Service Catalog allows Account Administrators to enable or disable certain cloud platform services for users of the account. It also allows certain services to be enabled or disabled for individual sub accounts.

### Learn More
* [How to Use the Service Catalog](../General/CenturyLinkCloud/getting-started-with-the-service-catalog.md)
* [Service Catalog FAQ](../General/CenturyLinkCloud/service-catalog-faq.md)
