{{{
  "title": "Getting Started with WordPress as a Service",
  "date": "04-30-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

###Overview

[WordPress](http://www.wordpress.org "WordPress.org") is a free open-source blogging tool and content management system (CMS) based on PHP and MySQL.

CenturyLink Cloud's WordPress as a Service is a secure, Enterprise class, cloud-based WordPress installation for enterprise level customers.

###Prerequisites

* Access to the CenturyLink Cloud platform as an authorized user.
 
###Configuring a New WordPress Site

1. Browse to the [CenturyLink Cloud WordPress Site Creation Login](wpaas-dashboard.useast.appfog.ctl.io "CenturyLink Cloud WordPress Site Creation Login")

  ![](../images/wp_getting_started/wp_getting_started_1.png)

2. Input your CenturyLink Cloud username and password and click Login

  ![](../images/wp_getting_started/wp_getting_started_2.png)

3. Click Create

  ![](../images/wp_getting_started/wp_getting_started_3.png)

4. Chose a Plan, input the Name for your site and your GitHub username, and click Create

  ![](../images/wp_getting_started/wp_getting_started_4.png)

5. When created, you will then see the credentials for your WordPress site, and its associated phpMyAdmin and GitHub repository.

  ![](../images/wp_getting_started/wp_getting_started_5.png)

6. You will also receive an email from CenturyLink Cloud with limited site details.

  ![](../images/wp_getting_started/wp_getting_started_6.png)
  
###Frequently Asked Questions

**Q: What are the differences between a standard WordPress install and a CenturyLink Cloud WordPress install?**

A: The CenturyLink Cloud WordPress as a service team has compiled a [knowledge base article for known WordPress Limitaions](../Managed Services/wordpress-known-limitations.md "knowledge base article for known WordPress Limitaions").

**Q: How do I migrate my existing WordPress Site to CenturyLink WordPress as a Service?**

A: The CenturyLink Cloud WordPress as a service team has compiled a [knowledge base article for manually migrating a WordPress site to CenturyLink Cloud](../Managed Services/wordpress-site-migration-to-centurylink-cloud.md "knowledge base article for manually migrating a WordPress site to CenturyLink Cloud").

**Q: Can I have persistent storage with CenturyLink Cloud WordPress as a Service?**

A: WordPress persistent storage must be [configured  with CenturyLink Cloud Object Storage](../Managed Services/wordpress-persistent-storage-configuration.md "How to Configure WordPress Persistent Storage").

**Q: How do I access the MySQL database for my WordPress Site?**

A: You can [access your WordPress database using phpMyAdmin](../Managed Services/wordpress-database-access-with-phpmyadmin.md "How to access MySQL with phpMyAdmin").

**Q: How do I install plugins and themes to my WordPress Site?**

A: You can [push plugins and themes to your WordPress site using your git repository](../Managed Services/wordpress-plugin-installation.md "How to access MySQL with phpMyAdmin").

**Q: How do I send email (such as password resets) with my WordPress Site?**

A: You must [configure SMTP for your WordPress site](../Managed Services/wordpress-SMTP-Configuration.md "How to access MySQL with phpMyAdmin") in order to send email.