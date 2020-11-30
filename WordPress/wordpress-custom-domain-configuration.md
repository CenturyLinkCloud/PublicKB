{{{
  "title": "WordPress Custom Domain Configuration",
  "date": "07-17-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTE

Lumen WordPress hosting is currently in a Limited Beta program with specific customers by invitation only and is not intended for production usage.

During the Limited Beta there is no production Service Level Agreement.

### Overview
Lumen WordPress supports custom domain name configuration after [setting up a new site](getting-started-with-wordpress-as-a-service.md).

### Prerequisite

You have added a CNAME, ALIAS, or similar DNS record between your custom domain and your supplied WordPress site
domain. For example, you could create a CNAME record like this:

```
www.example.com.    CNAME   example.useast.wordpress.ctl.io.
```

### WordPress Custom Domain Configuration

1. Browse to [wordpress.ctl.io](https://wordpress.ctl.io), login with your Lumen Cloud User Name and Password and click Login

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_01.png)

2. From the list of WordPress Sites, select the site you would like to configure a custom domain for.

  _In this example ctl-kb_

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_02.png)

3. Select the Domains tab.

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_03.png)

4. Click Add Domain

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_04.png)

5. Input your domain name and click Save

  _in this example wordpress.centurylink.com_

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_05.png)

6. You will then see your saved domain name as an additional domain that can be edited or deleted.

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_06.png)

7. Follow the steps to [update your site using git](wordPress-site-updates-with-git.md). Specifically, you will
   need to modify the file `wp-config.php`.
8. Look for the lines:

   ```
   define('WP_SITEURL', getenv("SITEURL"));
   define('WP_HOME', getenv("SITEURL"));
   ```

9. Replace both instances of `getenv("SITEURL")` with a URL using your new domain. For example:

   ```
   define('WP_SITEURL', "https://www.example.com");
   define('WP_HOME', "https://www.example.com");
   ```

   Note that the `WP_SITEURL` variable defines the base URL used for the WordPress administration console, and
   `WP_HOME` defines the base URL for the general, publicly accessible site.
10. When you are ready, you can [commit and push](wordPress-site-updates-with-git.md) your change back up to Lumen
    Git Hosting.
11. Your site is now using your custom domain name.
