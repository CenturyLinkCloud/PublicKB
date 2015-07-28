{{{
  "title": "Platform Specific: AF CLI Installation Issues",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Some users have been receiving an SSL certificate error when attempting to install the AF CLI tool. Please note that this error has nothing to do with us, but it rather has to do with an SSL certificate issue with <a href="af-cli-installation-issues.md">RubyGems</a>. They are aware of it and are working on a resolution.</p>
<h4>Here are a few suggestions for how to work around it.</h4>
<ol>
<li>Try this first:<br />
<pre>$ sudo gem install af --source http://rubygems.org</pre>
</li>
<li>If the first suggestion does not work, try the following.
<ol>
<li>Download the Ruby installer from <a href="http://rubyinstaller.org/downloads/">http://rubyinstaller.org/downloads/</a></li>
<li>Then download the version that matches the installer.</li>
</ol>
<p>Once you have unzipped both of those files locally, run the below commands:</p>
<pre>$ sudo gem update --system<br />$ sudo gem install af</pre>
</li>
<li>Finally, if neither of those work, try:<br />
<pre>$ sudo gem source -r https://rubygems.org<br />$ sudo gem source -a http://rubygems.org<br />$ sudo gem install af</pre>
<p>(<strong>Note</strong>: The first line will remove the SSL version of ruby gems.)<br />(<strong>Note</strong>: The second line of code will install the non-secure version of ruby gems and will give you a warning about it being insecure. Please consider how it may affect the rest of your system prior to implementing this.)</p>
</li>
</ol>
