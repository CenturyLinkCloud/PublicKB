{{{
  "title": "Building CoreOS Server Cluster on the CenturyLink Cloud",
  "date": "10-14-2014",
  "author": "Bryan Friedman",
  "attachments": [],
  "contentIsHTML": true
}}}

Overview
<p><a href="https://coreos.com/">CoreOS</a>&nbsp;is a lightweight Linux-based operating system that is designed to run&nbsp;<a href="https://www.docker.io/">Docker</a>&nbsp;containers. CoreOS is not currently supported natively
  as a VM template within the CenturyLink Cloud Control Portal, however it can be installed by using a self-managed PXE/DHCP Server and a dedicated network. This is easy to set up using the blueprints that have been created to help with the provisioning
  of a CoreOS cluster.</p>
<p><em>Note: These same instructions can be followed to setup a Panamax server in CenturyLink Cloud. Instead of the "CoreOS Server" blueprint, just use the "CoreOS Server with Panamax" blueprint below and all other steps are the same. For more information, you can reference the <a href="https://github.com/CenturyLinkLabs/panamax-ui/wiki/Installing-Panamax#centurylink-cloud">installation instructions on the Panamax support site</a>.</em>
</p>
Basic Instructions
<p>The basic steps are as follows, with further details below.</p>
<ol>
  <li>Create a dedicated network (VLAN) in the data center you wish to install CoreOS servers.</li>
  <ul>
    <li>Reference&nbsp;<a href="https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs">Creating and Deleting VLANs</a>&nbsp;for details</li>
    <li>Take note of the name of this network so you can use it later</li>
  </ul>
  <li>Deploy the "DHCP-PXE Server" blueprint.</li>
  <ul>
    <li>Make sure to deploy to the data center/VLAN you set up in Step 1 above</li>
  </ul>
  <li>Deploy the "CoreOS Server" blueprint to add the first server and create the cluster.</li>
  <ul>
    <li>For the "Execute on Server" option, be sure to select the name of the DHCP server you created in the previous step, <em>not</em> the CoreOS machine you are currently creating. (This is a very important step.)<strong><br /></strong>
    </li>
    <li>The server credentials entered will not actually be used to login to the server as you will use SSH key authorization to access your CoreOS servers.</li>
    <li>In the "SSH Public Key" field, you may provide the full string of a public key to be used for logging into the CoreOS server over SSH. (If you do not provide a value here, you will have to access the CoreOS server by first using SSH to login to the
      DHCP server and then using SSH from there to login to the CoreOS server.)</li>
    <li>After the Blueprint task is complete, view the "build log" and search for the text "IP Address of CoreOS Server" to obtain the IP address that was used for deploying the server.&nbsp;Take note of this address for future use as it will not be displayed
      in Control.</li>
  </ul>
  <li>Deploy the "CoreOS Server" blueprint for each additional server you'd like to add to the cluster.</li>
  <ul>
    <li>Repeat Step 3 for adding additional CoreOS servers into the cluster</li>
  </ul>
</ol>
<p>(Note: There are some <a href="#limitations">limitations</a>&nbsp;to the functionality that Control Portal will provide for interacting with these CoreOS servers.)</p>
Detailed Steps
<h3>Setup Network</h3>
<p>(You may also reference the article, <a href="https://t3n.zendesk.com/entries/21806469-Creating-and-Deleting-VLANs">Creating and Deleting VLANs</a> for more details about the below steps.)</p>
<ol>
  <li>In the main drop down menu, select "Networks".</li>
  <li>Change to the data center that you wish to provision to.</li>
  <li>Select "Add Network".&nbsp;This will kick off a new blueprint to add a network to your account.<strong><br /></strong>
  </li>
  <li>On the network page, select the data center that the network was added to.</li>
  <li>Select the network that was just added.</li>
  <li>Click on "Edit" and give the network a more friendly name and description such as "CoreOS | 10.xxx.xxx" and then select "Save". This will make it&nbsp;so you can more easily find and select this specific VLAN later.&nbsp;</li>
</ol>
<h3>Deploy DHCP-PXE Server</h3>
<ol>
  <li>In the main drop down menu, select "Blueprints Library".</li>
  <li>Make sure the data center is selected that you wish to provision to (the same one where you setup the network above).</li>
  <li>Find the blueprint called "DHCP-PXE Server" and click it.</li>
  <li>This will open the details of the blueprint. From here, click "deploy blueprint" to begin the process of provisioning the server.
    <br /><img src="https://t3n.zendesk.com/attachments/token/MLQZWQ2O9TaKVmU43Vlk11Arl/?name=dhcp-blueprint.jpg" alt="dhcp-blueprint.jpg" />
  </li>
  <li>The following page will now be displayed, requiring you to enter in some information about the server to be deployed:
    <ul>
      <li>Enter a strong password (twice)</li>
      <li>Select the server group you wish the server to be created in (Default Group is shown here, but you may select a different one if you have created a separate one for your CoreOS cluster for example)</li>
      <li>Select the network that you created in the first steps above</li>
      <li>Specify the primary and secondary DNS servers</li>
      <li>Choose the desired server type (if available) and service level</li>
      <li>You may also choose to rename the server instead of "DHCP"</li>
      <li>Leave "Specify Credential" options set to "no"</li>
    </ul>
    <img src="https://t3n.zendesk.com/attachments/token/dvPRI9TUAVdhfeXGfJVBGvfqt/?name=deploy-dhcp.jpg" alt="deploy-dhcp.jpg" />
    <br />
    <br />Now click the "next: step 2" button at the bottom of the page to move on to the next step.</li>
  <li>You can now review the selected settings and go back to the previous page (using the links on the left side) if you need to make any changes. If everything looks good, click the "deploy blueprint" button at the bottom of the page to start the blueprint
    deployment.</li>
  <li>This will add the blueprint to the queue. Once it completes successfully, you should see a new server set up in the group and data center that you chose during deployment. This server will act as the DHCP and PXE server for the CoreOS servers you will
    create in the following steps.</li>
</ol>
<h3>Deploy First CoreOS Server</h3>
<ol>
  <li>In the main drop down menu, select "Blueprints Library".</li>
  <li>Make sure the same data center is selected that you chose in the previous steps.</li>
  <li>Find the blueprint called "CoreOS Server" and click it.</li>
  <li>This will open the details of the blueprint. From here, click "deploy blueprint" to begin the process of provisioning the server.</li>
  <li>The following page will now be displayed, requiring you to enter in some information about the server to be deployed:
    <ul>
      <li>Enter a strong password (twice) <em>(Note: This password will not actually be used to login to the server as you will use SSH key authorization to access your CoreOS servers. However, you are still required to enter a strong password here in order to deploy the blueprint.)</em>
      </li>
      <li>Select the server group you wish the server to be created in (Default Group is shown here, but you may select a different one if you have created a separate one for your CoreOS cluster for example)</li>
      <li>Select the network that you created in the first steps above</li>
      <li>Specify the primary and secondary DNS servers</li>
      <li>Choose the desired server type (if available) and service level</li>
      <li>You may also choose to rename the server instead of "COREOS"</li>
      <li>Leave "Specify Credential" options set to "no"</li>
      <li><strong>Very Important Step: </strong><em>For "Execute on Server", select the name of the DHCP server you created in the previous step, NOT the COREOS machine you are currently creating. The script to install CoreOS runs remotely from the DHCP server, not on the CoreOS server itself since, as specified above, the password will not work to login directly to the CoreOS machine.</em>
      </li>
      <li>Optionally, you may provide the full string of a public key to be used for logging into the CoreOS server over SSH in the "SSH Public Key" field. If you do not provide a value here, you will have to access the CoreOS server by first using SSH to
        login to the DHCP server using the password provided when deploying that server, and then using SSH from there to login to the CoreOS server. (For information about how to generate an SSH key pair, you can follow the instructions <a href="http://git-scm.com/book/en/Git-on-the-Server-Generating-Your-SSH-Public-Key"
       >here</a>.)</li>
    </ul>
    <img src="https://t3n.zendesk.com/attachments/token/iKZpCmjII9uDEDeIC8Vgcq5zR/?name=deploy-coreos.jpg" alt="deploy-coreos.jpg" />
    <br />
    <br />Now click the "next: step 2" button at the bottom of the page to move on to the next step.</li>
  <li>You can now review the selected settings and go back to the previous page (using the links on the left side) if you need to make any changes. If everything looks good, click the "deploy blueprint" button at the bottom of the page to start the blueprint
    deployment.</li>
  <li>This will add the blueprint to the queue and take you to the "Request Details" page for the task. Wait for the task to complete, and when it has successfully completed, click the "build log" button.
    <br /><img src="https://t3n.zendesk.com/attachments/token/f3AJo1wpUfS8qi2wbJUembvhh/?name=coreos-queue-complete.jpg" alt="coreos-queue-complete.jpg" />
  </li>
  <li>This should display a message log with details from the blueprint deployment.</li>
  <ul>
    <li>Search for the text "Server: " and you should find the name of the server that was just deployed.</li>
    <li>Search for the text "IP Address of CoreOS Server" on the page and you should find a message that says "IP Address of CoreOS Server: 10.xxx.xxx.xxx" with the IP address that was used for the server. <em>Take note of this address for future use. (You may even wish to add it to the Description field on the server details page for the server with the name you found in the above step.)</em>
    </li>
    <li>Right below the IP Address message, you should also see the discovery URL that was used for the CoreOS cluster as well as the cloud-config file that was generated during install in case you find these helpful for interacting with your CoreOS server
      cluster.&nbsp;</li>
  </ul>
  <li>You should now see a new server set up in the group and data center that you chose during deployment with the name you found next to "Server: " in the previous step. This is your first CoreOS server in the cluster. If you provided a public SSH key,
    you should be able to login directly to the server using the command <code>ssh core@10.xxx.xxx.xxx</code> where 10.xxx.xxx.xxx is the IP address you took note of in the previous step. If you did <em>not</em> provide a public SSH key, you can access
    the server by first logging into the DHCP server you provisioned, and then using the <code>ssh core@10.xxx.xxx.xxx</code> command from within that server to login to the CoreOS box.</li>
</ol>
<p>
  <a name="limitations"></a>
</p>
<p><em>Note: While y<em>ou will be able to perform some power operations on this server (on/off/reboot), other f</em>unctionality within Control Portal when controlling this server will be limited. Here are some specific details around this limited functionality:</em>
</p>
<ul>
  <li><em>Control Portal will not know or display the IP address of this server. This is why steps 7 and 8 above are very important so you can be sure to capture the IP address information at build time.</em>
  </li>
  <li><em>As already mentioned above, though an "Admin Server Password" was set and can be retrieved from Control Portal, this password cannot be used to login to the server, which will require SSH key authentication instead.</em>
  </li>
  <li><em>The "snapshot", "clone", "convert to template", and "archive" options on the server details page may result in failure or unpredictable behavior.</em>
  </li>
  <li><em>You will not be able to "add public ip" using the "add public ip" option on the server details page.&nbsp;</em>
  </li>
</ul>
<h3>Deploy Additional CoreOS Servers into the Cluster</h3>
<p>You can repeat steps 1-9 from above, following the same procedure you did to create your first CoreOS server, and the blueprint will add it to the cluster that was created at the time that the first CoreOS server was provisioned.</p>
<p>If you would like to create a new cluster in the same VLAN, first rename the file <code>discovery-url</code> that is found in the home root directory of the DHCP server, then provision a new CoreOS server following the above steps and it will create a
  different cluster.</p>
<p>If you wish to add the CoreOS server to an existing cluster, simply populate the <code>discovery-url</code> file found in the home root directory of the DHCP server with the correct discovery URL of the cluster you would like to add the server to. (You
  will need to ensure that the VLAN you set the DHCP and CoreOS server up in has connectivity to the other servers in the cluster for this to work.)</p>