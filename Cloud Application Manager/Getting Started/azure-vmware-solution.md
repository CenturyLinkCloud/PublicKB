{{{
  "title": "Azure VMware Solution",
  "date": "08-26-2021",
  "author": "Randy Wansing",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Microsoft, in partnership with VMware, created a new solution tht would extend your current on-prem VMware instance into a VMware instance located in a Microsoft Datacenter.  These datacenters are located in multiple regions across the world.  Lumen's Cloud Application Manager along with Lumen's Managed Services Anywhere offering can mange the Azure VMware Solution for you.

### Audience

All Cloud Application Manager users who want to get their virtual machines deployed directly to the underlying provider or with any other deployment management tool to be automatically registered in Cloud Application Manager.

### Prerequisites

* Access to Cloud Application Manager [Management site](https://account.cam.ctl.io/#/providers).
* The user must have access to an already configured [provider](../Core Concepts/providers.md) in Cloud Application Manager, that supports the self-registration of virtual machines.
* Access to the underlying cloud provider account with authorization to deploy virtual infrastructure.

### Configuration
In order to do this step you have to already have an active Azure VMware Solution instance in your Azure subscription
- If you don't have one:
 - Go to your Azure Portal
  - Click on Resources
  - Search for Azur VMware Solution
  - Click on Learn More
  - Follow the instructions provided
- If you have an active Azure VMware Subscription and is already connected to your on-prem VMware Instance:
 - Logged into Cloud Application Manager
 - Under Management click on Providers
 - Click on New at the top
 - Select VMWare vCenter
  - Provide a Name
  - Add the Endpoint URL
  - Give Username
  - Give Password
  - Accept self-signed certificate
   - Only do this if you want to skip verfication of SSL Certificate when connecting to an HTTPs endpoint.

### Enable Managed Services Anywhere
- Click on your VMware vCenter Provider
- Go to the Services tab
- Click the Edit button for Managed Services
- Follow on screen instructions


### Contacting Cloud Application Manager Support

We’re sorry you’re having an issue in [Cloud Application Manager](https://www.ctl.io/cloud-application-manager/). Please review the [troubleshooting tips](../Troubleshooting/troubleshooting-tips.md), or contact [Cloud Application Manager support](mailto:incident@CenturyLink.com) with details and screenshots where possible.

For issues related to API calls, send the request body along with details related to the issue.
