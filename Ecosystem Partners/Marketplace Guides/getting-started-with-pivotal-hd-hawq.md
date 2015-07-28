{{{
  "title": "Getting Started with Pivotal HD + HAWQ - Blueprint",
  "date": "5-27-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the reader should feel comfortable deploying the Pivotal HD and HAWQyGemFire in-memory database on CenturyLink Cloud.

### Partner Profile

<img src="/knowledge-base/images/pivotal_hdhawq/product-pivotal-hd.png" style="border:0;float:right;max-width: 150px;">

Pivotal HD + HAWQ – “World’s Most Advanced Enterprise SQL on Hadoop Analytic Engine on the Leading Standards-Based Hadoop Distribution For Advanced Analytics”

http://pivotal.io/big-data/pivotal-hawq

#####Customer Support

|Sales Contact   	|
|:-	|
|sales-clc@pivotal.io   	|


### Description

Pivotal has integrated their HD and HAWQ technology with the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this HD+HAWQ solution.

Pivotal HD is an enterprise-ready Hadoop distribution, optimized for analytics, providing the core Apache Hadoop features and Hadoop-related project features augmented by Pivotal’s value-added extensions and analytics support.

Pivotal HAWQ natively supports various Hadoop file formats. Reduces extract, transform and load (ETL) processing and data movement, and directly contributes to lower cost of ownership of the data analytics solution. Pivotal HAWQ data federation capabilities are the most advanced in the industry. They enable enterprises to implement end-to-end data analytics initiatives, without having to execute major data transformation projects as a prerequisite.


### Audience

CenturyLink Cloud Users


### Deploying a New Cluster

You can achieve a single-button deployment of a new cluster, including an Ambari server and a collection of service nodes, using CenturyLink Cloud Blueprints.  These are architected for deployment on both on standard cloud servers and Hyperscale servers with 1TB of usable data space on each node.

#### Steps


1. **Locate the Blueprint in the Blueprint Library**

  Determine whether you will be building a test cluster with small nodes or a production cluster whose nodes are configured with increased CPU and RAM.

  <img src="/knowledge-base/images/pivotal_hdhawq/cluster_blueprint_tiles.png" style="border:0;max-width:250px;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for "Pivotal HAWQ" in the keyword search on the right side of the page.

2. **Click the Deploy Blueprint button.**

3. **Set Required parameters.**

  <img src="/knowledge-base/images/pivotal_hdhawq/deploy_cluster_parameters.png" style="max-width:450px;">

  * **EULA** - Click to accept the software end user license agreement
  * **Cluster ID ** - Set unique identifier for all hosts in this Greenplum cluster.  This is used to help other hosts find and join into the cluster
  * **Email Address** - Email address to receive build notification and HD+HAWQ access information
  * **Configure Cluster** - We can automatically configure your cluster distributing common services across your node, or choose **No** to leave all cluster configuration up to you.
  * **Install Demo** - Install a demo dataset to experience PHD HAWQ without any setup


4. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).  

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

5. **Review and Confirm the Blueprint**

6. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within 50 to 75 minutes.  Take note that the Blueprint status may indicate deployment has completed but there will be a several minute delay until the cluster itself is ready for use as some backup install tasks may still be in process.

  <img src="/knowledge-base/images/pivotal_hdhawq/ambari_install_progress.png" style="width:70%;">

7. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* to for error messages.

  <img src="/knowledge-base/images/pivotal_hdhawq/deploy_cluster_complete_email.png" style="border:0;width:70%;">

8. **Ambari Dashboard**

  Access the Ambari dashboard via port 8080 on your Ambari server.  Authenticate using the default credentials admin/admin.

  <img src="/knowledge-base/images/pivotal_hdhawq/ambari_dashboard.png" style="border:0;">

8. **Demo Application** (optional)

  If you elected to install the optional demo application you may access the Chicago Crime Database from one of the HAWQ nodes - look for an email once the install is completed for personalized access details to get started immediately.

  Execute these as the `gpadmin` user which already has permissions to the HAWQ datasource:

  ```
  > ssh root@hawq_server

  > su -l gpadmin
  > psql
  ```

  Example queries:

  ```
  -- Crime frequency by hour of day
  SELECT EXTRACT('hour' FROM crime_date) hour_of_day, count(*)
  FROM crimes
  GROUP BY 1
  ORDER BY 2 DESC LIMIT 3;

  -- (Requires https://github.com/mgoddard-pivotal/pg_geohash)
  -- Get a list of areas by crime prevalence, where the precision of the geohash
  -- is truncated to 6 characters to provide for wider "bins".
  SELECT SUBSTRING(LAT_LON_TO_GEOHASH(latitude, longitude) FROM 1 for 5) geohash, COUNT(*)
  FROM crimes
  GROUP BY 1
  ORDER BY 2 DESC
  LIMIT 20;

  -- Similar to above, but showing the (lat, lon) value of the center of each "grid"
  SELECT GEOHASH_TO_LAT_LON(SUBSTRING(LAT_LON_TO_GEOHASH(latitude, longitude) FROM 1 FOR 5)::text) "(lat, lon)", COUNT(*)
  FROM crimes
  WHERE latitude IS NOT NULL AND longitude IS NOT NULL
  GROUP BY 1
  ORDER BY 2 DESC
  LIMIT 100;

  -- This shows the inverse of LAT_LON_TO_GEOHASH function
  SELECT location, GEOHASH_TO_LAT_LON(LAT_LON_TO_GEOHASH(latitude, longitude))
  FROM crimes
  LIMIT 20;

  -- UDF needed in the view (next part)
  CREATE OR REPLACE FUNCTION url_escape (url text)
    RETURNS text
  AS $$
  import urllib
  if url == None:
    return url
  return urllib.quote(url)
  $$ LANGUAGE plpythonu;

  -- Create a VIEW on the crimes table, adding a wrapper to format
  -- the LOCATION column as a link to Google (for viewing on Google Maps)
  DROP VIEW IF EXISTS crimes_view;
  CREATE VIEW crimes_view AS
  SELECT
    case_number
    , crime_date
    , block
    , primary_type
    , description
    , location_desc
    , beat
    , district
    , ward
    , 'https://www.google.com/#q=' || url_escape(location) map_link
  FROM crimes
  WHERE location IS NOT NULL;

  -- Try the regular expression operator, ~* (case insensitive)
  SELECT * FROM crimes_view
  WHERE block ~* 'Wabash'
  ORDER BY crime_date DESC, primary_type DESC
  LIMIT 250;
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
* For issues related to interacting with an HD + HAWQ cluster review the [Pivotal KB](https://support.pivotal.io/hc/en-us/categories/200072578-Pivotal-HD-Knowledge-Base)
* For issues related to deploying the Pivotal HD + HAWQ Blueprints and application operation on CenturyLink Cloud and you have a paid license, please contact sales-clc@pivotal.io or follow your existing Pivotal support process if known.


**How do I login to my cluster for the first time?**

Access your new Pivotal HD+HAWQ cluster via ssh as the root user whose password you supplied at create time.  

You may access the Ambari dashboard using the default credentials of admin/admin.


**What applications are contained in the default installation?**

The 10-node cluster configuration is available via pre-configured Ambari Blueprints.  


[10-node Blueprint](https://github.com/dbbaskette/phd3-hawq-aws/blob/master/10-node-blueprint.json):

|Name | Cardinality  | Components  |
|:-:|---|:-:|
| Gateway | 1  | Ambari, Nagios, Zookeeper, Oozie.  (This is the Ambari server)  |
| Master 1 | 1  | Namenode, PXF, Zookeeper, Ganglia Server, HDFS, YARN  |
| Master 2 | 1  | Secondary Namenode, PXF, HAWQ Master, Zookeeper, History Server, HDFS, YARN, Ganglia  |
| Master 3 | 1  | Resource Manager, APP Timeline Server, HAWQ Standby, Zookeeper, Ganglia  |
| Master 4 | 1  | Zookeeper Server, Hive Server, Hive Metastore, Mysql Server, HCAT, Ganglia  |
| Slave | 5  | Node Manager, Data node, PXF, HAWQ, Ganglia |
