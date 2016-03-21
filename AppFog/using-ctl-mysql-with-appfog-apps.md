{{{
  "title": "Using CenturyLink MySQL Relational DB with AppFog Applications",
  "date": "03-16-2016",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

This article will provide an overview of our [MySQL-compatible Relational DB offering](https://www.ctl.io/relational-database/) and how it can be consumed by applications deployed to AppFog. We will use JavaScript with the [MySQL Node.js module](https://github.com/felixge/node-mysql/) to demonstrate using CenturyLink's Relational DB service.

### Relational DB Service Deployment Options

There are two options for provisioning a Relational DB Service (RDBS) instance for use with AppFog. Regardless of the provisioning method, the Relational DB service instance product and pricing model are the same. Pricing can be estimated from the Relational DB Services section of our [Price Estimator](https://www.ctl.io/estimator/).

<h5><a href="#cli">1. Provisioning using the AppFog CLI tool</a><h5>
- This method offers several RDBS instance options with preconfigured resource allocation.
- The preset resource allocation can not be scaled.
- The VCAP_SERVICES environment variable is available for connection to the service.
 
<h5><a href="#rdbs">2. Provisioning from the Relational DB page</a><h5>

- This method provides the abiltiy for users to customize resource allocation upon service creation.
- These RDBS instances can be scaled at anytime, requiring a restart which typically only takes a few minutes.
- Backups are readily available for download.
- Replication can be enabled or disabled.
- The VCAP_SERVICES environment variable is **not** available for connection to the service.

### Using An RDBS Instance To Host Multiple Databases

* An RDBS instance created from AppFog has a database named `default` created, which is provided in the `dbname` field of the VCAP_SERVICES environment variable. Users can create multiple databases within a single RDBS instance instead of creating a new RDBS instance for each application. *Note:* Since VCAP_SERVICES will only provide the `default` database for connection the user created database needs to be provided in the connection configuration. This example shows configuration to conncect to a user created database named `myapp-db`, instead of using VCAP_SERVICES to connect to the `default` database:

```
// set connection info from CenturyLink Relational DB service instance
// credentials from VCAP_SERVICES environment variable
if (process.env.VCAP_SERVICES) {
  var services = JSON.parse(process.env.VCAP_SERVICES);
  var ctlMysqlConfig = services["ctl_mysql"];

  if (ctlMysqlConfig) {
    var node = ctlMysqlConfig[0];
    connectionInfo = {
        host: node.credentials.host,
        port: node.credentials.port,
        user: node.credentials.username,
        password: node.credentials.password,
        database: 'myapp-db',
        ssl: {
          ca: node.credentials.certificate
        }
    };
  }
  ```
  
  * RDBS instances created from the Relational DB page are also able to host multiple databases, they do not have a `default` database created. Users must create a database within the instance.

<h3 id="cli">Create a Relational DB Service Instance from the AppFog CLI</h3>
 
[CenturyLink Relational DB](https://www.ctl.io/relational-database/) is included in the AppFog marketplace and can be provisioned using the Cloud Foundry CLI tool. In order to do this you must be [logged into an AppFog region](login-using-cf-cli.md). Service offerings can be viewed by running the following command in a terminal window:

```
$ cf marketplace
...
service       plans                             description   
ctl_mysql     micro*, small*, medium*, large*   CenturyLink's Relational DB Service, MySQL-compatible database-as-a-service with SSL encryption option and daily backups held 7 days.  Please see https://www.ctl.io/legal/ for terms of service.   
orchestrate   free                              Orchestrate DBaaS   

* These service plans have an associated cost. Creating a service instance will incur this cost.
```
Running `cf marketplace -s <SERVICE_NAME>` will provide resource and pricing information about plans available with that service.

The `cf create-service <SERVICE> <PLAN> <YOUR_SERVICE_NAME>` command will provision a new MySQL-compatible instance that can later be bound to an application deployed to AppFog. The following command will create a new micro Relational DB service instance named `acmedb`:

```
$ cf create-service ctl_mysql micro acmedb
```


##### Bind Relational DB to Application

To bind the Relational DB service instance to an [application deployed to AppFog](deploy-an-application.md) you can use the `cf bind-service <APP_NAME> <SERVICE_NAME>` command:

```
$ cf bind-service myapp acmedb
```

This will add the CenturyLink Relational DB service instance access credentials into the `myapp` application's runtime environment. To view these MySQL service instance credentials use the `cf env <APP_NAME>` command and they will be located in the VCAP_SERVICES environment variable which is a convention for Cloud Foundry enabled services:

```
$ cf env myapp
...
System-Provided:
{
 "VCAP_SERVICES": {
  "ctl_mysql": [
   {
    "credentials": {
     "certificate": "-----BEGIN CERTIFICATE-----\n{...}\n-----END CERTIFICATE-----",
     "dbname": "default",
     "host": "<SERVICE_URL>",
     "hostname": "<SERVICE_URL>",
     "jdbcUrl": "<JDBC_URL>",
     "name": "default",
     "password": "<PASSWORD>",
     "port": <PORT>,
     "username": "<USERNAME>"
    },
    "label": "ctl_mysql",
    "name": "acmedb",
    "plan": "micro",
    "tags": []
   }
  ],

```

These credentials can be populated into a MySQL client library for the specific runtime for your application. Below we will show an example using Node.js and the MySQL client module.



<h3 id="rdbs">Create a Relational DB Service from the Relational DB Page</h3>

To create a Reltaional DB Service (RDBS) from outside of AppFog either naviagate direclty to [rdbs.ctl.io](https://rdbs.ctl.io/), or from the [Control Portal](https://control.ctl.io) use the dropdown arrow in the upper right corner and select Relational DB from the menu. Our [Getting Started with Relational DB Service](https://www.ctl.io/knowledge-base/database/getting-started-with-mysql-rdbs/) article describes how to create an RDBS instance.

### Example: Using RDBS service in Node.js MySQL Client

This section will assume that you have an existing Node.js application named `myapp` which needs a MySQL database . The first step is to add the MySQL client module to the `myapp` Node.js application using NPM (Node Package Manager).

```
$ npm install mysql --save
```

Also, since commands are sent to MySQL asynchronously with promises, we should include the [Q Node.js module](https://www.npmjs.com/package/q).

```
$ npm install q --save
```

The application's package.json should include `mysql` and `q` modules similar to what is located under `dependencies` below:

```
{
  "name": "myapp",
  "version": "0.0.1",
  ...
  "dependencies": {
    ...
    "mysql": "^2.9.0",
    "q": "^1.1.2"
  }
}

```

##### Example Connecting to an RDBS Instance Created From AppFog CLI

Now that the Node.js MySQL client is available, we use require to pull the module into the application, pull credentials from application's AppFog deployment environment, and setup a function to enable execution of SQL statements against the MySQL database. Below is code that can be used to do all of this that can be put into a file named `dbconfig.js`:

```
var mysql = require('mysql');

// default connection info for local development
var connectionInfo = {
  user: 'user',
  password: 'myP@ssW0rd',
  database: 'myappdb'
};

// set connection info from CenturyLink Relational DB service instance
// credentials from VCAP_SERVICES environment variable
if (process.env.VCAP_SERVICES) {
  var services = JSON.parse(process.env.VCAP_SERVICES);
  var ctlMysqlConfig = services["ctl_mysql"];

  if (ctlMysqlConfig) {
    var node = ctlMysqlConfig[0];
    connectionInfo = {
        host: node.credentials.host,
        port: node.credentials.port,
        user: node.credentials.username,
        password: node.credentials.password,
        database: node.credentials.dbname,
        ssl: {
          ca: node.credentials.certificate
        }
    };
  }
}

// create function named 'query' to use for SQL statement execution
// against MySQL database
exports.query = function(query, callback) {
  var connection = mysql.createConnection(connectionInfo);
  connection.query(query, function(queryError, result) {
    callback(queryError, result);
  });
  connection.end();
};

``` 

##### Example Connecting to RDBS Instance Created From Relational DB Page

A conncection string will be provided to access your RDBS instance, the username and password are selected when creating the service. You can use a third-party tool or your local MySQL install to connect to your RDBS instance to create a database. 

```
var mysql = require('mysql');

// use RDBS connection info
var connectionInfo = {
  user: '<USER_NAME>',
  password: '<PASSWORD>',
  host: '<HOST>',
  port: '<PORT>',
  database: 'myappdb',
  ssl: {
    ca: '<DOWNLOADED_CERT>'
  }
};

// create function named 'query' to use for SQL statement execution
// against MySQL database
exports.query = function(query, callback) {
  var connection = mysql.createConnection(connectionInfo);
  connection.query(query, function(queryError, result) {
    callback(queryError, result);
  });
  connection.end();
};
```

### Example SQL Statement

To use the MySQL connection to execute SQL statements from the application, we must require our new `dbconfig` module and then send a valid SQL command to the query function:

```
var Q = require('q');
var dbconfig = require('./dbconfig');

var addItem = exports.addItem = function(name, description) {
  var insertStatement = 'insert into items (name, description) ' +
    'values ("' + name + '", "' + description + '")';
  dbconfig.query(insertStatement, function(queryError, result) {
    // handle error or result
  });
};

exports.findAllItems = function() {
  var selectStatement = 'select * from items';
  var deferred = Q.defer();
  dbconfig.query(selectStatement, function(queryError, result) {
    deferred.resolve(result);
  });
  return deferred.promise;
}
```
The code above provides a function that adds an item with a name and description into the items table. In addition, there is a corresponding function to find all items in the items table using a promise.
