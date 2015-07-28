{{{
"title": "Getting Started with Saratoga Data Flume - Blueprint",
"date": "4-27-2015",
"author": "Laurence Brevard and Bob Stolzberg",
"attachments": [],
"contentIsHTML": false
}}}

![Saratoga Data logo](../../images/ecosystem-saratoga-data-logo.png)

### Partner Profile
- Saratoga Data Systems, Inc. - Securely and accurately move your distributed data at unprecedented speeds
- [www.saratogadata.com](http://saratogadata.com/)

Customer Support:
- [support@saratogadata.com](mailto:support@saratogadata.com)
- 408-898-4307

Sales Support:
- [sales@saratogadata.com](mailto:sales@saratogadata.com)
- 408-898-4307

### Description
Saratoga Data Systems has provided their Flume accelerated file transfer technology on the CenturyLink Cloud platform.  The purpose of this KB article is to help the reader take advantage of this integration to achieve rapid time-to-value for this network and security solution.

Saratoga Data Systems helps CenturyLink Cloud customers address the business challenge of secure and reliable transmission of data over challenged networks by providing fast reliable file transfer using the flume client server software - now available as part of the CenturyLink Cloud Blueprint Engine.

### Solution Overview
![Saratoga Data Flume logo](../../images/ecosystem-saratoga-data-flume-logo.png)

Flume Network Optimization is a patented network protocol for transferring data that is unaffected by high latency and very resiliant in the face of errors and network interruption.

The 'flume' command line interface program implements this protocol wrapped in robust file management technology.

Data transmission is via a UDP data channel controlled and monitored by a separate TCP channel. By using UDP, 'flume' is able to transmit at full speed without the throttling effect on TCP caused by high latency and the requirement for each TCP data packet to be acknowledged before additional packets can be sent.

To achieve reliability with UDP, the TCP channel is used to indicate the need for replacement of missing or corrupted data. In addition to detecting packets have never arrived, two levels of CRC checksum are used for assurance that the data at the destination exactly matches that at the source.

In addition to the speed advantages of the protocol itself, the 'flume' program can optionally make use of additional technologies to reduce the actual amount of data transmitted:

1. Sending only files that have a changed date / time stamp
2. Sending only file differences ala rsync using the open source rsync library
3. Data compression using the standard open source zlib library

Flume can also optionally encrypt all communications using a selectable encryption technology provided via the open source Botan library.

A unique feature of Flume among file transfer programs is the ability to be used in a UNIX "pipe". This means that source data can come via 'stdin' and/or output can be to 'stdout'. If either of these modes is used at the remote location, Flume allows specification of what program is to run there to either: push data to 'stdin' or pull data from 'stdout'. See the Flume User Manual for more information on this feature.

### Offer
Saratoga Data is making their technology available for CenturyLink Cloud Users to deploy to their account.  Installation of the Flume Blueprint includes a license good for as much as two months (depending on the actual date of deployment). In order to purchase a license or entitlement, please contact [sales@saratogadata.com](mailto:sales@saratogadata.com)

### Audience
CenturyLink Cloud Users with high latency, challenged links, especially remote locations and via satellite-based connections.

### Impact
After reading this article, the user should feel comfortable getting started using the partner technology on CenturyLink Cloud.

After executing the steps in this Getting Started document, the users will have a functioning Linux operating system that includes the 'flume' software.

### Prerequisite
- Access to the CenturyLink Cloud platform as an authorized user.
- Identify a Network VLAN you want the Saratoga Data servers to reside on
- Possess a Flume license key

### Postrequisite
- If you want to access your VM over the internet, please perform the following tasks once you receive an email confirming you Blueprint completed successfully:

1. If you need to connect to your server via the Internet, Add a [Public IP](../../Network/how-to-add-public-ip-to-virtual-machine.md) to your server through Control Portal. Alternatively, you can [setup a VPN using OpenVPN](../../Network/how-to-configure-client-vpn.md) or similar technology.

2. [Allow incoming traffic](../../Network/how-to-add-public-ip-to-virtual-machine.md) for desired ports by clicking on the Servers Public IP through Control Portal. The ports used by 'flume' are controlled by a configuration file /etc/flume/ports but the standard ports to open are:
* TCP 22, 2354-2454
* UDP 2355-2454


### Install Flume Blueprint
1. Locate the Flume Blueprint
2. Starting from the CenturyLink Control Panel, navigate to the Blueprints Library and search for “Flume” in the keyword search on the right side of the page.
3. Locate the 'Install Flume File Transfer on Linux' Blueprint.
4. Choose and Deploy the Blueprint. Click the “Install Flume File Transfer on Linux” Blueprint.
5. Configure the Blueprint using the standard information.  There is nothing special required.
6. Review and Confirm the Blueprint.
7. Click “next: step 2”
8. Verify your configuration details.
9. Deploy the Blueprint.
10. Once verified, click on the ‘deploy blueprint’ button. You will see the deployment details along with an email stating the Blueprint is queued for execution.
11. This will kick off the blueprint deploy process and load a page to allow you to track the progress of the deployment.
12. Monitor the Activity Queue.
* Monitor the Deployment Queue to view the progress of the blueprint.
* You can access the queue at any time by clicking the Queue link under the Blueprints menu on the main navigation drop-down.
* Once the blueprint completes successfully, you will receive an email stating that the blueprint build is complete. Please do not use the new server until you have received this email notification.

### Accessing your Saratoga Data Flume Server
Access your Saratoga Data Flume server by connecting to the server via ssh to the public IP using root and the password created when deploying the blueprint.

* The flume data transfer program is invoked using the command line.
* For instruction on using Flume see the User Manual present on the newly created server. It is also available at [ftp://public.saratogadata.com/pub/sw/flume_2.3/Flume_2.3_User_Manual.pdf](ftp://public.saratogadata.com/pub/sw/flume_2.3/Flume_2.3_User_Manual.pdf)

You can also access a simple 'man' page with:
man flume

Or get integrated help using:
flume --help

For example to push data to another system (which must also have flume installed:
flume --source_file(s) --remote-host-name-or-ip:/remote/file/system/directory/

### Pricing
The costs associated with this Blueprint deployment are for the CenturyLink Cloud infrastructure only.  There are no Saratoga Data Flume license costs or additional fees bundled in.

### Frequently Asked Questions

#### Where do I obtain my Saratoga Data License or entitlements?
Existing CenturyLink Enterprise Customers can contact their Account Representative for help obtaining a Saratoga Data license, or contact Saratoga Data directly:
- via Email: [sales@SaratogaData.com](mailto:sales@SaratogaData.com)
- via Phone: 1-408-898-4307

#### Who should I contact for support?
* For issues related to deploying the Blueprint, licensing, Accessing or using the Saratoga Data application, please visit the [Saratoga Data Support Website](http://www.SaratogaDataSystems.com/support)
* For issues related to cloud infrastructure (VM’s, network, etc), or is you experience a problem deploying the Blueprint, please open a CenturyLink Cloud Support ticket by emailing [noc@ctl.io](mailto:noc@ctl.io) or [through the support website](https://t3n.zendesk.com/tickets/new)
