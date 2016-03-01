{{{
  "title": "IPS - Centurylink Dedicated Cloud Compute (DCC) FAQ",
  "date": "02-22-2016",
  "author": "Client-Security",
  "attachments": [],
  "contentIsHTML": false,
  "sticky": false
}}}
        
### FAQ for Installing and Implementing IPS Anywhere for CenturyLink Dedicated Cloud Compute (DCC)
        
This document is intended to summarize (aka Quick Start) the installation and notification configuration steps for CLC’s IPS “Anywhere” service as derived from the services public KBs.  
        
### Pre-Requisites 
  * Compatible server OS 
    * IPS supports all Managed DCC OS Images at this time
    * Supported OSs KB: https://www.ctl.io/knowledge-base/security/supported-ips-oses/
  * Firewall Rules
  * Centurylink Cloud Account

KB: https://www.ctl.io/knowledge-base/security/getting-started-with-ips/#prerequisites 
        
### Installing IPS on Target Server
        
The IPS “Anywhere” install requires 1-2 command lines to initiate the install of the servers IPS agent and automatically handles all of the backend configurations behinds the scenes.   
        
KB: https://www.ctl.io/knowledge-base/security/ipsanywhere/
        
Run below command in a terminal session on target server:
  * Linux-based Operating Systems
> * curl https://api.client-security.ctl.io/ips/scripts/install.sh | sudo CLC_USERNAME=<your.clc.username> CLC_PASSWORD=<your.clc.password> CLOUD_PROVIDER= CTL_DCC bash

  * Windows-based Operating Systems
> * Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
> * (New-Object System.Net.WebClient).DownloadFile("https://api.ts.client-security.ctl.io/ips/scripts/install.ps1","$env:temp\install.ps1") ; cd $env:temp ; .\install.ps1 -controlUser "<your.clc.account>" -controlUserPassword "<your.clc.password>" -accountAlias "<your.clc.account,alias>" -cloudProvider "CTL_DCC"
> * Note: for the user input, you will need to enclose the data in “”.  For example, if your username was testuser, for the option of -controlUser "<your.clc.account>", you would use -controlUser "test user”.

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
    * Linux-Based OSes: https://vimeo.com/155560998 
    * Windows-Based OSes: TBD
  * Demonstration about Why IPS is needed in addition to Anti-Virus: https://www.ctl.io/blog/post/anti-virus-is-not-enough/
