{{{
  "title": "How To Configure Client VPN",
  "date": "12-23-2014",
  "author": "jw@tier3.com",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Overview</h3>
<p>Client VPN enables users to connect to their secure isolated network. Each account has their own isolated VPN service that is provided at no charge. This service is built into the platform and managed by the network operation center. If you have any issues
  please&nbsp;contact support.</p>
<p>The initial configuration just requires a certificate to be downloaded and used when connecting to the vpn service but you can also do two-factor authentication where it requires a user name and password which below there is a configuration guide on this.
  To learn more about ways to connect such as persistent vpn connections, direct connections please go <a href="http://help.tier3.com/entries/20518933-network-access-options-for-connecting-to-tier-3-s-platform">here</a>.</p>
<h3>Current Limitations</h3>
<p>There are only a few limitations on this service as it is based on the <a href="http://www.openvpn.net">OpenVPN</a> project.</p>
<ul>
  <li>Maximum Concurrent Users: 19 (if you need more than that please use <a href="http://www.centurylinkcloud.com/products/support/service-tasks">service tasks</a>)</li>
  <li>Maximum Connection: 1Gbps&nbsp;</li>
</ul>
<h3>Getting Connected</h3>
<p>Our platform is built to be very efficient with resources which means that the Client VPN service will <strong>not be activated</strong> until after you build your first server. So first step is to <strong>make sure you deploy a server to be able to have your VPN server activated</strong>.</p>
<p><em><strong>From the Control Panel go to: Network &gt; VPN to be able to download the certificate and configuration file.</strong></em>
</p>
<p>Windows XP:</p>
<ol>
  <li>Download the OpenVPN client&nbsp;<a href="http://openvpn.net/index.php/open-source/downloads.html">here</a>. (We recommend 2.3.2 for Windows Users)</li>
  <li>Accept all the defaults during installation.</li>
  <li>After installing the client, download the certificate from the VPN page and extract the .ZIP file into the ‘config’ subdirectory under your client install location (generally C:\Program Files\OpenVPN).</li>
  <li>Start the OpenVPN GUI. This will place an icon in the notification area, right click it and choose connect.</li>
</ol>
<div>
  <p>Windows 7 Installation Instructions:</p>
  <ol>
    <li>Point your browser to <a href="http://openvpn.net/index.php/open-source/downloads.html">here</a>, download the “exe” file next to the “Windows Installer” option.&nbsp;(We recommend 2.3.2 for Windows Users)</li>
    <li>Find where you downloaded the OpenVPN Windows Installer, right-click on the file, and then choose Run as an administrator (XP users can just double click on the file to start the installation).</li>
    <li>Accept all the defaults during installation.</li>
    <li>After installing the client, download the certificate from the VPN page and extract the .ZIP file into the ‘config’ subdirectory under your client install location (generally C:\Program Files (x86)\OpenVPN\config. Whereas for Windows XP users, the
      directory structure is: C:\Program Files\OpenVPN\config ).</li>
  </ol>
  <p>Running the OpenVPN client with Windows 7:</p>
  <p>1.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Start the OpenVPN client by right clicking on the icon and select “Run as administrator” (Windows XP users can just double click on the client)</p>
  <p>2.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Right click on the OpenVPN client in the Windows Systems Tray (next to the clock on the bottom right of screen), and select Connect</p>
</div>
<div>&nbsp;</div>
<div>Apple OS X:</div>
<div>
  <ol>
    <li>Download the OpenVPN client&nbsp;<a href="http://code.google.com/p/tunnelblick/">here</a>&nbsp;(Tunnelblick_3.0b28.dmg).</li>
    <li>Accept all the defaults during installation.</li>
    <li>After installing the client, download the certificate from the VPN page and extract the .ZIP file.</li>
    <li>Run Tunnelblick - it will give you two options, select "Open Configuration Folder".</li>
    <li>Copy the contents of the unzipped directory (5 files) into this folder.</li>
    <li>Close Tunnelblick, and re-run.</li>
    <li>Right click Tunnelblick in the running program menu, go to options, choose connect.</li>
  </ol>
</div>
<p>Now you should be connected and able to connect to your server. Any issues please refer to the troubleshooting below.</p>
<h3>FAQ</h3>
<ul>
  <li>After I select Connect my OpenVPN client never establishes a connection (or the icon does not turn “green”), what could be wrong?</li>
  <ul>
    <li>Verify&nbsp;with the NOC which port our engineers have established and then check&nbsp;with your firewall administrator&nbsp;to ensure this port is open on your corporate firewall(s). Also, ensure your IT staff is not blocking this port with your
      Windows desktop firewall.</li>
  </ul>
  <li>Is this service using secure ssl?</li>
  <ul>
    <li>This service uses SSL certificates but does not run on the standard SSL port. In your configuration file (ends in OVPN) you can see the remote information such as:&nbsp;<strong>remote &lt;IPHOST&gt; &lt;PORT&gt; </strong>(example:&nbsp;remote 64.94.142.9
      1194).</li>
  </ul>
  <li>Is this a shared or isolated service?</li>
  <ul>
    <li>This is an isolated service for every account. Each account&nbsp;receives&nbsp;their own VPN instance to keep isolation and high security.</li>
  </ul>
  <li>Who handles the patching/maintenance of this service?</li>
  <ul>
    <li>The platform handles all of the VPN instance patching and maintenance. Occasionally you will need to upgrade you vpn client application.</li>
  </ul>
  <li>What if I want to use my own VPN service?</li>
  <ul>
    <li>There are two ways you can do this:
      <br />1) If it is a physical device you will need to have a persistent connection to your secure network. If you do have that then you can host a physical VPN server yourself and route across the&nbsp;persistent&nbsp;connection.
      <br />2) If you would like to use a software based VPN server then you can install it on a virtual server and configure the firewall rules to allow access. Many of our customers have done this but it will not be supported by the NOC.&nbsp;</li>
  </ul>
  <li>When I connect to the service I cant ping/connect to the server?</li>
  <ul>
    <li>This is one of the most common issues with Windows and the OpenVPN client. Make sure to run it as Administrator by holding down the shift key and right click on the application then select run as administrator.&nbsp;</li>
  </ul>
  <li>Can I use this to connect to my office?</li>
  <ul>
    <li>You cannot use it as a direct connect.&nbsp;To learn more about ways to connect such as persistent vpn connections, direct connections please go&nbsp;<a href="http://help.tier3.com/entries/20518933-network-access-options-for-connecting-to-tier-3-s-platform">here</a>.</li>
  </ul>
</ul>
<h3>Related Articles</h3>
<p><a href="http://help.tier3.com/entries/20905706-vpn-client-connection-troubleshooting">Client Connection Troubleshooting</a>
</p>
<p><a href="http://help.tier3.com/entries/20937527-configure-two-factor-authentication">Configure Two Factor Authentication</a>
</p>
<p><a href="http://help.tier3.com/entries/20352701-connect-to-multiple-openvpn-instances">Connect to Multiple OpenVPN Instances</a>
</p>