{{{
  "title": "Adding a New Organization Administrator",
  "date": "6-18-2021",
  "author": "John Grant",
  "keywords": ["cpc", "cloud", "vmware", "admin", "vcloud", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we demonstrate how to add a new user as an OrgAdmin to your VCD organization. When a new user is set up as an OrgAdmin, they have the ability to use the VMware Cloud Director Web Console, tenant portal, or vCloud OpenAPI to manage users and groups in their organization and assign them roles, including the predefined __Organization Administrator__ role.

### Steps to Add a New User as an Org Admin

* Log in to your Lumen Private Cloud on the VMware Cloud Foundation (LPC on VCF) environment.

  ![Login to Lumen Private Cloud on VMware Cloud Foundation](../../images/dccf/login-html5.png)

* Once logged in, select __Administration__ in the top menu.

  ![Catalog](../../images/dccf/adding-org-admin1.png)

* On the Users page, click __NEW__ to add a new user.

  ![Catalog](../../images/dccf/adding-org-admin2.png)

* A __Create User__ window will pop up. Type the user's credentials and password, then be sure "Enable" is checked to activate the user account. In the __Available roles__ dropdown menu, select __Organization Administrator__. Continue filling out the user's contact info if needed. Please note, only fields with a red asterisk are required. When finished, click __SAVE__.

   ![Catalog](../../images/dccf/adding-org-admin3.png)

* The new user will appear in the user list.

### Steps to Make an Existing User an Org Admin

* Log in to your Lumen Private Cloud on the VMware Cloud Foundation environment.

  ![Login to Lumen Private Cloud on VMware Cloud Foundation](../../images/dccf/login-html5.png)

* Once logged in, select __Administration__ in the top menu.

  ![Catalog](../../images/dccf/adding-org-admin1.png)

* On the Users page, select the user who's role you need to change from the list, then click __EDIT__.

  ![Catalog](../../images/dccf/adding-org-admin4.png)

* In the __Available Roles__ dropdown menu, select __Organization Administrator__. Then click __SAVE__.

  ![Catalog](../../images/dccf/adding-org-admin5.png)
