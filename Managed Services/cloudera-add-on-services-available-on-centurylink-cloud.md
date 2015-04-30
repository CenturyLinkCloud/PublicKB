{{{
  "title": "Cloudera Add-On Services Available on CenturyLink Cloud",
  "date": "04-28-2015",
  "author": "Tim Baumgartner",
  "attachments": [],
  "contentIsHTML": false
}}}

##Overview

The following Components are available add-ons when deploying a Cloudera blueprint on CenturyLink Cloud. Simply select the desired component and it will be fully configured and ready for use after the cluster builds.

###Accumulo

The Apache Accumulo™ sorted, distributed key/value store is a robust, scalable, high performance data storage and retrieval system. Apache Accumulo is an ideal solution for government agencies looking for a secure, distributed NoSQL data store to serve their most performance-intensive Big Data applications. Accumulo is an open source project integrated with CDH and provides the ability to store data in massive tables (billions of rows / millions of columns) for fast, random access. Accumulo was created and contributed to the Apache Software Foundation by the National Security Agency (NSA) and it has quickly gained adoption as a Hadoop-based key/value store for applications that require access to sensitive data sets.

[More Information on Accumulo](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/accumulo.html)

###HBase

Apache HBase is a distributed, scalable data store that runs on top of Apache Hadoop’s file system, the Hadoop Distributed File System (HDFS). HBase is a key component of an enterprise data hub (EDH), as its design caters to applications that require fast, random access to significant data sets. HBase, which is modeled after Google’s BigTable, can handle massive data tables containing billions of rows and millions of columns.

[More Information on HBase](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/hbase.html)

###Impala

Impala is a fully integrated, state-of-the-art analytic database architected specifically to leverage the flexibility and scalability strengths of Hadoop - combining the familiar SQL support and multi-user performance of a traditional analytic database with the rock-solid foundation of open source Apache Hadoop and the production-grade security and management extensions of Cloudera Enterprise.

[More Information on Impala](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/impala.html)

###Key-Value Store Indexer (Requires HBase and Solr)

The Key-Value Store Indexer service uses the Lily HBase NRT Indexer to index the stream of records being added to HBase tables. Indexing allows you to query data stored in HBase with the Solr service.

###Navigator

Cloudera Navigator is the only native end-to-end governance solution for Apache Hadoop-based systems. Through a single user interface, it provides visibility for administrators, data managers, data scientists, and analysts to secure, govern, and explore the large amounts of diverse data that land in Hadoop. Cloudera Navigator is part of Cloudera Enterprise’s comprehensive data security and governance offering and is a key part to meeting compliance and regulatory requirements.

[More Information on Navigator](http://www.cloudera.com/content/cloudera/en/products-and-services/cloudera-enterprise/cloudera-navigator.html)

###Sentry

A key part of compliance-ready security is controlling access to data. Apache Sentry (incubating) is a unified authorization mechanism so you can store sensitive data in Hadoop. Sentry is a fully integrated component of CDH and provides fine-grained authorization and role-based access control all through a single system. Sentry currently integrates with the open source SQL query frameworks, Apache Hive and Cloudera Impala, and the open source search engine, Cloudera Search, and can also extend to other computing engines within the Hadoop ecosystem. Sentry is a crucial part of compliance-ready security.

[More Information on Sentry](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/sentry.html)

###Solr

Solr is a standalone enterprise search server with a REST-like API. You put documents in it (called "indexing") via JSON, XML, CSV or binary over HTTP. You query it via HTTP GET and receive JSON, XML, CSV or binary results. Solr is highly reliable, scalable and fault tolerant, providing distributed indexing, replication and load-balanced querying, automated failover and recovery, centralized configuration and more. Solr powers the search and navigation features of many of the world's largest internet sites.

[More Information on Solr](http://lucene.apache.org/solr)

###Spark

Apache Spark is an open source, parallel data processing framework that complements Apache Hadoop to make it easy to develop fast, unified Big Data applications combining batch, streaming, and interactive analytics on all your data. For analysts and data scientists who rely on iterative algorithms (e.g. clustering/classification), Spark is 10-100x faster than MapReduce delivering faster time to insight on more data, resulting in better business decisions and user outcomes.

[More Information on Spark](http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/spark.html)
