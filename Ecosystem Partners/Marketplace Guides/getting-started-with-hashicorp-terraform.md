{{{
  "title": "Getting started with Hashicorp Terraform",
  "date": "12-10-2015",
  "author": "ecosystem@centurylink.com",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
After reading this article, the user should be able to provision infrastructure with
[Hashicorp Terraform](https://terraform.io) on CenturyLink Cloud.

### Description

#### [Terraform](http://terraform.io)
<img src="../../images/ecosystem-hashicorp-terraform.png" style="border:0;float:right;max-width: 150px;">

Hashicorp Terraform – “Terraform provides a common configuration to launch infrastructure — from physical and virtual servers to email and DNS providers. Once launched, Terraform safely and efficiently changes infrastructure as the configuration is evolved.”

### Audience
Terraform users wishing to deploy to CenturyLink Cloud. Familiarity with infrastructure automation and the Terraform toolkit are required.

Full [documentation](https://www.terraform.io/docs/providers/clc/index.html) for using Terraform on CLC.

### Steps
1. Install Terraform.
   * [https://terraform.io/downloads.html](https://terraform.io/downloads.html)

2. Set Credentials.
   The plugin expects CLC credentials set either as env vars:

	`CLC_USERNAME`, `CLC_PASSWORD`

	Or via Terraform variables:
	```
		provider "clc" {
  			username = ""
			password = ""
            account = "" # optional
		}
   ```
    If an account is not provided, it will default to the user's primary account. A sub-account may also be specified.

3. Test.
	 Save the following into a file named `testing.tf`.
	 ```
		provider "clc" {
  			username = ""
			password = ""
		}

		resource "clc_group" "web" {
		  location_id = "WA1"
		  name = "TERRA"
		  parent = "Default Group"
		}

		resource "clc_server" "srv" {
		  name_template = "trusty"
		  source_server_id = "UBUNTU-14-64-TEMPLATE"
		  group_id = "${clc_group.web.id}"
		  cpu = 2
		  memory_mb = 2048
		}  	
   ```
	And then run

	`terraform plan`

	Terraform should report the execution plan it will lay down.

	`terraform apply`

  will execute the plan and provision cloud resources.

  Check out the full options available for VMs (and other resources) on the
    [official docs](https://www.terraform.io/docs/providers/clc/index.html)

4. Explore the examples.
   Additional example and resources:
   * [examples](https://github.com/CenturyLinkCloud/terraform-provider-clc/tree/master/examples) * basic use
   * [mantl.io](https://github.com/CiscoCloud/mantl/blob/master/terraform/clc.sample.tf) - mesos from terraform + ansible
   * [terraform.py](https://github.com/CiscoCloud/terraform.py) - dynamic inventory for ansible

5. Start Terraforming.
   Use the provided Terraform resources to build out your infrastructure.
