{{{
  "title": "How to configure Java settings to access web user interfaces",
  "date": "12-15-2014",
  "author": "Lisa Macke",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>&nbsp;This article will help users properly configure their Java settings to connect to various web management interfaces, such as the Citrix Netscaler VPX.</p>
<h3>Prerequisites</h3>
<ul>
  <li>Must have log on rights to appliance or application&nbsp;</li>
  <li>Windows with IE, Chrome, or Firefox installed</li>
  <li>Applicable Ports open for the Web UI (i.e. TCP Ports 80,&nbsp;3008, &amp; 3010 open from your location to the management IP of the Netscaler)</li>
</ul>
<h3><strong>Detailed Steps</strong></h3>
<ol>
  <li>Close your preferred browser.</li>
  <li>Make sure you have the latest version of Java installed. You can download the latest version here:&nbsp;<a href="http://www.java.com/en/download">http://www.java.com/en/download</a>
  </li>
  <li>Launch the Java Control Panel by running “Configure Java” from your start menu</li>
  <li>On the General Tab under Temporary Internet Files click “Settings”</li>
  <li>Uncheck the box "Keep temporary files on my computer" and press OK
    <br />
    <br /><strong><img src="https://t3n.zendesk.com/attachments/token/RtbGDYl4Hv2U5UwJNtwUVABkQ/?name=Java1.png" alt="Java1.png" /><br /><br /></strong>
  </li>
  <li>Next go to the Security tab and change the slider to Medium. Please note that you are responsible for the security of your OS and computer.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/d5GBLPfcDrls0y3j3umRMGd37/?name=Java2.PNG" alt="Java2.PNG" />
    <br />
    <br />
  </li>
  <li>Add the Web UI IP Address to the Exception Site List:&nbsp;
    <ol>
      <li>Click on “Edit Site List”</li>
      <li>Click “Add”</li>
      <li>Enter the URL <a href="http://netscalerip/">http://</a>webui-ipaddress</li>
      <li>Ignore the http/https warning (Click “continue”)</li>
      <li>Click “OK”</li>
    </ol>
  </li>
  <li>Launch your web browser, and access the Web UI with the URL <a href="http://netscalerip/">http://</a>webui-ipaddress</li>
  <li>Throughout your experience you will see Java security prompts. Please click Allow and Run in order to continue</li>
</ol>
<h3>Additional Notes</h3>
<ul>
  <li><strong>Chrome Users</strong>: You may need to modify some advanced settings in your browser settings as well. Launch the Chrome menu and go to Settings. Click on Advanced settings. Click on Content settings.  Underneath JavaScript,
    check "Allow all sites to run JavaScript". Scroll down a bit further to "Protected Content". Uncheck the box "Allow identifiers for protected content (computer restart may be required)" &nbsp;Press done and close all instances of browser.
    &nbsp;</li>
  <li>Recent Java updates have made the Netscaler GUI less reliable, if you are still having issues with the Netscaler GUI, it is recommended that you use the older version of the UI that tends to have less issues.</li>
  <ul>
    <li>Log into the netscaler Web UI, then manually change the URL to: http://(netscalerip)/menu/guia</li>
  </ul>
</ul>

### Still Having Issues?

If you are still having issues, it is most likely related to your Java version. If when you go to the JavaSecurity Tab and you only see High and Very High, you may need to downgrade Java versions.Note: these steps remove the latest Java security updates and features so perform at your own risk.

Uninstall your current Java version.

Go to: http://www.oracle.com/technetwork/java/javase/downloads/java-archiv...

And locate this file: jre-8u11-windows-i586.tar.gz (Windows x86.  Only use x64 if you are using an x64 browser)

Download the file and install it.  This will restore the "Medium" security setting and should allow you to connect.
