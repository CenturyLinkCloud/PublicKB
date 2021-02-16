{{{
  "title": "WordPress Database Access with External Tools",
  "date": "07-17-2015",
  "author": "Bill Burge, Matt Wittmann",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTE

Lumen WordPress hosting is currently in a Limited Beta program with specific customers by invitation only
and is not intended for production usage.

During the Limited Beta there is no production Service Level Agreement.

## Overview

WordPress uses a MySQL relational database for storing and retrieving content like posts, pages, image paths and
comments as well as user login information.

At times it is necessary to manage the database to resolve issues or add functionality.  With your site, you get your connection details and can use the tool of your choice to administer the database.

### Prerequisites:

* A Lumen WordPress hosting site has been created.
* A suitable MySQL client is installed and ready to use. There are many compatible options—from the MySQL
  command-line interface to MySQL Workbench and other third-party tools.

## WordPress MySQL Database Access with external tools

1. In a Web browser, navigate to the [Lumen WordPress as a Service dashboard](https://wordpress.ctl.io/).
2. Log in and then choose the site whose database you want to manage from the list of sites.
3. Once the Site Details have loaded, click on the `Database` tab.
4. This page provides all the information your database client needs to connect to your WordPress site's database.

## Additional Links:

* [WordPress.org Database Description, Diagram, and Table Overview](https://codex.wordpress.org/Database_Description)
* [WordPress.org Database Code Reference (Functions, Hooks, classes, and methods)](https://developer.wordpress.org/reference)
