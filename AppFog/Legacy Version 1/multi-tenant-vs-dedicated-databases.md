{{{
  "title": "AppFog University: Multi-tenant vs. Dedicated Databases",
  "date": "1-20-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>In Platform-as-a-Service environments, developers have the choice of multiple database options: SQL vs. "<a href="http://en.wikipedia.org/wiki/NoSQL">NoSQL</a>," in-house vs. third party, and multi-tenant vs. single-tenant, often referred to as dedicated. In this post, we'll explore the differences between multi-tenant databases and dedicated databases, focusing on the pros and cons of each and attempting to address when each one is the right choice dependent on workload.</p>
<p><strong>Multi-tenant databases</strong><br /> Multi-tenant databases are those in which multiple different user accounts share the same database resources and processing space. Almost every PaaS vendor has a multi-tenant DB option bundled with their service. Multi-tenant databases are a fine choice for general app testing (outside of performance tuning and capacity analsysis) and for very small applications with low database I/O needs.  Often included with the price of a PaaS, or very affordable, multi-tenant DBs solve the simple needs of simple and sometimes even more sophisticated applications.</p>
<p>However, several problems arise with multi-tenant DBs when used with mission-critical, high performance applications. The multi-tenant DB in these scenarios can quickly turn into the weakest link of an application. Here are a few reasons why:</p>
<ol>
<li><strong>Scalability:</strong> At the application level, PaaS systems handle scaling very well. After all, this is precisely what they were initially designed to do. On the database level, however, most PaaS aren't able to scale easily with user demand.<br /> </li>
<li><strong>Performance:</strong> By nature, multi-tenant databases offer don't offer the same performance guarantees for your application that you would receive from a dedicated DB. While strong PaaS systems work to mitigate this at the shared DB level, the "noisy neighbor effect" can still be a significant issue to contend with. Additionally, multi-tennancy can make accurate performance testing very difficult.<br /> </li>
<li><strong>Security: </strong>As all resources are shared, the potential of your application being on a data node that houses other customers is great. While the "real world" threats of this scenario are few and far between, the concept of a shared environment does not sit well with many enterprise customers.<br /> </li>
<li><strong>Availability: </strong>Setting up a replicated DB, or especially a geographically shared DB, is almost never an option with a shared database.<br /> </li>
<li><strong>Compliance: </strong>Many compliance requirements state that a dedicated DB space is a must. Again, it's not so much a material risk as a "fill in the checkbox" need, but in these cases, a shared DB won't suffice.</li>
</ol>
<p><strong>Dedicated Databases<br /> </strong>Luckily, lots of options exist for dedicated databases with PaaS solutions. Some are integrated and built by the provider from scratch, some are re-branded solutions such as Amazon RDS, while others still are in the form of partnerships with 3rd parties.<br /> <strong><br /> </strong>The great thing about dedicated databases is that they resolve all of the issues noted above. Scalability is improved with the flexiblilty for muliple configurations for replication, etc. Performance can be vastly improved and the developer does not have to worry about concurrent connetion limits, etc. as with shared DBs. Dedicated DBs will also inherently fill more security requirements as they isolate each user from the next and don't contain a shared space.<br /> <strong><br /> </strong>Several of the more popular DB providers in the Cloud have been listed below. Each are worth checking out! Please let us know (link) who we've missed as well.</p>
<ul>
<li><a href="http://aws.amazon.com/rds/"><strong>Amazon RDS</strong></a> - Offering MySQL, Oracle, and SQL Server, starting at 2.5 cents per hour</li>
<li><strong><a href="http://www.rackspace.com/cloud/public/databases/">Rackspace Cloud Databases</a></strong> - High-performance MySQL DB service</li>
<li><a href="http://xeround.com"><strong>Xeround</strong></a> - High-availability MySQL DBaaS</li>
<li><a href="https://mongolab.com/home"><strong>MongoLab</strong></a> - Mongo DB hosting, monitoring, support, replication, backups</li>
<li><strong><a href="https://www.mongohq.com/">MongoHQ</a></strong> - Mongo DB hosting on Amazon and Joyent infrastructure</li>
<li><a href="http://www.cleardb.com"><strong>ClearDB</strong></a> - Multi-master, replicated MySQL DBs on Amazon EC2 and Azure instances</li>
</ul>
<p>When developing your applications, the database component is often the most important part of the application. Planning, performance tuning, and optimization are all things you should spend a good amount of focus on.  Considering the shared vs. dedicated DB argument is an important part of your exploration and we hope this document has gotten you started.<br /> </p>
