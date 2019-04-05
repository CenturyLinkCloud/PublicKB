{{{
"title": "Troubleshooting Tips",
"date": "04-01-2019",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Tips on Troubleshooting Cloud Application Manager

Check the proposed solutions to common issues before you contact Cloud Application Manager support in the event of a problem.

**In this article**
* Instance unreachable during an operation
* Instance is stuck deploying
* Instance is still terminating
* Instance hangs at the install Cloud Application Manager agent step
* Quick start box not installing properly
* Cloud Application Manager appliance is unavailable

### Instance Unreachable During an Operation

**Cause**

When you trigger a lifecycle operation on an instance, it goes into a processing state because the agent is not running at all, not running properly or can't communicate with CAM servers. This problem can affect instances launched through the Cloud Application Manager web interface, the API, or directly using the agent command.

**Solution 1**

Install the agent on the instance to bring it online. Then re-run the lifecycle operation.

1. Connect to the instance by SSH or RDP.

2. Install the agent. The command uses the token of the older agent to connect to the instance.
Linux instances deployed from the Cloud Application Manager cloud service:

```
curl -sSL https://cam.ctl.io | sudo bash
```
Windows instances deployed from the Cloud Application Manager cloud service (run the command as a PowerShell administrator):

```
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
(New-Object Net.WebClient).DownloadString("https://cam.ctl.io") | iex

```

Linux instances deployed from the Cloud Application Manager Appliance:

```
curl -ks 10.0.0.1 | sudo bash
**Note:** Replace 10.0.0.1 with your appliance IP or hostname.
```

Windows instances deployed from the Cloud Application Manager Appliance (run the command as a PowerShell administrator):

```
(New-Object Net.WebClient).DownloadString("http://10.0.0.1") | iex

```

If the problem persists connect to the instance over SSH or RDP and grab a copy of the agent /var/log/elasticbox/elasticbox-agent.log in the case of Linux or ProgramData\ElasticBox\elasticbox-agent.log in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Solution 2**

Check agent proxy settings (if configured to use one) at /usr/elasticbox/elasticbox.conf in linux or ProgramFiles\ElasticBox\Agent\elasticbox.conf in windows. If proxy is used for agent, make sure its working correctly and provide stable connectivity to CAM/Appliance servers.

**Solution 3**

Make sure the communication from CAM Agent to CAM servers works correctly.

1. Connect to the instance by SSH or RDP.

2. Run a ping command to check basic connectivity:

If using Cloud Application Manager:
```
ping -c3 cam.ctl.io
```

If using Cloud Application Manager Appliance:
```
ping -c3 10.0.0.1
**Note:** Replace 10.0.0.1 with your appliance IP or hostname.
```

If the above command does not get a reply, please take the corrective actions inside the VM, routers and firewalls to allow unrestricted communication between agent and CAM servers or CAM appliance.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent /var/log/elasticbox/elasticbox-agent.log in the case of Linux or ProgramData\ElasticBox\elasticbox-agent.log in the case of Windows (please not that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please and attach it when [Contacting support](mailto:incident@CenturyLink.com)


### Instance is Stuck Deploying

**Cause 1**

An instance can’t update its state because the Cloud Application Manager agent can’t connect to Cloud Application Manager. Poor agent network connectivity can cause this issue.

**Solution 1**

1. Restart the agent on the Linux or Windows instance:

   Linux:

   ```
   sudo /usr/elasticbox/elasticbox restart
   ```

   Windows (run in command prompt):

   ```
   net stop elasticbox
   net start elasticbox
   ```

2. In Cloud Application Manager, open the lifecycle editor of the instance and click **Reinstall**. The instance should reflect the proper status.

3. If problem persists, check connectivity between the Instance and CAM Servers/Appliance.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent /var/log/elasticbox/elasticbox-agent.log in the case of Linux or ProgramData\ElasticBox\elasticbox-agent.log in the case of Windows (please not that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please and attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Solution 2**

Check agent proxy settings (if configured to use one) at /usr/elasticbox/elasticbox.conf in linux or ProgramFiles\ElasticBox\Agent\elasticbox.conf in windows. If proxy is used for agent, make sure its working correctly and provide stable connectivity to CAM/Appliance servers.

**Solution 3**

Make sure the communication from CAM Agent to CAM servers works correctly.

1. Connect to the instance by SSH or RDP.

2. Run a ping command to check basic connectivity:

If using Cloud Application Manager:
```
ping -c3 cam.ctl.io
```

If using Cloud Application Manager Appliance:
```
ping -c3 10.0.0.1
**Note:** Replace 10.0.0.1 with your appliance IP or hostname.
```

If the above command does not get a reply, please take the corrective actions inside the VM, routers and firewalls to allow unrestricted communication between agent and CAM servers or CAM appliance.

3. In Cloud Application Manager, open the lifecycle editor of the instance and click **Reinstall**. The instance should reflect the proper status.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent /var/log/elasticbox/elasticbox-agent.log in the case of Linux or ProgramData\ElasticBox\elasticbox-agent.log in the case of Windows (please not that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please and attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Cause 2**

When a box script terminates with 100 exit code, typically because of apt-get failures, the Cloud Application Manager agent goes into sleep mode waiting for the machine or service to reboot.

**Solution**

1. Open the instance page in CAM to review the deployment logs
2. Identify which script is exiting with code 100.
3. Open lifecycle editor
4. Edit the previously identified and add the following line just after the command that exited with 100.

   ```
   [[ "$?" -eq "100" ]] && exit 1
   ```
5. Connect to Instance over SSH or RDP
6. Restart the agent.

   Linux:

   ```
   sudo /usr/elasticbox/elasticbox restart
   ```

   Windows (run in command prompt):

   ```
   net stop elasticbox
   net start elasticbox
   ```

* Restart the agent on the Linux or Windows instance.

### Instance is Still Terminating

**Cause**

Several concurrent terminate requests within seconds of each other can cause a race condition and keep the instance in running state.

**Solution**

From CAM instance page, Force the instance to terminate, or alternatively, in the lifecycle editor of the instance, click Force Terminate.

### Instance Hangs at the Install Cloud Application Manager Agent Step

**Cause**

Something causes the agent to hang even though it’s running on the instance.

**Solution**

1. Log in to the instance and kill the agent.

2. Redeploy the instance from the lifecycle editor in Cloud Application Manager. The agent should start deploying.

3. If problem persists connect to the instance over SSH or RDP and grab a copy of the agent /var/log/elasticbox/elasticbox-agent.log in the case of Linux or ProgramData\ElasticBox\elasticbox-agent.log in the case of Windows (please not that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please and attach it when [Contacting support](mailto:incident@CenturyLink.com)

### Catalog Box deployment not working

**Cause 1**

The box requirements are not met by the deployment policy box.

**Solution**

Please check out the Box readme documentation and the box requirements and make sure your provider and deployment policy box meets the minimum requirements (OS type/version, cpu, RAM etc).

**Cause 2**

The Catalog public boxes are provided as templates for quickstart deploying commonly used software packages. We do our best effort to keep them up to date but from time to time, software updates, deprecated packages/modules/libraries or just plain broken installation scripts might break them or render them unusuable.

**Solution**

We encourage you to contact [Contact support](mailto:incident@CenturyLink.com) to alert us of the broken box. In the meantime, you can define the install in a box using bash commands like apt-get, wget, cURL, and more.

### Cloud Application Manager Appliance is Unavailable

**Cause**

When you configure the hostname, SSL certificate, or block device for the appliance, there’s a chance that the appliance may become unavailable. This issue can happen because you set the hostname incorrectly, upload a non-matching SSL certificate and key, or the block device gets corrupt, runs out of space or dismounts from the system. As a result, the appliance fails to reboot. Instance operations fail, and the appliance can’t reach deployed instances properly.

**Solution**

[Contact support](mailto:incident@CenturyLink.com). We will walk you through recovering the appliance. Send us the appliance ID, version number shown at the top of the [setup console](../Appliance/appliance-initialsetup.md). And send us the logs you can download from the Logs section of the appliance setup console.

Logs help us debug your appliance issues. The .log files include recent audit information like who did what, user connections, and contain the logs of all the services. If possible, copy the logs from /data/logs away from the Appliance and have them ready for the CAM support team.

### Resource sharing problems

When trying to share a resource (Provider, Box, Instance) the desired user or team can't be found in the users list or the ownership of the resource cant be transfered to another user/team.

**Cause 1**

Resources can only be shared with other users or teams that belong to the same organization or have their organizations federated.

**Solution**

Make sure the resource owner and the desired user to share it with belong to the same organization or request the organization administrator to request the federation with the other organization though [Support](mailto:incident@CenturyLink.com).

**Cause 2**

Providers and Deployment policy boxes can only be shared with other users or teams that belong to the same cost center. Each user/team have an assigned costcenter that cannot be changed.

**Solution 1**

Make sure the resource owner and the desired user to share it with belong to the same costcenter. or request the organization administrator to request the federation with the other organization though [Support](mailto:incident@CenturyLink.com).

**Solution 2**

An organization administrator can edit the Costcenter and add any user in the organization (or federeated organizations) as a Costcenter administrator. Once the user is a costcenter administrator, any resource owned by any other user/team of the same costcenter could be shared with this user.

**Cause 3**

Providers and Deployment policy boxes ownership can only be transfered to other users or teams that belong to the same cost center. Each user/team have an assigned costcenter that cannot be changed.

**Solution**

Make sure the resource owner and the desired user to transfer ownership to belong to the same costcenter.
