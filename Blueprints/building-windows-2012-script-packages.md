{{{
  "title": "Building Windows 2012 Script Packages",
  "date": "1-7-2015",
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
  "contentIsHTML": true
}}}

Building Windows 2012 Script Packages
<p>In order to facilitate knowledge of the CenturyLink Cloud platform this article will provide sample scripts for use on Windows 2012 Virtual Machines. Detailed information on script and software package management can be found in <a href="../Blueprints/blueprints-script-and-software-package-management.md">this KB</a>. </p>
<h3>Important Tools</h3>
<ul>
  <li><a href="http://www.somacon.com/p113.php">GUID Generator</a>; &nbsp;Each package.manifest created and uploaded must contain a unique UUID. This tools provides a way to quickly generate a new one for each package built. <strong>Users must change the GUID on each package posted below</strong>.</li>
  <li><a href="http://geekswithblogs.net/Wchrabaszcz/archive/2013/09/04/how-to-install-windows-server-features-using-powershel--server.aspx">Windows 2012 Roles</a>&nbsp;</li>
</ul>
<h3>Support Information</h3>
<p>Customers are responsible for building, testing and managing private or privateshared Script blueprints in their environment. </p>
<h3>Install Windows 2012 File Services</h3>
<p>This sample package installs&nbsp;File Server, BranchCache for Network Files, Data Deduplication, DFS Namespaces, DFS Replication, File Server Resource Manager, File Server VSS Agent Service &amp; Server for NFS.</p>
<p><strong>package.manifest</strong></p>
<code><pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;
  &lt;Manifest&gt;
  &lt;Metadata&gt;
  &lt;UUID&gt;18631bbe-b99d-11e3-9710-bf401d5d46b0&lt;/UUID&gt;
  &lt;Name&gt;Install File Services&lt;/Name&gt;
  &lt;Description&gt;File Server manages shared folders and enables users to access files on this computer from the network. Includes File Server, BranchCache, Data Deuplication, DFS Namespace, DFS Replication, Resource Manager, VSS Agent, Server for
  NFS.&lt;/Description&gt;
  &lt;/Metadata&gt;
  &lt;Parameters/&gt;
  &lt;Execution&gt;
  &lt;Mode&gt;PowerShell&lt;/Mode&gt;
  &lt;Command&gt;install-file-services.ps1&lt;/Command&gt;
  &lt;/Execution&gt;
  &lt;/Manifest&gt;
</code></pre>
<p><strong>install-file-services.ps1</strong>
</p>
<code><pre>Import-Module ServerManager
  <br />Install-WindowsFeature -Name FS-FileServer, FS-BranchCache, FS-Data-Deduplication, FS-DFS-Namespace, FS-DFS-Replication, FS-Resource-Manager, FS-VSS-Agent, FS-NFS-Service -IncludeManagementTools
</code></pre>
<h3>Install Windows 2012 Web Server</h3>
<p>This sample package includes base Web Server (IIS) features and administrative tools. </p>
<p><strong>package.manifest</strong>
</p>
<code><pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;
  &lt;Manifest&gt;
   &lt;Metadata&gt;
   &lt;UUID&gt;7E5D92AE-BA61-11E3-9B2D-142C1E5D46B0&lt;/UUID&gt;
   &lt;Name&gt;Install IIS Web Server&lt;/Name&gt;
   &lt;Description&gt;Web Server provides support for HTML Web sites and optional support for ASP.NET, ASP, and Web server extensions. You can use the Web Server to host an internal or external Web site or to provide an environment for developers to create
  Web-based applications.&lt;/Description&gt;
   &lt;/Metadata&gt;
   &lt;Parameters/&gt;
   &lt;Execution&gt;
   &lt;Mode&gt;PowerShell&lt;/Mode&gt;
   &lt;Command&gt;install-iis.ps1&lt;/Command&gt;
   &lt;/Execution&gt;
  &lt;/Manifest&gt;</code></pre>
<p><strong>install-iis.ps1</strong>
</p>
<code><pre>Import-Module ServerManager
  Install-WindowsFeature -Name Web-WebServer -IncludeManagementTools</code></pre>
<h3>Install Windows 2012 FTP Services</h3>
<p>This sample package includes the FTP service built into Windows 2012 Web Server (IIS).</p>
<p><strong>package.manifest</strong>
</p>
<code><pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;
  &lt;Manifest&gt;
   &lt;Metadata&gt;
   &lt;UUID&gt;70CD1FB0-BA61-11E3-9264-0F2C1E5D46B0&lt;/UUID&gt;
   &lt;Name&gt;Install FTP Server (IIS)&lt;/Name&gt;
   &lt;Description&gt;FTP Server enables the transfer of files between a client and server by using the FTP protocol. Users can establish an FTP connection and transfer files by using an FTP client or FTP-enabled Web browser.&lt;/Description&gt;
   &lt;/Metadata&gt;
   &lt;Parameters/&gt;
   &lt;Execution&gt;
   &lt;Mode&gt;PowerShell&lt;/Mode&gt;
   &lt;Command&gt;install-ftp.ps1&lt;/Command&gt;
   &lt;/Execution&gt;
  &lt;/Manifest&gt;</code></pre>
<p><strong>install-ftp.ps1</strong>
</p>
<code><pre>Import-Module ServerManager
  Install-WindowsFeature -Name Web-Ftp-Server -IncludeManagementTools -IncludeAllSubFeature</code></pre>
<h3>Install Windows 2012 Domain Services &amp; Create new Forest</h3>
<p>This sample package installs&nbsp;Active Directory Domain Services, DNS and promotes the VM to a Domain Controller. This script is designed to create the first DC in a new forest. </p>
<p><strong>package.manifest</strong>
</p>
<code><pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;
  &lt;Manifest&gt;
   &lt;Metadata&gt;
   &lt;UUID&gt;13533ffe-0615-11e4-b8b1-8b051e5d46b0&lt;/UUID&gt;
   &lt;Name&gt;Install Windows 2012 Active Directory Domain Services&lt;/Name&gt;
   &lt;Description&gt;Windows 2012 Active Directory Domain Services (AD DS) stores information about objects on the network and makes this information available to users and network administrators. AD DS uses domain controllers to give network users access
  to permitted resources anywhere on the network through a single logon process.&lt;/Description&gt;
   &lt;/Metadata&gt;
   &lt;Parameters&gt;
   &lt;Parameter Name="IP Address" Type="String" Variable="T3.Server.IPAddress" Prompt="None"/&gt;
   &lt;Parameter Name="Domain Name" Type="String" Regex="(?=^.{1,254}$)(?:^[A-Za-z](?:(?:[-A-Za-z0-9]){0,61}[A-Za-z0-9])?(?:\.[A-Za-z](?:(?:[-A-Za-z0-9]){0,61}[A-Za-z0-9])?)*$)" Variable="T3.install-ad.DomainName"/&gt;
   &lt;Parameter Name="Safe Mode Administrator Password" Type="Password" Variable="T3.install-ad.SafeModeAdminPassword"/&gt;
   &lt;/Parameters&gt;
   &lt;Execution&gt;
   &lt;Mode&gt;PowerShell&lt;/Mode&gt;
   &lt;RebootOnSuccess&gt;true&lt;/RebootOnSuccess&gt;
   &lt;Command&gt;install-ad.ps1 ${T3.Server.IPAddress} ${T3.install-ad.DomainName} ${T3.install-ad.SafeModeAdminPassword}&lt;/Command&gt;
   &lt;/Execution&gt;
  &lt;/Manifest&gt;</code></pre>
<p><strong>install-ad.ps1</strong>
</p>
<code><pre>$ipAddress = $args[0]
  $domainName = $args[1]
  $pass = $args[2]
Import-Module ServerManager
  Add-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
  Add-WindowsFeature -Name DNS -IncludeManagementTools
$safepass = ConvertTo-SecureString -AsPlainText -String $pass -Force
  Install-ADDSForest -DomainName $domainName -DomainMode Win2012 -ForestMode Win2012 -SafeModeAdministratorPassword $safepass -SysVolPath C:\Windows\SYSVOL -DatabasePath C:\Windows\NTDS -LogPath C:\Windows\NTDS -InstallDNS -Force</code></pre>
<h3>Perform Active Directory Domain Join on Windows</h3>
<p>This sample package joins a virtual machine to Active Directory. Note: &nbsp;This is functional for Windows 2008 R2.</p>
<p><strong>package.manifest</strong>
</p>
<code><pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;
  &lt;Manifest&gt;
   &lt;Metadata&gt;
   &lt;UUID&gt;{08DC3134-966B-11E4-B51F-4E2C1E5D46B0}&lt;/UUID&gt;
   &lt;Name&gt;Perform Active Directory Domain Join on Windows&lt;/Name&gt;
   &lt;Description&gt;Joins a server to the specified domain.&lt;/Description&gt;
   &lt;/Metadata&gt;
   &lt;Parameters&gt;
   &lt;Parameter Name="Domain User" Type="String" Variable="T3.join-domain.User"/&gt;
   &lt;Parameter Name="Password" Type="Password" Variable="T3.join-domain.Password"/&gt;
   &lt;Parameter Name="Fully Qualified Domain Name" Type="String" Variable="T3.join-domain.FQDN"/&gt;
   &lt;Parameter Name="NetBIOS Domain Name" Type="String" Variable="T3.join-domain.NetBIOSDomain"/&gt;
   &lt;/Parameters&gt;
   &lt;Execution&gt;
   &lt;Mode&gt;PowerShell&lt;/Mode&gt;
   &lt;Command&gt;join-domain.ps1 ${T3.join-domain.User} ${T3.join-domain.Password} ${T3.join-domain.NetBIOSDomain} ${T3.join-domain.FQDN}&lt;/Command&gt;
   &lt;/Execution&gt;
  &lt;/Manifest&gt;</code></pre>
<p><strong>join-domain.ps1</strong>
</p>
<code><pre>$user = $args[0]
  $password = ConvertTo-SecureString $args[1] -AsPlainText -Force
  $DomainName = $args[2]
  $credential = New-Object System.Management.Automation.PSCredential $DomainName\$user, $password
Add-Computer -DomainName $args[3] -Credential $credential</code></pre>
