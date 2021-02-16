{{{
  "title": "Using Group Tasks to Install Software and Run Scripts on Groups",
  "date": "10-14-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong><strong>Last updated: &nbsp;Thu 10/8/2014 11:24 PST</strong></strong>
</p>
<p><strong>Description:</strong>
</p>
<p>Administrators use Lumen Cloud Blueprints to create templates for servers or entire environments. One valuable stage of this process is where users can select software or script packages to apply to the server(s). This capability helps administrators
  quickly prepare servers for their intended use. However, if an administrator wishes to install software on multiple servers after they have been provisioned, they either need to create a new blueprint that does this, or, use the&nbsp;<strong>Execute Package</strong>&nbsp;feature
  that lets users select a package to run against any or all of the servers in a particular Group.&nbsp;<strong>This is useful for performing tasks such as joining an entire set of servers to a domain, installing a new performance monitoring agent, or adding a software patch to a subset of machines.&nbsp;</strong>Packages
  execute against&nbsp;servers whether they are running or not. For servers that are not running, the service puts the server into a running state, executes the package, then restores the server to its previous state.</p>
<p><strong>Steps:</strong>
</p>
<p><strong>1. Navigate to a Group of Servers</strong>
  <p>Using the left navigation menu choose Infrastructure > Servers.
  <p>Locate the Group that contains servers that needs a bulk script or software installation. In the example below, the Group is named “Application Servers.”&nbsp;
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/jqJrgUtppupA68Z3wyjiKm9HX/?name=app-servers-group.png" alt="app-servers-group.png" />
  </li>
</ul>
<p><strong>2. Execute Package from Group actions menu</strong>
</p>
<ul>
  <li>Hover over the "actions" menu and choose the “execute package” option.&nbsp;
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/HN1Wwjw9zsjc494RKhTJr3zfS/?name=execute-package-menu.png" alt="execute-package-menu.png" />
  </li>
  <li>Select a package to apply to the servers in this group. You can view all packages, or filter based on visibility or name.&nbsp;
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/Q8GK3LLhITVJPOVrqJsC8bPXS/?name=select-package.png" alt="select-package.png" />
  </li>
  <li>After selecting a package, the description will appear along with a place to enter values for all the parameters defined the package, if there are any. Fill out all the fields then continue to scroll down.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/wqtdfIrjHOCoMu4Dm8TVpO5Hw/?name=parameters.png" alt="parameters.png" />
  </li>
  <li>Choose which of the servers in the Group will have the package installed. Only servers built from the package's supported OS templates will show as selectable. Once the server(s) have been selected, click "execute package" to begin the installation.
    <br
    />
    <br /><img src="https://t3n.zendesk.com/attachments/token/hYZhmMpiLuE2kZTbuoidYV6GI/?name=select-servers.png" alt="select-servers.png" />
  </li>
  <li>The Lumen Cloud Control Portal creates a Blueprint and runs the designated package on the selected machines.&nbsp;
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/UDIBiWIJNjnUUjTGLpVqIZvvA/?name=execute-package-queue.png" alt="execute-package-queue.png" />
  </li>
</ul>
<p><strong>3. Confirm Group Task Completion</strong>
</p>
<ul>
  <li>Navigate to the server details for one of the servers affected by the package execution. Grab the IP address of the server.</li>
  <li>Start the OpenVPN client and open up a secure connection to the Lumen Cloud.</li>
  <li>Initiate a Remote connection into the server. For Windows machines, use the RDP client.</li>
  <li>Confirm the package was run successfully.</li>
</ul>
