{{{
  "title": "Getting Started with MongoDB - Blueprint",
  "date": "3-17-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying the MongoDB database on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/mongodb/mongodb-logo.png" style="border:0;float:right;">

MongoDB – “simple and elegant with the freedom to scale”

http://www.mongodb.org/

#####Customer Support

* [MongoDB Community Support ](http://www.mongodb.org/get-involved)


### Description

MongoDB database technology has been integrated for automated deployment on the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this solution.

MongoDB is a cross-platform NoSQL document-oriented database. Its structure is JSON-like, making integration of data in certain types of applications easier and faster.


### Audience

CenturyLink Cloud Users


### Deploying on a new server


#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Determine whether you will be building a test cluster with small nodes or a production cluster whose nodes are configured with increased CPU and RAM.

  <img src="/knowledge-base/images/mongodb/mongodb_blueprint_tile.png" style="border:0;max-width:250px;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "MongoDB" in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="/knowledge-base/images/mongodb/deploy_parameters.png" style="max-width:450px;">

  * **Database Admin Username** - Username created in new MongoDB instance
  * **Database Admin Password** - Password created in new MongoDB instance

4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within ten minutes.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <img src="/knowledge-base/images/mongodb/deploy_complete_email.png" style="border:0;width:70%;">


### Pricing

The costs listed above in Steps 1 and 2 are for the infrastructure only.

MongoDB is Open Source community owned software with no associated cost to acquire.


### Frequently Asked Questions

**Where do I get my License?**

MongoDB is Open Source community owned software with no associated cost to acquire.

**Who should I contact for support?**

MongoDB is packaged and provided by CenturyLink as a courtesy to ease startup time. All support for this Open Source software is provided by the community. Please start at http://www.mongodb.org/

For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).


**Creating a User for your Application**

The database server is created with the admin user as the only user.  From there you will need to create a user for your Application.  You can do that by executing the following from your server:

```
[root@SERVER ~]# mongo <IP_ADDRESS>:27017/admin -u <USER_YOU_CREATED> -p <PASSWORD_OF_ADMIN_USER>
MongoDB shell version: 2.6.7
connecting to: <IP_ADDRESS>:27017/admin

> use testdb
switched to db testdb
> db.createUser(
... {
...   user: "report",
...   pwd: "<PASSWORD>",
...   roles: [
...     { role: "readWrite", db: "testdb" }
...     ]
... }
... )
Successfully added user: {
                "user" : "report",
                "roles" : [
                                {
                                                "role" : "readWrite",
                                                "db" : "testdb"
                                }
                ]
}
> exit
Bye

[root@SERVER ~]# mongo <SERVER_IP_ADDRESS>/testdb -u report -p <PASSWORD>
MongoDB shell version: 2.6.8
connecting to: <SERVER_IP_ADDRESS>:27017/testdb
> person = { name : "Joe" }
{ "name" : "Joe" }
> db.testdb.insert(person)
WriteResult({ "nInserted" : 1 })
> show collections
system.indexes
testdb
```

**What operating systems are supported for Unmanaged MongoDB?**

Unmanaged Red Hat 7
