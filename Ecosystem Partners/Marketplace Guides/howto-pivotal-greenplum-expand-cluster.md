{{{
  "title": "How to Add Nodes and Expand an Existing Pivotal Greenplum Cluster - Blueprint",
  "date": "3-2-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the user should feel comfortable expanding an existing Pivotal Greenplum cluster deployed on CenturyLink Cloud.

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

CenturyLink Cloud Users who have already [deployed a Pivotal Greenplum cluster](../../Ecosystem Partners/Marketplace Guides/getting-started-with-pivotal-greenplum-blueprint.md) and need to add capacity.


### Expanding an Existing Cluster

Single button deploy of an additional node to an existing cluster.  These are architected for deployment on both on standard cloud servers and Hyperscale servers.  1TB data space and two segments are available on the new node.

#### Steps


1. **Identify your current cluster installation posture**

  Capture the following information about the cluster you wish to expand:

  * Server type - standard cloud server or Hyperscale
  * Server sizing - small or large (in terms of CPU/RAM)
  * Mirroring - whether mirroring is enabled on your existing cluster
  * Cluster ID - the identifier given when deploying your cluster

  For even performance your new node should match all existing nodes in terms of type and sizing.

2. **Locate the Blueprint in the Blueprint Library**

  Based on the information captured in (1) above select the appropriate Blueprint card to continue.  Note that clusters with mirroring enabled must have nodes deployed in pairs.

  <img src="/knowledge-base/images/pivotal_greenplum/node_blueprint_tiles.png" style="border:0;">

  Starting from the CenturyLink Control Panel, navigate to the Blueprints Library. Search for “Pivotal Greenplum” in the keyword search on the right side of the page.

3. **Click the Deploy Blueprint button.**

4. **Set Required parameters.**

  <img src="/knowledge-base/images/pivotal_greenplum/deploy_add_node_parameters.png" style="border:0;">

  * **EULA** - Click to accept the software end user license agreement
  * **Cluster ID ** - set unique identifier already used for this Greenplum cluster.  This is used to help other hosts find and join into the cluster
  * **Email Address** - Email address to receive build notification and Greenplum access information

5. **Set Optional Parameters**

  Password/Confirm Password (This is the root password for the server. Keep this in a secure place).

  Set DNS to “Manually Specify” and use “8.8.8.8” (or any other public DNS server of your choice).

  Optionally set the server name prefix.

  The default values are fine for every other option.

6. **Review and Confirm the Blueprint**

7. **Deploy the Blueprint**

  Once verified, click on the `deploy blueprint` button. You will see the deployment details stating the Blueprint is queued for execution.

  This will kick off the Blueprint deploy process and load a page where you can track the deployment progress. Deployment will typically complete within 15 to 20 minutes.

8. **Deployment Complete**

  Once the Blueprint has finished execution you will receive an email confirming the newly deployed assets.  If you do not receive an email like the one shown below your cluster may have had a deployment error - review the *Blueprint Build Log* to look for error messages.

  <img src="/knowledge-base/images/pivotal_greenplum/deploy_add_node_complete_email.png" style="border:0;width:70%;">


### Frequently Asked Questions

**Restarting cluster expansions**

From the master host execute the following commands to remove all CenturyLink specific items used to maintain state as part of a cluster deployment.  After removing these files another Blueprint deployment can be safely executed.

```
# rm -rf ~gpadmin/{.expand_in_process.lck,.expand_hostlist,add_node_*}
```

There may also be Greenplum specific commands that need to be executed to cleanup.  These will be indicated in the error log files.

**Error message "Unable to locate master"**

There are several scenarios where this error message may appear:

  * Your cluster ID does not match the ID used for the initial cluster deployment.  If you're unable to locate this ID you may obtain it manually by finding the `greenplum-master-$CLUSTER_ID` field in the file `/usr/local/bpbroker/etc/bpbroker.json`
  * The new node and existing cluster are on different networks.  Resolve this by deploying your new nodes on the same network
  * The `bpbroker` service may not be running on the master host.  Execute the following command on the master host to start this:
  ```
  # /sbin/service brbroker restart
  ```
