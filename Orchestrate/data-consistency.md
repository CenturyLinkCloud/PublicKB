{{{
  "title": "Data Consistency",
  "date": "4-20-2015",
  "author": "Adam DuVander",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

The Orchestrate service is a multi-tenant query platform comprised of a number of different pieces of database technology. These databases have different consistency characteristics. You can find the full list of database technology we use [online](http://orchestrate.uservoice.com/knowledgebase/articles/354377-what-software-and-services-underpin-orchestrate), although this list may change in the future.

The Orchestrate service expresses consistency semantics which are an aggregate of the individual components.  Different API endpoints have different consistency semantics, which should be understood in order to build correct and predictable applications.

If you have questions about any of the information on the consistency semantics described on this page you can always reach us in the [Orchestrate Community chatroom](http://oio-community.useast.appfog.ctl.io) or contact us [via email](mailto:hello@orchestrate.io).

### Consistency Semantics

There are several different categories of consistency many of which involve discussions on the [CAP theorem](http://en.wikipedia.org/wiki/CAP_theorem). Still, you can divide Orchestrate's consistency semantics into two categories: "strongly consistent" and "eventually consistent".

As application developers, Strong Consistency is what we’re used to with relational databases. It means that we can be sure about the [read-your-write](http://www.dbms2.com/2010/05/01/ryw-read-your-writes-consistency/) (RYW) guarantee from a database. Distributed environments (Orchestrate is distributed and fault-tolerant) guarantee all replicas of your data update linearly in the same total order.

In the Orchestrate service all Key-Value (including list operations), Event and Graph queries are strongly consistent in the datastores. When you write data into the platform with these parts of the API you can expect to read the latest changes back on the next request.

Eventual consistency is a property of databases which are more "loosely connected". There's no synchronization phase on the read or write operation. In distributed environments replicas are updated asynchronously and may not converge to the same total order, while they will eventually converge on the same final value. The advantage of looser coupling is that the failure of one or more components is less likely to result in a system-wide outage.

You may wonder when a delay between the writing of data, and the ability to query it is tolerable. Yet this is a common property in search technology; including all Lucene-based search databases.

In the Orchestrate service all Search and Geospatial queries are eventually consistent in the datastores. When you write data to Orchestrate it is delivered asynchronously to the databases which index the information for use with search and geo queries.

### Working with Search and Geo

The best way to think about the search and geo portion of the API is that they operate asynchronously on the data you store into Orchestrate. They are systems used to generate additional representations from the data your store. These specialist indexes allow the Orchestrate service to provide much richer query functionality than would otherwise be possible.

The consequence of these asynchronous systems is that, for example, if you store 1500 key-value documents within a second it will take a few hundred milliseconds (or slightly longer) for the data to be available in search and geospatial queries. This is something you must be aware of when writing end-to-end or integration tests for your application.

There is no easy way to write test cases to verify an asynchronous system. A simple solution is to introduce a small artificial sleep period when data is stored during test cases to give the asynchronous task time to complete. This is an error prone approach but may serve the purpose.

Another approach is to bootstrap the dataset for your test cases before you run your tests although this may not always be possible.  In general, test cases whose success rely on a deterministic end state should use strongly consistent APIs to determine whether or not that state has been reached.

### Concurrency Control

In most application environments there are numerous server components querying multiple databases. The Orchestrate service removes the need to run this "query infrastructure". It consolidates queries that would require multiple databases under one API.

With Orchestrate at the heart of an application environment it's important to maximize concurrency when making API requests. In many cases, there'll be more than one instance of an application making the same kind of request. In these cases you could encounter the "lost update" problem which happens when multiple people edit a resource without knowledge of each others' changes. In this scenario, the last person to update a resource "wins", and previous updates are lost.

Fortunately, the HTTP protocol (and by design the Orchestrate API) has headers which enable an "optimistic concurrency control" mechanism. In optimistic concurrency control, requests do not lock data when they query it. When a request updates data, the system checks to see if another request changed the data after it was read. If another request updated the data, an error is raised. Typically, the client receiving the error rolls back the operation and starts over.

Every JSON document stored to the Orchestrate API is given a "ref". This is a unique identifier for the version of the document for a given key. The values associated with a particular "ref" are immutable, they are guaranteed not to change. This ref can be supplied with requests to the service. It's a mechanism for the request to indicate it "saw" a specific version of the document before making the modification attempt. In this way you can leverage optimistic concurrency controls to ensure that data is always updated in a consistent order.

As a best practice, use conditional updates and deletes to take advantage of our concurrency control feature.

If you need any help, or have any questions you can always reach us in the [Orchestrate Community chat room](http://oio-community.useast.appfog.ctl.io).
