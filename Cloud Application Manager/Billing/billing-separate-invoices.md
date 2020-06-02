{{{
"title": "Billing invoices",
"date": "07-10-2018",
"author": "Guillermo Sanchez",
"attachments": [],
"contentIsHTML": false
}}}

### Billing in separate invoices

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Billing in a single invoice](#billing-in-a-single-invoice)
* [Setting up billing for multiple invoices](#setting-up-billing-for-multiple-invoices)
* [Getting General Support](#getting-general-support)

### Overview

This article is meant to assist Cloud Application Manager customers who want their Cloud Application Manager charges divided across multiple CenturyLink invoices to align with separate lines of business.

### Audience

Cloud Application Manager organization administrators.

### Prerequisites

An active Cloud Application Manager account.

### Billing in a single invoice

This is the default behavior for any Cloud Application Manager customer. All Cloud Application Manager usage and support charges will be included in a single CenturyLink invoice for the customer organization.

### Billing divided across multiple invoices

To setup Cloud Application Manager to divide billing across multiple invoices to align with separate lines of business for the customer organization, you will need to match your line of business structure with the Cost Center structure in Cloud Application Manager.
To do so:

**From a CAM setup perspective:**
1.	Create a separate Cost Center for each line of business that is using Cloud Application Manager in your organization.
2.	Create a Workspace in each Cost Center.
3.	Create the corresponding Providers on each Workspace of the Cost Centers. Please, note that every subsequent cost associated to a Provider will be summarized into the Cost Center that owns the Workspace where the Provider is defined into.

**From a contracting perspective:**
1.	Each Cost Center will require a unique Billing Account Number (BAN) in order to generate a separate invoice specific to the Cost Center.
2.	A Cloud Application Manager order must be placed for each BAN to associate the CAM product to the BAN.
3.	Reach out to your CenturyLink CSP/CSM, Sales Representative, or TAM to facilitate a Cloud Application Manager order for each new BAN to align with your Cost Centers. 


### Getting General Support

Customers can contact the CenturyLink Global Operations Support center (support desk) directly for getting help with Cloud Application Manager as well as any other supported product that they’ve subscribed to.  Below are three ways to get help.

**Contact:**

1. **Phone:** 888-638-6771

2. **Email:** incident@centurylink.com

3. **Create Ticket in Cloud Application Manager:** Directly within the platform, users can “Create Ticket” by clicking on the “?” symbol in upper right corner near the users log-in profile icon.  This takes users directly to the Managed Servicers Portal where they can open, track and review status of issues that have been raised with the support desk.  Additionally, this is how a TAM can be engaged as well.

**Instructions:**

1. Provide your name
2. CAM account name
3. A brief description of your request or issue for case recording purposes

The support desk will escalate the information to the Primary TAM and transfer the call if desired.
