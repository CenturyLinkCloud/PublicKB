{{{
  "title": "How to Create a Custom Sized Pivotal Greenplum Cluster Blueprint",
  "date": "3-2-2015",
  "author": "<a href='https://twitter.com/KeithResar'>@KeithResar</a>",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the user should feel comfortable creating a new Blueprint to support Pivotal Greenplum clusters of arbitrary size on CenturyLink Cloud.

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

CenturyLink Cloud Users who will need to repeatedly deploy a Pivotal Greenplum cluster larger than that described in the [deploying a Pivotal Greenplum cluster](getting-started-with-pivotal-greenplum-blueprint.md) document.  If this will be a one time build then adding additional nodes using the expansion Blueprint may be easier.


### Creating a custom Blueprint

Single button deploy of an arbitrary sized Pivotal Greenplum cluster.

#### Steps

1. **Review creating a new Blueprint** referencing the [How to build a blueprint KB](../../Blueprints/how-to-build-a-blueprint.md) if necessary

  * (Wizard step 1) Complete as normal
  * (Wizard step 2) Do not add any servers in this step

2. **(Wizard step 3) Add new cluster Blueprint**

  Add a single new cluster to the Blueprint and any number of additional nodes.  Take note that if deploying your cluster in a mirrored configuration then an even number of nodes must be added.

  <img src="/knowledge-base/images/pivotal_greenplum/customize_blueprint.png" style="">

3. **Save Blueprint**
