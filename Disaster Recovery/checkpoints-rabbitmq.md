{{{
  "title": "SafeHaven Checkpoints and RabbitMQ",
  "date": "07-08-2016",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
SafeHaven uses RabbitMQ queues to validate and manage checkpoints. In certain complex configurations, or when setup errors have occurred, the queues will not be created correctly. This document walks through the steps to remediate queue creation failures.

### Detailed Steps
1. Identify a Protection Group with a missing RabbitMQ queue. This can be done via running the cluster diagnostics in the CMS (Help-> "Run Cluster Diagnostics"). The cluster diagnostics may report something like this:
   `IL1XXXSRN01 WARNING RabbitMQ checkpoint queue for IL1XXXPG01 target not active.`

   Another indication that there may not be a queue is if you have a Windows Protection Group that consistently does not generate clean checkpoints. If this is the case, check if there is a queue on the SRN.

2. To check if a RabbitMQ queue resides on the SRN, ssh into the Production SRN node. Issue the command `rabbitmqctl list_queues`. You should see an output similar to the following:

   ```
   root@IL1XXXSRN01:~# rabbitmqctl list_queues
   Listing queues ...
   0.0.0.0_main_thread     0
   iqn.2007-06.com.datagardens:IL1XXXPG01-PG-IL1XXXPG01-external_checkpoint 0
iqn.2007-06.com.datagardens:IL1XXXPG01-PG-IL1XXXPG01-external_monitoring 0
   ...done.
   ```

3. If you do not see the corresponding queue for the Protection Group, it is very simple to create it. First, log on to the Production VM via RDP.

4. Check to see if there is a certificate (cacert.pem) in the `C:\Program Files\SafeHaven-3.1 DRaaS Windows Replication Agent\tools\certs` folder. The date may indicate the source of the problem (i.e., cert exists from a previous protection group). Another indication may be the file size (a 0kb file).

5. Temporarily stop replication. Open up the "Tools" prompt under the SafeHaven DRaaS start menu folder. Check to see if the replication service is running by issuing the command `sc query dgrplctsvc`. Stop the replication service with the command `DgRplctSvc.exe -stop`.

6. The output should look similar to this:

   `C:\Program Files\SafeHaven-3.1 DRaaS Windows Replication Agent\tools>DgRplctSvc.exe -stop`

   `DgStopService: Stopping DgRplctSvc.`

   `DgStopService: DgRplctSvc is stopped.`

7. Open an Internet Browser and go to http://SRN.LOCAL.IP./certs.

8. Download the cacert.pem file to the `C:\Program Files\SafeHaven-3.1 DRaaS Windows Replication Agent\tools\certs` location.

9. Restart replication by issuing the command `DgRplctSvc.exe -start`. The output should look like this:

   `C:\Program Files\SafeHaven-3.1 DRaaS Windows Replication Agent\tools>DgRplctSvc.exe -start`

   `DgStartService: Start DgRplctSvc................................`

   `DgStartService: DgRplctSvc is running.`

10. Back on the Production SRN node, re-run the `rabbitmqctl list_queues` command. You should now see queues for the Protection Group corresponding to the Production VM that you just ran the process on.

11. Repeat as necessary.

If you do not feel comfortable with this process, or require additional assistance, please log a support request via email (help@ctl.io) or chat and the SafeHaven team will assist you.
