{{{
"title": "Getting Started with Fortinet",
"date": "06-08-2016",
"author": "Bob Stolzberg",
"contentIsHTML": false,
"sticky": false
}}}

![Fortinet logo](../../images/fortinet-logo.jpg)

### Partner Profile

Fortinet -- Delivering High-Performance, Next-Generation Firewall to the Cloud

For additional information about the company please visit [http://www.fortinet.com](//www.fortinet.com)

### Contact Fortinet

**Fortinet Sales and Support:**

* 24x7 Web Support: [https://support.fortinet.com](//support.fortinet.com)
* 24x7 Phone Support: (866) 648-4638
* Sales Telephone Support: Please email [Dustin Warner, dwarner@fortinet.com](mailto:dwarner@fortinet.com) or call: (720) 838-7353

### Description

Fortinet has integrated their next-generation firewall (NGFW) technology with the CenturyLink Cloud platform. The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this high-performance firewall solution.

Each FortiGate virtual appliance ships with the broadest range of security and network technologies of any virtual appliance on the market today. And, because all of these technologies are included with the FortiGate-VM license, you have complete flexibility to deploy the right mix of technologies to fit your unique, virtualized environment and address your concerns about migrating data to the cloud.

FortiGate is now available as part of the CenturyLink Cloud Platform.

### Solution Overview

Each FortiGate-VM delivers the same comprehensive suite of consolidated, integrated security technologies as industry-leading FortiGate physical appliances. This suite includes:

* The latest NGFW technologies, such as: IPv4/IPv6 firewall, application control, and intrusion prevention, which deliver unmatched granular management and control of data, applications, users, and devices.
* Technologies to block today’s spear phishing attacks, APT's, and other targeted attacks such as anti-spam, antivirus, Web content filtering, and data leak prevention.
* Essential protection for remote users and offices such as VPN, endpoint protection, two-factor authentication, and vulnerability management.
* Core networking support, such as IPv4/IPv6 dynamic routing, WAN optimization, traffic shaping, and VoIP.

Fortinet’s network security product strategy is built around a multi-tenant architecture. Fortinet solutions have the breadth and depth to address securing data as it moves to, through, and outside of the cloud. By providing centrally-managed physical and virtual appliances that deliver the broadest range of network security solutions in the industry, Fortinet can help protect your critical data, from the customer to the cloud and back.

### Offer

Fortinet has provided their FortiGate Platform virtual appliance, known as a partner template, that can be deployed to your CenturyLink Cloud account via a Service Task. Although Service Tasks are ordinarily billed to the end user account, CenturyLink will provide a refund for the Service Task costs associated with deploying the Fortinet Partner Template. The process to request a refund can be found in this document. The FortiGate virtual appliance is sold via flexible licensing and packaging. We also have trial licenses available upon request. To receive pricing for your environment and/or receive a trial license please contact Fortinet sales: [Dustin Warner, dwarner@fortinet.com](mailto:dwarner@fortinet.com) or via telephone: (720) 838-7353.

### Audience

* CenturyLink Cloud Users, Security Administrators, Network Security, Operations Teams

### Impact

After executing the steps in this Getting Started guide, users will have a functioning FortiGate High Performance Next-Gen Firewall upon which they can quickly start securing workloads in the cloud.

The deployment process for partner templates currently requires manual interaction via the Service Task process, but will be further automated in future releases of the CenturyLink Cloud Platform.

If you are interested in seeing this type of partner template deployment as an automated feature in the future, please share your input with us at [features@ctl.io](mailto:features@ctl.io)

### Prerequisite

* Access to the CenturyLink Cloud platform as an authorized user.
* A Network VLAN for the Fortinet partner template to be deployed on.
* A FortiGate VM License.
    **Note:** You will need to send this to CenturyLink Support at the time of deployment. You should have obtained a license from FortiGate sales.

### Deploying, Accessing, and Configuring the Fortigate Partner Template

The Fortinet partner template deploys in a virtual appliance model, as a CenturyLink Cloud partner template.  Follow these step by step instructions to deploy a Fortinet Fortigate partner template in to your CenturyLink Cloud account.

1. Open a Service Task Request Ticket via an email to [ServiceTasks@ctl.io](mailto:ServiceTasks@ctl.io). Attach your Fortinet license to the email and include the following details in the email:

    * CenturyLink Cloud Account Alias
    * CenturyLink Cloud Account PIN
    * Data Center (to import the image to)
    * Server Name (to import the image as)
    * VLAN (to add the server to)
    * Additional Notes

    **Note:** You will need to edit some of the information in the example below.

    **Example Email**

 ```
    ----
    TO: ServiceTasks@ctl.io

    EMAIL SUBJECT: Ecosystem Partner Template Import Request

    CLC Support Team,

    Please create a ticket to import the Ecosystem Partner Template image referenced below to my CenturyLink Cloud Account:

    - Import CenturyLink Ecosystem Partner Source Image: Fortinet Fortigate
    - My CenturyLink Cloud Account Alias: ####
    - My CenturyLink Cloud Account PIN: ######
    - Data Center to import image to: ###
    - Server Name to import image as: FORT
    - VLAN in the account to add the Server to: vlan_####_#.#.#.#
    - Additional Notes or work to be done: None

    Please let me know if you have any questions or issues. Kindly send me a reply once the work has been completed and let us know the IP address of the server where this technology has been deployed.

    Thank you very much,

    Your_Name_Here

    -----
```

2. The suppport team will send you an email once the template has been deployed. This email will also contain the IP address of the server so that you can access the template.

    **Note:** When accessing your VM for the first time or for any administration, we recommend you connect to your CenturyLink Cloud environment via Client VPN.

3. Using a web browser, navigate to `https://server_ip_address`. (This can be the private IP if you are connected via VPN, or a Public IP if you added one and opened the proper firewall rules).

4. Log in with the newly-created administrator account.  The login will be supplied by the CenturyLink support team.

5. Once logged in, configure the High Performance Next-Gen Firewall by following the [FortiNet documentation](//support.fortinet.com).

**Note:** Refer to [http://support.fortinet.com](//support.fortinet.com) for additional how-to information. A FortiNet support user account is required (you can sign up for this on the site).

### Postrequisite

To access your Fortinet partner template over the internet, please perform the following tasks once your VM has been deployed to your account.

1. If required, [Add a Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through the Control Portal.

2. If required, [allow incoming traffic for the admin port](../../Network/how-to-add-public-ip-to-virtual-machine.md) by clicking on the Server's Public IP in the Control Portal.

    **Warning:** Please make sure your firewall rules are properly configured to only allow specific source traffic. If you do not configure source traffic rules you risk exposing your VM to the entire internet.

    **Note:** When accessing your VM for the first time or for any administration, we recommend you connect to your CenturyLink Cloud environment via Client VPN.

### Pricing

There are no Fortinet license costs included. The cost to deploy the Fortinet Partner Template will be billed as a Service Task, but CenturyLink will provide a credit for those costs. In order to receive a credit, please follow the instructions below. More information about Service Tasks and fees is [available here](//www.ctl.io/service-tasks).

### To Request a Credit for the Service Task Fee

Request a credit on your account to reimburse any expense to deploy the partner template.

Please copy and paste the email below and send it to [ecosystem@ctl.io](mailto:ecosystem@ctl.io).

```
----

TO: Ecosystem@CTL.io

EMAIL SUBJECT:   Requesting Credit for Fortinet Partner Template Deployment

CLC Ecosystem Team,

I am requesting a credit be placed on my account to cover the fees associated with deploying the Fortinet Partner Template to my account under the Service Task deployed on MM/DD/YYYY.  My CenturyLink Cloud username or account alias the credit needs to be placed on is ######

Thank you very much, your_name_here

----
```

### Frequently Asked Questions

**Q:** Where do I obtain my Fortinet License or entitlements?

**A:** Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Fortinet license, or contact Fortinet directly: Please email [Dustin Warner, dwarner@fortinet.com](mailto:dwarner@fortinet.com) or via telephone: (720) 838-7353.


**Q:** Who should I contact for support?

**A:**
* For issues regarding the Fortinet appliance, the application or functionality of it, please contact Fortinet via their 24x7 Web Support: [https://support.fortinet.com](//support.fortinet.com), or via Phone Support: (866) 648 4638.

* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new).
