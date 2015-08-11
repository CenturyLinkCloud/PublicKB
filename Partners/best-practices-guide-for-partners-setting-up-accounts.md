{{{
  "title": "Best Practices Guide for Partners Setting Up Accounts in CenturyLink Cloud",
  "date": "5-20-2015",
  "author": "",
  "attachments": [],
  "contentIsHTML": false
}}}

**This Best Practices Guide** is designed to educate Partners on the best ways to setup and organize accounts for CenturyLink Cloud. To begin, let’s review the commonly used terms when setting up accounts:

- **Hierarchy:**  This is the term we use to describe the manner in which accounts are organized in CenturyLink Cloud.  Accounts are organized from top to bottom, not side to side or from the bottom up.

- **Parent Accounts** are at the top of the hierarchy.  These accounts are sometimes referred to as Parent (or Root Parent) Accounts.  Partner’s are at the top of the hierarchy. (need language around distributors)

- **Sub Accounts** are accounts that are added under a Parent Account.

- **Trials** are a sales tool for you to extend to customers the opportunity to use CenturyLink Cloud – free of charge - for 30 days or up to $2500.

### Getting Started
You will use _**Sub Accounts**_ to create your Account Hierarchy. Sub Accounts are used to create the following:

-    Demo Accounts
-    Internal use/workloads
-    Customer Accounts and Trials

_**Sub Accounts**_ have many advantages:
-    They are hierarchical – user permissions flow down, not up or sideways.
-    Sub Accounts may share the Parent Account networks or have their own.
-    Settings are inherited from the Parent Account.
-    Users in the Sub Account can override inherited settings, if desired.
-    After the Sub Account is created, you can edit the settings.
-    If you no longer need a Sub Account, you can close it via the “Request to close” link.

When you create a _**Sub Accounts**_– you will also create an Account Alias.
-    An Account Alias is a string of 2-4 alphanumeric characters that is used to identify an account and relate servers to that account by naming convention.
-    An Account Alias is a required field when setting up an account.
-    Account Alias’ are globally unique so duplicate aliases are not allowed.

_**Note:** An Account Alias cannot be reused, even after deletion of the original account with that alias._

### Best Practices for Creating your Account Hierarchy
Now that you know the kinds of accounts you can create in CenturyLink Cloud, let’s review the best practices for creating your account hierarchy.

### The Flat Account Hierarchy
is the most commonly used account structure. Here’s an example of how Sub Accounts are organized using this preferred hierarchy:

**Flat Account Hierarchy**

**ACME (Partner Main Account)**
- Acme Cloud Demo Account
- Acme Cloud Internal Account 1
- Acme Cloud Internal Account 2
- Customer 1
- Customer 2

_**Note:** The bulleted items are ALL separate Sub Accounts under the Parent Account, Acme Cloud._

### Demo Accounts
Demo Accounts are designed for you to test and demo the product.  Think of your Demo Account as a sandbox to play and learn the features of CenturyLink Cloud.  This is also where you will demo the product for customers.  The Demo Account is created as a Sub Account under the Parent Account.  Partners create a Parent Demo Account using the following naming convention:
>(Parent Account Name)+Demo Account”.
>    For example:
    (Acme Cloud)Demo Account

Setting up your Demo Account this way insures you receive the **$3000 demo credit each month**.

> **Note:** Make sure you do not setup Sub Accounts (including Customer Accounts) in the Parent Demo Account.

### Internal use/ workloads
Internal use/workloads Accounts are created when you are using CenturyLink Cloud within your organization.  For example, if your company uses CenturyLink Cloud in different locations or groups, you will create these accounts using the following naming convention:
>(Parent Account Name= ACME Cloud)+ City”

> For example: Acme Cloud – California

**Group:**
>(Parent Account Name= ACME Cloud)+ - Group Name

>For example: Acme Cloud– Central Marketing Group

### Customer Accounts
Customer Accounts are just what the name suggests:  accounts for your customers.  Customer Accounts are created as Sub Accounts as well, and are the next set of accounts in your Account Hierarchy.  When you create a Sub Account, you also create an Account Alias.  Customer Accounts are created using the following naming convention:
>“Customer Name”
>
>For example: ABC Services

**Customer Trials**
Trials are Customer Accounts.  Trials give customers a chance to stand up resources and see how our cloud performs on an actual project or workload.      They are not billed for the 1st 30 days of use or $2500.

When a Trial is converted to a regular, paying customer, the customer does not need to recreate the work they’ve done during the Trial.  The cloud environment for trialing customers is exactly the same as the environment for paying customers.

_**Requesting a Customer Trial**_
To request a trial, use the following process:

1. Create a Customer Account in the Control Portal.
2. Request a Customer Trial via email to cloudpartnerhelp@centurylinkcloud.com
3. The Email Subject should read as follows:  “Request – Partner Name – Customer Alias”
4. In the body of the email, please include the following:
>+ Partner Name
>+  Partner Contact
>+  Partner Contact Email
>+  Customer Name
>+  Customer Alias (Portal Alias)
>+  Trial Start Date

5. You will get a confirmation email from the CenturyLink Cloud team confirming the trial has been setup for the customer.

_**Tips for Setting up Customer Trials**_

It’s best to group Trials together so you can easily view, track and manage which customers are trialing at any point in time.  After 30 days, CenturyLink will start billing you (the Partner) for your customer’s usage.  When a trial is created, an Account Alias is also created.  Trials should be created using the following naming convention:

“Trial- Customer Name”+ ”30 days out from Trial start date(end of Trial date).”
>For example, if you create a trial for your customer – ABC Corp – on 4/6/15, create the account this way:
 >+ Trial– ABC Corp– 05/6/15

7 days before the end of the Trial, the CenturyLink Cloud Team will let you know that the customer Trial expires soon.  This is a good time to follow-up with the customer to determine whether they want to convert to a paying customer.

At the end of the Trial, the CenturyLink Cloud Team will email you letting you know that the customer Trial has expired and we will begin billing you (the partner) for that customer’s usage.

_**End of Trial: Customer cancels use of CenturyLink Cloud**_

If the customer does not convert to a paying customer, you need to email the CenturyLink Cloud Team - cloudpartnerhelp@centurylinkcloud.com informing them of the customer’s decision to not become a paying customer and ask for closing the account.  You need to close the account before the end of the trial date (in this case, 05/6/15), otherwise you will be billed for that customer’s usage, beginning 5/7/15.
The customer account will be removed from the portal by CenturyCloud Team after the request is made.

## Service Catalog
The Service Catalog allows Account Administrators to enable or disable certain cloud platform services for users of the account. It also allows certain services to be enabled or disabled for individual sub accounts.

[Learn More About how to use Service Catalog](../General/getting-started-with-the-service-catalog.md)
[Service Catalog FAQ](../General/service-catalog-faq.md)
