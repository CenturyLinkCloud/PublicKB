{{{
  "title": "Converting unmanaged virtual machines to managed",
  "date": "5-28-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
[CenturyLink Cloud Managed Operating System Services](//www.ctl.io/managed-services/operating-system/) provide maintenance and management of your Windows & Red Hat cloud servers, 24x7.  For a flat hourly fee, our engineers will perform support and administrative functions on your behalf.

Customers may wish to enable Managed OS on virtual machines already deployed in an **unmanaged** state to offload critical IT functions.  In order to facilitate this process the CenturyLink Cloud platform provides an automated [Blueprint](//www.ctl.io/blueprints/) to convert unmanaged virtual machines into a managed operating system.

Of course, you may also consider using the CenturyLink Cloud API to handle these actions programmatically. What follows is the simplest method, via the Control Portal.

### Audience

Users employed by companies that have agreed to terms with [CenturyLink Sales](http://www.centurylink.com/) for the CenturyLink Cloud product.

### Prerequisites
* An understanding of the standard server creation process.
* Some idea of the benefits included with [managed servers](../Managed Services/managed-operating-system-frequently-asked-questions.md)


### Important Information
* Conversion from **Managed** to **Unmanaged** Operating System Services is not currently a supported feature.
* It is advised that customers perform the conversion during a maintenance window due to potential impact on running services.
* It is recommended to create a snapshot of the VM before running the management process
* Normally, a single CPI Blueprint will take between ten and thirty minutes to complete. However, this can be influenced by jobs in the queue
* Due to security concerns, customers will be unable to convert a sub-account VM to Managed while using an IP address from a parent account network. The network chosen for the VM must belong to the same account upon which the machine resides.
* To preconfigure network access, prior to making an unmanaged VM Managed, please be sure at least one [new, managed server](../Managed Services/created-a-managed-server-now-what.md) has been created in the desired VLAN/Network.


### Compatibility Matrix
The table below provides a matrix of the supported locations and Operating Systems for conversion.

**Cloud Location**|**Operating System**
------------------|--------------------
GB3 - Great Britain (Slough)<p>VA1 - US East (Sterling)<p>UC1 - US West (Santa Clara)<p>US Central (Chicago) - IL1<p>Canada (Toronto - Mississauga) - CA3<p>APAC (Singapore) - SG1|Red Hat Enterprise Linux 5 - 64-bit<p>Red Hat Enterprise Linux 6 - 64-bit<p>Red Hat Enterprise Linux 7 - 64-bit<p>Windows 2008 R2 Standard - 64-bit<p>Windows 2008 R2 Enterprise - 64-bit<p>Windows 2008 R2 DataCenter Edition - 64-bit<p>Windows 2012 DataCenter Edition - 64-bit<p>Windows 2012 R2 DataCenter Edition - 64-bit<p>

### Converting Unmanaged Windows Virtual Machines to Managed
1. Log on to the [Control Portal](https://control.ctl.io/). Using the left side navigation bar, click on **Orchestration** > **Blueprints Library**. Select a Cloud location that supports managed operating system services.

    ![Select cloud location](../images/vm-to-managed1.png)

2. Using the search feature, input **CPI** to filter the blueprints.

    ![search for CPI and filter](../images/converting-unmanaged-virtual-machines-to-managed-02.png)

3. Choose the **Managed-Win for CPI** blueprint and select the deploy blueprint icon.

    ![deploy CPI Windows blueprint](../images/converting-unmanaged-virtual-machines-to-managed-03.png)

4. In Step 1 (customize blueprint) select the Windows Virtual Machine you wish to convert to a managed server.  Each of the 4 customization areas **require** the user to select the virtual machine you wish to convert and all of them should be set to the same instance.

    ![customize blueprint](../images/converting-unmanaged-virtual-machines-to-managed-04.png)

5. In Step 2 validate your inputs and select the deploy blueprint button.

    ![deploy blueprint](../images/converting-unmanaged-virtual-machines-to-managed-05.png)

6. Validate the Job completes in the queue

    ![queue windows conversion](../images/converting-unmanaged-virtual-machines-to-managed-06.png)

### Converting Unmanaged Linux Virtual Machines to Managed
1. Log on to the [Control Portal](https://control.ctl.io/). Using the left side navigation bar, click on **Orchestration** > **Blueprints Library**. Select a Cloud location that supports managed operating system services.

    ![Select cloud location](../images/vm-to-managed1.png)

2. Using the search feature, input **CPI** to filter the blueprints.

    ![search for CPI and filter](../images/converting-unmanaged-virtual-machines-to-managed-02.png)

3. Choose the **Managed-RHEL for CPI** blueprint and select the **deploy blueprint** button.

    ![deploy CPI linux blueprint](../images/converting-unmanaged-virtual-machines-to-managed-07.png)

4. In Step 1 (customize blueprint) select the Linux Virtual Machine you wish to convert to a managed server. Each of the 3 customization areas **require** the user to select the virtual machine you wish to convert and all of them should be set to the same instance.

    ![customize blueprint](../images/converting-unmanaged-virtual-machines-to-managed-08.png)

5. In Step 2 validate your inputs and select the **deploy blueprint** button.

    ![deploy blueprint](../images/converting-unmanaged-virtual-machines-to-managed-09.png)

6. Validate the job completes in the queue

    ![queue linux conversion](../images/converting-unmanaged-virtual-machines-to-managed-10.png)


  After creating a VM for management or after deploying the blueprint to convert an existing VM to a managed one, the VM will be 'Under Construction' while background processes are completed. You will not have access to the server during that time. Please allow up to a 60 minutes. If there are any issues beyond that time, contact us via email <a href="mailto:request@centurylink.com">request@centurylink.com</a> or by phone at the following numbers.

    * In the US: 888.638.6771
    * UK: +44.118.322.6100
    * Singapore: +65.6305.8099.

  Please do not email the CenturyLink Cloud NOC or raise the issue via chat - faster responses to inquiries will come from the email address and support numbers above. This is because Managed support is provided by a different team than Platform support.

### Validation
The user will receive a notification email once the virtual machine is successfully converted to Managed.
```
Your request "Managed server build VA1CCVARHEL01" has successfully completed.
```

Validation can also be confirmed by looking for an asterisk (*) next to the name of the server in the Control Portal.

![managed servers in control](../images/converting-unmanaged-virtual-machines-to-managed-11.png)
