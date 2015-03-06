{{{
  "title": "Failed to open Remote PowerShell connection",
  "date": "4-7-2014",
  "author": "Bryan Dreyer",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description (goal/purpose)</h3>
<p>Your Windows Server must be properly configured in order for PowerShell based blueprints to successfully run against it. Most images are already configured properly, however if you receive an error about failing to open the Remote PowerShell connection,
  the following KB article may help you resolve the issue.</p>
<h3>Audience</h3>
<ul>
  <li>All users of CLC</li>
</ul>
<h3>Prerequisites</h3>
<ul>
  <li>What are pre-reqs to running a script based blueprint?</li>
</ul>
<h3>Additional Information</h3>
<p>The full error message in your failed blueprint may look something like the following:</p>

```
[Error] Could not run package: System.ApplicationException: Failed to open Remote PowerShell connection after %time% seconds ---&gt; System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server %serverIP% failed with
  the following error message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that the computer is accessible over the network, and that a firewall exception for the WinRM service is enabled and allows access from
  this computer. By default, the WinRM firewall exception for public profiles limits access to remote computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic.
  
[STACK TRACE]
...
[/STACKTRACE]
```

<h3>How to Resolve</h3>
<p>While PowerShell based blueprints fail, command based blueprints will not. There is a public script package that contains the necessary commands properly configure WinRM. The package is called&nbsp;<em>Enable Powershell 2.0 Remoting</em>. From the g<em>roup tasks</em> dropdown on the Group information page you can choose to <em>execute script</em>, then find the script to execute, and apply it to the necessary machines.</p>
<h3>Detailed Steps</h3>
<ol>
  <li>Navigate to the group details page that contains the server(s) you need to fix</li>
  <li>Hover over the <em>group tasks</em> button and select <em>execute script</em>
  </li>
  <li>In the search box, start typing <em>Enable Powershell 2.0 Remoting</em> then click the entry to check it, and select <em>Add</em>
  </li>
  <li>Check the box next to the server(s) you need to deploy too and click OK.</li>
  <li>Once the blueprint completes, you should be able to process PowerShell based blueprints.</li>
</ol>
