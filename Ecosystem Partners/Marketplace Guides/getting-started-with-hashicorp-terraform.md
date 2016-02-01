{{{
  "title": "Getting started with Hashicorp Terraform",
  "date": "12-10-2015",
  "author": "albert.choi@ctl.io",
  "attachments": [],
  "contentIsHTML": false
}}}



### Overview

After reading this article, the user should be able to provision infrastructure with
[Hashicorp Terraform](https://terraform.io) on CenturyLink Cloud. 

### Description

#### [http://terraform.io](http://terraform.io)

<img src="../../images/ecosystem-hashicorp-terraform.png" style="border:0;float:right;max-width: 150px;">

Hashicorp Terraform – “Terraform provides a common configuration to launch infrastructure — from physical and virtual servers to email and DNS providers. Once launched, Terraform safely and efficiently changes infrastructure as the configuration is evolved.”


The CLC plugin enables the user to provision with terraform's declarative infrastructure language. 


Github repo: [https://github.com/CenturyLinkCloud/terraform-provider-clc](https://github.com/CenturyLinkCloud/terraform-provider-clc)


### Audience

Terraform users wishing to deploy to CenturyLink Cloud. Familiarity with infrastructure automation and the terraform toolkit are required. 

### Steps


1. **Install Terraform**

	Tested against terraform v0.6.8
  
	[https://terraform.io/downloads.html](https://terraform.io/downloads.html)


2. **Download the CLC Driver**

	See [installation](https://github.com/CenturyLinkCloud/terraform-provider-clc/#installation) options. 
	
	Recommended: download a pre-built binary from 
	[releases](https://github.com/CenturyLinkCloud/terraform-provider-clc/releases)
	

3. **Install the binary into your shell path**
	
	(strip the architecture extension) 
	
	```
	$ mv terraform-provider-clc.linux-amd64 $(dirname $(which terraform))/terraform-provider-clc
	$ chmod +x $(dirname $(which terraform))/terraform-provider-clc
	```
	

4. **Register the plugin**

	Create or modify your `~/.terraformrc` file. You'll need at least this:

	```
	providers {
	    clc = "/path/to/terraform-provider-clc"
	}
	```




5. **Set Credentials**

	The plugin expects CLC credentials set either as env vars: 
	
	`CLC_USERNAME`, `CLC_PASSWORD`, `CLC_ACCOUNT`
	
	
	Or via terraform variables: 
	
		provider "clc" {
  			username = ""
			password = ""
			account = ""
		}

6. **Test**

	Save the following into a file called `testing.tf`
	
		provider "clc" {
  			username = ""
			password = ""
			account = ""
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
		  password = "Green123$"
		}  	

	And then run 
	
	`terraform plan`
	
	If all goes well, terraform should report the execution plan it will lay down in 
	
	`terraform apply`

	
	

7. **Explore the examples**

	Additional [examples](https://github.com/CenturyLinkCloud/terraform-provider-clc/tree/master/examples) are included in the plugin repository. 
	
	

8. **Start terraform'ing**

	Use the provided terraform resources to build out your infrastructure. 

