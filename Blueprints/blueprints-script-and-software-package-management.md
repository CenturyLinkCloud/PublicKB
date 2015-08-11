{{{
  "title": "Blueprints Script and Software Package Management",
  "date": "12-18-2014",
  "author": "Trent Anderson",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Last updated:  2/3/2015 03:05 PST</strong>
</p>
Description
<p>Software and script packages (henceforth referred to as "packages") are one way that Blueprint Designers can customize their environments. They can be configured to run scripts and executables or install software. The definition of a package is
  also responsible for generating the UI at Blueprint deployment time to gather the requisite set of parameters from the User.</p>
Package Format
<p>Packages must be .zip files and contain the following:</p>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>package.manifest</strong>
        </p>
      </td>
      <td>
        <p>Defines the metadata, parameter list and execution guidelines for the Package.</p>
        <p>An Xml Schema (.xsd) is available to validate the package.manifest file before uploading.</p>
        <p><em>This file is required in all Packages.</em>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>[executable]</strong>
        </p>
      </td>
      <td>
        <p>At least one executable file must be included in the Package. CenturyLink Cloud supports the following executable types:</p>
        <p>-        Standard .exe</p>
        <p>-        Command line scripts (anything that can be run from cmd.exe for Windows or the shell on Linux)</p>
        <p>-        PowerShell scripts (.ps1 files)</p>
        <p><em>* Note: The permissions of this file for Linux scripts must be set to be executable (chmod 755). In order to best achieve this, the file must be created and zipped on a Linux or Unix-based platform.</em>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>[resources]</strong>
        </p>
      </td>
      <td>
        <p>Any additional files that the main executable may require for proper execution.</p>
        <p>The executable is run from the Package root folder, so any file/folders should be accessed relative to the root.</p>
      </td>
    </tr>
  </tbody>
</table>
<p><em>Note: The zip file should be created on a comparable environment to the one in which the script will be running. In other words, for a script that will run on Linux, it should be created on a Unix-based platform, and for a Windows script, it should be created on a Windows machine.</em>
</p>
<p>This rest of this document will explain how to construct the package.manifest file and explain what information is available to the package at execution time.</p>
&lt;Manifest&gt; Element
<p>The root node for the package manifest.</p>
<pre>&lt;Manifest&gt;<br />  &lt;Metadata&gt;<br />  &lt;Parameters&gt;<br />  &lt;Execution&gt;<br />&lt;/Manifest&gt;</pre>
<h3>Parent Element</h3>
<p>None.</p>
<h3>Attributes</h3>
<p>None.</p>
<h3>Child Elements</h3>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Metadata</strong>
        </p>
      </td>
      <td>
        <p>Provides descriptive information regarding the package, its contents and capabilities.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Parameters</strong>
        </p>
      </td>
      <td>
        <p>Defines parameters that are used during execution of the package.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Execution</strong>
        </p>
      </td>
      <td>
        <p>Defines how the package it to be executed</p>
      </td>
    </tr>
  </tbody>
</table>
&lt;Metadata&gt; Element
<p>Provides descriptive information to uniquely identify the package, its contents and capabilities.</p>
<pre>&lt;Metadata&gt;<br />  &lt;UUID&gt;<br />  &lt;Parameters&gt;<br />  &lt;Name&gt;<br />  &lt;Description&gt;<br />&lt;/Manifest&gt;</pre>
<h3>Parent Element</h3>
<p>&lt;Manifest&gt;</p>
<h3>Attributes</h3>
<p>None.</p>
<h3>Child Elements</h3>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>UUID</strong>
        </p>
      </td>
      <td>
        <p>A GUID that uniquely identifies the Package.
          <br />This value is used internally by the Blueprint deployment process as well as to identify a Package when updates are submitted.</p>
        <p><em>This value should not be changed for minor updates (i.e. updated script logic).</em>
        </p>
        <p><em>This value should be changed for major update (i.e. updated parameter list).</em>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p>The name of the Package.</p>
        <p><em>Max length: 100 characters</em>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
      <td>
        <p>A detailed description of the Package.</p>
        <p>This value is used to display information to designers who choose to add this Package to their Blueprint.</p>
      </td>
    </tr>
  </tbody>
</table>
&lt;Parameters&gt; Element
<p>Defines the list of parameters required to execute the Package.</p>
<pre>&lt;Parameters&gt;<br />  &lt;Parameter&gt;<br />&lt;/Parameters&gt;</pre>
<h3>Parent Element</h3>
<p>&lt;Manifest&gt;</p>
<h3>Attributes</h3>
<p>None.</p>
<h3>Child Elements</h3>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Parameter</strong>
        </p>
      </td>
      <td>
        <p>See &lt;Parameter&gt; Element.</p>
      </td>
    </tr>
  </tbody>
</table>
<h3>&lt;Parameter&gt; Element</h3>
<p>Defines how a Parameter will be presented in the UI.</p>
<pre>&lt;Parameter Name= Type= Variable= Hint= Prompt= Global= Regex= &gt;<br />  &lt;Option&gt;<br />&lt;/Parameter&gt;</pre>
<h4>Parent Element</h4>
<p>&lt;Parameters&gt;</p>
<h4>Attributes</h4>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
      <td>
        <p><strong>Required?</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p>Display name for the Parameter.</p>
        <p><em>Ignored if Prompt = ‘none’.</em>
        </p>
      </td>
      <td>
        <p>Yes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Type</strong>
        </p>
      </td>
      <td>
        <p>The Parameter type.</p>
        <p><em>See below</em><em> for values</em>
        </p>
      </td>
      <td>
        <p>Yes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Variable</strong>
        </p>
      </td>
      <td>
        <p>This is a variable name which you can refer to in the execution command for your package. Our recommendation is that you name your variables to include your CenturyLink Cloud account alias and your Package Name (e.g. T3.install-ad.DomainName) to ensure
          that you don’t encounter any name conflicts with other scripts you’ve included in a Blueprint.</p>
      </td>
      <td>
        <p>Yes</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Hint</strong>
        </p>
      </td>
      <td>
        <p>Additional description to communicate the meaning/use of the Parameter. If specified this will be displayed below the input field on the Blueprint deployment form.</p>
        <p><em>Ignored if Prompt = ‘none’</em>
        </p>
      </td>
      <td>
        <p>No</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Default</strong>
        </p>
      </td>
      <td>
        <p>Sets the default parameter value. If you specify a default it cannot be empty.</p>
      </td>
      <td>
        <p>No</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Prompt</strong>
        </p>
      </td>
      <td>
        <ul>
          <li>None: Parameter will have no representation in the UI</li>
          <li>Build: Parameter will be prompted for when a Blueprint is being built</li>
          <li>Design: Parameter will be prompted for when Blueprint is being designed/deployed</li>
          <li>Global: Parameter will be prompted only once when it exists in multiple packages</li>
        </ul>
        <p><em>Default = ‘None’</em>
        </p>
      </td>
      <td>
        <p>No</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Global</strong>
        </p>
      </td>
      <td>
        <p>True to indicate that is Parameter is defined in multiple Packages but should only be prompted for once at Blueprint Deployment.</p>
        <p><em>Default = ‘false’<br />All reference to this Parameter in all Packages will have the same value.</em>
        </p>
      </td>
      <td>
        <p>No</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Regex</strong>
        </p>
      </td>
      <td>
        <p>A Regular Expression to validate user input for a String Parameter.</p>
        <p><em>Ignored if Type != ‘String’</em>
        </p>
      </td>
      <td>
        <p>No</p>

      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Required</strong>
        </p>
      </td>
      <td>
        <p>A Boolean value indicating if this parameter requires a value or not.</p>
        <p><em>Default = 'true'</em>
        </p>
      </td>
      <td>
        <p>No</p>
      </td>
    </tr>
  </tbody>
</table>
<h4>Parameter Type</h4>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Type</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
      <td>
        <p>UI Element</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Network</strong>
        </p>
      </td>
      <td>
        <p>The CenturyLink Cloud internal network name.</p>
        <p>The list contains all networks that belong to the account, and the user is required to select one.</p>
        <p><em>It is unlikely that a Package would ever need this piece of information.</em>
        </p>
      </td>
      <td>
        <p>Drop Down List</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Numeric</strong>
        </p>
      </td>
      <td>
        <p>A numeric value.</p>
        <p>The text is validated to ensure only numeric values are accepted.</p>
      </td>
      <td>
        <p>Textbox</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Option</strong>
        </p>
      </td>
      <td>
        <p>A list of values where one item must be selected.</p>
        <p><em>1 or more </em><em>Option</em><em> elements must be defined.</em>
        </p>
      </td>
      <td>
        <p>Drop Down List</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>MultiSelect</strong>
        </p>
      </td>
      <td>
        <p>A list of values where any number of items may be selected.</p>
        <p><em>1 or more </em><em>Option</em><em> elements must be defined.</em>
        </p>
      </td>
      <td>
        <p>Checkbox List</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Password</strong>
        </p>
      </td>
      <td>
        <p>A masked string value.</p>
        <p><em>Strong password validation will be enforced.</em>
        </p>
      </td>
      <td>
        <p>Password box</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Server</strong>
        </p>
      </td>
      <td>
        <p>A list of server names.</p>
        <p>The list will include all existing servers as well as any servers that will be built as part of the Blueprint.</p>
      </td>
      <td>
        <p>Drop Down List</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>ServerIP</strong>
        </p>
      </td>
      <td>
        <p>A list of server name where the selected value is IP Address.</p>
        <p>The list will include all existing servers, all servers that will be deployed as part of the Blueprint as well as an option to manually enter an IP Address.</p>
      </td>
      <td>
        <p>Drop Down List</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>String</strong>
        </p>
      </td>
      <td>
        <p>A generic string.</p>
        <p><em>If Regex is supplied, the value will be validated using the specified regular expression</em>
        </p>
      </td>
      <td>
        <p>Textbox</p>
      </td>
    </tr>
  </tbody>
</table>
<h4>System Parameters</h4>
<p>Named Parameters defined by CenturyLink Cloud that can be accessed from within the Package.
  <br /><em>To use a System Parameter it must be defined in the Parameter list with Prompt=’none’</em>
</p>
<table>
  <tbody>
    <tr>
      <td>
        <p>Name</p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>T3.Identity.User</strong>
        </p>
      </td>
      <td>
        <p>The username of the individual initiating the Blueprint deployment.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>T3.Server.Name</strong>
        </p>
      </td>
      <td>
        <p>The name of the current server being built.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>T3.Server.IPAddress</strong>
        </p>
      </td>
      <td>
        <p>The IP Address of the current server being built.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>T3.Server.Password</strong>
        </p>
      </td>
      <td>
        <p>The local Administrator password of the current server being built.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>T3.Identity.Account</strong>
        </p>
      </td>
      <td>
        <p>The account alias that this Blueprint is being deployed under.</p>
      </td>
    </tr>
    <tr>
        <td valign="top" width="174">
        <p><strong>T3.Datacenter</strong></p>
        </td>
        <td valign="top" width="624">
        <p>The data center that the Blueprint is being deployed in.</p>
        </td>
    </tr>
  </tbody>
</table>
<h3>&lt;Option&gt; Element</h3>
<p>Defines the options for Option and MultiSelect Parameters</p>
<pre>&lt;Option Name= Value= /&gt;</pre>
<h4>Parent Element</h4>
<p>&lt;Parameter&gt;</p>
<h4>Attributes</h4>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p>The name of the option.</p>
        <p>This value is used to label the option in the UI</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Value</strong>
        </p>
      </td>
      <td>
        <p>The value of the option.</p>
      </td>
    </tr>
  </tbody>
</table>

&lt;Execution&gt; Element
<p>Defines how the Package should be executed.</p>
<pre>&lt;Metadata&gt;<br />  &lt;Mode&gt;<br />  &lt;Command&gt;<br />&lt;/Manifest&gt;</pre>
<h3>Parent Element</h3>
<p>&lt;Manifest&gt;</p>
<h3>Attributes</h3>
<p>None.</p>
<h3>Child Elements</h3>
<table>
  <tbody>
    <tr>
      <td>
        <p><strong>Name</strong>
        </p>
      </td>
      <td>
        <p><strong>Description</strong>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Mode</strong>
        </p>
      </td>
      <td>
        <table>
          <tbody>
            <tr>
              <td>
                <p><strong>Name</strong>
                </p>
              </td>
              <td>
                <p><strong>Details</strong>
                </p>
              </td>
            </tr>
            <tr>
              <td>
                <p><strong>Command</strong>
                </p>
              </td>
              <td>
                <p>Windows Only</p>
                <p>Executes the package as the local administrator by calling the command specified from a command prompt.</p>
              </td>
            </tr>
            <tr>
              <td>
                <p><strong>PowerShell</strong>
                </p>
              </td>
              <td>
                <p>Windows Only</p>
                <p>Executes the package via Remote PowerShell as the local administrator.</p>

                <p><em>Note: ‘Negotiate’ Authentication mode is used when establishing the remote connection.</em>
                </p>
              </td>
            </tr>
            <tr>
              <td>
                <p><strong>Ssh</strong>
                </p>
              </td>
              <td>
                <p>Supported on Linux</p>
              </td>
            </tr>
          </tbody>
        </table>
        <p><em>Package is copied to remote server and executed from the root of the Package directory.</em>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Command</strong>
        </p>
      </td>
      <td>
        <p>The command to be executed.</p>
        <p>You can specify Parameters to be passed to the Package using the following format:</p>
        <p>${Parameter.Variable}</p>
        <p>All Parameters specified in the Parameter list will be replaced with the appropriate values at runtime.</p>
        <p><em>Command must be relative to the root of the Package directory.<br /><br /></em>
        </p>
        <p>Example:</p>
        <p>/dir/my.cmd ${My.Custom.Value}</p>
        <p>Executes the my.cmd file located in a sub folder called ‘dir’,  replacing ${My.Custom.Value} with its runtime value.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>RebootOnSuccess</strong>
        </p>
      </td>
      <td>
        <p>(Boolean) - Valid values are: ‘true’ or ‘false’</p>
        <p>true – Specify ‘true’ to reboot the server once the package has executed.</p>
        <p>false – (default) The server will not reboot.</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Persistent</strong>
        </p>
      </td>
      <td>
        <p>(Boolean) - Valid values are: ‘true’ or ‘false’</p>
        <p>true – Specify ‘true’ to persist the package on the server.</p>
        <p>false – (default) The package will not be persisted after execution.</p>
      </td>
    </tr>
  </tbody>
</table>
<p>
  <a name="uploading"></a>
</p>
Uploading and Publishing a Package
<p>Once the package.manifest has been created, validated, and zipped with the all other required files, the following steps should be followed to get the package uploaded and published to the Control Portal.</p>
<ol>
  <li>Login to control portal and navigate to the Scripts page.
    <br /><img src="../images/2014-06-05-001-Scripts-Menu.png" alt="2014-06-05-001-Scripts-Menu.png" />
  </li>
  <li>Click on the "+ new script" button.
    <br /><img src="../images/2014-06-05-002-New-Script.png" alt="2014-06-05-002-New-Script.png" />
  </li>
  <li>You will be presented with two options for uploading the package: Browser or FTP. For packages less than 4MB, you can easily upload directly through your web browser by choosing "Browser Upload". For packages larger than 4MB, they <em>must</em> be
    uploaded using the "FTP Upload" option, but this option is available for smaller packages as well. Selecting the "FTP Upload" option will create an FTP account and path and display the credentials and URL to use for uploading. (Note that you
    may <a href="../Control Portal/ftp-users-in-control-portal.md">create your own FTP users </a>for this purpose. Packages must be placed in the root folder as indicated by the display. Once uploaded, Package zip files
    will appear in the Unpublished list.)
    <br /><img src="../images/upload-package.png" alt="upload-package.png" />
  </li>
  <li>If you chose "Browser Upload" you will see a prompt allowing you to browse for the file. Select the zip file that contains the package.manifest and supporting files and then click "upload script package" to upload it to the server. (If you chose
    the "FTP Upload" option, after uploading the package to the folder using an FTP client, click on the "Unpublished" tab and move on to step 5.)
    <br /><img src="../images/2014-06-05-005-Upload-File.png" alt="2014-06-05-005-Upload-File.png" />
  </li>
  <li>Now publish the package by clicking the "publish" button next to the package name in the list of unpublished packages.
    <br /><img src="../images/2014-06-05-006-Publish.png" alt="2014-06-05-006-Publish.png" />
  </li>
  <li>The publication process will then load and perform basic validation of the package. If successful, you will be presented with a form showing the contents of your Manifest as well as a sample UI form with the parameters that will be prompted for at deployment
    time. If everything looks right, click the "next" button to move on.</li>
  <li>You will be presented with a page where you can specify additional metadata for the package. First, choose to publish the package as a "Script" or "Software". (There is no functional difference here, just categorization.) Then choose the desired Operating
    System flavor (Linux or Windows) followed by checking the box next to the specific versions of the OS that the package supports (i.e. Windows 2003 or 2008, Ubuntu vs. Redhat, etc.). The last step is to select the visibility of the package. Private
    packages are only visible to users in the account where it was created, Shared packages are visible to users in the account where it was created and all sub-accounts underneath, and Public packages are available to all accounts. (Please review
    <a
    href="../Blueprints/creating-public-blueprint-packages.md">Creating Public Blueprint Packages </a>before publishing a public package.) Finally, click the "Publish" button to kick off the publishing process.
      <br /><img src="../images/2014-06-05-008-Package-Details.png" alt="2014-06-05-008-Package-Details.png" />
  </li>
  <li>The package is then queued for asynchronous publishing and the deploy time will depend upon the size of the package. Once the publish operation is complete, it will appear in the package library. (You can click the "Details Page" link to check the status
    of the publish.)
    <br />
    <br /><img src="../images/2014-06-05-009-Package-Done.png" alt="2014-06-05-009-Package-Done.png" />
  </li>
</ol>
