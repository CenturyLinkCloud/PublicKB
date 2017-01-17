{{{
"title": "Installing the Virtual Appliance in vCenter",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Installing the Virtual Appliance in vCenter
If you don’t have internet access in the vCenter, download all the files and import them locally into your vCenter network. If you have access, you can directly import the appliance in the open virtualization format (OVF) and vCenter will download the disk images for you.

**In this article:**
* vCenter Requirements
* Installing the Appliance in vCenter
* Connecting the Appliance to the vCenter Network
* Next Steps

### vCenter Requirements
* Datacenter running vSphere vCenter 5.0 or later
* Linux virtual machine template
* 4 CPU cores, 8 GB memory, 100 GB hard drive space

### Installing the Appliance in vCenter
**Steps**
1. Copy the OVF file download URL.
   **Note:** If you don’t have internet access, download all the files and import them locally into your vCenter network.
2. In the vCenter vSphere client, click **File > Deploy OVF Template**.
3. In the wizard, under Deploy from a file or URL, paste in the URL. Click **Next**.
4. (Optional) Edit the name and select the folder where the appliance will live. Click **Next**.
5. Select the cluster and a host that will run the appliance. Click **Next**.
   ![appliance-vcenter1.png](../images/ElasticBox/appliance-vcenter1.png)

6. Choose a cluster resource pool if available to centrally manage the compute and storage resources for the appliance.<br>
    ![appliance-vcenter2.png](../images/ElasticBox/appliance-vcenter2.png)

7. Select the datastore to store the appliance. The datastore virtual disk format is set to Thin. Thin provision conserves disk space and expands as needed. This means the appliance uses the space required now but takes up more space as usage grows.
   ![appliance-vcenter3.png](../images/ElasticBox/appliance-vcenter3.png)

8. Review the appliance settings before you deploy. Select **Power on after deployment**. Click **Finish**.
   ![appliance-vcenter4.png](../images/ElasticBox/appliance-vcenter4.png)

### Connecting the Appliance to the vCenter Network
In these steps, you connect the ElasticBox appliance to the vCenter datacenter network and then turn it on.

**Steps**
1. In the vSphere Client, right-click the ElasticBox appliance that you just installed.
2. Click **Edit Settings > Hardware tab**. The OVF template pre-selects the required processing speed and the network adapter. Make sure they are set as follows:
   ![appliance-vcenter5.png](../images/ElasticBox/appliance-vcenter5.png)

   * CPUs. Two CPU virtual sockets to increase parallel processing.
   * Network adapter. A valid network to connect the appliance to your datacenter.

3. Now start the appliance. Right-click the appliance, click **Power > Power On**.

### Next Steps
* [Configure networking](./appliance-networking.md)
* [Set up the appliance for use](./appliance-initialsetup.md)

### Contacting ElasticBox Support
We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
