{{{
"title": "Cloud Platform - Release Notes: September 13, 2016",
"date": "09-13-2016",
"author": "Anthony Hakim",
"attachments": [],
"contentIsHTML": false
}}}


### Enhancements (1)

* __Ubuntu 16.04 Support__

  Lumen Cloud now supports Ubuntu 16 as an OS template for servers. Customers can now create and deploy 64-bit Ubuntu 16 virtual instances to all data centers. Check out [what’s new in version 16](http://www.ubuntu.com/server) and read the [Ubuntu 16.04 Release Notes](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04) for more information.

  ![Ubuntu 16.04](../../images/2016-09-13_Ubuntu16_04.png)

### Announcements (1)

* __Relational DB now available in Runner!__

  Users can now incorporate Relational DB into a Runner job to deploy a MySQL-compatible Relational DB instance to IL1, VA1, NY1, UC1, GB3, SG1 or CA3.  Visit https://runner.ctl.io to view Relational DB in the marketplace and https://www.ctl.io/relational-database/ for additional product information. [Standard pricing applies](https://www.ctl.io/pricing/).

  ![Relational DB](../../images/2016-09-13_RDB.png)

### Bug Fixes (2)

  * __Control Portal - Minor User Interface improvements__

    - Occasionally, when a user tried to create a new server but hit an account resource limit, the error notification message they received didn't clearly indicate why they couldn't create a server.
    - The user flow for creating new Anti Affinity policies from the new server page was broken.
