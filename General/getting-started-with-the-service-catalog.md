{{{
  "title": "Getting Started with the Service Catalog",
  "date": "3-5-2015",
  "author": "Mary Cadera",
  "attachments": [],
  "contentIsHTML": false
}}}

###General

The Service Catalog is accessible in the Control Portal by Account Administrators only. It can be found under the Account menu in the green navigation bar.

###Settings

There are two settings that an Account Administrator can choose for an account and its sub accounts: “Can Use” and “In Service Catalog.” These settings allow for restrictions on a user’s ability to access or view the availability of a particular service. “In Service Catalog” only applies to sub accounts. It can be adjusted for existing sub accounts, and can be set as a default for sub accounts that are created in the future.

####*Can Use*
This setting allows Account Administrators to determine whether or not account users “Can Use” the service. When this setting is toggled to ON, Account Administrators allow users (with the appropriate permissions) at that account level to have full access to the service. The service also defaults to being visible in the service catalog for all sub accounts.

See Additional Settings, below, for more details on adjusting the “Can Use” settings for individual sub accounts.

![service catalog can use toggle](../images/service-catalog-can-use-toggle.png)


#### *In Service Catalog*
This setting allows Account Administrators to pre-determine visibility and accessibility to the service. This setting applies only to an account’s sub accounts. When this setting is toggled to ON, the Account Administrator of any subsequently created sub account will be able to see the service in the Service Catalog, and the service will be immediately accessible to users of that account that have the appropriate permissions to use the service.

When this setting is toggled to OFF, the Account Administrator of the new sub account will not see the service in the catalog and users will not have access to the service.

![service catalog in service](../images/service-catalog-in-service.png)


####*Additional Settings*
The Account Administrator of a parent account can restrict visibility and access to services in the Service Catalog for its sub accounts on an account by account basis. The ability to use a service and the ability to see a service can also be set independently of one another. This is done by checking the “In Service Catalog” and “Can Use” boxes next to each sub account in the sub account list.

Note that turning off the “In Service Catalog” option for a sub account automatically turns off “Can Use” for that sub account. The inverse is not true. For sub accounts, “Can Use” can be turned off, but “In Service Catalog” can remain on, if desired.

![service catalog sub account settings](../images/service-catalog-sub-account-settings.png)


These settings can also be toggled across all sub accounts with a single click by using the “all” and “none” buttons on the upper left and right corners of the sub account list.

![service catalog all or none](../images/service-catalog-all-or-none.png)


###Examples

Say you want to turn off Premium Backup for your own account’s users and all your sub accounts. How would that look?

Set “Can Use” for your own account to OFF, and “Submit Changes.”

![service catalog can use off](../images/service-catalog-can-use-off.png)


*Note that it is not currently possible to disable a feature at the parent account level but also have it enabled for sub accounts.*

But what if you want your own account’s users to have access to the service, and you want to restrict both the visibility and the access to your sub accounts?

First, leave “can use” for your own account set to ON.

Next, either click the “none” button to turn off the availability of the feature for all sub accounts, or select on an account by account basis which accounts you want to restrict access to. Note that turning off the “In Service Catalog” option for sub accounts automatically turns off “Can Use.” The inverse is not true. “Can Use” can be turned off, but “In Service Catalog” can remain on, if desired.

![service catalog none toggle](../images/service-catalog-none-toggle.png)


In both the above examples, for an account where “Can Use” has been turned OFF, premium storage is unavailable when a user of that account is provisioning a server.

So how does this flow through to the end user?

Here’s how the Create Server process looks to a user of an account with Premium Backup enabled in the Service Catalog. Storage Backup Level appears as an option, and the user gets to select Standard or Premium:

![service catalog example 1](../images/service-catalog-example-1.png)


This is how the Create Server process looks to a user of an account with Premium Backup disabled in the Service Catalog. Storage Backup Level defaults to Standard, and the option to select Premium Storage simply doesn’t appear in the server creation process:

![service catalog example 2](../images/service-catalog-example-2.png)


###IMPORTANT
It is important to note that if certain services are in use and “can use” is toggled OFF, this service can get into a state where the ability to manage it is turned off, but the service is still running and consuming resources in the background. (This is because the Service Catalog manages access to a service, but it does not control the service itself.) This can lead to a situation where account users cannot control (or in some cases even see) a service, even though it is in use and incurring charges.

This is scenario is avoidable if Account Administrators remain aware of the possibility and take measures to avoid it, such as conducting a usage audit before disabling a service. Further, this does not apply to all services; only some are at risk of entering this undesirable state because of the nature of the service. Presently, the following services should be carefully audited before they are disabled:

#####Load Balancer
