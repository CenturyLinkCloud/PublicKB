{{{
  "title": "FTP Users in Control Portal",
  "date": "7-9-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

<div class="kb-post-overview">
  <h3>Overview</h3>
  <p>The CenturyLink Cloud Control Portal allows for the creation of FTP users. These FTP users are intended to be used <em>only for the uploading of custom script and software packages</em> to be run as part of a Blueprint or directly on a server or group of servers. The FTP users created in Control Portal may also be used for uploading VM images for import. This article should explain what the FTP users service is used for and the process for using it.</p>
</div>

<div class="kb-post-audience">
  <ul>
    <li>CenturyLink Cloud customers</li>
  </ul>
</div>

<h3>Audience</h3>
<ul>
  <li>CenturyLink Cloud customers</li>
</ul>
<h3>Creating FTP Users</h3>
<ol>
  <li>Select "FTP Users" from the main drop down menu.
    <br /><img src="https://t3n.zendesk.com/attachments/token/TBdfKe5e2A38fXpNqdMOubJHo/?name=ftp-users-menu.png" alt="ftp-users-menu.png" />
  </li>
  <li>This will display a page showing the FTP users that have been created. To create a new one, click "create ftp user".
    <br /><img src="https://t3n.zendesk.com/attachments/token/OWAsKWr6OWSUGBvzwXoGiHbl0/?name=ftp-users-list.png" alt="ftp-users-list.png" />
  </li>
  <li>Enter the alias for the FTP user and click "create user". Notice it will prepend your account alias to the username.
    <br /><img src="https://t3n.zendesk.com/attachments/token/0KTnQOfFJmlpf8YeplC2losZb/?name=create-ftp-user.png" alt="create-ftp-user.png" />
  </li>
  <li>You will see that a strong password is assigned to the user you created and is listed in the list of users along with the server name to login to.</li>
</ol>
<h3>Uploading Script Package</h3>
<ol>
  <li>Notice that when you create a new script package from the Scripts page, you have the option to upload via the web browser or via FTP. For smaller packages, it is very easy to use the browser upload option. However, for packages that are larger than
    4 MB, it is recommended that you use the FTP upload option. This (and only this) is what the user(s) you created in the previous steps should be used for.
    <br /><img src="https://t3n.zendesk.com/attachments/token/eE1Z9P5I2wt434TLwDqNGjiVR/?name=upload-script-package.png" alt="upload-script-package.png" />
  </li>
  <li>When you click the "FTP Upload" option, notice that it will give instructions for how to upload a package. It even creates an FTP user for you if you don't already have one called ALIAS_BlueprintUser and displays the username and password here.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/Nhi3rT6DLum5wtZffNn6q9LIT/?name=ftp-instructions.png" alt="ftp-instructions.png" />
  </li>
  <li>Using the server name, username, and password listed (or the one from your previous steps of creating a new user), login to the FTP server with your favorite FTP client.
    <br /><img src="https://t3n.zendesk.com/attachments/token/kj6hWAdxPDXuWCzF338dK5ykl/?name=ftp-client-upload.png" alt="ftp-client-upload.png" />
  </li>
  <li>Now, in the Scripts section under the Unpublished tab, you should see the script that you uploaded. Clicking "publish" will take you through the process of completing the publication of your script package.
    <br /><img src="https://t3n.zendesk.com/attachments/token/ffuFBkYXpmxPgv7LmZGJqamCP/?name=unpublished-package.png" alt="unpublished-package.png" />
    <br />See <a href="https://t3n.zendesk.com/entries/20348448-Blueprints-Script-and-Software-Package-Management">Blueprints Script Package Management</a>&nbsp;for more information on how to create and publish packages for upload.</li>
</ol>
<h3>Additional Usage</h3>
<p>The FTP account may also be used for uploading OVF templates or VM images to import.</p>
