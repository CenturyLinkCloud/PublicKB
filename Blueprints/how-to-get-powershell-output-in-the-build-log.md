{{{
  "title": "How to Get PowerShell Output in the Build Log",
  "date": "11-11-2014",
  "author": "Bryan Dreyer",
  "attachments": []
}}}

<h3>Description (goal/purpose)</h3>
<p>When using Blueprint scripts, you can choose to use one of two&nbsp;execution&nbsp;modes: PowerShell or Command.&nbsp; If you use the PowerShell execution mode, the package will execute via Remote PowerShell in an un-hosted scripting environment.&nbsp;
  By design, Remote PowerShell returns data as an object,&nbsp; the un-hosted environment doesn't understand these objects so it's not possible to return that data into the build log.&nbsp; You can log any output directly to your server and gather it
  later, or you can use the information below to change your script package to run in Command execution mode.</p>
<h3>Audience</h3>
<ul>
  <li>All Users of the Platform</li>
</ul>
<h3>Additional Information</h3>
<p>Script Package&nbsp;Basics: &nbsp;<a href="https://t3n.zendesk.com/entries/20348448-Blueprints-Script-and-Software-Package-Management">https://t3n.zendesk.com/entries/20348448-Blueprints-Script-and-Software-Package-Management</a>
</p>
<h3>Detailed Information</h3>
<p>The scripting environment used for the Command execution mode can run PowerShell scripts as well.&nbsp; However, PowerShell executes as it's own process within the environment and the environment will continue to wait (essentially hanging) unless you
  start the PowerShell script in the specific way outlined below.</p>
<p>&nbsp;</p>
<p><em>***Please note, this&nbsp;post is provided for informational purposes only and&nbsp;that changes like this have NOT been extensively tested against&nbsp;existing PowerShell scripts or various types of PowerShell Command Outputs. ***</em>
</p>
<p>Make the following changes to your package manifest:</p>
<p><em>&lt;Mode&gt;Command&lt;/Mode&gt;</em>
</p>
<p><em>&lt;Command&gt;cmd /c "echo . | powershell ./install.ps1" ${Arg}&lt;/Command&gt;</em>
</p>
<p>&nbsp;</p>