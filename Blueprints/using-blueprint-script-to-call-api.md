{{{
  "title": "Using Blueprint Script to Call API",
  "date": "10-8-2014",
  "author": "Bryan Friedman",
  "attachments": [
    {
      "url":"nPGy5LUM95cCvDR1YzdfjMUPL-package.zip",
      "type":"application/zip",
      "file_name":"package.zip"
    }
  ],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>It can sometimes be helpful to expose metadata about CenturyLink Cloud servers or other components to the servers themselves, making details around data centers, groups, the server itself, or even other servers available for use on a server. This type
  of information can potentially be used for such things as balancing clusters or as part of specific configuration files on the server. By combining the flexibility of Blueprints and Scripts with the power of the v2 API, you can easily accomplish something
  like this. The following use case is one example of how to achieve this sort of functionality. It queries the API for the ID and name of the data center that the current server is in and writes this information to a file on the server.</p>
<h3>Steps</h3>
<ol>
  <li><strong>Write a shell script to perform the query and write the file.</strong>
  </li>
  <ol>
    <li><p>Before creating any Blueprints or Scripts in the Control Portal, write a shell script that will run on a Linux server. It needs to call the API, get the information needed, and write it out to a file. It will also need five command line parameters to perform these operations:</p>
      <pre># Take parameters from command line<br /> USERNAME="$1"   # Username of the control portal user to connect to API as<br /> PASSWORD="$2"   # Password for this user<br /> ACCOUNT="$3"    # The account alias to query in the API (Example: BRYF)<br /> SERVERID="$4"   # The server ID to query in the API (Example: WA1BRYF2NDSRV01)<br /> FILENAME="$5"   # The complete path and file name to write the information out to</pre>
    </li>
    <li><p>Next, initialize some other variables to use in the calls to the API and the parsing of the JSON that it returns.</p>
      <pre># Names of value keys to get from JSON responses<br />TOKENKEY="bearerToken"<br />DCKEY="locationId"<br /><br /># Build JSON for authorization request<br />AUTHJSON="{\"username\":\"$USERNAME\",\"password\":\"$PASSWORD\"}"<br /><br /># Store URLs for API requests<br />BASEURL="https://api.tier3.com/v2"<br />AUTHURL="$BASEURL/authentication/login"<br />GETSRVURL="$BASEURL/servers/$ACCOUNT/$SERVERID"</pre>
    </li>
    <li>Additionally, the script will need to parse the JSON string that is returned from the API calls. Here is a very simple example of a function that will find a specific key and return the value in a JSON string. Feel free to use your favorite JSON parsing
      method that is supported in shell scripts (i.e. python or <a href="https://github.com/micha/jsawk">jsawk</a>). (Though limited, this example sticks with standard Linux commands like <code>sed</code>, <code>awk</code>, and <code>grep</code>,
      so no additional libraries are required.)
      <br />
      <pre># Simple helper function to parse JSON response ($1) and return value for given key ($2)<br />jsonGetVal() {<br />    echo $1 | sed 's/[{}]//g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i&lt;=n; i++) print a[i]}' |<br />       sed 's/\"//g' | grep $2 | awk 'BEGIN { FS = ":" } ; {print $2}'<br />}</pre>
    </li>
    <li>Then the script makes three sequential calls to the API using <code>curl</code> and the parameters and variables initialized above along with the JSON parsing. The first call is to authenticate, the second will get the data center ID, and the third
      one is for getting the data center name. (For more details on using the API in general, refer to the&nbsp;<a href="//www.ctl.io/api-docs/v2">API v2 Knowledge Base</a>.)
      <br />
      <pre># Call to authentication API to get token<br />AUTHRESP=`curl -s -H "Content-Type: application/json" -d $AUTHJSON $AUTHURL`<br />TOKEN=`jsonGetVal $AUTHRESP $TOKENKEY`<br /><br /># Call to server API to get data center id for given server id<br />SRVRESP=`curl -s -H "Authorization: Bearer $TOKEN" $GETSRVURL`<br />DCID=`jsonGetVal "$SRVRESP" $DCKEY`<br /><br /># Call to DC API to get data center name for given ID<br />GETDCURL="$BASEURL/datacenters/$ACCOUNT/$DCID"<br />DCRESP=`curl -s -H "Authorization: Bearer $TOKEN" $GETDCURL`<br />DCNAME=`jsonGetVal "$DCRESP" name`</pre>
    </li>
    <li>Finally, write the information out the file as specified by the parameter.
      <br />
      <pre># Write information to given file name<br />echo -e "$DCID\n$DCNAME" &gt; $FILENAME</pre>
    </li>
  </ol>
  <li><strong>Create&nbsp;the script package.</strong> (For details on creating script packages in general, refer to the article&nbsp;<a href="../Blueprints/blueprints-script-and-software-package-management.md">Blueprints Script and Software Package Management</a>.)</li>
  <ol>
    <li>Save the script from Step 1 as <code>install.sh</code>.</li>
    <li>Now, create the package manifest XML with all the information needed to upload the script to the control portal. This file contains the name and description of the package, along with the parameters needed and the command to execute. The five parameters
      defined above are passed to the command, retrieving three of them from the pre-defined system parameters (server name, user, and account alias) and prompting for the other two (password and filename).
      <br />
      <br />
      <pre>&lt;?xml version="1.0" encoding="utf-8"?&gt;<br />&lt;Manifest&gt;<br />  &lt;Metadata&gt;<br />    &lt;UUID&gt;fb50a8ac-cf77-4bac-97c0-f9f9ca76cf6d&lt;/UUID&gt;<br />    &lt;Name&gt;Write DC Info to File (Linux)&lt;/Name&gt;<br />    &lt;Description&gt;<br />    Writes file to system with ID and name of data center for the current Linux server.<br />    &lt;/Description&gt;<br />  &lt;/Metadata&gt;<br />  &lt;Parameters&gt;<br />    &lt;Parameter Name="Server Name" Type="String" Variable="T3.Server.Name" Prompt="false"/&gt;<br />    &lt;Parameter Name="Control Username" Type="String" Variable="T3.Identity.User" Prompt="false"/&gt;<br />    &lt;Parameter Name="Account Alias" Type="String" Variable="T3.Identity.Account" Prompt="false"/&gt;<br />    &lt;Parameter Name="Current Control User Password" Type="Password" Variable="T3.DCInfo.UserPassword" /&gt;<br />    &lt;Parameter Name="Complete Path and File Name to Write" Type="String" Variable="T3.DCInfo.PathToFile" /&gt;<br />  &lt;/Parameters&gt;<br />  &lt;Execution&gt;<br />    &lt;Mode&gt;Ssh&lt;/Mode&gt;<br />    &lt;Command&gt;install.sh ${T3.Identity.User} ${T3.DCInfo.UserPassword} ${T3.Identity.Account} ${T3.Server.Name} ${T3.DCInfo.PathToFile}&lt;/Command&gt;<br />    &lt;Persistent&gt;false&lt;/Persistent&gt;<br />  &lt;/Execution&gt;<br />&lt;/Manifest&gt;</pre>
    </li>
    <li><p>Save this file as <code>package.manifest</code>.</li>
    <li><p>Create a ZIP file that contains the two files just created (<code>package.manifest</code> and <code>install.sh</code>) at the top level (not nested in a folder). Save this ZIP file as <code>package.zip</code>.</li>
  </ol>
  <li><p><strong>Upload the script to the control portal.&nbsp;</strong>(For details on creating script packages in general, refer to the article<a href="../Blueprints/blueprints-script-and-software-package-management.md">Blueprints Script and Software Package Management</a>.)</li>
  <ol>
    <li><p>Login to control portal and navigate to the Scripts page.
    <p><img src="../images/2014-06-05-001-Scripts-Menu.png" alt="2014-06-05-001-Scripts-Menu.png" />
    </li>
    <li><p>Click on the "+ new script" button.
    <p><img src="../images/2014-06-05-002-New-Script.png" alt="2014-06-05-002-New-Script.png" />
    </li>
    <li><p>Choose "Browser Upload" and then upload the <code>package.zip</code> file.
      <p><img src="../images/2014-06-05-005-Upload-File.png" alt="2014-06-05-005-Upload-File.png" />
    </li>
    <li><p>Now publish the package by clicking the "publish" button next to the package name in the list of unpublished packages.
      <p><img src="../images/2014-06-05-006-Publish.png" alt="2014-06-05-006-Publish.png" />
    </li>
    <li><p>Click the "next" button on the displayed information page and then select the desired attributes for the package. In this example, select "Scripts", "Linux" (selecting all Linux flavors) and finally "Private". Then click the "Publish" button.
      <p><img src="../images/2014-06-05-008-Package-Details.png" alt="2014-06-05-008-Package-Details.png" />
    </li>
    <li><p>The package is queued for publishing. Once the publish operation is complete, it is a usable script. (You can click the "Details Page" link to check the status of the publish.)
      <p><img src="../images/2014-06-05-009-Package-Done.png" alt="2014-06-05-009-Package-Done.png" />
    </li>
  </ol>
  <li><strong>Execute script on [multiple] server(s) within a group. </strong>(Alternatively, you could create a Blueprint and use this Script as the last task of the build procedure.)</li>
  <ol>
    <li><p>From the group page, select "execute package" from the actions menu.</p></li>
    <li><p>Select the Script you uploaded in the previous steps. It should be listed under "private scripts" as seen here:</p>
      <p><img src="../images/exec-pkg-write-dc.png" alt="exec-pkg-write-dc.png" /></p>
    </li>
    <li>Now enter the values for the parameters that were defined as the prompts indicate. First, your Control Portal password, and then the path to write the file to. This example will use the path <code>/tmp/dc-info.txt</code>.
      <p><img src="../images/write-dc-params.png" alt="write-dc-params.png" /></p>
    </li>
    <li>
      <p>Finally, select the servers to execute the script on and click the "execute package" button.</p>
      <p><img src="../images/exec-pkg-write-dc-select-servers.png" alt="exec-pkg-write-dc-select-servers.png" /></p>
    </li>
    <li>You will then be redirected to the Queue page to see the status of the running task. When it is completed, log on to one of the servers to confirm the file exists and has the data as expected.</li>
  </ol>
</ol>
