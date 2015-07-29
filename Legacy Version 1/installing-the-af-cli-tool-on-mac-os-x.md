{{{
  "title": "Platform Specific: Installing the AF CLI Tool on Mac OS X",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>We recommend using version 2.0 or older as some users have reported issues with Ruby 2.2 compiling.</p>
<pre><code>$ gem install af
</code></pre>
<ul>
<ul>
<ul>
<li><strong>OSX Yosemite Users:</strong>
<ul>
<li>System Ruby has changed with an update to Yosemite; however, using system Ruby to install the af gem can result in permissions errors.</li>
<li>A fresh install of Yosemite and using the iCloud user as the admin may also break the permissions of your home folder.</li>
<li>It is recommended that you use RVM as your Ruby version manager to get around these issues.</li>
<li>Follow the instructions below beginning at step 4.</li>
</ul>
</li>
<li>If you're on Mac OS X 10.7 Lion and you're having trouble, you will need to do the following:</li>
<ol>
<li>
<p>Install Xcode 4.3 and the Xcode command line tools (use the <em>downloads</em> preference pane to download the command line tools).</p>
</li>
<li>
<p>Install <a href="https://github.com/Homebrew/homebrew/blob/master/share/doc/homebrew/Installation.md#installation">Homebrew</a>.</p>
</li>
<li>
<p>Install <em>libksba</em> with Homebrew.</p>
<pre>$ brew install libksba</pre>
</li>
<li>
<p>Install <a href="https://rvm.io/rvm/install/">RVM</a>.</p>
</li>
<li>
<p>Install Ruby.</p>
<pre>$ rvm install ruby</pre>
</li>
<li>
<p>Check or change the version of Ruby being used.</p>
<pre>$ rvm list
$ rvm use &lt;ruby version&gt;</pre>
</li>
<li>
<p>Check your <em>.bash_profile</em> and verify RVM is loading <strong>after</strong> system ruby. Look for this line at the <strong>end</strong> of the file.</p>
<pre>[[ -s "$HOME/.rvm/scripts/rvm" ]]; source "$HOME/.rvm/scripts/rvm"<br /> # Load RVM into a shell session *as a function*</pre>
</li>
<li>
<p>Install <em>af.</em></p>
<pre>$ gem install af
$ af login</pre>
</li>
</ol>
</ul>
</ul>
</ul>
