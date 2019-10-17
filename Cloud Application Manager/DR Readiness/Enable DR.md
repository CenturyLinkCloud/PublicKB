{{{
  "title": "Enable DR",
  "date": "09-26-2019",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Enable DR](#enable-dr)

### Overview <a name="overview"></a>

This article is meant to assist users of Cloud Application Manager willing to use Disaster Recovery feature, trying to enable Disaster Recovery from CAM portal

### Audience <a name="audience"></a>

All users of Cloud Application Manager who wants to use Disaster Recovery feature.

### Prerequisites <a name="prerequisites"></a>

* A production server on CLC 
* An existing node pair

### Enable DR <a name="enable-dr"></a>

1. Navigate to the production windows server, click on **Enable DR**

![image](https://user-images.githubusercontent.com/20582531/65724457-ae30c680-e06d-11e9-9ee5-099dca8f5ff4.png)



2. Click on ** Start**

![image](https://user-images.githubusercontent.com/20582531/65724487-bdb00f80-e06d-11e9-8f90-ff22b48eecd8.png)

3. Check the box to approve the reboot then click on **Initiate Protection**

![image](https://user-images.githubusercontent.com/20582531/65724636-14b5e480-e06e-11e9-959b-c3c258aec9d1.png)

3. Fill in the detailed information of each Provider:
 * Decide the maximum servers to protect
 * Choose where to deploy your Prod node
 * Choose where to deploy your Recovery node
 * Click on Create

If you have additional questions, please [contact CLoud Application Manager Support](mailto:incident@CenturyLink.com)
