# AppFog Tips

Add Session Persistence to your AF deployed Java application
 - Automatically persists your session data to a redis service and will keep your session alive in the event any of the underlying PaaS DEA servers experience failure or individual Java instances crash.
```
This Tip assumes:
- Redis is a consumable service in your AppFog environment's marketplace.
- You are using the Java Buildpack.
```
```shell
# cf create-service p-redis shared-vm session-replication
Creating service session-replication in org AF / space Dev as user...
OK

# cf bind-service apptest session-replication
Binding service session-replication to app apptest in org AF / space Dev as user...
OK
TIP: Use 'cf restage' to ensure your env variable changes take effect

# cf restage apptest
-----> Downloading Tomcat Redis Store 1.2.0_RELEASE from https://download.run.pivotal.io/redis-store/redis-store-1.2.0_RELEASE.jar (found in cache)
         Adding Redis-based Session Replication

# cf services
Getting services in org AF / space Dev as user...
OK

name                   service         plan           bound apps       last operation
session-replication    p-redis         shared-vm      apptest          succeeded
```
