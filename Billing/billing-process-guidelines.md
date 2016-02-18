{{{
  "title": "Ecosystem Partner Billing Setup Process",
  "date": "02-17-2016",
  "author": "Andrew Brunette",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

## Ecosystem Partner Billing Setup Process

### Description
This document describes the process and responsible parties for setting an Ecosystem Partner product up to be billed to the customer when the Blueprint that loads the product is run.

### Audience
Ecosystem and sales team members who are working with Ecosystem partner companies that wish to bill for their products in the Ecosystem Marketplace.

| Step Name | Description | Responsible Team(s) |
| --- | --- | --- |
| Provider Signup | Provider signs up as a customer, and agrees to Supplemental Terms which establishes them legally as a Provider Partner. | Ecosystem |
| Provider Integration | Provider completes an integration | Ecosystem |
| Billing Model Definition | Provider Partner and ecosystem team member define the product and pricing model functionally. Select products, configurations, define price level and billing trigger for each item.  This is a design task, defining the billing model to be implemented in subsequent steps. This pricing is defined at net levels to provider | Ecosystem |
| SKU Setup | Setting up the SKU in Platform.  This will be done by creating a ticket to Mary Cadera/Jared Ruckle (need to define these people functionally, rather than by name).  Cadera/Ruckle will create the SKU so the product can be billed. | Ecosystem to create ticket, Platform to instantiate SKUs. |
| Billing Trigger Task Creation | Creation of a programmatic task to be called by the Blueprint or Runner job so that either a subscription is created or an accumulator is incremented.  The task will be added to the BP or Runner job, so that it is executed whenever the job is run.  An application will need to be created for the case of templates or API using applications.  This will be executed as the result of the service task that is performed to set up the Template.  API processing is unknown, and out of scope at this time.  | Platform to create task, ecosystem to add to job. |
| A/P Setup | The provider partner enters information to the partner portal that is sufficient to setup the accounts payable vendor information.  This information will be manually provided to A/P in the near term for setting up the partner as a payable target.  | Provider sets up in portal with Ecosystem assistance. |
| Pricing Estimator | Pricing is added to the Estimator at GROSS rates, including CTL markup | Platform |
| Price List Publication to Marketplace Price List | Rate card and product list is published to Marketplace website, AT GROSS RATES, eg., including CTL markup. | Digital  |
| Usage happens | End customer uses things and accumulates charges | Customer |
| Summary Report Creation |  Report is created that summarizes usage by provider partner, product, customer.  This is control report for all monthly activity, and should allow revenue recording | Platform |
| Provider Report Creation | Report is created for each provider, summarizing usage by product and customer, so that provider knows what amount is due. | Platform |
| Provider creates invoice | Partner report is submitted to provider, provider creates invoice back to CTL which drives payment | Provider |
| Acounting Entries are made | Entries are submitted to BRM for billing to customers. | Finance |
| Bad Debt | Nothing happens, CenturyLink will assume bad debt charges | N/A |
