{{{
"title": "Using DCC",
"date": "06-20-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using DCC

**Creating a provider**

Creating and synchronizing a DCC provider is like the rest of Cloud Service Providers. The only difference is the way we pass the credentials. For DCC we use the username and password we get when we create an account on the Dedicated Cloud Compute Portal (DCC).

> User must have "customer purchase permission" and an associated billing account in DCC to be able to operate in CAM.<br>
> you can ask to get it fixed by opening a ticket [Here](https://savvisstation.savvis.com)<br>

![centurylink-add-provider-credentials-2.png](../../images/cloud-application-manager/centurylink-add-provider-credentials-2.png)

Once you save the provider, it will start syncing. It will load all the different deployment options available to use wth our Policy Boxes and make them available on our UI.

The user is normally linked to a company and this company linked to a set of metadata like BillingSite, Clusters, Domains, etc.

Virtual machines get deployed on clusters. If we don't have enough information to deploy a cluster, then the cluster will not be available as a deployment option for the Policy Boxes. Nonetheless, we will display an alert, as you can see on the following screenshot:

![centurylink-cluster-error-alert.png](../../images/cloud-application-manager/centurylink-cluster-error-alert.png)

When the synchronization process finishes, we can go to provider's "Configuration" tab. There we will see the list of Linux and Windows Services available to deploy on each cluster.

![centurylink-services-list.png](../../images/cloud-application-manager/centurylink-services-list.png)

**Editing Policy Boxes on DCC**

Besides the services list, we can see two example Policy Boxes for Linux and Windows. We can customize them any time to fit our needs.

![centurylink-dcc-example-policy-boxes.png](../../images/cloud-application-manager/centurylink-dcc-example-policy-boxes.png)

To do this, we ned to access the details by selecting "Code", then "Edit", where we can change the following options:

| Option | Description |
|--------|-------------|
| Company | A user can be linked to multiple companies (multi-tenant). We can select which of them we want the VM to be billed against. |
| BillingSite |	The account where the VM creation will be billed. A company can have multiple Billing Sites. |
| Datacenter | Clusters are grouped in Datacenters. To select a Cluster, we will first have to select the Datacenter the Cluster belongs to. |
| Cluster |	Hardware specifications where the VM will be deployed. Each Cluster has a list of its own associated Machine Configurations, Operative Systems, storages and Network segments. This section will only show those that allow us to deploy the VMs when synchronization happens. |
| Machine Configuration | Set of values and restrictions associated with CPU, RAM, Instances and Burn in Period. |
| OS | List of supported Operative System that the Cluster supports. |
| Language | Each Operative System supports multiple installation languages. |
| Instances | You can deploy several servers at once, with the restriction that all the operations will run on all the instances (start, stop, delete and script boxes installation). |
| VCPU | Number of CPUs. |
| VRAM | Amount of memory assigned to the Virtual Machine. |
| Storage | Volume where the OS disk will be mounted. The user is responsible for assigning a segment with enough available space. CAM will only create the necessary disks to install the OS, if you need any extra disk you will need to add it from DCC portal. |
| Network | Net segment where the VM is configured. Please note that the IP address is set automatically, so the user must select a segment with available IP addresses. |

![centurylink-dcc-policy-box-options.png](../../images/cloud-application-manager/centurylink-dcc-policy-box-options.png)

![centurylink-dcc-policy-box-options-2.png](../../images/cloud-application-manager/centurylink-dcc-policy-box-options-2.png)

Once the Box deploys, we can see the traces of what is happening with the provider. At the end of the process it will show us a script that will have to be manually executed on the newly created Virtual Machine.

![centurylink-dcc-deployment-traces.png](../../images/cloud-application-manager/centurylink-dcc-deployment-traces.png)

Credentials for the Virtual Machine over email, and it should have privileges to install the CAM agent using the script shown above.

> To run this script, the user needs access to the new Virtual Machines. This task, as the creation of the account, needs to be done by DCC.<br>

Once this is done, the deployment process is finished.