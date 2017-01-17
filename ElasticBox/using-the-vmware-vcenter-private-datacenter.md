{{{ "title": "Using the VMware vCenter Private Datacenter",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}


### Using the VMware vCenter Private Datacenter

**In this article:**

* Prerequisites
* Registering your vCenter in ElasticBox
* Deploying in your vCenter

### Prerequisites

* vCenter server is version 5.0 or later.
* vCenter has at least one Windows or Linux template to connect your account successfully in ElasticBox.
* vCenter templates are bootstrapped with the ElasticBox agent.
* If your vCenter datacenter is behind a firewall, open the following ports to allow ElasticBox users, the ElasticBox agent, and instances to communicate with each other.
	* Ports 443: Allows users behind a firewall to access ElasticBox and allow the vCenter VMs to talk to ElasticBox.
	* Port 8085: Allows ElasticBox to communicates over this port with vCenter, sync with vCenter configuration, and run instance operations on virtual machines.

### Minimum User Permissions

A vCenter user needs minimum rights to be able to authenticate, deploy and manage instances through ElasticBox. Although these are for vCenter 5.5, similar permissions apply for earlier versions.

| Assign access for | With privileges |
|-------------------|-----------------|
| Datastore | <li>Allocate space</li><li>Browse datastore</li> |
| Global |	Cancel task |
| Manage custom attributes | Set custom attribute |
| Network |	Assign network |
| Resource | Assign virtual machine to resource pool |
| Scheduled task | <li>Create tasks</li><li>Run task</li> |
| Tasks | <li>Create tasks</li> |
| Virtual machine (Configuration) | <li>Add new disk</li><li>Add or remove device</li><li>Advanced</li><li>Change CPU count</li><li>Change resource</li><li>Memory</li><li>Modify device settings</li><li>Remove disk</li><li>Rename</li><li>Reset guest information</li><li>Set annotation</li><li>Settings</li> |

### Bootstrapping VM Templates with the ElasticBox Agent

vCenter templates need elasticbox-init to allow the ElasticBox agent to execute box scripts at deploy time.

**Linux**
Follow these steps to install elasticbox-init on a Linux template.

**Steps**
1. Log in to the vSphere client and open the Linux virtual machine.

2. SSH into the virtual machine.

3. [Install the VMware tools.](https://www.vmware.com/support/ws55/doc/ws_newguest_tools_linux.html)

4. Run this command with root privileges to install elasticbox-init:

   `curl -L https://elasticbox.com/agent/linux/vsphere/template_customization_script.sh | sudo bash`

   * **Note:** If running ElasticBox as an appliance, replace elasticbox.com with the appliance hostname or IP address.

**Windows**
Follow these steps to run a script that creates a scheduled task on a Windows Server 2012 template. When you deploy, ElasticBox clones this template and installs the agent using the scheduled task.

**Steps**
1. Log in to the Windows Server 2012 virtual machine template using remote desktop protocol (RDP).

2. [Install the VMware tools](https://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1018377).

3. [Download the scheduled task script.](https://elasticbox.com/agent/windows/vsphere/template_customization_script.ps1)

   * **Note:** If running ElasticBox as an appliance, replace elasticbox.com with the appliance hostname or IP address.

4. Right-click the script and click **Run PowerShell**.

### Registering Your vCenter in ElasticBox

In order to deploy to a vCenter private datacenter, you must first provide information to connect. Currently, ElasticBox only supports the vCenter API for vSphere.

**Steps**
1. In ElasticBox, click **Providers** > **New Provider**.

2. Select **VMware vSphere**.

3. Enter the endpoint URL for the vCenter server and a username, password to the vCenter API.
   * **Note:** The endpoint URL must be in the form of **https://<servername>** or **https://<ipaddress>**. Be sure to use https and not http.

   ![add-vsphere-provider-1.png](../images/ElasticBox/add-vsphere-provider-1.png)

### Deploying in Your vCenter

Select deployment metadata from a deployment profile to launch VMs to your vCenter Server.

![vsphere-deployment-profile-2.png](../images/ElasticBox/vsphere-deployment-profile-2.png)


**Deployment**

| Deployment Option | Description |
|-------------------|-------------|
| Provider | Select a vCenter account registered in ElasticBox. |


**Resource**

| Deployment Option | Description |
|-------------------|-------------|
| Datacenter | Select the datacenter whose objects are available for your vCenter deployment like hosts, clusters, resource pools, folders. |
| Template | Select the OS template based on which you deploy the instance. Only Linux templates show for Linux boxes as do Windows templates for Windows boxes. |
| Flavor | Select a template size for CPU and memory. Tiny, Small, Medium are sizes ElasticBox provides. Or choose from ones you added. For example, if you choose **Tiny**, the instance is provisioned with 1 CPU and 1GB of RAM. By default, ElasticBox provides template sizes as flavors based on compute and memory capacity. In addition to these flavors, you can add custom ones to the vCenter account in ElasticBox in the Configuration tab. Under Flavors, click **New** and specify the CPU and memory. |
| Customization | This is optional. Apply a custom specification to the instance. It usually has settings to configure the OS and network. |
| Instances | Select the number of machines to provision. |


**Placement**

| Deployment Option | Description |
|-------------------|-------------|
| Compute Resource | Place the VM in a host, cluster, vApp, or resource pool in the datacenter. Select **Any host** to place in a host ElasticBox picks randomly. |
| Network |	Select the network for the instance. |
| Folder | From the folders shown, select one to place the VM. |


**Disks dd**

| Deployment Option | Description |
|-------------------|-------------|
| Disks	| By default, an instance gets the template disk. For more storage, increase the template disk size and add up to seven more disks.<li>You can’t remove the template disk, but you can adjust its size. Type in the new size and press enter to save changes.</li><li>To add a disk, select a datastore from available ones in the datacenter. Specify the size in gigabytes, and click **Add**. Each disk can be up to 62 TB, disk can be up to 62 TB, but if the datastore doesn’t have such capacity, the instance won’t deploy.</li><li>Note that additional disks communicate through the same controller as the template disk.</li> |

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
