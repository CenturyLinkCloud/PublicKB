{{{
  "title": "Using Group Tasks to Install Software and Run Scripts on Groups",
  "date": "10-26-2021",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>Administrators use Lumen Cloud Blueprints to create templates for servers or entire environments. One valuable stage of this process is where users can select software or script packages to apply to the server(s). This capability helps administrators
  quickly prepare servers for their intended use. However, if an administrator wishes to install software on multiple servers after they have been provisioned, they either need to create a new blueprint that does this, or use the&nbsp;<strong>Execute Package</strong>&nbsp;feature
  that lets users select a package to run against any or all of the servers in a particular Group.</p>
  
  <p><strong>This is useful for performing tasks such as joining an entire set of servers to a domain, installing a new performance monitoring agent, or adding a software patch to a subset of machines.&nbsp;</strong>Packages
  execute against&nbsp;servers whether they are running or not. For servers that are not running, the service puts the server into a running state, executes the package, and then restores the server to its previous state.</p>
<p><strong>Steps:</strong>
</p>
<p><strong>1. Navigate to a Group of Servers</strong>.
  <p>Using the left navigation menu choose Infrastructure > Servers.
  <p>Locate the Group that contains servers that need a bulk script or software installation.
    <br />
  </li>
</ul>
<p><strong>2. Execute Package from Group actions menu</strong>.
</p>
<ul>
  <li>Hover over the "actions" menu and choose the “execute package” option.&nbsp;
    <br />
  </li>
  <li>Select a package to apply to the servers in this group. You can view all packages, or filter based on visibility or name.&nbsp;
    <br />
  </li>
  <li>After selecting a package, the description will appear along with a place to enter values for all the parameters defined the package, if there are any. Fill out all the fields, and then continue to scroll down.
    <br />
  </li>
  <li>Choose which of the servers in the Group will have the package installed. Only servers built from the package's supported OS templates will show as selectable. Once the server(s) have been selected, click "execute package" to begin the installation.
    <br/>
  </li>
  <li>The Lumen Cloud Control Portal creates a Blueprint and runs the designated package on the selected machines.&nbsp;
    <br />
  </li>
</ul>
<p><strong>3. Confirm Group Task Completion</strong>
</p>
<ul>
  <li>Navigate to the server details for one of the servers affected by the package execution. Grab the IP address of the server.</li>
  <li>Start the OpenVPN client and open up a secure connection to the Lumen Cloud.</li>
  <li>Initiate a Remote connection into the server. For Windows machines, use the RDP client.</li>
  <li>Confirm that the package was run successfully.</li>
</ul>
