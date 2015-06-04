{{{
  "title": "Platform Specific: How To Manage Multiple Ruby Versions on Windows",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Windows users can install Uru to manage multiple versions of Ruby. The repository and more detailed instructions can be found here: <a href="https://bitbucket.org/jonforums/uru">https://bitbucket.org/jonforums/uru</a></p>
<ol>
<li>Windows 8.1 was used when creating this tutorial and uses the Chocolatey package manager which can be found at: <a href="https://chocolatey.org">https://chocolatey.org/</a></li>
<li>Download the <a href="https://bitbucket.org/jonforums/uru/wiki/Downloads"> uru.0.7.7.nupkg</a> packag</li>
<li>Open an administrative level cmd.exe or powershell shell</li>
<li>Change to the directory which contains uru's *.nupkg file</li>
<li>Execute <code>choco install uru -source %CD% if using cmd.exe</code><br />Execute <code>choco install uru -source $PWD If using powershell</code></li>
<li>Close your admin level shell and open a new, non-admin cmd.exe or powershell shell</li>
<li>Start using uru and your registered rubies</li>
<li>This site provides the <a href="https://bitbucket.org/jonforums/uru/wiki/Examples"> Uru manual</a></li>
<li>Here are some sample commands:</li>
</ol>
<ul>
<li>List registered Rubies:
<p><code>uru ls</code></p>
</li>
<li>Register a Ruby:
<p><code>uru admin add C:\ruby200\bin</code></p>
</li>
<li>Use a different Ruby: <code>$ uru 174</code> <code> ---&gt; Now using jruby 1.7.4 tagged as `174`</code></li>
</ul>
