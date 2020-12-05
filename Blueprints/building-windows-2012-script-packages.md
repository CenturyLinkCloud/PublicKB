{{{
  "title": "Building Windows 2012 Script Packages",
  "date": "2-24-2016",
  "author": "Chris Little",
  "attachments": [
    {
      "url":"../attachments/Install FTP (IIS).zip",
      "type":"application/zip",
      "file_name":"Install FTP (IIS).zip"
    },
    {
      "url":"../attachments/Install File Services.zip",
      "type":"application/zip",
      "file_name":"Install File Services.zip"
    },
    {
      "url":"../attachments/Install IIS (Web Server).zip",
      "type":"application/zip",
      "file_name":"Install IIS (Web Server).zip"
    },
    {
      "url":"../attachments/Install Windows 2012 Active Directory Domain Services.zip",
      "type":"application/zip",
      "file_name":"Install Windows 2012 Active Directory Domain Services.zip"
    },
    {
      "url":"../attachments/Perform Active Directory Domain Join on Windows.zip",
      "type":"application/zip",
      "file_name":"Perform Active Directory Domain Join on Windows.zip"
    }
  ],
  "contentIsHTML": false
}}}

### Overview
In order to facilitate knowledge of the Lumen Cloud platform this article will provide sample scripts for use on Windows 2012 Virtual Machines. Detailed information on script and software package management can be found in [our KB](../Blueprints/blueprints-script-and-software-package-management.md)

### Important Tools
* [GUID Generator:](http://www.somacon.com/p113.php) Each package.manifest created and uploaded must contain a unique UUID. This tools provides a way to quickly generate a new one for each package built. **Users must change the GUID on each package posted below.**
* [Windows 2012 Roles](https://technet.microsoft.com/en-us/library/hh831669.aspx)

### Support Information
Customers are responsible for building, testing and managing private or privateshared Script Blueprints in their environment.

### Install Windows 2012 File Services
This sample package installs File Server, BranchCache for Network Files, Data Deduplication, DFS Namespaces, DFS Replication, File Server Resource Manager, File Server VSS Agent Service Server for NFS.

**package.manifest**
```
<?xml version="1.0" encoding="utf-8"?>
  <Manifest>
  <Metadata>
  <UUID>18631bbe-b99d-11e3-9710-bf401d5d46b0</UUID>
  <Name>Install File Services</Name>
  <Description>File Server manages shared folders and enables users to access files on this computer from the network. Includes File Server, BranchCache, Data Deuplication, DFS Namespace, DFS Replication, Resource Manager, VSS Agent, Server for
  NFS.</Description>
  </Metadata>
  <Parameters/>
  <Execution>
  <Mode>PowerShell</Mode>
  <Command>install-file-services.ps1</Command>
  </Execution>
  </Manifest>
```

**install-file-services.ps1**
```
Import-Module ServerManager

Install-WindowsFeature -Name FS-FileServer, FS-BranchCache, FS-Data-Deduplication, FS-DFS-Namespace, FS-DFS-Replication, FS-Resource-Manager, FS-VSS-Agent, FS-NFS-Service -IncludeManagementTools
```

### Install Windows 2012 Web Server
This sample package includes base Web Server (IIS) features and administrative tools.

**package.manifest**
```
<?xml version="1.0" encoding="utf-8"?>
  <Manifest>
   <Metadata>
   <UUID>7E5D92AE-BA61-11E3-9B2D-142C1E5D46B0</UUID>
   <Name>Install IIS Web Server</Name>
   <Description>Web Server provides support for HTML Web sites and optional support for ASP.NET, ASP, and Web server extensions. You can use the Web Server to host an internal or external Web site or to provide an environment for developers to create
  Web-based applications.</Description>
   </Metadata>
   <Parameters/>
   <Execution>
   <Mode>PowerShell</Mode>
   <Command>install-iis.ps1</Command>
   </Execution>
  </Manifest>
```

**install-iis.ps1**
```
Import-Module ServerManager
  Install-WindowsFeature -Name Web-WebServer -IncludeManagementTools
```

### Install Windows 2012 FTP Services
This sample package includes the FTP service built into Windows 2012 Web Server (IIS).

**package.manifest**
```
<?xml version="1.0" encoding="utf-8"?>
  <Manifest>
   <Metadata>
   <UUID>70CD1FB0-BA61-11E3-9264-0F2C1E5D46B0</UUID>
   <Name>Install FTP Server (IIS)</Name>
   <Description>FTP Server enables the transfer of files between a client and server by using the FTP protocol. Users can establish an FTP connection and transfer files by using an FTP client or FTP-enabled Web browser.</Description>
   </Metadata>
   <Parameters/>
   <Execution>
   <Mode>PowerShell</Mode>
   <Command>install-ftp.ps1</Command>
   </Execution>
  </Manifest>
```

**install-ftp.ps1**
```
Import-Module ServerManager
  Install-WindowsFeature -Name Web-Ftp-Server -IncludeManagementTools -IncludeAllSubFeature
```

### Install Windows 2012 Domain Services and Create new Forest
This sample package installs Active Directory Domain Services, DNS and promotes the VM to a Domain Controller. This script is designed to create the first DC in a new forest.

**package.manifest**
```
<?xml version="1.0" encoding="utf-8"?>
  <Manifest>
   <Metadata>
   <UUID>13533ffe-0615-11e4-b8b1-8b051e5d46b0</UUID>
   <Name>Install Windows 2012 Active Directory Domain Services</Name>
   <Description>Windows 2012 Active Directory Domain Services (AD DS) stores information about objects on the network and makes this information available to users and network administrators. AD DS uses domain controllers to give network users access
  to permitted resources anywhere on the network through a single logon process.</Description>
   </Metadata>
   <Parameters>
   <Parameter Name="IP Address" Type="String" Variable="T3.Server.IPAddress" Prompt="None"/>
   <Parameter Name="Domain Name" Type="String" Regex="(?=^.{1,254}$)(?:^[A-Za-z](?:(?:[-A-Za-z0-9]){0,61}[A-Za-z0-9])?(?:\.[A-Za-z](?:(?:[-A-Za-z0-9]){0,61}[A-Za-z0-9])?)*$)" Variable="T3.install-ad.DomainName"/>
   <Parameter Name="Safe Mode Administrator Password" Type="Password" Variable="T3.install-ad.SafeModeAdminPassword"/>
   </Parameters>
   <Execution>
   <Mode>PowerShell</Mode>
   <RebootOnSuccess>true</RebootOnSuccess>
   <Command>install-ad.ps1 ${T3.Server.IPAddress} ${T3.install-ad.DomainName} ${T3.install-ad.SafeModeAdminPassword}</Command>
   </Execution>
  </Manifest>
```

**install-ad.ps1**
```
$ipAddress = $args[0]
  $domainName = $args[1]
  $pass = $args[2]
Import-Module ServerManager
  Add-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
  Add-WindowsFeature -Name DNS -IncludeManagementTools
$safepass = ConvertTo-SecureString -AsPlainText -String $pass -Force
  Install-ADDSForest -DomainName $domainName -DomainMode Win2012 -ForestMode Win2012 -SafeModeAdministratorPassword $safepass -SysVolPath C:\Windows\SYSVOL -DatabasePath C:\Windows\NTDS -LogPath C:\Windows\NTDS -InstallDNS -Force
```

### Perform Active Directory Domain Join on Windows
This sample package joins a virtual machine to Active Directory.

**package.manifest**
```
<?xml version="1.0" encoding="utf-8"?>
  <Manifest>
   <Metadata>
   <UUID>{08DC3134-966B-11E4-B51F-4E2C1E5D46B0}</UUID>
   <Name>Perform Active Directory Domain Join on Windows</Name>
   <Description>Joins a server to the specified domain.</Description>
   </Metadata>
   <Parameters>
   <Parameter Name="Domain User" Type="String" Variable="T3.join-domain.User"/>
   <Parameter Name="Password" Type="Password" Variable="T3.join-domain.Password"/>
   <Parameter Name="Fully Qualified Domain Name" Type="String" Variable="T3.join-domain.FQDN"/>
   <Parameter Name="NetBIOS Domain Name" Type="String" Variable="T3.join-domain.NetBIOSDomain"/>
   </Parameters>
   <Execution>
   <Mode>PowerShell</Mode>
   <Command>join-domain.ps1 ${T3.join-domain.User} ${T3.join-domain.Password} ${T3.join-domain.NetBIOSDomain} ${T3.join-domain.FQDN}</Command>
   </Execution>
  </Manifest>
```

**join-domain.ps1**
```
$user = $args[0]
  $password = ConvertTo-SecureString $args[1] -AsPlainText -Force
  $DomainName = $args[2]
  $credential = New-Object System.Management.Automation.PSCredential $DomainName\$user, $password
Add-Computer -DomainName $args[3] -Credential $credential
```
