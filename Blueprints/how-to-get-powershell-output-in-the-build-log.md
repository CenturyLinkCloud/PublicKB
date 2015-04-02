{{{
  "title": "How to Get PowerShell Output in the Build Log",
  "date": "11-11-2014",
  "author": "Bryan Dreyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

When using Blueprint scripts, you can choose to use one of two execution modes: PowerShell or Command. If you use the PowerShell execution mode, the package will execute via Remote PowerShell in an un-hosted scripting environment. By design, Remote PowerShell returns data as an object,  the un-hosted environment doesn't understand these objects so it's not possible to return that data into the build log. You can log any output directly to your server and gather it later, or you can use the information below to change your script package to run in Command execution mode.</p>

### Audience

* All Users of the Platform

### Additional Information

Script Package Basics: [Blueprint Package Management](../Blueprints/blueprints-script-and-software-package-management.md)


### Detailed Information

The scripting environment used for the Command execution mode can run PowerShell scripts as well. However, PowerShell executes as it's own process within the environment and the environment will continue to wait (essentially hanging) unless you start the PowerShell script in the specific way outlined below.</p>

***Please note, this post is provided for informational purposes only and that changes like this have NOT been extensively tested against existing PowerShell scripts or various types of PowerShell Command Outputs. ***

Make the following changes to your package manifest:

```
<Mode>Command</Mode>
<Command>cmd /c "echo . | powershell ./install.ps1" ${Arg}</Command>
```
