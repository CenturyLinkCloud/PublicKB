{{{
  "title": "How to Map an AppFog v1 URL to an AppFog v2 Application",
  "date": "02-17-2016",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

When migration is complete your billing subscription can be canceled from the [Account](https://console.appfog.com/#account) page of the web console. Please be sure to cancel your subscription as we are not aware when individual user migration is complete. The billing system will not automatically prorate the subscription and issue a refund. If applicable, please open a [Support Ticket](https://support.appfog.com/tickets/new) or email support@appfog.com to receive a prorated refund of your subscription.

### Overview
In response to feedback from AppFog v1 users we have developed a proxy service that will allow users to continue to utilize their AppFog v1 default URL ending in `*.aws.af.cm` and route traffic from that URL to an application on AppFog v2. This service will remain in place until July 1, 2016. Users can use the `X-Forwarded-Host` header to identify the original source of the request.

### Map An Application
Map your AppFog v1 application to the new AppFog v2 default domain, which must end in `*.ctl.io`. The syntax is `af map <YOUR_APPNAME> <AFv2_DOMAIN>`. Here is an example using an application named `foo`:

```
af map foo foo.useast.appfog.ctl.io
```
This will stop the application on AppFog v1 and put it in a "Suspended" state. Requests to the AppFog v1 application will then be routed to the provided AppFog v2 URL. Due to Varnish caching, there may be a delay of up to five minutes before requests are routed to AppFog v2.

### Unmap an Application
When unmapping a `*.ctl.io` domain from an AppFog v1 application the application will be set to a "Stopped" state. If desired, you can then start the application.  Due to Varnish caching, there may be a delay of up to five minutes while requests are still routed to AppFog v2.

```
af unmap foo foo.useast.appfog.ctl.io
```

### Important

If mapping an AppFog v1 URL to an AppFog v2 applicataion users should still cancel their billing subscription for AppFog v1 from the [Account Page](https://console.appfog.com/#account) of the AppFog v1 web console. Even without a billing subscription the mapping will remain active. **Do not** request for your AppFog v1 account to be deleted, which requires a support ticket. Deleting your AppFog v1 account will remove all URL mappings.
