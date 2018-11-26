{{{
  "title": "How To:  Create Customer Specific OS Templates",
  "date": "6-6-2016",
  "author": "Chris Little",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Overview

CenturyLink Cloud customers may choose to create their own baseline OS templates for deployment within the Control Portal. These templates may include customization, software packages, security templates or other components. Customers should take care to test and validate the packages or changes being applied, to ensure that the OS instance functions properly after the template process is complete. Customers are responsible for this validation and ongoing support of changes made to OS Templates.

### Exclusions

* The Convert to Template option is unsupported for customers who leverage virtual machines with the multi-vNIC feature
* Text files stored on user's Desktops will NOT be carried over in the Clone if they are stored on the C Drive of a windows virtual machine

### Important Notices

**_DO NOT RUN THE CONVERT TO TEMPLATE FUNCTION ON A PRODUCTION/LIVE VIRTUAL SERVER_**. Customers should create a virtual instance with their specific configurations on a non-production virtual instance. The convert to template function actually modifies and moves the virtual machine to the templates group.

Customers creating OS Templates for Windows Servers should carefully review the [Microsoft Sysprep for Server Roles TechNet Article](//msdn.microsoft.com/en-us/windows/hardware/commercialize/manufacture/desktop/sysprep-support-for-server-roles). Sysprep is a component of creating an OS Template and as such certain OS Roles are not supported in both the template or clone process. **_For Windows Servers the CenturyLink Cloud Platform performs the sysprep function on behalf of customers when using the Convert To Template feature._**

### Steps

1. Use the [Create Server](../Servers/creating-a-new-enterprise-cloud-server.md) Control Portal function to deploy a baseline operating system supported on the CenturyLink Cloud platform. Alternatively, customers can elect to import a server template in the form of an OVF file. If the image to import meets the [requirements for self-service VM import](../Servers/self-service-vm-import-ovf-requirements.md), this can be done by following the steps outlined in [Using Self-Service VM Import](../Servers/using-self-service-vm-import.md). Otherwise, CenturyLink Cloud provides [service tasks](//www.ctl.io/products/support/service-tasks) to perform custom imports and customers can engage this group for fees.

2. Login to the newly created OS Instance and apply the customization or packages that should be part of the Template. We recommend after all changes are made a clean reboot of the OS prior to proceeding to step #3.

3. Navigate to the Server Instance built in step #1 in the Control Portal. Select the Convert to Template button under the Action Menu.

    ![Select Convert to Template](../images/how-to-create-customer-specific-os-templates-01.png)

4. Using the convert to template user interface input details about the template you wish to create.

    - Source Server Admin/Root Password:  The administrative password for the source VM
    - Template Description: The description is how you will identify your template when creating new servers
    - Publish Settings: Allows customers to define where the template is displayed. Customers with sub accounts can choose to permit access to this template using the Private Shared function.

      ![Convert to template UI](../images/how-to-create-customer-specific-os-templates-02.png)

5. The Convert to Template task can be tracked via the Queue

    ![Queue for Job](../images/how-to-create-customer-specific-os-templates-03.png)

6. Once the Convert to Template job is complete customers can test the deployment of the new template by using the Create Server function. The Template Description defined previously should be visible in the Operating System pull down menu.

    ![Deploy Template](../images/how-to-create-customer-specific-os-templates-04.png)

### FAQ

**Q: I've created a custom template in Data Center A, but when I try to create a VM from the template in Data Center B it's not showing?**

A: Customer created templates do not replicate to all data centers out of the box today. If you need templates copied to other data centers within the same account alias please [open a support request](../Support/how-do-i-report-a-support-issue.md).  Copying templates to a different account alias will incur a [VM Transfer](https://www.ctl.io/service-tasks/#vm-transfer) fee.

**Q: I've created a custom template in my account, but when I try to create a VM from the template in my _sub_ accounts, it's not showing?**

A: Make sure that when you perform the convert to template function that you are selecting the "Private Shared" option described in step 4 above. This setting allows customers to permit access to this template from sub accounts as well.

**Q: What fees are associated with use of custom OS templates?**

A: Templates are stored in a group called 'Templates' within the server groups area of Control. Template storage is billed on a per GB basis as Standard Storage. Rates are available from your Sales Representative. 

**Q: What format should my virtual machine use if I choose to leverage  self-service import?**

A: Self-service import requires the use of the OVF format for importing. See the [requirements for self-service VM import](../Servers/self-service-vm-import-ovf-requirements.md) for more information.
