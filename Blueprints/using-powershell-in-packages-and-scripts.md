{{{
  "title": "Using PowerShell in Packages and Scripts",
  "date": "5-31-2015",
  "author": "Ted Henley",
  "attachments": [],
  "contentIsHTML": false
}}}

### Related
* [Understanding the Difference Between Templates, Blueprints and Packages](understanding-the-difference-between-templates-blueprints-and-packages.md)
* [Building Windows 2012 Script Packages](building-windows-2012-script-packages.md)


### Overview

When creating packages and scripts, there are many different options.  This article offers some guidance on using PowerShell as your scripting language.

* Be sure to set the execution mode to "PowerShell" in the package.manifest.
* Avoid use of console commands, such as Write-Host.  These will cause your scripts to fail when run in a script or package.
* Scripts are executed from a temporary directory.  Any files you output, such as logs should be written to a directory in another directory.  Alternatively, you can set a flag in the package to [make the directory permanent](blueprints-script-and-software-package-management.md).
* The built-in methods to encrypt passwords and data does not typically work as the key changes for each system.
* Specify the PowerShell version required in the script to ensure it only runs if that version is present.  This is particularly important if you are using the API with the Invoke-RestMethod as it requires version 3.
* Use error trapping and logging to determine if the script executed properly.  
* Using "exit 0" in a script will tell the platform it was successful.  Any other exit codes are considered failures.
