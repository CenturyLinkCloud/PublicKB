{{{
"title": "Troubleshooting Tips",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Tips on Troubleshooting ElasticBox

Check the solutions to common issues before you contact ElasticBox support in the case of a problem.

**In this article**
* Instance unreachable during an operation
* Instance is stuck deploying
* Instance is still terminating
* Instance hangs at the install ElasticBox agent step
* Quick start box not installing properly
* ElasticBox appliance is unavailable

### Instance Unreachable During an Operation

**Reason**

When you trigger a lifecycle operation on an instance, it goes into a processing state because the agent is not running at all or not running properly. This problem can affect instances launched through the ElasticBox web interface, the API, or directly using the agent command.

**Solution**

Install the agent on the instance to bring it online. Then re-run the lifecycle operation.

1. Connect to the instance by SSH or RDP.

2. Install the agent. The command uses the token of the older agent to connect to the instance.
Linux instances deployed from the ElasticBox cloud service:

```
curl -ks ebx.co | sudo bash
```
Windows instances deployed from the ElasticBox cloud service (run the command as a PowerShell administrator):

```

(New-Object Net.WebClient).DownloadString("http://ebx.co") | iex

```

Linux instances deployed from the ElasticBox Appliance:

```
curl -ks 10.0.0.1 | sudo bash
```

Windows instances deployed from the ElasticBox Appliance (run the command as a PowerShell administrator):

```
(New-Object Net.WebClient).DownloadString("http://10.0.0.1") | iex

```

**Note:** Replace 10.0.0.1 with your appliance IP or hostname.

### Instance is Stuck Deploying

**Reason 1**

An instance can’t update its state because the ElasticBox agent can’t connect to ElasticBox. Poor agent network connectivity can cause this issue.

**Solution**

Restart the agent on the Linux or Windows instance:
Linux:

```
sudo /usr/elasticbox/elasticbox restart
```

Windows (run in command prompt):

```
net stop elasticbox
net start elasticbox
```

2. In ElasticBox, open the lifecycle editor of the instance and click **Reinstall**. The instance should reflect the proper status.

**Reason 2**

The Linux or Windows image on the instance doesn’t have cloud-init.

**Solution**

ElasticBox needs cloud-init for its agent to execute box script configuration on the VM image. Install cloud-init on the image and launch a new instance.

**Reason 3**

When box scripts exit with 100 typically because of apt-get failures, the ElasticBox agent goes into sleep mode waiting for the machine or service to reboot.

**Solution**

Place the apt-get exit code in the file executing it and to the last line of executable code, add this:

```
[[ "$?" -eq "100" ]] && exit 1
```

Restart the agent on the Linux or Windows instance.

### Instance is Still Terminating

**Reason**

Several concurrent terminate requests within seconds of each other can cause a race condition that keeps the instance in flux.

**Solution**

Force the instance to terminate. In the lifecycle editor of the instance, click Force Terminate.

### Instance Hangs at the Install ElasticBox Agent Step

**Reason**

Something causes the agent to hang even though it’s running on the instance.

**Solution**

1. Log in to the instance and kill the agent.

2. Redeploy the instance from the lifecycle editor in ElasticBox. The agent should start deploying.

### Quick Start Box Not Installing Properly

**Reason**

A broken puppet manifest or chef recipe can cause the box to not install properly.

**Solution**

[Contact support](mailto:support@elasticbox.com) to alert us of the broken box. In the meantime, you can define the install in a box using bash commands like apt-get, wget, cURL, and more.

### ElasticBox Appliance is Unavailable

**Reason**

When you configure the hostname, SSL certificate, or block device for the appliance, there’s a chance that the appliance may become unavailable. This issue can happen because you set the hostname incorrectly, upload a non-matching SSL certificate and key, or the block device gets corrupt, runs out of space or dismounts from the system. As a result, the appliance fails to reboot. Instance operations fail, and the appliance can’t reach deployed instances properly.

**Solution**

[Contact support](mailto:support@elasticbox.com). We will walk you through recovering the appliance. Send us the appliance version number shown at the top of the setup console. And send us the logs you can download from the Logs section of the appliance setup console.
Logs help us debug your appliance issues. The .log files include recent audit information like who did what, user connections, and contain the logs of all the services.
