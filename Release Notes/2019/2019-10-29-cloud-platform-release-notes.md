{{{
"title": "Cloud Platform - Release Notes: October 29, 2019",
"date": "10-29-2019",
"author": "Thomas Broadwell",
"keywords":["centurylink", "cam", "alm", "optimization"],
"attachments": [],
"contentIsHTML": false
}}}


### Announcements (2)

#### [Cloud Application Manager Platform](https://www.ctl.io/cloud-application-manager/)

##### CenturyLink Cloud subaccount support

Cloud Application Manager now supports CenturyLink Cloud (CLC) subaccounts. A new tab with the subaccounts defined per provider has been added in the CLC provider details page. From there you can register the first level of subaccounts as new providers in Cloud Application manager, either individually by clicking on the register icon on each line or in bulk by selecting them and clicking on the register option in the bulk actions dropdown. It is also possible to specify the account alias that needs to be registered when defining a new CLC provider, if the credentials provided have access to that account (either they are defined in that account or in a parent account). 

#### [Application Lifecycle Management](https://www.ctl.io/cloud-application-manager/application-lifecycle-management/)

##### Added support for manual registration in vCloud based provider types

Cloud Application Manager has added the feature to manually register vCloud or CenturyLink Private Cloud on vCloud Foundation compute instances. There is now a toggle when registering an instance to make it automatic, that allows Cloud Application Manager to take care of all the registration process, although this requires a restart of the machine, or to make it manual, that will show a command snippet for the user to manually execute inside the machine for it to be registered without requiring restart.

### Announcements (1)

#### Notice of Completion: Migration for CenturyLink Cloud Shared Load Balancer Customers to Cloud Load Balancing-as-a-Service

This serves as notice that the effort to Migrate CenturyLink Cloud Shared Load Balancer Customers to Cloud Load Balancing-as-a-Service has been successfully completed. You can learn more about the new offer and view pricing on the [Cloud Load Balancing-as-a-Service product page](https://www.ctl.io/load-balancing/). If you have additional questions, please feel free to contact [noc@ctl.io](mailto:noc@ctl.io), or read our [knowledge base article](../../General/LBaaS/LBaaSFAQ.md).
