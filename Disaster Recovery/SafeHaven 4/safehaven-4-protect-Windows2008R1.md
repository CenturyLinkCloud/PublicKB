{{{
  "title": "SafeHaven 4: Protect Windows Server 2008R1",
  "date": "2-11-2016",
  "author": "Shi Jin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Important Notes

The official support of Windows Server 2008R1 was discontinued since the release of SafeHaven-3.1.1 in December, 2015. This document provides a good-will method for customers to get SafeHaven Disaster Recovery as a Servce(DRaaS) protection on their legacy servers still running Windows Server 2008R1. Customers are strongly advised to upgrade to a newer server OS instead of keep running this legacy Windows server 2008R1 OS. Use this document only if there is absolutely no other options.

Also please note that **only 64bit** Windows 20008R1 is supported. The 32bit Windows 2008R1 is not supported.

### What's the Same as for Supported OS

* Creating a protection group using SafeHaven-4 just the same way for any supported Windows OS
* The DR operations such as failover/test-failover/failback are exactly the same

### What's Different from the Supported OS?

#### Special Windows Local Replication Agent Binary

The Windows Local Replication Agent (LRA) for Windows server 2008R1 needs some special treatment from Windows server 2008R2 or later OSes because there are certain Windows APIs not available.

The URL to download this special build is: https://d17b4h8tf54deh.cloudfront.net/SH-4.0.0/safehaven_windows_driver_win2008r1.exe


Also please note that this method does not support automated LRA installation. Only manual instllation is supported for Windows 2008R1

#### LRA Installation

##### Install Prerequisite: PowerShell v2

Before installing LRA, we have to get powershell v2 installed. If you already have powrshell v2 installed, you can skip this step. Note that Powershell v1 is not sufficient for this use case



* Open Server Manager and natigate to Features->Add Features
* Download and install Powershell v2 from https://www.microsoft.com/en-ca/download/details.aspx?id=20430. Specifically, it installs a Windows update named **KB968930**
* A server restart is required after the powershell v2 installation: it may take some time since it goes through the Windows update procedure
* Confirm the powershell version by running this command in powershell

```
Windows PowerShell
Copyright (C) 2009 Microsoft Corporation. All rights reserved.

PS C:\Users\Administrator> get-host


Name             : ConsoleHost
Version          : 2.0
InstanceId       : 287d5f86-2d4e-42ba-a475-5ec36c926a14
UI               : System.Management.Automation.Internal.Host.InternalHostUserInterface
CurrentCulture   : en-US
CurrentUICulture : en-US
PrivateData      : Microsoft.PowerShell.ConsoleHost+ConsoleColorProxy
IsRunspacePushed : False
Runspace         : System.Management.Automation.Runspaces.LocalRunspace
```

##### Driver Installation

* Once the LRA installation exe is downloaded, launch it from a cmd.exe (for a unknown reason, double clicking the EXE does not work during our tests)
* The rest of installatino is similar to supported OSes. In the end, a reboot is required.

##### Start Replication with Manager.exe

Lanuch Manager.exe the same way as for supported OSes. The only difference is on the page choosing the mapping between source and destination disks
* For supported OSes, the uninitialized disks are hidden from the source disk column
* For Win2008R1, since the concept of initialized/uninitialized disk does not exist, no such filtering would be done.

Note that a similar behavior is observed in the InbandToOutofbandConverter.exe
