{{{
  "title": "Wordpress Known Limitations",
  "date": "05-12-2015",
  "author": "Jordan Mahaney",
  "attachments": [],
  "contentIsHTML": false
}}}

### WordPress Multisite
WordPress Multisite allows a single WordPress installation to house a network of separate sites. This feature is *disabled* by default in CenturyLink Cloud WordPress, and __is not__ supported.

### Local File Storage
CenturyLink Cloud WordPress __does not__ offer long term local file system storage for media, plugins, or themes. Traditional WordPress hosting on physical or virtual machines save site content to the local disk by default, but in the Cloud environment we have configured your WordPress site to work differently.

> #### Media Content
> Your CenturyLink Cloud WordPress comes with a Cloud Storage plugin pre-installed. This is the preferred method of bypassing local file storage.

> #### Plugins and Themes
Plugins and themes should be added to the git repository that comes with your CenturyLink Cloud WordPress site to ensure the changes are persisted long term.

For more details on safely installing and storing custom content, see [Persistent Storage Configuration](../Managed Services/persitent-storage-configuration.md)

### Custom SSL and https
SSL and https are configured automatically when your CenturyLink Cloud WordPress site is installed. This configuration uses an SSL certificate issued to the infrastructure housing your site. There is currently no way to to replace the default certificates with custom SSL certificates .

Custom SSL is supported by adding a CDN to your site which will allow you to bring your own SSL certificates.

While HTTPS is enabled by default on your site, HTTP is also enabled. Disabling traffic to your site via insecure channels is not supported via the core infrastructure, but can also be achieved by adding a CDN to your site that has the ability to redirect traffic from HTTP to HTTPS.

### Plugins and themes through console
As mentioned above, the recommended method of installing plugins and themes is via direct addition to the source code using Git. The plugin and theme area of the WordPress administrative site is disabled by default to discourage using this method for installation, as it will lead to eventual loss of the files added through the console.

### Dedicated IP addresses
CenturyLink Cloud WordPress sites do not have dedicated IP Addresses. Dedicated IP addresses are unnecessary given the design of underlying cloud infrastructure. Although dedicated IP addresses are commonly believed to be a requirement for building SEO and SSL, neither of use cases are impaired by having a lack of dedicated IP.

### PhP mail
The default mail functionality is disabled in CenturyLink Cloud WordPress and cannot be enabled on the underlying infrastructure. We understand working e-mail is a crucial part of the WordPress forgot password functionality, so your WordPress site will come with a pre-installed plugin enabling use of e-mail service providers.

For more details on email configuration, see [SMTP Configuration](../Managed Services/wordpress-SMTP-Configuration.md)
