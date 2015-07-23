{{{
  "title": "Getting Started with Pivotal Greenplum - Blueprint",
  "date": "3-2-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying the Pivotal Greenplum database on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/pivotal_greenplum/pivotal_greenplum_logo.png" style="border:0;float:right;">

Pivotal Greenplum – “Best-in-class, enterprise-grade analytical data warehouse..”

http://pivotal.io/big-data/pivotal-greenplum-database

#####Customer Support

|Sales Contact      |
|:- |
|sales-clc@pivotal.io       |


### Description

Pivotal has integrated their Greenplum technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this Greenplum solution.

Greenplum incorporates key performance capabilities, flexible data analytics, enterprise grade robustness, seamless integration with analytics stacks and a database management framework focused on reducing total cost of ownership.


### Audience

CenturyLink Cloud Users

### Deployment Packages


|[Deploy a New Cluster](#deploying-a-new-cluster)   	|[Expand an Existing Cluster](howto-pivotal-greenplum-expand-cluster.md)   	|
|:-	|:-	|
|<p>Deploy a minimal cluster sized for testing.<p>When you're ready, deploy a production capable cluster using the same pattern.<p>See [Deploying a new cluster](#deploying-a-new-cluster) to get started.  If you're looking for a single-button deploy of clusters with more nodes see our guide on [Creating larger cluster Blueprints](howto-pivotal-greenplum-larger-clusters.md)   	|<p>Grow existing clusters to their optimal size from day zero or to accommodate growth over time.<p>We'll cleanly add capacity and leave any application disrupting work to you.<p>See [Expanding an existing cluster](howto-pivotal-greenplum-expand-cluster.md) to get started.   	|



### Deploying a New Cluster

You can achieve a single-button deployment of a new cluster including a master host, a standby master for failover, and two nodes, using CenturyLink Cloud Blueprints.  These are architected for deployment on both on standard cloud servers and Hyperscale servers.  1TB data space and two segments are available on each node.

#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Determine whether you will be building a test cluster with small nodes or a production cluster whose nodes are configured with increased CPU and RAM.

  <img src="/knowledge-base/images/pivotal_greenplum/cluster_blueprint_tiles.png" style="border:0;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for “Pivotal Greenplum” in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="/knowledge-base/images/pivotal_greenplum/deploy_cluster_parameters.png" style="max-width:450px;">

  * **EULA** - Click to accept the software end user license agreement
  * **Cluster ID ** - Set unique identifier for all hosts in this Greenplum cluster.  This is used to help other hosts find and join into the cluster
  * **Email Address** - Email address to receive build notification and Greenplum access information


4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  It is also used to identify the `gpadmin` user for Web Control Center access.

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within 15 to 20 minutes.

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <img src="/knowledge-base/images/pivotal_greenplum/deploy_cluster_complete_email.png" style="border:0;width:70%;">

8. **Web Command Center** (optional)

  If you elected to install the optional web command center you may access it via http on port 20800.  Authenticate using the `gpadmin` user and your administrative credentials

  <img src="/knowledge-base/images/pivotal_greenplum/web_command_center.png" style="border:0;">

8. **Demo Application** (optional)

  If you elected to install the optional demo application you may access the database from the master server.  Follow the [Pivot Greenplum demo lab](https://github.com/pivotalsoftware/pivotal-samples/tree/master/Labs) to quickly get up to speed on the Greenplum platform.  Authenticate using the `gpadmin` user and your administrative credentials

  ```
  [gpadmin@localhost ~]$ psql default
  psql (8.2.15)
  Type "help" for help.

  default=# \dt retail_demo.*
                          List of relations
     Schema    |          Name          | Type  |  Owner  |   Storage
  -------------+------------------------+-------+---------+-------------
   retail_demo | categories_dim         | table | gpadmin | append only
   retail_demo | customer_addresses_dim | table | gpadmin | append only
   retail_demo | customers_dim          | table | gpadmin | append only
   retail_demo | date_dim               | table | gpadmin | append only
   retail_demo | email_addresses_dim    | table | gpadmin | append only
   retail_demo | order_lineitems        | table | gpadmin | append only
   retail_demo | orders                 | table | gpadmin | append only
   retail_demo | payment_methods        | table | gpadmin | append only
   retail_demo | products_dim           | table | gpadmin | append only
  (9 rows)

  default=#
  ```

12. **Enable public access** (optional)

  Servers are built using private IPs only with access with client or IPSEC VPN.  For access from the Internet at large add a public IP to your master server.

  <a href="../../Network/how-to-add-public-ip-to-virtual-machine.md">
    <img style="border:0;width:50px;vertical-align:middle;" src="../../images/shared_assets/fw_icon.png">
    Adding a public IP to your virtual machine
  </a>



### Pricing

The costs listed above in the above steps are for the infrastructure only.

After deploying this Blueprint, you may secure entitlements to the technology using the following steps:

 * Email: sales-clc@pivotal.io

### Frequently Asked Questions

**Where do I obtain my license?**

Contact your Pivotal account manager or inquire via email to [centurylinkcloud-sales@pivotal.io](mailto:centurylinkcloud-sales@pivotal.io)

**Who should I contact for support?**

* For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
* For issues related to interacting with a Greenplum cluster review the [Pivotal KB](https://support.pivotal.io/hc/en-us/categories/200072608)
* For issues related to deploying the Pivotal Greenplum Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact sales-clc@pivotal.io or follow your existing Pivotal support process if known.


**How do I learn more about the application?**

View Pivotal's [Getting Started](http://gpdb.docs.pivotal.io/gpdb-434.html) guide and other documentation from the Pivotal documentation hub.

<img src="/knowledge-base/images/pivotal_greenplum/getting_started_pdf.png" style="max-height: 300px;margin-left:1em;">


**How do I login to my cluster for the first time?**

Access your new Pivotal Greenplum cluster via ssh as the root user whose password you supplied at create time.  

Best practices are to create non-administrative user access.  This can be done by creating another user or by configuring the gpadmin user for remote access.  This can be done by executing the following commands:

```
# chsh gpadmin bash
# passwd gpadmin
```
