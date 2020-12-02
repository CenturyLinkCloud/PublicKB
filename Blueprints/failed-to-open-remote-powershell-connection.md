{{{
  "title": "Failed to open Remote PowerShell connection",
  "date": "4-7-2014",
  "author": "Bryan Dreyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
Your Windows Server must be properly configured in order for PowerShell based Blueprints to successfully run against it. Most images are already configured properly, however if you receive an error about failing to open the Remote PowerShell connection, the following KB article may help you resolve the issue.

### Audience
* All users of Lumen Cloud

### Prerequisites
* None

### Additional Information
The full error message in your failed Blueprint may look something like the following:

```
[Error] Could not run package: System.ApplicationException: Failed to open Remote PowerShell connection after %time% seconds ---&gt; System.Management.Automation.Remoting.PSRemotingTransportException: Connecting to remote server %serverIP% failed with the following error message : WinRM cannot complete the operation. Verify that the specified computer name is valid, that the computer is accessible over the network, and that a firewall exception for the WinRM service is enabled and allows access from this computer. By default, the WinRM firewall exception for public profiles limits access to remote computers within the same local subnet. For more information, see the about_Remote_Troubleshooting Help topic.

[STACK TRACE]
...
[/STACKTRACE]
```

### How to Resolve
While PowerShell based Blueprints fail, command based Blueprints will not. There is a public script package that contains the necessary commands properly configure WinRM. The package is called *Enable Powershell 2.0 Remoting*. From the *group tasks* drop-down on the Group information page you can choose to *execute script*, then find the script to execute, and apply it to the necessary machines.

### Detailed Steps
1. Navigate to the group details page that contains the server(s) you need to fix.
2. Hover over the *group tasks* button and select *execute script*.
3. In the search box, start typing *Enable Powershell 2.0 Remoting* then click the entry to check it, and select *Add*.
4. Check the box next to the server(s) you need to deploy too and click OK.
5. Once the Blueprint completes, you should be able to process PowerShell based Blueprints.
