{{{
  "title": "WordPress Cloud Flare SSL Termination",
  "date": "08-25-2015",
  "author": "Earl Herman",
  "attachments": [],
  "contentIsHTML": false
}}}
### IMPORTANT NOTECenturyLink Cloud WordPress hosting is currently in a Limited Beta program with specific customers by invitation only and is not intended for production usage.During the Limited Beta there is no production Service Level Agreement.## Overview:

There is currently no automated method for adding SSL termination for a WordPress site in CenturyLink Cloud's WordPress. There are multiple methods that could be used to terminate SSL for an existing WordPress site in CenturyLink Cloud WordPress site. This method covers using CloudFlare CDN's SSL Termination.

### This migration path assumes the following:

* Working knowledge of basic WordPress functionality
* Working knowledge of how to [Configure SSL on Cloud Flare] (https://support.cloudflare.com/hc/en-us/articles/204468848-How-do-I-access-or-change-any-of-my-SSL-settings-)

### Prerequisites:

1. A CenturyLink WordPress site
2. A Custom FQDN added to your WordPress Site.
3. Your Custom FQDN referencing your website "wordpress.ctl.io" URL4.	An existing [CloudFlare] (https://www.cloudflare.com/) account
## CloudFlare Settings Supported* SSL (with SPDY) = Full, FLexible, or Off (Strict is not currently supported)
* HTTP Strict Transport Security (HSTS)
 * Max Age Header (max-age)			= Any Setting
 * Apply HSTS policy to subdomains	= On or Off
 * Preload								= On or Off
 * No-Sniff Header						= On or Off
* Authenticated Origin Pulls			= On or Off
