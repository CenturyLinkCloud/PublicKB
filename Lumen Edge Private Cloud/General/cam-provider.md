{{{
  "title": "Configuring a Provider for CAM",
  "date": "7-12-2021",
  "author": "Anthony Hakim",
  "keywords": ["cpc", "cloud", "vmware", "cam", "support", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

### Description
In this KB article, we walk through how to enable a Cloud Application Manager Provider for Lumen Private Cloud on VMware Cloud Foundation™.

### Prerequisites
* You must have a Cloud Application Manager Account.
* Your base URL, Organization, and user credentials for Lumen Private Cloud on VMware Cloud Foundation.
__Note:__ The Organization name is __case sensitive__.

### Steps

* Go to https://www.ctl.io/cloud-application-manager/ and Log In to your account. In the __Cloud Application Manager__ page, click on __Providers__ on the left side.

![CAM Provider](../../images/dccf/cam-provider1.png)

* Click __New__ and select __Lumen Private Cloud on VMware Cloud Foundation__ from the __Provider__ drop down list.

![CAM Provider](../../images/dccf/cam-provider2.png)

* Fill in the details:
  * __Name:__ Enter a name for the Provider.
  * __Description:__ (Optional).
  * __Enable Managed Services:__ Enable if you want Managed OS and Applications.
  * __URL:__ Your Base URL (example - https://S123456ch3a.vcf.ctl.io).
  * Organization: Your Organization (displayed in the top left corner when logged in to Lumen Private Cloud on VMware Cloud Foundation. If using VCD 9.5 or higher with the HTML5 UI, the organization will be displayed in the center towards the top of the screen). __Note:__ The Organization name is __case sensitive__.
  * __Username:__ Lumen Private Cloud on VMware Cloud Foundation user account.
  * __Password:__ Password for above account.

* Click __Save__.  

![CAM Provider](../../images/dccf/cam-provider3.png)

* The Provider will synchronize. Once completed, you can begin using Cloud Application Manager with Lumen Private Cloud on VMware Cloud Foundation.

![CAM Provider](../../images/dccf/cam-provider4.png)
