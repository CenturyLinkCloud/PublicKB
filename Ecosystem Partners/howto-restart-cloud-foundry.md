# Restarting Cloud Foundry
    This KB assumes:
        - You have a fully functional Cloud Foundry (CF) stack.
        - Access via bosh cli to the BOSH Director.
        - Are running a fully redundant CF stack that can handle individual component restarts.

BOSH and Cloud Foundry have been designed for fault tolerance and to recover on their own.  However, there are rare occasions where a direct manual restart of one (or many) of the CF jobs can help to restore full health. The BOSH Health Monitor does health-checks, which are very basic and catch most issues.  BOSH continues to improve in this regard, but in the meantime the following commands and scripts can prove valuable when supporting a CF stack. 

First, ensure you are connected to the right deployment & BOSH Director:
```shell
# bosh status
Config
             /root/.bosh_config

Director
  Name       microbosh
  URL        https://10.155.75.20:25555
  Version    1.2719.1.0 (00000000)
  User       admin
  UUID       2cb86d7b-ba72-4383-b125-e185768a746a
  CPI        openstack
  dns        enabled (domain_name: microbosh)
  compiled_package_cache disabled
  snapshots  disabled

Deployment
  Manifest   /data1/cf.yml
```


Run a Cloud Check to ensure BOSH can't detect/fix the problem on its own.  This is the preferred method and should ALWAYS be tried first.
```shell
# bosh cck
Performing cloud check...

Processing deployment manifest
------------------------------

Director task 526
  Started scanning 18 vms
  Started scanning 18 vms > Checking VM states. Done (00:00:00)
  Started scanning 18 vms > 18 OK, 0 unresponsive, 0 missing, 0 unbound, 0 out of sync. Done (00:00:00)
     Done scanning 18 vms (00:00:00)

  Started scanning 4 persistent disks
  Started scanning 4 persistent disks > Looking for inactive disks. Done (00:00:00)
  Started scanning 4 persistent disks > 4 OK, 0 missing, 0 inactive, 0 mount-info mismatch. Done (00:00:00)
     Done scanning 4 persistent disks (00:00:00)

Task 526 done

Started         2015-04-02 14:44:33 UTC
Finished        2015-04-02 14:44:33 UTC
Duration        00:00:00

Scan is complete, checking if any problems found...
No problems found
```
If your environment STILL has issues and the Cloud Check shows perfect health... it's time to dig deeper.  It is always best to be targeted and take a surgical approach when troubleshooting.  Logging into each core CF server and viewing VCAP logs for errors is how one would accomplish this task.  Once a root cause component is found, one can restart that particular job if they think it could fix the problem.
First, view the servers in the environment:
```shell
# bosh vms
Deployment `cf'

Director task 527

Task 527 done

+-----------+---------+---------------+---------------+
| Job/index | State   | Resource Pool | IPs           |
+-----------+---------+---------------+---------------+
| api/0     | running | large         | 10.155.75.200 |
| api/1     | running | large         | 10.155.75.212 |
| api/2     | running | large         | 10.155.75.213 |
| core/0    | running | large         | 10.155.75.198 |
| core/1    | running | large         | 10.155.75.214 |
| core/2    | running | large         | 10.155.75.215 |
| haproxy/0 | running | large         | 10.155.75.35  |
| haproxy/1 | running | large         | 10.155.75.36  |
| runner/0  | running | xlarge        | 10.155.75.216 |
| runner/1  | running | xlarge        | 10.155.75.217 |
| runner/2  | running | xlarge        | 10.155.75.218 |
| runner/3  | running | xlarge        | 10.155.75.219 |
| runner/4  | running | xlarge        | 10.155.75.220 |
| runner/5  | running | xlarge        | 10.155.75.224 |
| runner/6  | running | xlarge        | 10.155.75.223 |
| runner/7  | running | xlarge        | 10.155.75.222 |
| runner/8  | running | xlarge        | 10.155.75.221 |
| runner/9  | running | xlarge        | 10.155.75.225 |
+-----------+---------+---------------+---------------+
```
Then, restart the suspected troublesome Job.  Let's pretend here we suspect our second API server:
```shell
# bosh restart api 1
```
For reference, the Job names you see above map to the following CF components in this example:
```shell
  - name: core
    templates:
      - name: nats
      - name: nats_stream_forwarder
      - name: etcd
      - name: etcd_metrics_server
      - name: hm9000
      - name: uaa
      - name: login

  - name: api
    templates:
      - name: gorouter
      - name: cloud_controller_ng
      - name: cloud_controller_clock
      - name: cloud_controller_worker
      - name: loggregator
      - name: loggregator_trafficcontroller

  - name: runner
    templates:
      - name: dea_next
      - name: dea_logging_agent
      - name: metron_agent
```
It takes time, however, for one to understand the stack well enough to be this precise... especially in a mass outage situation where time is of the essence.

In these situations the need to restore service sometimes overrules the surgical approach. A full stack restart can be a faster alternative with minimal risk, especially if people can't use the environment anyway.  A shell script like the following can be used (ensure your stack's data layer is listening and healthy before running this):
```shell
#!/bin/sh
echo yes | bosh restart core 0
echo yes | bosh restart core 1
echo yes | bosh restart core 2
echo yes | bosh restart api 0
echo yes | bosh restart api 1
echo yes | bosh restart api 2
echo yes | bosh restart haproxy 0
echo yes | bosh restart haproxy 1
echo yes | bosh restart runner 0
echo yes | bosh restart runner 1
echo yes | bosh restart runner 2
echo yes | bosh restart runner 3
echo yes | bosh restart runner 4
echo yes | bosh restart runner 4
echo yes | bosh restart runner 5
echo yes | bosh restart runner 6
echo yes | bosh restart runner 7
echo yes | bosh restart runner 8
echo yes | bosh restart runner 9
bosh vms
bosh cck
```
The order you see above does have some importance.  Your data, nats, & etcd services should be up and healthy first.  Next your router and cloud controller components... and finally, the dea nodes can be brought up.  If done one at a time, like seen here, user impact can be minimized.

If you run a CF environment that includes a data layer within the stack (vs. external), something like the following could be used.
```shell
#!/bin/sh
echo yes | bosh restart data
echo yes | bosh restart core 0
echo yes | bosh restart core 1
echo yes | bosh restart core 2
echo yes | bosh restart api 0
echo yes | bosh restart api 1
echo yes | bosh restart api 2
echo yes | bosh restart haproxy 0
echo yes | bosh restart haproxy 1
echo yes | bosh restart runner 0
echo yes | bosh restart runner 1
echo yes | bosh restart runner 2
echo yes | bosh restart runner 3
echo yes | bosh restart runner 4
echo yes | bosh restart runner 4
echo yes | bosh restart runner 5
echo yes | bosh restart runner 6
echo yes | bosh restart runner 7
echo yes | bosh restart runner 8
echo yes | bosh restart runner 9
bosh vms
bosh cck
```
