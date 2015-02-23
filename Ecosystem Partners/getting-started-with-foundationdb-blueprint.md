{{{
  "title": "Getting Started with FoundationDB - Blueprint",
  "date": "2-5-2014",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud.

### Partner Profile

<img src="foundationdb_images/Foundation-db-logo.png" style="border:0;float:right;">

FoundationDB – “A multi-model database for all of your needs.”

http://www.foundationdb.com

####Customer Support

centurylinkcloud-sales@foundationdb.com

CenturyLink Cloud Account Alias: FDB

### Description

FoundationDB has integrated their technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this FoundationDB solution.

FoundationDB's mission is to provide data storage technology that frees engineers and companies to focus on problems other than building their data stack. To that end, FoundationDB is creating a new generation of database technology that combines the advantages of modern NoSQL databases with the power and reliability of ACID transactions.

### Audience

CenturyLink Cloud Users

### Deploy in Two Flavors

<table>
  <tr>
    <th>
	  <h1><a style="color: #0f6bb4;" href="https://foundationdb.com/key-value-store"><img style="vertical-align: middle;" src="foundationdb_images/kv_store_icon.png" width="48" height="45">Key-Value Store</a></h1>
	</th>
    <th>
	  <h1 style="padding-left: 90px;"><img style="vertical-align: middle;" src="foundationdb_images/sql_layer_icon.png" width="48" height="44"><a style="color: #6bac4d;" href="https://foundationdb.com/layers/sql">SQL Layer</a></h1>
	</th>
  </tr>

  <tr>
    <td>
      <p>The Key-Value Store is a database that combines scalability, fault-tolerance, and high performance with incredibly powerful multi-key ACID transactions.</p>

      <p>This deploys on CenturyLink Cloud with the following configuration: FoundationDB key-value store version 3.0.4, deployed as a 3-node, 6-process cluster with the SSD storage engine and double redundancy.</p>
    </td>
    <td>
      <p>The SQL Layer is an ANSI SQL engine that stores its data in the Key-Value Store, inheriting its incredible properties. It is best suited for operational (OLTP) applications with high concurrency.</p>

      <p>This deploys on CenturyLink Cloud with the following configuration: FoundationDB 3.0.4 (3-node, 6-process cluster) with a single instance of the SQL Layer on a dedicated node.</p>
    </td>
  </tr>
</table>

### Steps

1. **Locate the Blueprint in the Blueprint Library**

  Click either of the items at right to access that Blueprint directly.

  [![](foundationdb_images/foundation-1.png)](https://control.tier3.com/blueprints/browser/details/2002) [![](foundationdb_images/foundation-2.png)](https://control.tier3.com/blueprints/browser/details/2089)

  Alternately, starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for “FoundationDB” in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**
3. **Set Required parameters.**

  Select "FD1" in the drop down if not pre-populated - this will be your master server.

4. **Set Optional Parameters**

  ![](foundationdb_images/foundation-3.png)

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment. Generally, it will take 15 to 20 minutes to configure all of the components.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.

8. **Validate Foundation DB Core Installation**

  ![](foundationdb_images/foundation-4.png)

  Login to your master server and execute the fdbcli tool.  If your display looks similar to the image at right your database is ready to use.

  ```
  [root@VA1KRAPFDB101 ~]# fdbcli
  Using cluster file `/etc/foundationdb/fdb.cluster'.
  
  The database is available.
  
  Welcome to the fdbcli. For help, type `help'.
  fdb> status
  
  Using cluster file `/etc/foundationdb/fdb.cluster'.
  
  Configuration:
    Redundancy mode        - double
    Storage engine         - ssd
    License                - See foundationdb.com/license
    Coordinators           - 1
  
  Cluster:
    FoundationDB processes - 6
    Machines               - 3
    Memory availability    - 4.5 GB per process on machine with least available
    Fault Tolerance        - 0 machines
    Server time            - Mon Feb 23 17:00:42 2015
  
  Data:
    Replication health     - Healthy
    Moving data            - 0.000 GB
    Sum of key-value sizes - 0 MB
    Disk space used        - 0 MB
  
  Operating space:
    Storage server         - 19.7 GB free on most full server
    Log server             - 19.7 GB free on most full server
  
  Workload:
    Read rate              - 10 Hz
    Write rate             - 1 Hz
    Transactions started   - 4 Hz
    Transactions committed - 1 Hz
    Conflict rate          - 0 Hz
  
  Client time: Mon Feb 23 17:00:42 2015
  ```

9. **Validate SQL Layer Installation (optional)**

  ![](foundationdb_images/foundation-5.png)

  Login to your SQL server and execute the 'fdbsqlcli' tool.  Execute the command `SELECT VERSION();` and verify a response similar to the image at right.

  ```
  [root@VA1KRAPSQL101 ~]# fdbsqlcli
  fdbsql (driver 2.0, layer 2.0.2)
  root=> SELECT VERSION();
           _SQL_COL_1
		   -----------------------------
		    FoundationDB 2.0.2 +1059266
			(1 row)

			root=>
  ```

10. **Getting started with FoundationDB - Key-Value Store**

  [![](foundationdb_images/kv_getting_started.png)](https://foundationdb.com/key-value-store/documentation/index.html)

  Click the link at right to get started with using the Foundation DB application.

11. **Getting started with FoundationDB - SQL Layer**

  [![](foundationdb_images/sql_getting_started.png)](https://foundationdb.com/layers/sql/documentation/index.html)

  Click the link at right to get started with using the Foundation DB application.

12. **Enable public access (optional)**

  Servers are built using private IPs only with access with client or IPSEC VPN.  For access from the Internet at large add a public IP to your master server.

  <a href="../Network/how-to-add-public-ip-to-virtual-machine/"><img src="foundationdb_images/fw_icon.png"></a>


### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

Get started with a paid Silver, Gold, and Platinum support plans are available from https://foundationdb.com/pricing.

Email: centurylinkcloud-sales@foundationdb.com

### Frequently Asked Questions

**Where do I obtain my FoundationDB license?**

Paid Silver, Gold, and Platinum support plans are available from https://foundationdb.com/pricing.

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../Support/how-do-i-report-a-support-issue.md).
* For issues related to deploying the FoundationDB Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact centurylinkcloud-sales@foundationdb.com or follow your existing FoundationDB support process if known.
* For issues related to deploying the FoundationDB Blueprints and application operation on CenturyLink Cloud and you do not have a paid license, [sign up for access to the support community](https://foundationdb.com/get).

**How do I learn more about the application?**

[![](foundationdb_images/kv_getting_started.png)](https://foundationdb.com/key-value-store/documentation/index.html)

[FoundationDB](https://foundationdb.com/key-value-store/documentation/index.html) has a massive store of [documentation](https://foundationdb.com/key-value-store/documentation/index.html) to help you get started and tutorials to make you successful.


