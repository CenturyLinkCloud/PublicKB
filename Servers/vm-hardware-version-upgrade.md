{{{
	"title": "Virtual Machine Hardware Version Upgrade",
	"date": "05-24-2018",
	"author": "Matt Schwabenbauer",
	"attachments": [],
	"related-products" : [],
	"contentIsHTML": false,
	"sticky": true
}}}

### Description
On May 23, 2018, CenturyLink Cloud upgraded the Virtual Machine (VM) hardware version for all VMs in each of our public cloud service locations. This upgrade was released in order to apply guest-level protection from the Meltdown and Spectre security vulnerabilities.

### Applying the update

In order for the update to take effect, all VMs in each CenturyLink Cloud service location will need to be issued a shut down command followed by a power on command. Customers may issue the "Shut Down" server power operation from the Control Portal or API, followed by the "On" server power operation to apply the update.

NOTE: VMs running Windows Operating Systems must upgrade their VMware Tools before following the subsequent steps to complete this update. Instructions on updating the VMware Tools for VMs in CenturyLink Cloud can be [found here](https://www.ctl.io/knowledge-base/servers/self-service-updates-of-vmware-tools/)

Alternatively, the shut down command can be initiated from a VM Operating System directly, followed by the "On" server power operation from the Control Portal or API. Issuing a "Reboot" server power operation or an Operating System-level reboot command will not cause the update to take effect, since the VM must be completely powered off. There is no minimum amount of time a VM needs to remain in a powered off state in order for the update to take effect.

For more information about CenturyLink Cloud server power operations, please review [this guide](https://www.ctl.io/guides/servers/server-power-operations/).

Customers may also use the "Reset" or "Power Off" followed by "Power On" server power operations from the CenturyLink Cloud Control Portal or API to apply the update. These power operations force a VM to power off, similar to switching off the power on a physical computer. The "Reset" or "Power Off" server power operations should only be used in the event that a shut down command is unable to properly power off a VM.

### Checking the VM hardware version

After the update has been applied to a VM, it will be running VM hardware version 11.

To check the VM hardware version from a VM running Windows, run the following commands from a remote Powershell session connected to the VM or from the command prompt or Powershell console on the VM directly:

```
cd C:\Program Files\VMware\VMware Tools\
VMwareToolboxCmd.exe -v
```

To check the VM hardware version from a VM running a Linux Operating system, run the following command from a terminal SSH session connected to the VM:

```
vmware-toolbox-cmd -v
```

### More Information

Customers should not expect any change to the regular operation of their VMs after the update has been applied. This update will not make any Operating System or application-level changes.

Application of this update is not mandatory and there is no deadline for completion. Customers may initiate the shut down and power on commands at any time that is convenient.

While this update is not mandatory, CenturyLink Cloud recommends that this update is applied as soon as possible in order to benefit from guest-level protection against the Meltdown and Spectre security vulnerabilities. We also recommend that customers apply any Operating System or application-level patches that may be available to protect against these vulnerabilities.

Patches to protect against the Meltdown and Spectre security vulnerabilities have already been applied across all CenturyLink Cloud service hosting infrastructure.

More information about the Meltdown and Spectre security vulnerabilities can be found [here](https://www.netformation.com/featured/notice-on-meltdown-and-spectre-vulnerability/).

If you would like more information, please submit a ticket or contact our support team by e-mailing help@ctl.io.
