{{{
  "title": "Migrating SSL Support to AppFog v2",
  "date": "09-28-2015",
  "author": "Ben Heisel",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### IMPORTANT

This document is for users of AppFog v1 for migration to the next generation of AppFog that is located in CenturyLink Cloud Control Portal.

Before deleting any applications or services on AppFog v1 ensure you have local copies. Once apps and services are deleted it is **permanent**. We will not be able to provide a backup.

### AppFog SSL Support

AppFog v2 does not provide user SSL endpoints as available on AppFog v1. If you need your SSL certificate please login to open a [Support Ticket](https://support.appfog.com) or email support@appfog.com. We are unable to provide your certificate key.

For SSL support for a custom domain on AppFog v2 we recommend utilizing a service such as CloudFlare's Flexible SSL. CloudFlare's Flexible SSL will provide SSL support from the end user to their server, and endusers will see the SSL icon lock in their browser. When provisioning CloudFlare's Flexible SSL be sure to select "Flexible" under the SSL option, the default is "Full". Note, CloudFlare's Flexible SSL does not provide SSL support from the CloudFlare server to AppFog. CloudFlare's Full SSL product would require installation of your certificate on the AppFog server, which is not supported.


### Related Support Documentation:
* [CloudFlare SSL](https://www.cloudflare.com/ssl)
* [CloudFlare SSL Knowledge Base](https://support.cloudflare.com/hc/en-us/categories/200276247)
* [CenturyLink WordPress and CloudFlare](../wordpress/wordpress-cloudflare-ssl-configuration.md)
