{{{
  "title": "The AF CLI Tool: AppFog CLI Tool Manual",
  "date": "1-24-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>AF Tool</h3>
<p>The <em>af</em> gem is based on CloudFoundry's <em>vmc</em> gem but includes features specific to AppFog and has the default target set to AppFog's service. Check out the <a href="https://github.com/appfog/af">GitHub repo</a>.</p>
<ul>
<li><a href="#installation">Installation</a>
<ul>
<li><a href="installing-the-af-cli-tool-on-linux.md">Linux</a></li>
<li><a href="installing-the-af-cli-tool-on-mac-os-x.md">Mac OS X</a></li>
<li><a href="installing-the-af-cli-Tool-on-windows.md">Windows</a></li>
</ul>
</li>
<li><a href="#usage">Usage</a></li>
<li><a href="#af-cli-getting-started">General</a></li>
<li><a href="#apps">Apps</a>
<ul>
<li><a href="#app-creation">Application Creation</a></li>
<li><a href="#app-ops">Application Operations</a></li>
<li><a href="#app-updates">Application Updates</a></li>
<li><a href="#app-info">Application Information</a></li>
<li><a href="#app-download">Application Download</a></li>
<li><a href="#app-env">Application Environment</a></li>
<li><a href="#services">Services</a></li>
<li><a href="#admin">Administration</a></li>
<li><a href="#system">System</a></li>
<li><a href="#misc">Misc</a></li>
<li><a href="#help">Help</a></li>
</ul>
</li>
</ul>
<h2 id="installation">Installation</h2>
<p>The <em>af</em> command line tool is written in Ruby and installed as a gem.</p>
<p>We recommend using version 2.1 or older as some users have reported issues with Ruby 2.2 compiling.</p>
<h3><a href="installing-the-af-cli-tool-on-linux.md">Linux</a></h3>
<p>The gems can be installed manually, with Bundler, or alongside RVM. Click the link above for more detailed instructions.</p>
<h3><a href="installing-the-af-cli-tool-on-mac-os-x.md">Mac OS X</a></h3>
<p>Ostensibly, you should only have to use <code>gem install af</code> to install the gem on stock OS X. However, some users may need to use RVM to accomplish this. Please click on the link above for the detailed instructions.</p>
<h3><a href="installing-the-af-cli-Tool-on-windows.md">Windows</a></h3>
<p>There was a program created to handle the installation of Ruby. It comes with RubyGems built-in, with which you can install the <em>af</em> gem. Click the link above more detailed instructions.</p>
<h2 id="usage">Usage</h2>
<p>The AF Tool uses angle brackets <code>&lt;&gt;</code> for required input and square brackets <code>[]</code> for optional input.</p>
<pre>af [options] command [] [command_options]</pre>
<pre>Try 'af help [command]' or 'af help options' for more information.</pre>
<h2 id="af-cli-getting-started">General</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>target [url] </code></td>
<td>Reports current target or sets a new target</td>
</tr>
<tr>
<td><code>login [email] [--email, --passwd] </code></td>
<td>Login</td>
</tr>
<tr>
<td><code>info </code></td>
<td>System and account information</td>
</tr>
</tbody>
</table>
<h2 id="apps">Apps</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>apps </code></td>
<td>List deployed applications</td>
</tr>
</tbody>
</table>
<h3 id="app-creation"><a href="getting-started-overview.md">Creation</a></h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>push [appname] </code></td>
<td>Create, push, map, and start a new application.</td>
</tr>
<tr>
<td><code>push [appname] --infra </code></td>
<td>Push application to specificed infrastructure.</td>
</tr>
<tr>
<td><code>push [appname] --path </code></td>
<td>Push application from specified path.</td>
</tr>
<tr>
<td><code>push [appname] --url </code></td>
<td>Set the url for the application.</td>
</tr>
<tr>
<td><code>push [appname] --instances &lt;N&gt; </code></td>
<td>Set the expected number <code>&lt;N&gt;</code> of instances.</td>
</tr>
<tr>
<td><code>push [appname] --mem M </code></td>
<td>Set the memory reservation for the application.</td>
</tr>
<tr>
<td><code>push [appname] --runtime RUNTIME </code></td>
<td>Set the runtime to use for the application.</td>
</tr>
<tr>
<td><code>push [appname] --no-start </code></td>
<td>Do not auto-start the application.</td>
</tr>
<tr>
<td><code>push [appname] --no-resources</code></td>
<td>Do not check for existing resources. Useful workaround for 5XX errors during a push.</td>
</tr>
</tbody>
</table>
<h3 id="app-ops">Operations</h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>start &lt;appname&gt; </code></td>
<td>Start the application</td>
</tr>
<tr>
<td><code>stop &lt;appname&gt; </code></td>
<td>Stop the application</td>
</tr>
<tr>
<td><code>restart &lt;appname&gt; </code></td>
<td>Restart the application</td>
</tr>
<tr>
<td><code>delete &lt;appname&gt; </code></td>
<td>Delete the application</td>
</tr>
<tr>
<td><code>clone &lt;src-app&gt; &lt;dest-app&gt; [infra] </code></td>
<td>Clone the application and services</td>
</tr>
</tbody>
</table>
<h3 id="app-updates">Updates</h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>update &lt;appname&gt; [--path] [--no-resources]<br /></code></td>
<td>Update the application bits. For the "--no-resources" flag, see the push command above.</td>
</tr>
<tr>
<td><code>mem &lt;appname&gt; [memsize] </code></td>
<td>Update the memory reservation for an application</td>
</tr>
<tr>
<td><code>map &lt;appname&gt; &lt;url&gt; </code></td>
<td>Register the application to the url</td>
</tr>
<tr>
<td><code>unmap &lt;appname&gt; &lt;url&gt; </code></td>
<td>Unregister the application from the url</td>
</tr>
<tr>
<td><code>instances &lt;appname&gt; &lt;num|delta&gt; </code></td>
<td>Scale the application instances up or down</td>
</tr>
</tbody>
</table>
<h3 id="app-info">Information</h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>crashes &lt;appname&gt; </code></td>
<td>List recent application crashes</td>
</tr>
<tr>
<td><code>crashlogs &lt;appname&gt; </code></td>
<td>Display log information for crashed applications</td>
</tr>
<tr>
<td><code>logs &lt;appname&gt; [--all] </code></td>
<td>Display log information for the application</td>
</tr>
<tr>
<td><code>files &lt;appname&gt; [path] [--all] </code></td>
<td>Display directory listing or file download for path</td>
</tr>
<tr>
<td><code>stats &lt;appname&gt; </code></td>
<td>Display resource usage for the application</td>
</tr>
<tr>
<td><code>instances &lt;appname&gt; </code></td>
<td>List application instances</td>
</tr>
</tbody>
</table>
<h3 id="app-download">Download</h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>pull &lt;appname&gt; [path] </code></td>
<td>Downloads last pushed source to &lt;appname&gt; or [path]</td>
</tr>
<tr>
<td><code>download &lt;appname&gt; [path] </code></td>
<td>Downloads last pushed source to zipfile</td>
</tr>
</tbody>
</table>
<h3 id="app-env"><a href="environment-variables.md">Environment</a></h3>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>env &lt;appname&gt; </code></td>
<td>List application environment variables</td>
</tr>
<tr>
<td><code>env-add &lt;appname&gt; &lt;variable[=]value&gt; </code></td>
<td>Add an environment variable to an application</td>
</tr>
<tr>
<td><code>env-del &lt;appname&gt; &lt;variable&gt; </code></td>
<td>Delete an environment variable to an application</td>
</tr>
</tbody>
</table>
<h2 id="services">Services</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>services </code></td>
<td>Lists of services available and provisioned</td>
</tr>
<tr>
<td><code>create-service &lt;service&gt; [--name,--bind] </code></td>
<td>Create a provisioned service</td>
</tr>
<tr>
<td><code>create-service &lt;service&gt; --infra </code></td>
<td>Create a provisioned service on a specified infrastructure</td>
</tr>
<tr>
<td><code>create-service &lt;service&gt; &lt;name&gt; </code></td>
<td>Create a provisioned service and assign it &lt;name&gt;</td>
</tr>
<tr>
<td><code>create-service &lt;service&gt; &lt;name&gt; &lt;app&gt; </code></td>
<td>Create a provisioned service and assign it &lt;name&gt;, and bind to &lt;app&gt;</td>
</tr>
<tr>
<td><code>delete-service [servicename] </code></td>
<td>Delete a provisioned service</td>
</tr>
<tr>
<td><code>bind-service &lt;servicename&gt; &lt;appname&gt; </code></td>
<td>Bind a service to an application</td>
</tr>
<tr>
<td><code>unbind-service &lt;servicename&gt; &lt;appname&gt; </code></td>
<td>Unbind service from the application</td>
</tr>
<tr>
<td><code>clone-services &lt;src-app&gt; &lt;dest-app&gt; </code></td>
<td>Clone service bindings from &lt;src-app&gt; application to &lt;dest-app&gt;</td>
</tr>
<tr>
<td><code>export-service &lt;service&gt; </code></td>
<td>Export data from a specified service</td>
</tr>
<tr>
<td><code>import-service &lt;service&gt; &lt;url&gt; </code></td>
<td>Import data to a specified service</td>
</tr>
<tr>
<td><code>tunnel &lt;servicename&gt; [--port] </code></td>
<td>Create a local tunnel to a remote service</td>
</tr>
<tr>
<td><code>tunnel &lt;servicename&gt; &lt;clientcmd&gt; </code></td>
<td>Create a local tunnel to a remote service and start a local client</td>
</tr>
</tbody>
</table>
<h2 id="admin">Administration</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>user </code></td>
<td>Display user account information</td>
</tr>
<tr>
<td><code>passwd </code></td>
<td>Change the password for the current user</td>
</tr>
<tr>
<td><code>logout </code></td>
<td>Logs current user out of the target system</td>
</tr>
<tr>
<td><code>add-user [--email, --passwd] </code></td>
<td>Register a new user (requires admin privileges)</td>
</tr>
<tr>
<td><code>delete-user &lt;user&gt; </code></td>
<td>Delete a user and all apps and services (requires admin privileges)</td>
</tr>
</tbody>
</table>
<h2 id="system">System</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>runtimes </code></td>
<td>Display the supported runtimes of the target system</td>
</tr>
<tr>
<td><code>frameworks </code></td>
<td>Display the recognized frameworks of the target system</td>
</tr>
<tr>
<td><code>infras </code></td>
<td>Display the available infrastructures</td>
</tr>
</tbody>
</table>
<h2 id="misc">Misc</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>aliases </code></td>
<td>List aliases</td>
</tr>
<tr>
<td><code>alias &lt;alias[=]command&gt; </code></td>
<td>Create an alias for a command</td>
</tr>
<tr>
<td><code>unalias &lt;alias&gt; </code></td>
<td>Remove an alias</td>
</tr>
<tr>
<td><code>targets </code></td>
<td>List known targets and associated authorization tokens</td>
</tr>
</tbody>
</table>
<h2 id="help">Help</h2>
<table class="table table-bordered table-striped">
<tbody>
<tr>
<td><code>help [command] </code></td>
<td>Get general help or help on a specific command</td>
</tr>
<tr>
<td><code>help options </code></td>
<td>Get help on available options</td>
</tr>
</tbody>
</table>
<h2 id="troubleshooting">Troubleshooting</h2>
<p><a href="i-am-having-trouble-updating-my-application.md">I am having trouble updating my application.</a><br /> <a href="push-pull-and-update-commands.md">Push, Pull, and Update Commands</a></p>
