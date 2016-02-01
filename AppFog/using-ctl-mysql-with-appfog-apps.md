{{{
  "title": "Using CenturyLink MySQL with AppFog Applications",
  "date": "10-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

### Audience

Application developers

### Overview

This article will provide an overview of our [new CenturyLink MySQL Database-as-a-Service offering](https://www.ctl.io/dbaas/) that is currently in beta and how it can be consumed by applications deployed to AppFog. We will use JavaScript with the [MySQL Node.js module](https://github.com/felixge/node-mysql/) to demonstrate using the CenturyLink MySQL service.

#### Warning - MySQL Service in Beta

The [CenturyLink MySQL Database-as-a-Service](https://www.ctl.io/dbaas/) recently went into beta and is currently included in the AppFog marketplace. You can find via the Cloud Foundry CLI by running the following command in a terminal window:

```
$ cf marketplace
...
service       plans                description   
ctl_mysql     micro                CenturyLink's BETA MySQL DBaaS.  For development use only; not subject to SLAs.
```

As the description mentions, the `ctl_mysql` service is in beta and is for development use only at this time. Although we have no guarantees of service availability yet our DBaaS team is focused on providing the best service possible as they gather feedback. Please go the [DBaaS product page](https://www.ctl.io/dbaas/) to learn more.

### Create a MySQL Service Instance

To create a new CenturyLink MySQL service instance, we can use the Cloud Foundry CLI. In order to do this you must be [logged into an AppFog region](login-using-cf-cli.md). The following command will create a new CenturyLink MySQL service instance named `acmedb`:

```
$ cf create-service ctl_mysql micro acmedb
```

The `cf create-service` command will provision a new MySQL instance that can later be bound to an application deployed to AppFog.

### Bind MySQL to Application

To bind the MySQL service instance to an [application deployed to AppFog](deploy-an-application.md) you can use the `cf bind-service` command:

```
$ cf bind-service myapp acmedb
```

This will add the CenturyLink MySQL service instance access credentials into the `myapp` application's runtime environment. To view these MySQL service instance credentials use the `cf env` command and they will be located in the VCAP_SERVICES environment variable which is a convention for Cloud Foundry enabled services:

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
     "host": "{IP Address}",
     "password": "{Password}",
     "port": {Port Number},
     "username": "{Username}"
    },
    "label": "ctl_mysql",
    "name": "acmedb",
    "plan": "micro",
    "tags": []
   }
  ],

```

These credentials can be populated into a MySQL client library for the specific runtime for your application. Below we will show an example using Node.js and the MySQL client module.

### Example: Using Credentials from Environment in Node.js MySQL Client

This section will assume that you have an existing Node.js which needs a MySQL database named `myapp`. The first step is to add the MySQL client module to `myapp` Node.js application using NPM (Node Package Manager) for including the dependency.

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

Now that the Node.js MySQL client is available, we use require to pull the module into the application, pull credentials from application's AppFog deployment environment and setup a function to enable execution of SQL statements against the MySQL database. Below is code that can be used to do all of this that can be put into a file named `dbconfig.js`:

```
var mysql = require('mysql');

// default connection info for local development
var connectionInfo = {
  user: 'user',
  password: 'myP@ssW0rd',
  database: 'myappdb'
};

// set connection info from CenturyLink MySQL service instance
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
