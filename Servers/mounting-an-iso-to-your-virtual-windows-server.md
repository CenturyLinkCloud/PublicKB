{{{
  "title": "Mounting an .ISO to your virtual Windows server",
  "date": "12-31-2014",
  "author": "Roham Ghashghai",
  "attachments": []
}}}

<h3>Description (goal/purpose)</h3>
<p>This KB provides details on what software we recommend using to mount an .ISO file that you have downloaded.</p>
<h3>Audience</h3>
<ul>
  <li>Customer's</li>
</ul>
<h3>Impact</h3>
<p><strong>*Caution*: When downloading any software from the web you are at risk of downloading malicious content, CenturyLink does not take&nbsp;responsibility&nbsp;for any content&nbsp;you download from the web.&nbsp;<br /></strong>
</p>
<h3>Prerequisites</h3>
<p>Software to mount the .ISO.</p>
<p>We recommend using a simple mounting tool called&nbsp;wincdemu this can be located here:&nbsp;http://wincdemu.sysprogs.org/download/ or you may use any software that you are familiar with.&nbsp;</p>
<h3>Detailed Steps</h3>
<p>1. First you will need to download the .iso you are wanting to mount. We do not recommend downloading .iso's from P2P networks or Torrent shares.</p>
<p>2. Once the file is download you will need to install WINCDEMU (link is provided above).&nbsp;WinCDEmu driver binaries are signed, so that the 64-bit Windows will load them. However, they do not have the WHQL certificate, so Windows will ask you to confirm
  driver installation:</p>
<p>3. To mount the .iso: Open the folder containing the image file, double-click at the image. Alternatively, you can right-click and select "Select drive letter &amp; mount" from the context menu.&nbsp;Click at the OK button or press enter. If you don't
  want to see this dialog every time you mount an image, set the "Manage drive letters automatically" checkbox.&nbsp;A new virtual drive will appear among all other drives in the "computer" folder:</p>
<p>4.&nbsp;You can use the virtual drive the same way as you would use a "real" optical disc - browse its contents, open files, start programs.&nbsp;Once you are done with the image, right-click on the virtual drive and select "Eject".&nbsp;You can alternatively
  unmount the image by double-clicking at the image file again.</p>
<p>&nbsp;</p>