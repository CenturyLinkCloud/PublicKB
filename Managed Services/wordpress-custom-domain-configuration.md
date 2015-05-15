{{{
  "title": "WordPress Custom Domain Configuration",
  "date": "05-15-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

CenturyLink Cloud WordPress supports custom domain name configuration after [setting up a new site](getting-started-with-managed-wordpress.md "Getting Started with Managed WordPress").

1. Browse to https://wpaas-dashboard.useast.appfog.ctl.io, login with your CenturyLink Cloud User Name and Password and click Login

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_1.png "wp_custom_domain_configuration_1.png")

2. From the list of WordPress Sites, select the site you would like to configure a custom domain for.

  _In this example ctl-kb_

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_2.png "wp_custom_domain_configuration_2.png")

3. Select the Domains tab.

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_3.png "wp_custom_domain_configuration_3.png")

4. Click Add Domain

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_4.png "wp_custom_domain_configuration_4.png")

5. Input your domain name and click Save

  _in this example wordpress.centurylink.com_
  
  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_5.png "wp_custom_domain_configuration_5.png")

6. You will then see your saved domain name as an additional domain that can be edited or deleted.

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_7.png "wp_custom_domain_configuration_7.png")

7. Login to your WordPress site using the CenturyLink Cloud provided URL and browse to Settings > General

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_8.png "wp_custom_domain_configuration_8.png")

8. Find the section with the following variables
  * WordPress Address (URL)
  * Site ADdress (URL)

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_9.png "wp_custom_domain_configuration_9.png")

9. Input your domain name 

  _in this example wordpress.centurylink.com_
  
  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_10.png "wp_custom_domain_configuration_10.png")

10. Scroll to the bottom and click Save Changes

  ![](../images/wp_custom_domain_configuration/wp_custom_domain_configuration_11.png "wp_custom_domain_configuration_11.png")
  
11. Your site is now using your custom domain name.