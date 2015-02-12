{{{
  "title": "Connect to Multiple OpenVPN Instances",
  "date": "2-13-2014",
  "author": "Russ Malloy",
  "attachments": [],
  "contentIsHTML": true
}}}

<h4>Description</h4>
<p>Some customers have large organizations with a Parent account and several sub-accounts with their own OpenVPN setups. With the new version of OpenVPN ( Version 2.3.2 ) , creating or listing multiple connections has changed, this article describes how
  to set up multiple connection end points for you to connect to.</p>
<h4>Audience</h4>
<ul>
  <li>All Windows Users of OpenVPN</li>
</ul>
<h4>Pre-Requisites</h4>
<ul>
  <li>A properly installed instance of OpenVPN - see <a href="https://t3n.zendesk.com/entries/20914433-How-To-Configure-Client-VPN">How to Configure Client VPN</a>
  </li>
</ul>
<h4>Detailed Steps</h4>
<ol>
  <li>Disconnect from all OpenVPN connections</li>
  <li>Navigate to your OpenVPN configuration direction (i.e. C:\Program Files\OpenVPN\config)</li>
  <li>Create a folder for each end point connection you require. In this example we will use Connection_A and Connection_B</li>
  <li>Move or download the OpenVPN files to the newly created folder(s). The following files should exist in each folder: <strong>ca.crt, default.crt, default.key, default.ovpn, tlsauth.key</strong>
  </li>
  <li>You must rename the default.ovpn file to a unique name across all sub folder... it's usually best to just use the parent folder name (i.e. Connection_A, Connection_B)</li>
  <li>You can run the following commands in PowerShell to automatically rename the default.ovpn files to their parent folder names</li>
  <ul>
    <li>
      <p><strong>cd "C:\Program Files\OpenVPN\config"</strong>
      </p>
    </li>
    <li><strong>dir | %{gci $_ -Filter *.ovpn |&nbsp;Rename-Item -NewName {$_.Directory.Name + ".ovpn"}}</strong>
    </li>
  </ul>
  <li>Now you can start OpenVPN (running as administrator). Right-click the OpenVPN icon in the system tray (where the clock is), and you can select the connection you wish to make.</li>
</ol>
<h4>Additional Information</h4>
<p>Please note that by default you may only connect to a single end point with OpenVPN because you only have a single TAP adapter. For each additional TAP adapter you create you'll be able to connect to multiple end points simultaneously.</p>
<p>To add additional TAP adapters, run&nbsp;the&nbsp;addtap.bat command file&nbsp;located at&nbsp;C:\Program Files\TAP-Windows\bin. Each time you run that script a new TAP adapter will be created and you can simultaneously connect to another end point.</p>