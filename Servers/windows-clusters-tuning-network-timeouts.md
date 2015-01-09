{{{
  "title": "Windows Clusters Tuning Network Timeouts",
  "date": "12-4-2014",
  "author": "Thomas Duffy",
  "attachments": []
}}}

<p>Since Windows 2008, Windows Server Failover Clustering has experienced premature fail overs when left with a default configuration.&nbsp;By default Microsoft configures the cluster for the most aggressive recovery situation. This needs to be changed within
  a virtualized environment.&nbsp;Most commonly a fail over will occur when a VMware snapshot is occurring on one or more of the servers involved in the cluster. To help alleviate this problem there are some configuration changes that need to be made
  to the cluster once it has been installed and configured. There are 4 main configuration changes that can be made.</p>
<p>If the servers within the cluster are all running on the same subnet you will want to change 2 different settings. The first will be the SameSubnetDelay. This is the frequency, in seconds, at which heartbeats are sent between cluster nodes. The second
  will be the SameSubnetThreshold. This is the number of heartbeats that can be missed before one of the nodes decides it is time to take action to ensure clustered services remain active. It is recommended to change the SameSubnetDelay from the default
  value of 1 second to the maximum of 2 seconds. Also recommended is to change the SameSubnetThreshold from the default of 5 heartbeats to 10 heartbeats. This can be set to a maximum of 120 heartbeats. These settings will configure the cluster to allow
  20 seconds of missed communication before a node tries to take over the services.</p>
<p>If the servers within the cluster are running on a different subnet you will want to change 2 different settings. The first will be the CrossSubnetDelay. This is the frequency, in seconds, at which heartbeats are sent between cluster nodes. The second
  will be the CrossSubnetThreshold. This is the number of heartbeats that can be missed before one of the nodes decides it is time to take action to ensure clustered services remain active. It is recommended to change the CrossSubnetDelay from the default
  value of 1 second to 2 seconds. This can be set to a maximum of 4 seconds. Also recommended is to change the CrossSubnetThreshold from the default of 5 heartbeats to 20 heartbeats. This can be set to a maximum of 120 heartbeats. These settings will
  configure the cluster to allow 40 seconds of missed communication before a node tries to take over the services.</p>
<p>All 4 of these settings can be made to a cluster if some servers are on the same subnet and other servers are on a different subnet.</p>

<p>For additional information on the subject, please refer to the following blog post.</p>
<p>http://blogs.msdn.com/b/clustering/archive/2012/11/21/10370765.aspx</p>