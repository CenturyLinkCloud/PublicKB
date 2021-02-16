{{{
  "title": "Dedicated Cloud Compute Cloning",
  "date": "05-11-2017",
  "author": "",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Cloning Live Virtual Machine (“VM”) Instances and Cloning to Template

Dedicated Cloud Compute VM instances can be cloned. Lumen provides the client with two cloning options at this time, Clone Live VM Instance and a Save to Template function. Both of these functions automatically clone the primary boot volume and secondary volumes of a VM. Customer may not clone Lumen-managed applications, and may clone non- Lumen-managed applications at its own risk.

**Clone Live VM Instance**: Allows customers to actively replicate a running VM for use and deployment. An existing VM is shut down and cloned. The clone is stripped of its previous system identity or “prepped/sysprep” and redeployed as a new VM with similar characteristics as the original VM. When cloning a VM, customers have the option to change the CPU, RAM size, and IP Address of the clone, compared to the original VM.

**Clone to Template**: Allows customers to save a VM as a stored image or template for future use. An existing VM is cloned; the clone is stripped of its previous system identity or “prepped/sysprep” and stored in Lumen Image Management Storage repository. Customers can then deploy that image multiple times in the future, updating the CPU, RAM, and IP Address settings on the newly deployed VMs.
