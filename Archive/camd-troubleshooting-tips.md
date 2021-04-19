{{{
"title": "Cloud Application Manager Dedicated Edition Troubleshooting Tips",
"date": "09-09-2019",
"author": "Guillermo Sanchez",
"attachments": [],
"keywords": ["cam","troubleshooting", "tips", "cloud application manager", "appliance", "data center edition", "dce", "dedicated", "cam-d"],
"contentIsHTML": false
}}}

### Tips on Troubleshooting Cloud Application Manager Dedicated Edition issues

Check the proposed solutions to common issues before you contact Cloud Application Manager support in the event of a problem.

**In this article**

* [Instance Unreachable During an Operation](#instance-unreachable-during-an-operation)
* [Instance is Stuck Deploying](#instance-is-stuck-deploying)
* [Instance is Still Terminating](#instance-is-still-terminating)
* [Instance Hangs at the Install Cloud Application Manager Agent Step](#instance-hangs-at-the-install-cloud-application-manager-agent-step)
* [Catalog Box deployment not working](#catalog-box-deployment-not-working)
* [Cloud Application Manager Appliance is Unavailable](#cloud-application-manager-appliance-is-unavailable)
* [Resource sharing problems](#resource-sharing-problems)
* [Instance fails to register in Cloud Application Manager](#instance-fails-to-register-in-cloud-application-manager)

### Instance Unreachable During an Operation

**Cause**

When you trigger a lifecycle operation on an instance, it goes into a processing state and does not finish. This can occur if the agent does not have direct connectivity to the Cloud Application Manager Dedicated Edition (CAM appliance), or if the agent has been stopped or else if it is not running properly. This problem can affect instances launched through the Cloud Application Manager web interface, the API, or directly using the agent command.

**Solution 1**

Make sure the communication from CAM Agent to CAM appliance works correctly.

1. Connect to the instance by SSH or RDP.

2. Run a command to check basic connectivity, such as the following or an equivalent one:

    ```
    telnet 10.0.0.1 443
    ```

    **Note:** Replace 10.0.0.1 with your appliance IP or hostname.

If the above command does not get a reply, please take the corrective actions inside the VM, routers and firewalls to allow unrestricted communication between agent and CAM appliance. Ensure that the port 443 is open in the CAM appliance for the CAM agent to connect back successfully.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Solution 2**

Check agent proxy settings (if configured to use one) at `/usr/elasticbox/elasticbox.conf` in linux or `ProgramFiles\ElasticBox\Agent\elasticbox.conf` in windows. If proxy is used for agent, make sure its working correctly and provide stable connectivity to CAM appliance.

**Solution 3**

Install the agent on the instance to bring it online. Then re-run the lifecycle operation.

1. Connect to the instance by SSH or RDP.

2. Install the agent. The command uses the token of the older agent to connect to the instance.

    Linux instances deployed from the Cloud Application Manager Appliance:

    ```
    curl -ks 10.0.0.1 | sudo bash
    ```

    **Note:** Replace 10.0.0.1 with your appliance IP or hostname.

    Windows instances deployed from the Cloud Application Manager Appliance (run the command as a PowerShell administrator):

    ```
    (New-Object Net.WebClient).DownloadString("http://10.0.0.1") | iex
    ```

If the problem persists connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected, please attach it when [Contacting support](mailto:incident@CenturyLink.com)

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

3. If problem persists, check connectivity between the Instance and the CAM appliance.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Solution 2**

Check agent proxy settings (if configured to use one) at `/usr/elasticbox/elasticbox.conf` in linux or `ProgramFiles\ElasticBox\Agent\elasticbox.conf` in windows. If proxy is used for agent, make sure its working correctly and provide stable connectivity to the CAM appliance.

**Solution 3**

Make sure the communication from CAM Agent to CAM appliance works correctly.

1. Connect to the instance by SSH or RDP.

2. Run a command to check basic connectivity, such as the following or an equivalent one:

    ```
    telnet 10.0.0.1 443
    ```

    **Note:** Replace 10.0.0.1 with your appliance IP or hostname.

If the above command does not get a reply, please:

1. Take the corrective actions inside the VM, routers and firewalls to allow unrestricted communication between agent and the CAM appliance. Ensure that the port 443 is open in the CAM appliance for the CAM agent to connect back successfully.

2. In Cloud Application Manager, open the lifecycle editor of the instance and click **Reinstall**. The instance should reflect the proper status.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)

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

If the problem persists connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected, please attach it when [Contacting support](mailto:incident@CenturyLink.com)

### Catalog Box deployment not working

**Cause 1**

The box requirements are not met by the deployment policy box.

**Solution**

Please check out the Box readme documentation and the box requirements and make sure your provider and deployment policy box meets the minimum requirements (OS type/version, cpu, RAM etc).

**Cause 2**

The Catalog public boxes are provided as templates for quickstart deploying commonly used software packages. We do our best effort to keep them up to date but from time to time, software updates, deprecated packages/modules/libraries or just plain broken installation scripts might break them or render them unusuable.

**Solution**

We encourage you to [Contact support](mailto:incident@CenturyLink.com) to alert us of the broken box. In the meantime, you can define the install in a box using bash commands like apt-get, wget, cURL, and more.

### Cloud Application Manager Appliance is Unavailable

**Cause**

When you configure the hostname, SSL certificate, or block device for the appliance, there’s a chance that the appliance may become unavailable. This issue can happen because you set the hostname incorrectly, upload a non-matching SSL certificate and key, or the block device gets corrupt, runs out of space or dismounts from the system. As a result, the appliance fails to reboot. Instance operations fail, and the appliance can’t reach deployed instances properly.

**Solution**

[Contact support](mailto:incident@CenturyLink.com). We will walk you through recovering the appliance. Send us the appliance ID, version number shown at the top of the [setup console](../Dedicated Edition/camd-initialsetup.md). And send us the logs you can download from the Logs section of the appliance setup console.

Logs help us debug your appliance issues. The `.log` files include recent audit information like who did what, user connections, and contain the logs of all the services. If possible, copy the logs from `/data/logs` away from the CAM Appliance and have them ready for the CAM support team.

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

### Instance fails to register in Cloud Application Manager

**Cause**

An instance registration (import) is waiting for the CAM agent to install, but the agent installation never seems to be completed.

**Solution 1**

Make sure the communication from the instance to be register to CAM appliance works correctly.

1. Connect to the instance by SSH or RDP.

2. Run a command to check basic connectivity, such as the following or an equivalent one:

    ```
    telnet 10.0.0.1 443
    ```

    **Note:** Replace 10.0.0.1 with your appliance IP or hostname.

If the above command does not get a reply, please:

1. Take the corrective actions inside the VM, routers and firewalls to allow unrestricted communication between the instance and the CAM appliance. Ensure that the port 443 is open in the CAM appliance for the CAM agent to connect back successfully.

2. In Cloud Application Manager, open the instance details page and click **Retry import** if available, or **Cancel import** and start the import process again. The instance should now finish the registration process successfully.

If the connectivity seems to be working as expected and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)

**Solution 2**

The CAM agent might be stopped and not able to complete the registration process due to the instance SSL stack not supporting TLS 1.2 at minimum. This might happen in old Windows machines using a .Net Framework version earlier than 4.5 (in the 4.5 version you have to opt-in to use it, while in versions 4.6 and above it is the default).

Check if ElasticBox logs (`C:\program files\elastic Box` in Windows) have something such as:

```
2019-09-05 17:45:07Z Exception setting "SecurityProtocol": "Cannot convert null to type "System.Net.SecurityProtocolType" due to invalid enumeration values. Specify one of the following enumeration values and try again. The possible enumeration values are "Ssl3, Tls"."
```

This message confirms that the TLS 1.2 protocol required is not supported by the environment executing the script. Upgrade the environment to a version that supports TLS 1.2 to address this issue (for example, for older Windows environments this might require to upgrade the .Net Framework version that the script uses).

If the TLS 1.2 support seems to be available in the instance and the problem persists, connect to the instance over SSH or RDP and grab a copy of the agent `/var/log/elasticbox/elasticbox-agent.log` in the case of Linux or `ProgramData\ElasticBox\elasticbox-agent.log` in the case of Windows (please note that the folder is hidden in Windows and the exact path must be entered to navigate to the folder). Once the log file is collected please attach it when [Contacting support](mailto:incident@CenturyLink.com)
