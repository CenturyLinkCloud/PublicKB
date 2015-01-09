{{{
  "title": "Windows Firewall Settings Blocking FTP Site Access on a Windows Server",
  "date": "12-30-2013",
  "author": "Dave Burkhardt",
  "attachments": []
}}}

<p>In the event you are unable to establish a FTP connection on a newly provisioned FTP site using Microsoft's Publishing Service for IIS 7.0 or 7.5, the likely culprit is that you are utilizing the Windows Firewall service, and you will need to configure
  your Windows Firewall settings to allow FTP traffic to pass.</p>
<p>The following article describes the steps to enable this traffic and the configurations options to consider before you allow access:
  <br />http://www.iis.net/learn/publish/using-the-ftp-service/configuring-ftp-firewall-settings-in-iis-7</p>