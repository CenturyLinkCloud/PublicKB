{{{
"title": "Cloud Platform - Release Notes: June 8, 2017",
"date": "6-6-2017",
"author": "Chris Meyer",
"attachments": [],
"contentIsHTML": false
}}}

### New Features (4)

* __Cloud Application Manager__

  - __Global Navigation__

    We have additional updates to the Global Navigation bar at the top of the website. In our attempt to provide One Portal View of all CenturyLink Cloud and Hosting Services, we released “Services” Menu in our last release allowing users to navigate easily between Cloud Application Manager, CenturyLink Public Cloud, Managed Hosting and Managed Security portals. We have now enabled Private Cloud navigation that will take users to CenturyLink Dedicated Cloud Compute portal. Going forward users will see an additional navigation menu called “Sites”, that will allow them to switch between multiple sites within Cloud Application Manager.

  - __Sites Menu__

    We are introducing two new sites within Cloud Application Manager. “Optimization” and “Monitoring”. The current site that allows users to leverage Application Lifecycle Management will be labeled “Management” site. The Sites Menu will allow users to navigate between “Management”, “Optimization” and “Monitoring” sites within Cloud Application Manager.

    With this change, we have moved the existing Menu options “Dashboard’, “Instances”, “Boxes”, “Providers” and “Settings” to the left hand navigation bar.

  - __Cloud Optimization Site__

    CenturyLink is committed to providing value added services to our Reseller Customers. With our newly launched Cloud Optimization Site, customers who purchased AWS Services through CenturyLink can now get the additional reporting capabilities on their AWS infrastructure. Once users navigate to the Cloud Optimization Site, they will be authorized with their Cloud Application Manager credentials and will see Optimization recommendations. Now, users will see “Savings” and “Best Practices” modules. As we continue to improve the Cloud Optimization Site users will see additional recommendation related to utilization, cost, and inventory in the coming weeks.

  - __Monitoring Site__

    Customers who purchased Managed Services from CenturyLink will now have additional insight into the Managed Servers that have been deployed in multiple cloud platforms. After navigating to the Monitoring site, the users will be authorized with their Cloud Application Manager credentials and will see “Events”, “Policies”, “Servers”, ‘Suppressions” and “Graphs”. At this time, end users are going to have a “Read Only” view of the monitoring and suppression policies and will be able to see graphs on Operating Systems metrics. Users will have an option to request changes to the monitoring policies if they think there needs to be changes to the policies.


### Enhancements (3)

* __Cloud Application Manager__
  - __Billing__

    Users can now view Monthly Estimates and Usage History for the spend across all the services within Cloud Application Manager. A new menu option “Billing” under Organization context will provide a Billing Dashboard and Usage History. The Billing dashboard provides the following information:

    * Month to date charges
    * Month Estimate charge
    * One time charges
    * Monthly Billing History graph<p>

  - __Help Menu__

    We are expanding our Help Menu options and the updated Help Menu will have links that navigate to:

    * Create Ticket
    * Support Center
    * Knowledge Base
    * Submit Feedback
    * System Status


* __Load Balancing-as-a-Service (LBaaS) - Additional Health Check:  SSL Port__

    Load Balancing-as-a-Service has added an additional Health Check option - Checking an SSL Port.  This Health Check option enables an SSL Handshake by sending an SSLv3 client hello message.  The check is valid if the server answers a valid SSL server hello message.

### Ecosystem - Partner Integrations (6) <p>

* __Commercial Products Launched:__

  * [Server General KMS for MySQL](https://www.ctl.io/marketplace/partner/ZZP2/product/Server%20General%20KMS%20for%20MySQL/) - A Key Management-as-a-Service (KMS) specifically designed for MySQL servers. It delivers easy-to-use key management and compliance at a fraction of the cost existing database players charge for securing their databases. On-boarding included.
  * [Server General TDE](https://www.ctl.io/marketplace/partner/ZZP2/product/Server%20General%20TDE/v/4.0.2/) - A data encryption service that makes it easy to set-up, manage and administer data-at-rest encryption of sensitive information stored in Database (MySQL, PostgreSQL, MongoDB, Couchbase) or File servers. On-boarding included.
  * [C3DNA Controller for Adobe Experience Manager (AEM)](https://www.ctl.io/marketplace/partner/DIME/product/C3DNA%20AEM%20Controller/v/1.0/) - Enables secure, real-time Adobe Experience Manager (AEM) cloning and live migration without VM motion. Controller is used to manage multiple Platform components - virtual appliances running the AEM software.
  * [C3DNA Platform for Adobe Experience Manager (AEM)](https://www.ctl.io/marketplace/partner/DIME/product/C3DNA%20AEM%20Platform/v/1.0/) - The Platform for AEM component hosts the Adobe Experience Manager software (sold separately). Deploy after Controller.
 
### Bug Fixes (1)

* __IaaS - Enhancements Related to Overall Stability and Availability__

  CenturyLink Cloud Infrastructure-as-a-Service has implemented improvements to our cloud infrastructure and Control Portal software. These additions are meant to improve customer experience by increasing availability and improving platform stability.
