{{{
"title": "Using Microsoft Azure",
"date": "04-19-2017",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using Microsoft Azure

There are two different flavors of Azure and Cloud Application Manager has providers for both. This document is in reference to Classic Azure.

*Name** | **URL of Portal** | **Name of Related Cloud Application Manager Provider** | **KB article**
--- | --- | --- | ---
Classic Azure | https://manage.windowsazure.com | Classic Azure | This document
Microsoft Azure | https://portal.azure.com | Microsoft Azure  | [Using Microsoft Azure](./using-microsoft-azure.md)

Each of Cloud Application Manager's Microsoft Azure Providers gives you the option of setting it up either for an existing or a new Azure Customer Account. Existing accounts are your responsibility and will continue to be billed to you by Azure. New Accounts will automatically be generated on your behalf and the credentials pulled into the Provider via [Cloud Optimization](../Cloud Optimization/partner-cloud-integration.md), allowing you to hand off platform-level support and billing to CenturyLink.

If you want to learn how to use the New Account feature, please visit [Partner Cloud: Getting Started With a New Azure Customer](../Cloud Optimization/partner-cloud-integration-azure-new.md). The rest of this article assumes you will be using an existing, Azure Customer Account without any integration with CenturyLink.

If you do have an existing Azure account that you want CenturyLink to manage or support, please contact cloudsupport@centurylink.com. Please provide the name and domain of your account. Also, please describe any products, services, or resources within your Customer Account that are not currently shown in this list of [permitted products](../Cloud Optimization/partner-cloud-integration-azure-capabilities.md). We likely have already have begun work to enable your products.

### Before You Begin

You need an Microsoft Azure subscription to be able to consume Azure services. Follow these steps to create one.

### Steps

1. Login to the [Azure portal](https://portal.azure.com/) using your Microsoft Account.
2. Create a new Azure application in the Azure Active Directory. <b>Be sure to select "Native" when selecting the application type.</b>
3. Log back in to the Azure portal and go to subscriptions tab, select *Access Control (IAM)* and then select  *+ Add* on the new screen.
4. Select *Contributor* role. (If you do not see the Contributor role, you may need to talk to your administrator.)
5. Search for the application you just created in step 2 and click OK!
6. Return to the "App Registrations" panel in Step 2. Select the app, and select "Keys" in the "Settings" panel. Give the key any name and expiration date, and select "Save." The value of the key will be generated. Copy and keep the value (secret key) as you won't see it anymore once you navigate away.
7. Complete your Microsoft Azure Provider for an existing account with the information below:
> Subscription ID: The active subscription ID<br>
> Client ID: The Application ID<br>
> Secret: The key value generated in Step 4<br>
> Tenant: Copy from Azure Active Directory > Properties > Directory ID<br>

If you cannot find a specific template that you are looking for in Cloud Application Manager be sure to check out the [Azure github quickstart templates](https://github.com/Azure/azure-quickstart-templates).

### Registering Your Microsoft Azure Subscription (ARM) in Cloud Application Manager

To connect to Microsoft Azure in Cloud Application Manager, you need to follow these steps.

**Steps**

1. In Cloud Application Manager, go to **Providers** > **New Provider** and select **Microsoft Azure**.
   ![microsoft-azure-add-provider-1.png](../../images/cloud-application-manager/microsoft-azure-add-provider-1.png)

2. Fill the form with Subscription ID, Application ID, Secret and Tenant obtained in previous section and save.
   ![microsoft-azure-credentials-2.png](../../images/cloud-application-manager/microsoft-azure-credentials-2.png)

Once pressed the save button our new provider starts to synchronize with our azure account from which you will get the following information:

* VM images of windows family operating systems.
* VM images of operating systems of Linux family.
* Region list which we can deploy the mentioned services as well as the templates of Azure Resource Manager.
* List of deployed Virtual Machines that are currently not being managed from Cloud Application Manager.

During synchronization, we can get warnings about locations may be ignored because there are no associated virtual networks to them. This is because Cloud Application Manager does not create virtual networks but requires one in the deployment operation of one virtual machine.

The result of the synchronization process will be the creation of one ARM template box and two policy boxes (Windows and RHEL respectively) in case of exist a virtual network in our account.

### Deploying Instances in Azure

You can deploy to the following services in Azure:

* Windows based virtual machines
* Linux based virtual machines
* Azure resource manager templates

**Azure OS Images Available to Deploy in Cloud Application Manager**

As part of the result of synchronization process you can find a list of available operative systems that you can use in your policy boxes. You can check this list in **Providers** page > **Configuration**.

![microsoft-azure-os-images-available-to-deploy-3.png](../../images/cloud-application-manager/microsoft-azure-os-images-available-to-deploy-3.png)

This images are what we show in image list from policy box edition.

**Microsoft Azure Compute Deployment Options**

To deploy a virtual machine with compute services you can edit one of windows or RHEL policy boxes or create a new one. Then you can save your changes and click **Deploy**.

![microsoft-azure-compute-deployment-options-4.png](../../images/cloud-application-manager/microsoft-azure-compute-deployment-options-4.png)

**Resources**

| Option | Description |
|--------|-------------|
| Location | Select the region where you want to deploy the virtual machine. Each location has available its own images, networks and sizes so is the first parameter you have to choose.<br>Only locations with networks available are shown. |
| OS Image | Select the guest OS to run in the worker role instance. Note that Windows 2008 images are not synced at this time because the Cloud Application Manager agent doesn’t work on them. |
| Size | Select a size to set the number of CPU cores, memory, and disk size to store your OS files, process temporary memory, and store application data. For more information, see the [Azure help](https://msdn.microsoft.com/en-us/library/azure/dn197896.aspx). Note that D-Series sizes use solid-state drive disks. |
| Username | Specify a username to be able to RDP or SSH into the instance directly. |
| Password | Specify a password to be able to RDP or SSH into the instance directly. |
| SSH Certificate | Only in Linux machines you can specify a certificate to access via ssh. |
| Instances | Specify the number of instances to spawn. Note that at this time, we don’t autoscale or load balance instances. To enable that, you have to manually configure these options in [Azure](https://msdn.microsoft.com/en-us/library/hh680914). |


**Network**

| Option | Description |
|--------|-------------|
| Virtual Network |	This network has to be created before because Cloud Application Manager doesn't deploy any. |
| Subnet | This subnet is the resource related to  the virtual machine's network interface. Actually a virtual network is not used at deployment time. |

If you can't create any policy box on Windows Azure provider probably you have to create a virtual network from azure portal or you may deploy a new one with a template as we describe in following section.

**Microsoft Azure ARM Template Deployment Options**

Azure ARM Templates are supported on Cloud Application Manager with Microsoft Azure provider. You can deploy whatever you want with the same syntax you use on Azure APIs and portal. For this purpose you can create a custom deployment policy and deploy it with an ARM Template box together.

**Steps**

1. Create Deployment Policy:
   * Go to **Boxes** > **New** > **Deployment Policy**.
   ![microsoft-azure-create-new-deployment-policy-5.png](../../images/cloud-application-manager/microsoft-azure-create-new-deployment-policy-5.png)
   * **Select Azure Resource Manager** on the menu.
   ![microsoft-azure-select-arm-new-deployment-policy-box-6.png](../../images/cloud-application-manager/microsoft-azure-select-arm-new-deployment-policy-box-6.png)
   * Select provider, name and description fields.
   ![microsoft-azure-select-provider-name-7.png](../../images/cloud-application-manager/microsoft-azure-select-provider-name-7.png)
   * Click **Save**.

2. Edit Deployment Policy.
   * Go to **Template** > **Code** and press **Edit**.
   * Put your own template and click **Save**.

3. Deploy Template.
   ![microsoft-azure-deploy-template-8.png](../../images/cloud-application-manager/microsoft-azure-deploy-template-8.png)
   * From Template click **Deploy**.
   * **Select** one ARM Template Box.
   * Choose a name and description for the new instance.
   * Press **Deploy**.

### Registering Existing Instances from your Azure Account

You can import existing Virtual Machines into you workspace only in one click. The list of available instances you can import come with your Microsoft Azure provider synchronization.

**Available Instances**

As part of the result of synchronization process you can find a list of available virtual machines that already exist in your account but not used yet in Cloud Application Manager. You can import an existing one clicking **Import** button.

The only requirement is instance must be in Running status.

![microsoft-azure-available-instances-9.png](../../images/cloud-application-manager/microsoft-azure-available-instances-9.png)

We strongly recommend synchronize your Azure provider before you try to register the virtual machine. This due to such instance may be registered by another user before you try to register it. This way you can avoid this kind of problems.

### Shutdown and Terminate Instances in Azure

**Shutdown Instance**

When a shutdown operation is executed from Cloud Application Manager, the virtual machine is stopped on Azure but not deallocated, in order to maintain the VM configuration and not loose the IP address. This means that the virtual machine will continue billed.

To deallocate a virtual machine stopped, you have to enter on Azure portal and click again on Stop.

**Terminate Instance**

When a terminate operation is executed from Cloud Application Manager, this operation execute the dispose scripts from your box instance and then deletes the virtual infrastructure. You can't revert the action and since you can lose data, be sure you want to perform this action in the first place.

### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:cloudsupport@centurylink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
