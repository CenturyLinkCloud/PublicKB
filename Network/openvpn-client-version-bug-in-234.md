{{{
  "title": "OpenVPN client version bug in 2.3.4",
  "date": "9-17-2014",
  "author": "Jon McClary",
  "attachments": []
}}}

<strong>Description:</strong>
<p>&nbsp;In some cases, connection issues have been observed with OpenVPN client for Windows, version 2.3.4. The issue does not always reproduce, and we have not identified the specific criteria which causes the failure.&nbsp;</p>
Impact
<p>&nbsp;The specific symptom is a VPN disconnect, which will not clear until the client machine is rebooted, due to a ‘hung’ or ‘stuck’ OpenVPN Daemon process in Windows.</p>
<p>&nbsp;&nbsp;</p>
<p><img src="https://t3n.zendesk.com/attachments/token/Vwt21hq3g9dp2UVNrzPTrfdlL/?name=Process.png" alt="Process.png" />
</p>

<p>&nbsp;Attempting to end the task in Task Manager or to kill the process via command line fails. The only effective method in which to end the process is via a reboot of the client machine.</p>
<p>&nbsp;Our recommendation at this time is to use OpenVPN 2.3.2. It&nbsp;has not been observed to suffer the connection issue described for 2.3.4, and is immune to the Heartbleed vulnerability. There is no need to uninstall 2.3.4 first, as during the install
  process any other version previously installed will be removed.&nbsp;</p>
<p>
  <br /><strong>To verify your current version via Windows:</strong>
</p>
<p>
  <br />1.&nbsp; &nbsp; Browse to C:\Program Files\OpenVPN\bin</p>
<p>2.&nbsp; &nbsp; Right click on openvpn.exe</p>
<p>3.&nbsp; &nbsp; Click ‘Properties’</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 1.&nbsp; &nbsp; See version information:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/o6C6NBssxDUJgPcWKrvGbu3Qz/?name=version_gui.png" alt="version_gui.png" />
</p>
<p>&nbsp; &nbsp; &nbsp;<strong>To verify version via CLI:</strong>
</p>
<p>&nbsp; &nbsp; &nbsp;1. &nbsp; &nbsp;Open Cmd
  <br />&nbsp; &nbsp; &nbsp;2. &nbsp; &nbsp;Enter the following:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;'C:\Program Files\openvpn\bin\openvpn.exe' –version</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img src="https://t3n.zendesk.com/attachments/token/dNpUJZUr3w3AWVWJVIIE3iy8I/?name=version_cli.png" alt="version_cli.png" />
</p>

<p><strong>To change your version to 2.3.2:</strong>
</p>
<p><strong>&nbsp; Note: </strong>This does not require a reboot unless you're running version 2.3.4 and the OpenVPN Dameon process is already in a hung state.</p>
<p>&nbsp; 1. Run the installer, which you can download here:&nbsp;<a href="http://swupdate.openvpn.org/community/releases/openvpn-install-2.3.2-I006-i686.exe">OpenVPN 2.3.2</a>
</p>
<p>&nbsp; 2. When prompted whether you want to allow the program to make changes to your computer, select 'yes'</p>
<p>&nbsp; 3. The OpenVPN Setup Wizard will open. Click 'Next'</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/QSRZuOWfHfBrjPwInbq4yxUr0/?name=wizard1.JPG" alt="wizard1.JPG" />
</p>
<p>&nbsp; 4. Agree to the EULA</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/eC9hfzZQIkyAbKR2uXqXYZjkC/?name=wizard2.JPG" alt="wizard2.JPG" />
</p>
<p>&nbsp; 5. Leave defaults checked, and click 'Next'</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/9BTuzjkA81tWyUZOrilkKSHSv/?name=wizard3.JPG" alt="wizard3.JPG" />
</p>
<p>&nbsp; 6. Click Install, changing the destination folder first if you wish to</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;1. This will automatically remove any previously installed versions and install 2.3.2</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/bzLGlvyNhCsovu0wIqW2gd3SU/?name=wizardpath.JPG" alt="wizardpath.JPG" />
</p>

<p>&nbsp;7. Click 'Next' when finished &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;<img src="https://t3n.zendesk.com/attachments/token/kI90vpZAHQr8hrfrn7D836oxI/?name=wizard4.JPG" alt="wizard4.JPG" />
</p>
<p>&nbsp;&nbsp;</p>
<p>&nbsp; 8. Click 'Finish'&nbsp;</p>
<p>&nbsp; &nbsp; &nbsp;&nbsp;<img src="https://t3n.zendesk.com/attachments/token/tzRTqgLhAKUFQoxQFBgh02VbV/?name=wizard5.JPG" alt="wizard5.JPG" />
</p>


