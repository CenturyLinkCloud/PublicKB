{{{
"title": "Using CenturyLink Cloud",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}


### Using CenturyLink Cloud

Automate application deployments through Cloud Application Manager when you launch to Linux or Windows virtual servers in the CenturyLink Cloud public cloud. Cloud Application Manager simplifies deployments with a dedicated focus on applications rather than infrastructure.

**In this article:**

* Register CenturyLink Cloud provider in Cloud Application Manager
* Deploy to CenturyLink Cloud from Cloud Application Manager

### Register CenturyLink Cloud Provider in Cloud Application Manager

You need a [CenturyLink Cloud account](//www.ctl.io/) to be able to deploy from Cloud Application Manager. When you have an account, follow these steps to register it in Cloud Application Manager to automate your deployments.

**Steps**

1. In Cloud Application Manager, go to **Providers** > **New Provider** and select **CenturyLink.**

2. Enter the CenturyLink username and password as shown and save.

   ![centurylink-add-provider-credentials-1.png](../../images/cloud-application-manager/centurylink-add-provider-credentials-1.png)

### Deploy to CenturyLink Cloud from Cloud Application Manager

Select from the following deployment profile options to launch workloads on Linux or Windows machines.

Note a couple of things about instances you deploy on CenturyLink Cloud through Cloud Application Manager.

* Instance name. Each instance is assigned a name that has the format of DatacenterFirst_six_letters_of_instance_nameCounter. i.e., UC1CITTPUBLIC01 for an instance deployed on UC1 (US West - Santa Clara) of a box called Public Proxy.
* Instance Description. Depending on the number of instances you spin up through Cloud Application Manager, each instance is assigned a description that has the format of dasherized-instance-name-datacenter-service_ID-machine-number.

**Deployment**

| Option | Description |
|--------|-------------|
| Provider |  Select a CenturyLink Cloud account registered in Cloud Application Manager. |


**Resource**

| Option | Description |
|--------|-------------|
| Server Type | Select a server type, for example, standard. |
| Datacenter | Select a location to place the instance, for example, UC1. |
| Group |	Select placement group for the new instance. |
| Template | Select from a list of CenturyLink Cloud Linux or Windows images. Images are specific to the box service type, that is, Linux or Windows. |
| Instances | Specify the number of instances to provision. |
| Admin/root Password | Choose Admin/root password for your instance. |
| Confirm Password | Confirm the password. |


**Network**

| Option | Description |
|--------|-------------|
| Network |	Select a vLan for the new instance. |
| Public IP	| Check the box to attach a public IP address to the new instance. |


**Compute**

| Option | Description |
|--------|-------------|
| CPUs | Select virtual CPUs for the instance. You can get up to 16 cores. |
| Memory | Allocate RAM for the instance. You can get up to 128 GB. |

**Disks**

By default, the machine is provisioned with 17GB local disk space. You can add more disks in RAW format or Partitioned, up to 1024 GB.

### Shutdown and Terminate Instances in CenturyLink Cloud

**Shutdown Instance**

Initiates a graceful shutdown of the corresponding server or servers. Like the “off” power command, all memory and CPU charges cease, monitors are disabled, and the machine is left in a powered off state. Any licensing charges (if applicable) and storage charges continue accruing.

More information [here](https://www.ctl.io/guides/servers/server-power-operations/).

**Terminate Instance**

The server is terminated and any disks are also deleted. The charges stop.

The history of the instance on Cloud Application Manager is preserved until the instance is deleted.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
