{{{
  "title": "IPS - Centurylink Public Cloud on VMware Cloud Foundation FAQ",
  "date": "06-06-2018",
  "author": "Client-Security",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}
        
### FAQ for Installing and Implementing IPS Anywhere for CenturyLink Public Cloud on VMware Cloud Foundation
        
This document is intended to summarize (aka Quick Start) the installation and notification configuration steps for CLC’s IPS “Anywhere” service as derived from the service's public KBs.  
        
#### Pre-Requisites 
  * Compatible server OS 
    * IPS supports all Managed CenturyLink Public Cloud OS Images at this time
    * Supported OSs KB: https://www.ctl.io/knowledge-base/security/supported-ips-oses/
  * Firewall Rules
  * Centurylink Cloud Account
  * Admin or SUDO/root server privileges

KB: https://www.ctl.io/knowledge-base/security/getting-started-with-ips/#prerequisites 
        
### Installing IPS on Target Server
        
The IPS “Anywhere” install requires 1-2 command lines to initiate the install of the servers IPS agent and automatically handles all of the backend configurations behinds the scenes.   
        
KB: https://www.ctl.io/knowledge-base/security/ipsanywhere/
        
##### Content Properties

| Name | Type | Description | Req. |
| --- | --- | --- | --- |
| CLC_USERNAME | string | Control Portal user name value | Yes |
| CLC_PASSWORD | string | Control Portal password value. | Yes |

#### Linux-based Operating Systems

##### Content Example

    CLC_USERNAME=TestUser
    CLC_PASSWORD=YourPassword

##### Install Command

    curl https://api.client-security.ctl.io/ips/scripts/install.sh | sudo CLC_USERNAME=<your.clc.username> CLC_PASSWORD=<your.clc.password> CLOUD_PROVIDER=CTL_DCC bash


#### Windows-based Operating Systems

##### Content Example

    CLC_USERNAME="TestUser"
    CLC_PASSWORD="YourPassword"

##### Set Server to Accept Install

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

##### Install Command 

    (New-Object System.Net.WebClient).DownloadFile("https://api.ts.client-security.ctl.io/ips/scripts/install.ps1","$env:temp\install.ps1") ; cd $env:temp ; .\install.ps1 -controlUser "<your.clc.account>" -controlUserPassword "<your.clc.password>" -accountAlias "<your.clc.account,alias>" -cloudProvider "CTL_DCC"



### Notifications
There are two ways to  set/update IPS event notifications.  The first is to send a request to help@ctl.io for the Client Security Team and the second is to send a request to the IPS API directly.  

If sending an email, send the following data as needed:
  * The servers to update the notification on
  * The email addresses or email addresses to send notifications to. 
  * The WebHook URL to send notifications to.  NOTE: There can only be 1 WebHook setup.
  * The syslog server to forward event data to.  NOTE: There can only be 1 syslog server setup.

The full documentation for the IPS API is documented in the KB link listed below.  Examples of how to request each of the notification mediums (Email, Slack, Webhook, & Syslog) are reviewed.   

  * IPS API KB: https://www.ctl.io/knowledge-base/security/ips-api/

### Additional KBs and Links
  * Product Details: https://www.ctl.io/intrusion-prevention-service/

  * KB Repository (All of CLC’s IPS KBs, current and future, can be found in our KB repository):  https://www.ctl.io/knowledge-base/security/#1
  * Videos to help with Installation
    * Linux-Based OSes: https://vimeo.com/156468735 
    * Windows-Based OSes: https://vimeo.com/156470065 
  * Demonstration about Why IPS is needed in addition to Anti-Virus: https://www.ctl.io/blog/post/anti-virus-is-not-enough/
