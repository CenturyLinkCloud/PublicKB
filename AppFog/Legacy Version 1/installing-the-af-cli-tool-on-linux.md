{{{
  "title": "Platform Specific: Installing the AF CLI Tool on Linux",
  "date": "1-22-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><em> <strong>UPDATE</strong>: Finally! The new <code>af</code> gem no longer requires your system Ruby version to be between 1.8.7 and 1.9.3, and you no longer need to install the <code>caldecott</code> gem! This article has been updated to reflect this. </em></p>
<hr />
<p>This article describes how to install the CLI tool in Linux. There are also instructions for installing it using <a href="#bundler">Bundler</a> or <a href="#rvm">RVM</a>, if you'd prefer.</p>
<h2>Installing the CLI Tool Manually</h2>
<p>Dependencies include:</p>
<ul>
<li><em>ruby1.9.3</em></li>
<li><em>rubygems</em> and/or <em>rubygems-integration</em></li>
<li><em>ruby-dev</em></li>
<li><em>openssl</em></li>
<li><em>libstd++</em> or <em>libstdc++6</em></li>
<li><em>libssl-dev</em></li>
<li><em>g++</em></li>
<li><em>libmysql-ruby</em> or <em>ruby-mysql</em></li>
<li>the latest <em>eventmachine</em> Ruby gem
<ul>
<li><code>gem install eventmachine</code></li>
</ul>
</li>
</ul>
<p>Ensure you have the above dependencies satsified, then try to install the <em>af</em> gem:</p>
<p><code>sudo gem install af</code></p>
<p><em>Note: You may need to append it with <code>--source https://rubygems.org</code></em>.</p>
<p><em>Note: If you have issues with tunneling, you may need to reinstall the </em>eventmachine<em> gem after installing the </em>libssl-dev<em> package.</em></p>
<h2><a name="rvm"></a>Installing the CLI Tool Using RVM</h2>
<p><a href="https://rvm.io">RVM</a> is a version management package for systems that need more that one version of Ruby. Below are the instructions on how to set it up.</p>
<h4>Step I: Install the stable version RVM.</h4>
<ol>
<li>Add the proper key using the command below.<br />
<pre>gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3</pre>
</li>
<li>Install RVM and a stable version of Ruby with <a href="http://curl.haxx.se/docs/">cURL</a> as follows.<br />
<pre>curl -sSL https://get.rvm.io | bash -s stable</pre>
</li>
</ol>
<p>Note: I <em>did not</em> use <code>sudo</code> for this. That is best practice to prevent the need to use it when making CLI commands.</p>
<h4>Step II: Activate RVM.</h4>
<p>If you noticed during the installation of RVM, it said:</p>
<blockquote>To start using RVM you need to run `source /home/af/.rvm/scripts/rvm`</blockquote>
<p>So you will use the following in your current shell window.</p>
<pre>source ~/.rvm/scripts/rvm</pre>
<h4>Step III: Install the AF gem.</h4>
<pre>gem install af</pre>
<p>If you run into issues, check out the <a href="http://rubygems.org/gems/af">gem's page</a> and ensure you have all the dependencies installed (e.g., if you receive an error saying, "rdoc requires json" try <code>gem install json</code>.).</p>
<p><em>You should be good to go! Use <code>af login</code> to access the CLI tool and use <code>af help</code> to get a list of commands. Don't forget to prepend your them with <code>af</code>!</em></p>
<h2><a name="bundler"></a>Installing the CLI Tool Using Bundler</h2>
<p><a href="http://bundler.io/">Bundler</a> is a gem that manages installation of other gems. Below is the instructions on how to set it up.</p>
<h4>Step I: Install and configure Bundler</h4>
<ol>
<li>Install the Bundler gem with this command:<br />
<pre>sudo gem install bundler</pre>
</li>
<li>Edit your Gemfile and add in the AF and Caldecott gems. It should include the following.
<pre>source "https://rubygems.org"<br />gem 'af'</pre>
<p>The Gemfile is usually located under your home folder, but you can also use the command below. It may take a minute to find it.</p>
<pre>sudo find / -name Gemfile | grep -e Gemfile</pre>
</li>
</ol>
<h4>Step II: Installing the AF gem.</h4>
<p>Using Bundler:</p>
<pre>bundle install</pre>
<p><em>You should be good to go! Use <code>af login</code> to access the CLI tool and use <code>af help</code> to get a list of commands. Don't forget to prepend your them with <code>af</code>!</em></p>
