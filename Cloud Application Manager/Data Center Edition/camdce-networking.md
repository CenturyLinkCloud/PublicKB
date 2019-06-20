{{{
"title": "Configuring Network Settings of Cloud Application Manager Data Center Edition",
"date": "05-24-2019",
"author": "Diego Sanjuan",
"keywords": ["cam", "cloud application manager", "Data Center edition", "appliance", "setup", "network"],
"attachments": [],
"contentIsHTML": false
}}}


**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Steps](#steps)
* [Contacting Cloud Application Manager Support](#contacting-cloud-application-manager-support)


### Overview


This article shows how to configure and how the appliance connects to the network, once it's up and running. By default, it tries to get a dynamic IP address via DHCP. But we recommend that you set a static IP address with these steps so that Cloud Application Manager services are always available at the same address to users.


### Audience


All Cloud Application Manager Data Center Edition users who wants to configure Cloud Application Manager Data Center Edition (appliance) static address.


### Prerequisites


* Your Cloud Application Manager Data Center Edition (appliance) should be properly deployed and running in your preffered platform. You can refer to the [Cloud Application Manager Data Center Edition documentation](camdce-overview.md).
* You need to have access to HTTPS (443) port of the appliance to access its setup console.


### Steps


* Locate the VM console where you installed the appliance in vCenter or OpenStack.
   ![appliance-networking1.png](../../images/cloud-application-manager/appliance-networking1.png)

* In the Advanced Menu, select **Networking > Static IP**.
   ![appliance-networking2.png](../../images/cloud-application-manager/appliance-networking2.png)

* Enter settings based on your network configuration to set up a static IP address for the appliance. When done, click **Apply**.
   ![appliance-networking3.png](../../images/cloud-application-manager/appliance-networking3.png)

   * **IP Address** - Unique IPv4 address the appliance needs to connect to the network.
   * **Netmask** - Subnet mask or address of nearest local area network, for example, 255.255.255.0.
   * **Default Gateway** - Enter the subnet router’s IP address. This is similar to the IP address except for the last digit.
   * **Name Server** -  Enter the preferred and alternate DNS server addresses in each name server field.

* Reboot the appliance to apply the configuration changes. In the appliance console, click **Advanced Menu > Reboot**.


### Contacting Cloud Application Manager Support


We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.

In the case of a box error, share the box in the workspace that your organization and Cloud Application Manager can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at C:\ProgramData\ElasticBox\Logs\elasticbox-agent.log

