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

AppFog v2 provides SSL for default domains, such as &lt;appname&gt;.useast.appfog.ctl.io. SSL endpoints for custom domains are not available on AppFog v2. If you need your SSL certificate please login to open a [Support Ticket](https://support.appfog.com) or email support@appfog.com. We are unable to provide your certificate key.

For SSL support for a custom domain on AppFog v2 we recommend utilizing a service such as CloudFlare. CloudFlare, or a similar provider, will provide SSL support with their SSL certificate from the end user to the CloudFlare server. You would then need a CNAME record at CloudFlare pointing to hello-node.useast.appfog.ctl.io or hello-node.useast.appfog.ctl.io. Communication from CloudFlare to AppFog would then be encrypted with the AppFog *.appfog.ctl.io SSL certificate. When configuring SSL on CloudFlare select the Full SSL option. The "Flexible" SSl option will only provide SSL from the end user to CloudFlare. The "Full Strict" option is not supported by AppFog.


### Related Support Documentation:
* [AppFog v2 Custom Domain](../AppFog/setup-custom-domain-for-appfog-app.md)
* [CloudFlare SSL](https://www.cloudflare.com/ssl)
* [CloudFlare SSL Knowledge Base](https://support.cloudflare.com/hc/en-us/categories/200276247)
* [CenturyLink WordPress and CloudFlare](../WordPress/wordpress-cloudflare-SSL-configuration.md)
