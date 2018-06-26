{{{
  "title": "Using CenturyLink MySQL Relational DB with AppFog Applications",
  "date": "02-08-2016",
  "author": "Chris Sterling",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false
}}}

<strong>The AppFog service will be retired as of June 29, 2018. Beginning on this date, the AppFog Platform-as-a-Service will no longer be available, including all source code, env vars, and database information.</strong>

### Audience

Application developers

### Overview

This article will provide an overview of our [MySQL-compatible Relational DB offering](https://www.ctl.io/relational-database/)
and how it can be consumed by applications deployed to AppFog.
We will use JavaScript with the [MySQL Node.js module](https://www.npmjs.com/package/mysql)
to demonstrate using CenturyLink's Relational DB service.

[CenturyLink Relational DB](https://www.ctl.io/relational-database/) is included in the AppFog marketplace.
You can find it via the Cloud Foundry CLI by running the following command in a terminal window:

```
$ cf marketplace
...
service       plans                              description   
ctl_mysql     mysql_single, mysql_replicated     CenturyLink's Relational DB Service, MySQL-compatible database-as-a-service with SSL encryption option and daily backups held 7 days.  Please see https://www.ctl.io/legal/ for terms of service.
```

### Create a Relational DB Service Instance

To create a new CenturyLink Relational DB service instance, we can use the Cloud Foundry CLI.
In order to do this you must be [logged into an AppFog region](login-using-cf-cli.md). The following
command will create a new micro Relational DB service instance named `acmedb`:

```
$ cf create-service ctl_mysql mysql_single acmedb
```

The `cf create-service` command will provision a new MySQL-compatible instance that can later be
bound to an application deployed to AppFog.

### Bind Relational DB to Application

To bind the Relational DB service instance to an [application deployed to AppFog](deploy-an-application.md) you can use the `cf bind-service` command:

```
$ cf bind-service myapp acmedb
```

This will add the CenturyLink Relational DB service instance access credentials into the `myapp` application's
runtime environment. To view these MySQL service instance credentials use the `cf env` command
(or the "Environment" area for an application in the AppFog UI) and they will be
located in the VCAP_SERVICES environment variable which is a convention for Cloud Foundry enabled services:

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
    "plan": "mysql_single",
    "tags": []
   }
  ],

```

These credentials can be populated into a MySQL client library for the specific runtime for your application.
Below we will show an example using Node.js and the MySQL client module.

### Delete a Relational DB Service Instance

To delete a Relational DB service use the `cf delete-service` command.

```
cf delete-service acmedb
```

Before deleting a service it must be unbound from any applications using the `cf unbind-service` command.

```
cf unbind-service myapp acmedb
```

Note: Attempts to immediately delete a newly created Relational DB service will result in the below error. Waiting several minutes to pass after creating a new Relational DB instance will allow the service to be deleted.

```
FAILED
Server error, status code: 502, error code: 10001, message: Service instance tezt: The service broker returned an invalid response for the request to https://addons.ctl.io/brokers/cfv2/usea
st/v2/service_instances/c724ac99-5119-4f08-bf10-410344bacbcc. Status Code: 409 Conflict, Body: {}
```

### Example: Using Environment Credentials in Node.js

This section will assume that you have an existing Node.js app which needs a MySQL database named `myapp`.
The first step is to add the MySQL client module to `myapp` Node.js application using NPM (Node Package Manager)
for including the dependency.

```
$ npm install mysql --save
```

Also, since commands are sent to MySQL asynchronously with promises, we should include
the [Q Node.js module](https://www.npmjs.com/package/q).

```
$ npm install q --save
```

The application's package.json should include `mysql` and `q` modules similar to what is located under `dependencies` below:

```
{
  "name": "myapp",
  "version": "0.0.1",
  "dependencies": {
    "mysql": "^2.9.0",
    "q": "^1.1.2"
  }
}

```

Now that the Node.js MySQL client is available, we use require to pull the module into the application,
pull credentials from application's AppFog deployment environment and setup a function to enable execution
of SQL statements against the MySQL database. Below is code that can be used to do all of this that can be put
into a file named `dbconfig.js`:

```
var mysql = require('mysql');

// default connection info for local development
var connectionInfo = {
  user: 'user',
  password: 'myP@ssW0rd',
  database: 'myappdb'
};

// set connection info from db service instance credentials from VCAP_SERVICES environment variable
if (process.env.VCAP_SERVICES) {
  var services = JSON.parse(process.env.VCAP_SERVICES);
  var ctlMysqlConfig = services['ctl_mysql'];

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

// create function 'query' for SQL statement execution against MySQL database
exports.query = function(query, callback) {
  var connection = mysql.createConnection(connectionInfo);
  connection.query(query, function(queryError, result) {
    callback(queryError, result);
  });
  connection.end();
};

```

To use the MySQL connection to execute SQL statements from the application, we must require
our new `dbconfig` module and then send a valid SQL command to the query function:

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

The code above provides a function that adds an item with a name and description into the items table.
In addition, there is a corresponding function to find all items in the items table using a promise.

### Example: Using Environment Credentials in Java

The Java example below uses [Gradle](http://gradle.org/) as its build system. The
build file, `build.gradle`, appears below:

```
plugins {
    id 'java'
    id 'com.github.johnrengelman.shadow' version '1.2.3'
}

repositories {
    mavenCentral()
}

dependencies {
    compile 'org.mariadb.jdbc:mariadb-java-client:1.3.6'
    compile 'com.google.code.gson:gson:2.6.2'
}

jar {
    manifest {
        attributes 'Main-Class': 'main.Main'
    }
}
```

* The [shadow](https://github.com/johnrengelman/shadow) build plugin is used to bundle a fat jar that includes all the dependencies.
* [gson](https://github.com/google/gson) is used to parse the environment services json.
* The MySQL compatible connector [mariadb-java-client](https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/) is used to communicate with the ctl_mysql service.

And here's the code for `src/main/java/main/Main.java`:

```
package main;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import java.sql.*;
import java.util.Properties;

public class Main {

    public static void main(String args[]) throws Exception {
        Connection conn = buildConnection();

        //AppFog expects a process to stay running, so loop forever and query every 5 seconds
        while (true) {
            String query = "select name, description from items";
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                System.out.println("Row (name, description) '" + rs.getString(1) + "', '" + rs.getString(2) + "'");
            }
            Thread.sleep(5000);
        }
    }

    //establish a database connection
    private static Connection buildConnection() throws InstantiationException, IllegalAccessException, ClassNotFoundException, SQLException {
        ServicesConfig servicesConfig = loadServicesConfig();

        Class.forName("org.mariadb.jdbc.Driver").newInstance();
        String connectionString = "jdbc:mysql://" +
                servicesConfig.ctl_mysql[0].credentials.host +
                ":" + servicesConfig.ctl_mysql[0].credentials.port +
                "/" + servicesConfig.ctl_mysql[0].credentials.dbname;

        Properties properties = new Properties();
        properties.setProperty("user", servicesConfig.ctl_mysql[0].credentials.username);
        properties.setProperty("password", servicesConfig.ctl_mysql[0].credentials.password);
        properties.setProperty("useSSL", "true");
        properties.setProperty("serverSslCert", servicesConfig.ctl_mysql[0].credentials.certificate);

        return DriverManager.getConnection(connectionString, properties);
    }

    //parse the environment json into credentials object
    private static ServicesConfig loadServicesConfig() {
        Gson gson = new GsonBuilder().create();
        ServicesConfig servicesConfig = gson.fromJson(System.getenv("VCAP_SERVICES"), ServicesConfig.class);
        assert servicesConfig != null;
        assert servicesConfig.ctl_mysql != null && servicesConfig.ctl_mysql.length == 1;
        assert servicesConfig.ctl_mysql[0].credentials != null;

        return servicesConfig;
    }

    //objects representing json vcap services
    private class ServicesConfig {
        private CtlMysqlConfig[] ctl_mysql;
    }

    private class CtlMysqlConfig {
        Credentials credentials;
    }

    private class Credentials {
        private String certificate;
        private String dbname;
        private String host;
        private String password;
        private Integer port;
        private String username;
    }
}
```

`main()` is a loop that runs simply forever: AppFog expects a program to continue running, so this
example simply queries every five seconds indefinitely and prints out the results.

`buildConnection()` establishes the database connection with the provisioned ctl_mysql database.
It takes an object representing the parsed environment and builds up a proper connection string. Note
the use of properties `useSSL` and `serverSslCert` to establish a secure connection. `serverSslCert`
is the reason I chose the MySQL compatible MariaDB connector. Establishing a secure connection
with a certificate string is a bit more cumbersome in other drivers.

`loadServicesConfig()` parses the environment to get database credentials/host/cert/port. There are quite a few
json parsing libraries out there; pick your favorite. I included the asserts for getting started in the event
that someone begins with this code example; a real world app would want use thorough error handling.

Finally, below is the deployment file `manifest.yml`. The property `no-route` is included as the
app doesn't respond to http requests
(the Diego runtime also requires [disabling health checks](using-diego.md) in non-webapps):

```
applications:
- name: java-mysql
  memory: 512M
  instances: 1
  path: build/libs/java_mysql-all.jar
  no-route: true
  buildpack: https://github.com/cloudfoundry/java-buildpack.git
```
