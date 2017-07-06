{{{
"title": "Using CenturyLink DCC",
"date": "06-20-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using CenturyLink DCC

**Creating a provider**

Select CenturyLink DCC from the Provider list and enter a username and password to logon to the CenturyLink DCC Portal.

> The user must have "customer purchase permission" and an associated billing account in CenturyLink DCC to operate in the Cloud Application Manager.<br>
> If this is not the case, open a ticket [here](https://savvisstation.savvis.com) to get it fixed.<br>

![centurylink-add-provider-credentials-2.png](../../images/cloud-application-manager/centurylink-add-provider-credentials-2.png)

Once the provider imformation is saved, Cloud Application Manager starts synchronizing the Provider account. After the synchronization is complete, Cloud Application Manager creates default Deployment Policies with the different deployment options available.

![centurylink-dcc-example-policy-boxes.png](../../images/cloud-application-manager/centurylink-dcc-example-policy-boxes.png)

The user account used when creating the Provider is linked to a Company, Billing Site, Clusters, and Domains, etc.

When the synchronization process finishes, the list of Linux and Windows Services available to deploy on each cluster is available on the provider's "Configuration" tab.

![centurylink-services-list.png](../../images/cloud-application-manager/centurylink-services-list.png)

**Editing Policy Boxes on CenturyLink DCC**

In addition to the services list, Cloud Application Manager creates two example Policy Boxes for Linux and Windows. These can be customized any time.

To do this, access the details by selecting "Code", then "Edit", where the following options are available:

| Option | Description |
|--------|-------------|
| Company | A user can be linked to multiple companies (multi-tenant). Cloud Application Manager can select which of them to bill. |
| BillingSite |	The account where the VM creation is billed. A company can have multiple Billing Sites. |
| Datacenter | Clusters are grouped in Datacenters. To select a Cluster, Cloud Application Manager needs to know the Datacenter the Cluster belongs to. |
| Cluster |	Hardware specifications where the VM will be deployed. Each Cluster has a list of its own associated Machine Configurations, Operating Systems, Storages, and Network Segments. This section will only show those that allows Cloud Application Manager to deploy the VMs when synchronization happens. |
| Machine Configuration | The set of values and restrictions associated with CPU, RAM, Instances and Burn in Period. |
| OS | The list of supported Operative System that the Cluster supports. |
| Language | Each Operative System supports multiple installation languages. |
| Instances | Cloud Application Manager can deploy several servers at once, with the restriction that all the operations run on all the instances (start, stop, delete, and script boxes installation). |
| VCPU | The number of CPUs. |
| VRAM | The amount of memory assigned to the Virtual Machine. |
| Storage | The volume where the OS disk wis mounted. The user is responsible for assigning a segment with enough available space. Cloud Application Manager only creates the necessary disks to install the OS. If you need any extra disk, you will need to add it from CenturyLink DCC portal. |
| Network | The net segment where the VM is configured. Please note that the IP address is set automatically. The user must select a segment with available IP addresses. |

![centurylink-dcc-policy-box-options.png](../../images/cloud-application-manager/centurylink-dcc-policy-box-options.png)

![centurylink-dcc-policy-box-options-2.png](../../images/cloud-application-manager/centurylink-dcc-policy-box-options-2.png)

**Deploying Instances from Deployment Policies**

Virtual machines get deployed on clusters. If Cloud Application Manager doesn't have enough information to deploy a cluster, the cluster will not be available as a deployment option for the Policy Boxes. In that case, Cloud Application Manager displays an alert as follows.

![centurylink-cluster-error-alert.png](../../images/cloud-application-manager/centurylink-cluster-error-alert.png)

Once the Box deploys, Cloud Application Manager shows the traces of what is happening with the provider. At the end of the process it displays a script that has to be executed manually on the newly created Virtual Machine.

![centurylink-dcc-deployment-traces.png](../../images/cloud-application-manager/centurylink-dcc-deployment-traces.png)

Credentials for the Virtual Machine are sent via email which contains the necessary privileges to install the Cloud Application Manager agent using the script shown above.

> To run this script, the user needs access to the new Virtual Machines. This task, as in the creation of the account, needs to be done by CenturyLink DCC.<br>

Once this is done, the deployment process is complete.
