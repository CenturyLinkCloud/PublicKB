{{{
  "title": "Data Import",
  "date": "4-20-2015",
  "author": "Adam DuVander",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

There are a number of tools available to help with importing data into the Orchestrate service. These tools are designed to be run in one of [the data centers](https://orchestrate.io/docs/multi-data-center) that Orchestrate is deployed in to minimise the time for the import operation to complete.

We do have plans to add an option to import data into Orchestrate from directly within the Dashboard, via an S3 bucket or via a file upload. If you'd like to follow the progress on this work, please vote for the feature in our [UserVoice](http://orchestrate.uservoice.com/forums/221954-general/suggestions/6740446-data-import-from-the-dashboard).

If you need any help, or have any questions about any of our import tools you can always reach us in the [Orchestrate Community chatroom](http://oio-community.useast.appfog.ctl.io).

All of our import tools are open-source on [GitHub](https://github.com/orchestrate-io).

### Use the Orchestrate Bulk API

The [Orchestrate Bulk API](https://orchestrate.io/docs/apiref#bulk) provides endpoints for POSTing multiple records (any combination of items, events, and relationships) within the body of a single HTTP request. This can be a convenient way of reloading data from an [Orchestrate Export](./data-export.md), since bulk operation objects use a compatible data-model as export files.

### Import from SQL Databases

Our [JDBC-importer](https://github.com/orchestrate-io/jdbc-importer) allows users to transfer data from existing JDBC compatible databases. It supports MySQL and PostgreSQL by default. Oracle DB and the Microsoft SQL Server JDBC drivers are under restrictive licenses and must be configured manually.

You can download the tool from the [releases page](https://github.com/orchestrate-io/jdbc-importer/releases). It's been developed in Java and requires the Java Runtime Environment 6 or greater.

The importer works by executing a SQL `SELECT` statement you've written on the SQL database you'd like to connect and import from. These records are then written to Orchestrate in parallel into a collection name of your choice. The tool is configured via command line options or using a JSON config file.

```
{
  "selectQuery": "SELECT * FROM table WHERE deleted = 0",
  "primaryField": "id",
  "source": "jdbc:mysql://localhost/yourDb",
  "username": "mysqluser",
  "password": "mysqlpassword",
  "apiKey": "yourOrchestrateApiKey",
  "collection": "yourCollectionName"
}
```

To run the importer with the config file use:

```
java -jar orchestrate-jdbc-importer-uber-jar.jar config.json
```

For more advanced options check out the project [on GitHub](https://github.com/orchestrate-io/jdbc-importer).

### Import from MongoDB, CouchDB and other NoSQL databases

[Orchestrate-mongo](https://github.com/orchestrate-io/orchestrate-mongo) and [orchestrate-couchdb](https://github.com/orchestrate-io/orchestrate-couchdb) are NodeJS applications for copying data from MongoDB and CouchDB into the Orchestrate service. They can be downloaded and installed via NPM.

Both of these tools can be run as daemon processes or as command line tools. Both are configured using environment variables. The environment variables are:

* ORCHESTRATE_API_KEY
* MONGODB_DATABASE (or COUCHDB_URL respectively)
* MONGODB_USERNAME (or COUCHDB_USERNAME respectively)
* MONGODB_PASSWORD (or COUCHDB_PASSWORD respectively)
* MONGODB_COLLECTION (or COUCHDB_DATABASE respectively)

For more information on these tools you can find the [orchestrate-mongo](https://github.com/orchestrate-io/orchestrate-mongo) and [orchestrate-couchdb](https://github.com/orchestrate-io/orchestrate-couchdb) projects on GitHub.

We currently don't have any official tools to handle other NoSQL databases, if this is something you need please [get in touch](mailto:support@orchestrate.io) or create a new [UserVoice idea](http://orchestrate.uservoice.com/).

### Import from CSV

[Orc-csv](https://github.com/orchestrate-io/orc-csv) is our NodeJS tool to upload data in CSV files to the Orchestrate service.

The tool works by reading a CSV file and writing the data into Orchestrate in parallel. The structure of the CSV file is expected to have a "header line" which is used as the field names for the JSON objects that are stored to Orchestrate. e.g.

```
name,age,gender
Some Name, 20, male
Another Name, 30, female
```

You can download and install the tool with NPM:

```
npm install -g orc-csv
```

When the tool has been installed you can run it by passing command line arguments to the application. You'll need to provide an API key, the name of the collection to write the CSV records into and the full path to the CSV file:

```
orc-csv -u "your-api-key" -c "collection-name" -f file.csv
```

For more advanced options check out the project [on GitHub](https://github.com/orchestrate-io/orc-csv).

### Import from XML or JSON

We currently don't have any official tools to handle XML or JSON file imports, if this is something you need please [get in touch](mailto:support@orchestrate.io) or create a new [UserVoice idea](http://orchestrate.uservoice.com/).

### Custom Data Formats

To import data from more specialist data formats (like binary formats produced by different database engines) please open a support ticket on our [Dashboard](https://dashboard.orchestrate.io). We're happy to help with the import process and/or build the necessary tools to handle the task.

### Handling Large Imports

We understand that it can be impractical to handle very large imports (datasets larger than a few GBs). We have a number of internal tools to efficiently store and index very large datasets into the Orchestrate service. We're happy to help with the import process, please open a support ticket on our [Dashboard](https://dashboard.orchestrate.io) and we'll manage the data import for you.
