{{{
  "title": "AppFog v1 Retirement FAQ",
  "date": "10-13-2015",
  "author": "Ian Plosker",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

#### When will AppFog v1 be discontinued?

December 15, 2015 is the last day AppFog v1 will be supported; the service will discontinue after this date.

#### What do I need to do?

If you are currently using AppFog to host your applications, you need to migrate your applications by Dec 16, 2015 to AppFog v2 or another PaaS. 

If you are no longer using AppFog, no action is needed.

#### What happens if I need more time?

Please reach out to support@appfog.com, if you need help migrating your applications to AppFog v2. We are confident that we can build a migration plan that will work for you.

####  Why is AppFog v2 replacing AppFog v1? 

AppFog v1 was built on an older version of Cloud Foundry. There is no easy migration path between these versions. We decided that rather than carry AppFog v1's limitations to the new version of Cloud Foundry, we'd start over and work to build a platform for cloud-native apps that supports the latest and greatest CF features. Further, we are building several new services to augment the core Cloud Foundry features. 

#### How do I export my data from AppFog v1 services?
        
We’ve compiled a [migration guide](https://www.ctl.io/knowledge-base/appfog/legacy-version-1/appfog-version-1-docs/#migration-guides) to help you transition off of AppFog v1, please click here to see how to export data from your AppFog v1 account.

#### How long will it take me to migrate my applications to AppFog v2?

In many cases, less than one hour. If a transfer from a database service is required, you should plan for it to take longer. The length of time will depend on the size of the dataset that needs to be  moved.

#### Where do I go if I have questions about how to move my applications to AppFog v2? 

We've created a [migration guide](https://www.ctl.io/knowledge-base/appfog/legacy-version-1/appfog-version-1-docs/#migration-guides) that details the steps required to move your applications.  If you have questions or run into issues, you can file a support ticket with AppFog Support by emailing [support@appfog.com](mailto:support@appfog.com).

#### What happens if I don’t move my application in time?
        
Any applications still running on AppFog v1 after Dec 16, 2015 will become unavailable when the service is shut down; it will not be recoverable. If you need help migrating your applications, please reach out at [support@appfog.com](mailto:support@appfog.com).

#### Why should I move to AppFog v2 and not another platform?

There are many reasons to make the move to AppFog v2:

- **Robust feature set to help developers**. Based on most recent stable versions of the open source Cloud Foundry platform
- **Competitive pricing**. Only pay for what you use
- **Integrated into the CenturyLink Cloud Control Portal**. Includes additional management features and easy access to other cloud services

#### What services are supported on AppFog v2?

AppFog v2 includes native support for the following CenturyLink services: MySQL and Orchestrate. 

We believe the best services are those that are fully managed, easy to use, and require little user maintenance. As such, we plan to offer additional fully managed services both within CenturyLink Cloud and with partnerships to bring third party services to the AppFog v2 marketplace.

#### What are the support options for AppFog v2?

CenturyLink Cloud provides a number of a la carte support options.  For more details visit: https://www.ctl.io/support/

#### Why has AppFog v2 switched to usage-based pricing? 

In most cases, this pricing model is cheaper for our end users. We want pricing to be both fair and simple. AppFog v2's pricing model only charges based on the amount of memory reserved for your applications - $0.04/GB hour. 

#### Why is there no longer a free tier?

Having a free tier was not a sustainable model for this service. We believe that by offering a generous trial and fair pricing, we can build a sustainable product that provides a lot of value to users.

#### Are there any major features of AppFog v1 that are not available in AppFog v2?

A major difference between the two versions is that we no longer provide first party services like MySQL, Redis, and MongoDB for free. Also, SSL for custom domains is no longer provided as part of the service. 

#### Are there any modifications I must make to my AppFog v1 applications to be compatible with AppFog v2?

Most applications will need little to no modifications to deploy and run on AppFog v2. The majority of modifications needed to move from AppFog v1 to AppFog v2 will be around the add-ons and services the application depends on.  For more details see our [migration guide](https://www.ctl.io/knowledge-base/appfog/legacy-version-1/appfog-version-1-docs/#migration-guides).

#### How long does the discount for AppFog v2 apply and how does it work?

Your discount will apply for one full year from the day you sign up as an AppFog v2 customer. After filling out the discount request form (sent to you originally via email), the discount will be applied automatically by the time of your first bill.

#### What are the benefits of AppFog being integrated into the CenturyLink Cloud Control Portal?

CenturyLink Cloud features one of the most sophisticated service infrastructures in the market, with a great interface and lots of options for managing complex workflow and third-party applications in the cloud. Integration into the CenturyLink Cloud Portal allows for quick and easy access to all other high performance cloud services.

#### What do I do if I’m using PHP 5.3 or PHP 5.4?

AppFog v2 supports PHP 5.4 and 5.5 out of the box.  The Cloud Foundry buildpack recently removed support for PHP 5.4, because it is no longer receiving updates and patches.  As PHP 5.3 and PHP 5.4 are out of support and no longer receiving updates, we recommend migrating PHP 5.3 and 5.4 applications to PHP 5.5. 

If this is not possible, contact [support@appfog.com](mailto:support@appfog.com).  We've created a custom buildpack for PHP 5.3 that is available for users who cannot upgrade to an officially supported version of PHP.
