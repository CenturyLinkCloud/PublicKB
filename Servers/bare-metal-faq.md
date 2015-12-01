{{{
  "title": "Bare Metal FAQ",
  "date": "06-29-2015",
  "author": "Bryan O'Neal",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description

CenturyLink Bare Metal servers introduce the ability to provision and manage physical machines from the CenturyLink Cloud platform in a self-service, on-demand, and highly automated fashion.

This FAQ addresses commonly asked questions about the service. For further information on this service and how it compares to virtual servers, see [Server Comparison Matrix](../Servers/server-comparison-matrix.md).


**What are the available configurations for Bare Metal servers?**

* 4 cores (3.6GHz E3), 16 GB RAM, 10Gb NIC
  * Storage is 2x1TB 7200 RAID 1 (0.91TB usable)
* 12 cores (2.4GHz 2x6 E5), 64 GB RAM, dual 10Gb NIC
  * Storage is 4x2TB 7200 RAID 5 (5.46TB usable)
* 20 cores (2.3GHz 2x10 E5), 128 GB RAM, dual 10Gb NIC
  * Storage is 6x2TB 7200 RAID 5 (9.09TB usable)

**Why don't I see the option to provision a Bare Metal server type?**

There are a couple reasons you might not see the option for Bare Metal servers.  First, check your data center and the current [availability for Bare Metal servers](https://www.ctl.io/data-centers/#/filters/Bare%20Metal).  Bare Metal servers are not available in all data centers. If you are in a data center where Bare Metal servers should be available, contact Customer Care to have them check to see if Bare Metal servers need to be enabled for your account.

**Why am I seeing an error saying "limit exceeded" for CPU, memory, or storage when I try to provision a Bare Metal server?**

All accounts start with a pre-defined resource (CPU/memory/storage) limit per data center. Bare Metal server resources are included as part of these limits. If you've reached the limits for your account, you may contact Customer Care to [request an increase on your resource limits](../Control Portal/how-to-increase-resources-on-account.md).

**Can I increase or decrease CPU, memory or storage resources on Bare Metal servers?**

No, the CPU, memory and storage are static resources on each individual Bare Metal server and can not be changed once a particular configuration has been provisioned. The best available path for adjusting the resource configuration is to provision a new server with the desired configuration and plan to migrate any data as necessary.

**What are the self-service actions available to me through the Control portal for Bare Metal servers?**

Through the Control portal you are able to power the Bare Metal server on or off, perform a server reset and add a single public IP.

**What are the best suited workloads for this new server class?**

Any applications not well-suited to virtualization whether it be performance or licensing restrictions related, database and application workloads where consistent performance is critical, grid or HPC (High Performance Computing), data analytics, caching and indexing.

**How do I connect my Bare Metal servers over the network to my CenturyLink Cloud virtual servers?**

Bare Metal servers share the same network as CenturyLink Cloud virtual servers so it's as easy as creating and connecting networks amongst all your server types.  For more information on Network features of CenturyLink Cloud platform, reference the [Network Section](https://www.ctl.io/knowledge-base/network/#1) of our knowledge base.

**Since these servers use local storage, how do I avoid application failure if underlying hardware fails?**

It is your responsibility to maintain any data recovery or restoration process that may be necessary in the case of a critical hardware failure. An integrated backup solution will be available at some point but is not currently.

**How is hardware support and replacement handled for Bare Metal servers?**

CenturyLink is responsible for all hardware replacement for Bare Metal servers.  We monitor the Bare Metal servers underlying hardware using agentless SNMP monitoring via iLO.  If an incident is detected a ticket for investigation is automatically generated and the customer is notified. In the case where a server becomes completely unavailable the process to replace the server will begin immediately with consent from the customer. For additional service level details please reference the Bare Metal servers SLA on the [SLA page](https://www.ctl.io/legal/sla/).

**What are the security features available for Bare Metal servers?**

Bare Metal servers can be incorporated in the same firewall policies currently available with other CenturyLink Cloud server types. All Bare Metal servers are also provisioned with fully encrypted local storage for the protection of customer data.

**What should I do if I do not see the configuration of CPU/Memory/Storage I want?**

We've initially launched with a limited number of Bare Metal server configuration types and fully expect to expand upon the number of types and quantity available of each based on customer feedback.  The server configuration screen will provide an up to date indication of our available server types.  If you do not see a configuration type there that suits your needs, please submit a [Feature Request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/) including a brief explanation of your use case and the need for a particular configuration of resources.

**What features do Bare Metal servers share with CenturyLink Cloud virtual servers?**

While there are multiple in common between the two, there are several features available on virtual servers within CenturyLink Cloud that do not apply to Bare Metal servers.  Please see the [Server Comparison Matrix](../Servers/server-comparison-matrix.md) for more detail.

**Is there a term commit option available for Bare Metal servers?**

Yes, customers may work with their respective Sales representative to make use of the existing Cloud Term Commit process for Bare Metal servers in the same way they would for CenturyLink Cloud virtual servers.

**May I have console or iLO access to my Bare Metal server?**

No, there are a select number of management capabilities available through the Control portal including power operations and the ability to reset the server. No additional iLO or console access is included with the service.

**Can I change the administrator/root password of my server through Control or the API?**

Yes, the password is set at the time of server creation and can be changed after the fact. The password should only be [changed through the Control portal](../Servers/how-to-change-a-server-administrator-password.md) or API.  Changing the password through the OS will cause the “show credentials” link in the Control portal to no longer display accurate credentials.

**Where are Bare Metal servers available geographically?**

Bare Metal servers availability can be viewed on the [CenturyLink Cloud data centers page](https://www.ctl.io/data-centers/#/filters/Bare%20Metal).

**What should I do if my Bare Metal server becomes unresponsive?**

Contact our Customer Care group by submitting a support request using the link at the top right side of this site.  If a ticket has not already been automatically generated, they will respond to your request and begin investigation.

**How is data destruction handled in the cases of hard drive failure/replacement and/or server relinquishment for Bare Metal servers?**

All local storage associated with Bare Metal servers is fully encrypted.  As such, destruction is not necessary to protect sensitive data.  New encryption keys are automatically generated for each newly provisioned server. Encryption is controlled exclusively by the disk array controller and not within the OS or elsewhere. We control the encryption keys and each key is tied directly to the logical volume on the array controller. When the logical volume is deleted there is no recovery path as the associated key is destroyed at the same time by the array controller. Thus, the data is rendered unrecoverable as part of our routine rediscovery and provisioning process for servers being decommissioned.

**Do I still get billed for a Bare Metal server that is turned off?**

Yes, Bare Metal servers are dedicated to you once they have been provisioned and will continue to bill the normal hourly rate regardless of the state of the server.  Under certain circumstances, if a server has become unavailable to the point where it has exceeded the SLA for availability, credits may be applicable for the lost server time.

**Can I customize my storage configuration on a Bare Metal server?**

No, the storage configurations provisioned for Bare Metal servers are all either RAID 1 or RAID 5 depending on the server configuration type and tampering with that configuration could result in loss of management access which could disrupt support. Each server is provisioned with two partitions, one 300GB boot partition and a second partition for the remaining storage capacity for that particular configuration type.

**Can I customize my network interface configuration on a Bare Metal server?**

Yes, Bare Metal servers do support multiple vNIC configurations. Additional vNICs can be [added through the API](//www.ctl.io/api-docs/v2/#servers-add-secondary-network). It is not advised to make any other manual network configuration changes as they may be detrimental to associated support and automated provisioning services.

**Can I bring my own OS image?**

No, the available Operating Systems include Windows 2012 Standard Edition R2, Windows 2012 Datacenter Edition, RHEL6, CentOS 6, and Ubuntu 14. If there is a particular OS image you would like to see incorporated please [submit a feature request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/).

As an alternative to a custom image, Bare Metal servers do support the [execute package](https://www.ctl.io/knowledge-base/servers/using-group-tasks-to-install-software-and-run-scripts-on-groups/) action from the Control Portal as well as through the [API](https://www.ctl.io/api-docs/v2/#server-actions-execute-package), allowing you to install the same software or run the same scripts on many servers at once.

**When running "execute package" a Bare Metal server, why does the Blueprint fail?**

Your server may be using an older version of the OS image from before package execution was supported on Bare Metal. Follow the instructions below for the specific OS that your server is running to ensure packages can be executed successfully.

_On Windows_

  - Enable "File and Printer Sharing" on the server. The following PowerShell command will enable it, or you may turn it on through the Management Console in Windows.

        netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes

_On Linux_

  - The `Ciphers` line in `etc/ssh/sshd_config` must support the **`aes256-cbc`** cipher:

        Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes256-cbc

  - Ensure that the `unzip` command package is installed on the server.


If you still have problems with failing Blueprints, contact Customer Care by submitting a support request using the link at the top right side of this site.

**Can I use my own licensing for the OS?**

No, the licensing is factored into the cost of the Bare Metal server where applicable and cannot be separated from the service.  If you would be interested in using your own OS licensing with Bare Metal servers, please let us know in a [feature request](https://www.ctl.io/knowledge-base/support/how-do-i-submit-a-feature-request/).

**What's the difference between Windows 2012 Standard and Windows 2012 Datacenter Edition on Bare Metal servers?**

Both are capable of leveraging the Hyper-V role to provision VMs on the Bare Metal server, but the Datacenter Edition license allows for unlimited VMs to be provisioned on a physical host while the Standard Edition is limited to two VMs running concurrently on the physical server host.

**How do I activate my Windows VMs provisioned on a Windows 2012 Datacenter Edition Bare Metal server?**

The answers will differ depending on which Windows OSes you are trying to activate.  Guest VMs running Windows 2012 R2 will automatically activate using [AVMA (Automatic Virtual Machine Activation)](https://technet.microsoft.com/en-us/library/dn303421.aspx) using the host's Hypervisor. Guest VMs running Windows 2008 R2 can activate either using Multi-Activation Keys (MAKs) obtained from Microsoft, or by using the volume license keys available on [Microsoft's site](https://technet.microsoft.com/en-us/library/jj612867.aspx?f=255&MSPPError=-2147217396) along with the CenturyLink KMS host. To use our KMS you will need to manually specify the KMS host on the guest VM.

1. You will need the VM to be on a CenturyLink Cloud customer VLAN to access our KMS host and the IP/port associated.
  ```
  172.17.1.21:1688
  ```

2. You can test TCP port by telnetting to the IP over the appropriate port.
  ```
  telnet 172.17.1.21 1688
  ```

3. To specify the KMS host, use the following command:
  ```
  slmgr /skms 172.17.1.21:1688
  ```

Windows VMs in a Hyper-V environment on Bare Metal servers should use IPs in the same VLAN as configured in the Control portal for the host Bare Metal server.  It is also recommended that IPs be higher in the range so VMs claiming from that same range will not encounter IP conflicts.  Additional IPs for guest VMs can be obtained by submitting a customer support request. For activation of older Windows OSes on guest VMs you will need to obtain your own MAKs and/or activation solution.

**Does CenturyLink provide OS media (ISO's) for guest VMs on Windows 2012 Datacenter Edition with Hyper-V?**

Customers are responsible for supplying their own guest VM OS media when using the Windows 2012 Datacenter Edition virtualization features.
