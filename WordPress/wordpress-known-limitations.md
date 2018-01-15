{{{
  "title": "Known Limitations",
  "date": "10-19-2015",
  "author": "Jordan Mahaney, Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTE

CenturyLink WordPress hosting is currently in a Limited Beta program with specific customers by invitation only and is not intended for production usage.

During the Limited Beta there is no production Service Level Agreement.

## Known Limitations of CenturyLink WordPress Hosting
CenturyLink WordPress hosting is designed to minimize the management of a WordPress site by abstracting away many of the typical installation and maintenance tasks. The platform is cloud native, so there are several use cases that work differently than a traditional hosted WordPress site or may be completely unavailable.


* [__WordPress Multisite__](#multisite)
* [__Local File Storage__](#storage)
* [__Custom SSL and HTTPS__](#ssl)
* [__Plugins and themes through console__](#plugins)
* [__Dedicated IP addresses__](#ip-address)
* [__PHP mail__](#mail)

## <a name="multisite"></a>WordPress Multisite
WordPress Multisite allows a single WordPress installation to house a network of separate sites. This feature is currently *disabled* by default in CenturyLink Cloud WordPress hosting, and __is not__ supported.

## <a name="storage"></a>Local File Storage
CenturyLink WordPress hosting __does not__ offer long term local file system storage for media, plugins, or themes. Traditional WordPress hosting on physical or virtual machines save site content to the local disk by default.  In the Cloud environment we have configured your WordPress site to work differently by allowing the site to use a previously created object storage bucket.

For more details please check out the Knowledge Base articles to [create an object storage bucket](https://www.ctl.io/knowledge-base/object-storage/using-object-storage-from-the-control-portal/) and how to [create a WordPress site with object storage](https://www.ctl.io/knowledge-base/wordpress/getting-started-with-wordpress-as-a-service/).

> #### Media Content
>CenturyLink WordPress hosting comes with a cloud storage plugin pre-installed. This is the preferred method of bypassing local file storage.

> #### Plugins and Themes
Plugins and themes should be added to the git repository that comes with your CenturyLink Cloud WordPress hosting to ensure the changes are persisted long term.

## <a name="ssl"></a>Custom SSL and HTTPS
SSL and HTTPS are configured automatically when your WordPress site is installed. This configuration uses an SSL certificate issued to the infrastructure housing your site. There is currently no way to to replace the default certificates with custom SSL certificates .

Custom SSL is supported by adding a [CDN](https://www.ctl.io/knowledge-base/wordpress/wordpress-cloudflare-ssl-configuration/) to your site which will allow you to bring your own SSL certificates.

While HTTPS is enabled by default on your site, HTTP is also enabled. Disabling traffic to your site can also be achieved in two ways. Either by:

* changing the URL value in the WordPress admin console to https

```settings -> general -> WordPress Address (URL)``` and ```settings -> general -> Site Address (URL)```
* adding a [CDN](https://www.ctl.io/knowledge-base/wordpress/wordpress-cloudflare-ssl-configuration/) to your site that has the ability to redirect traffic from HTTP to HTTPS.

## <a name="plugins"></a>Plugins and themes through console
As mentioned above, the recommended method of installing plugins and themes is via direct addition to the source code using Git. The plugin and theme area of the WordPress administrative site is disabled by default to discourage using this method for installation, as it will lead to eventual loss of the files added through the console.

For more details on installing plugins and themes, see the [plugin install article](https://www.ctl.io/knowledge-base/wordpress/wordpress-plugin-installation/).

We have also configured a [local development environment](https://www.ctl.io/knowledge-base/wordpress/wordpress-local-development/) that comes with all sites created and allows users to search, download and install plugins and themes from the WordPress admin console and then push those updates to your live site with [Git](https://www.ctl.io/knowledge-base/wordpress/wordpress-site-updates-with-git/).

## <a name="ip-address"></a>Dedicated IP addresses
The sites do not have dedicated IP Addresses. Dedicated IP addresses are unnecessary given the design of underlying cloud infrastructure. Although dedicated IP addresses are commonly believed to be a requirement for building SEO and SSL, neither of use cases are impaired by having a lack of dedicated IP.

## <a name="mail"></a>PHP mail
The default PHP mail functionality is disabled and cannot be enabled on the underlying infrastructure. We understand working e-mail is a crucial part of the WordPress forgot password functionality, so your site will come with a pre-installed plugin enabling use of e-mail service providers.

For more details on the email configuration, see [WordPress SMTP Configuration](wordpress-SMTP-Configuration.md)
