{{{
  "title": "Exporting a VM to an OVF from VMware Workstation for Import into the Tier 3 Cloud",
  "date": "4-16-2013",
  "author": "Jake Malmad",
  "attachments": []
}}}

<h3>Description:</h3>
<p>OVF (<strong>Open Virtualization Format</strong>) is an open standard for packaging and distributing virtual machines or virtual appliances. The OVF standard is not proprietary, and thus cross-platform compatible regardless of hypervisor (VMware, Hyper-V,
  Xen). This article details the steps associated with exporting a virtual machine from VMware Workstation for import into the Tier 3 cloud.</p>
<h3>Steps:</h3>
<p><strong>1.</strong> Launch VMware Workstation. In the “Library” pane, select the machine you wish to export.</p>
<blockquote>
  <h3><img src="https://t3n.zendesk.com/attachments/token/mx7ijhmj682spxl/?name=library.png" alt="library.png" /></h3>
</blockquote>
<p><strong>2.</strong> Select “File” -&gt; “Export to OVF”. A dialog box will appear asking to specify the destination directory in which the OVF will be saved. Browse to the desired location and click “Save”.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/joqgy8yyglu8gwy/?name=exportovf1.png" alt="exportovf1.png" />
</p>
<p><strong>3.</strong> A progress bar will be displayed showing the task completion.</p>
<p><strong>4.</strong> To reduce file transfer time, and ensure file integrity, it is recommended to use an archival tool such as the open source 7zip to compress the OVF folder. Once the archive is created, it is advised calculate a checksum to ensure the
  integrity of your files. This can be done in most archival programs, in 7zip, simply highlight the archive and go to “File” and selecting “Calculate Checksum”. The checksum value can provided to the Tier 3 NOC to ensure the integrity of the uploaded
  archive</p>
<p>
  <br />.<img src="https://t3n.zendesk.com/attachments/token/vosgvxtvv8qe6qo/?name=checksum.PNG" alt="checksum.PNG" />
</p>
<p><strong>5.</strong> Upload the archive to the provided FTP location for import.</p>

<p>Additionally, the same procedure can be performed with <a href="http://www.vmware.com/support/developer/ovf/" target="_blank">OVF Tool</a>. Once the OVF tool is downloaded, launch a command prompt or terminal window in the appropriate location. While
  the OVF tool can perform advanced configuration commands, the simplest operation is:</p>
<pre> ovftool &lt;source&gt; &lt;destination&gt;</pre>