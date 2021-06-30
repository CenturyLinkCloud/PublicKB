{{{
  "title": "Adding to your Catalog",
  "date": "6-30-2021",
  "author": "John Grant",
  "keywords": ["cpc", "cloud", "vmware", "catalog", "ovf", "template", "vapp", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we show you the steps for adding a new catalog to your libraries in Lumen Private Cloud on VMware Cloud Foundation™. We also demonstrate how to add an Open Virtualization Format (OVF) Template to your Catalog. In addition, we also have step-by-step instructions on adding an Existing vApp to your Catalog. In this case, an existing vApp could consist of one or more VMs.

A catalog is a container for vApp templates and media files in an organization. Organization administrators and catalog authors within Lumen Private Cloud on VMware Cloud Foundation can create catalogs in an organization. Catalog contents can be shared with other users within Lumen Private Cloud on VMware Cloud Foundation.

Lumen Private Cloud on VMware Cloud Foundation contains organization (private) catalogs, and access to its public catalog. Organization catalogs include vApp templates and media files that you can share with other users in the organization.

### Steps to Adding a New Catalog

Create a catalog template by doing the following:

* Log in to your Lumen Private Cloud on VMware Cloud Foundation (LPC on VCF) environment.

  ![Login to Lumen Private Cloud on VMware Cloud Foundation](../../images/dccf/login-html5.png)

* Once logged in, click the Data Centers summary box.

  ![Catalog](../../images/dccf/data-centers-summary.png)

* Under __Compute__ in the side menu, select __vApps__.

  ![Catalog](../../images/dccf/catalog-create-template.png)

* Select the verticle ellipsis, and click __Create Template__.
* In the __Add to Catalog__ window, click __Select Catalog__, and then click the radio button for your catalog. 

Specify how the template should be created:
  - __Make Identical Copy:__ vApps that are created from this vApp template inherit the guest operating system settings specified in the template. If you select this option and guest customization is enabled, the guest operating system is personalized. IP addresses of the NICs in the template are reserved.
  - __Customize VM Settings:__ Guest operating system is personalized regardless of the vApp template settings when the template is instantiated. IP addresses of the NICs in the template are released.

* Select the radio button for __Make identical copy__ or __Customize VM settings__.
* Click __OK__.

![Catalog](../../images/dccf/catalog-select-catalog.png)

### Steps to add an OVF Template

* Click __Libraries__ in the top menu.

  ![Catalog](../../images/dccf/add-to-catalog2-html5.png)

* In the __Libraries__ page, click __NEW__ at the top of the vApp Templates screen.

  ![Catalog](../../images/dccf/add-to-catalog3-html5.png)

* In the __Create vApp Template from OVF__ window, either enter the __URL__ to the OVF, or __Browse...__ to the __Local file__, then click __NEXT__.

  ![Catalog](../../images/dccf/add-to-catalog4-html5.png)

* Review the details, then click __NEXT__. On the next screen (Select vApp Template Name) enter the __Name__ and optional Description, then select the catalog from the __Catalog__ dropdown.

  ![Catalog](../../images/dccf/add-to-catalog5-html5.png)

* The template will be shown in the template list and the progress of the upload will be shown in the __Recent Tasks__ pane at the bottom of the screen.

  ![Catalog](../../images/dccf/add-to-catalog6-html5.png)

* Once the vApp Template is successfully imported, it can be used to deploy VMs inside of Lumen Private Cloud on VMware Cloud Foundation.

### Steps to add an Existing vApp to your Catalog
In this example, we will work with the Engineering vApp to create a new vApp Template. If the vApp is running, it is added to the catalog as a vApp template with all of its VMs in a suspended state.

* Click __Data Centers__ in the top menu, and then click the Virtual Data Center summary box.
* In the left pane, click __vApps__. 
* Click the __Actions__ dropdown on the vApp and select __Add to Catalog...__.

  ![Catalog](../../images/dccf/add-to-catalog7-html5.png)

* Select the catalog to add the vApp to in the __Catalog__ dropdown. Select __Overwrite catalog item__ if you want the new catalog item to overwrite any existing vApp Template that has the same name. Type a __Name__ and optional Description for the vApp template.

* Click __OK__ to finish.

  ![Catalog](../../images/dccf/add-to-catalog8-html5.png)

  The vApp is saved as a vApp template and appears in the specified catalog.
