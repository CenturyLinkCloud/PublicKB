{{{
  "title": "Getting Started With AppFog v1: Application Configuration Using Manifest Files and AFIgnore",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>When creating an application on AppFog you may need to save settings that will be applied when it is deployed. The main configuration files that are applicable are the application manifest and .afignore.</p>
<p><a href="#app_manifest">Application Manifest</a><br /> <a href="#create_manifest">Creating a Manifest</a><br /> <a href="#child_manifest">Child Manifests</a><br /> <a href="#symbol_res">Symbol Resolution</a><br /> <a href="#multi_manifest">Multi-App Manifests</a><br /> <a href="#zip_files">ZIP Files</a></p>
<h3 id="app_manifest">Application Manifest</h3>
<p>You can use manifest documents with AppFog to simplify app deployment. These manifest documents describe apps in human-editable format. <span class="wysiwyg-font-size-medium wysiwyg-font-size-small">They</span> can also describe anything from simple "Hello World" apps to complex multi-app hierarchies with inter-app dependencies and service binding information.</p>
<p>The manifests feature uses a YAML document, aptly named <code>manifest.yml</code>. You'll typically place this manifest document in your app’s root directory, though you can specify a different location by telling the <code>af</code> tool which to use with the <code>-m</code> flag.</p>
<p>You can create the manifest by hand, or let <code>af</code> automatically create it for you after an <code>af push</code> or with the <code>af manifest</code> command.</p>
<p>When you <code>af push</code> an app that has a manifest, <code>af</code> will simply read the input values from the file rather than prompt you for each configuration.</p>
<p>Not only can you automate <code>af push</code> with manifests, you can also bypass interactive inputs for a large portion of <code>af</code>'s commands to make using the command-line tool more efficient and user-friendly. For example, you can leave the app name out when issuing an <code>af update</code> command, and <code>af</code> will retrieve the app name from an existing manifest document.</p>
<p>Here’s the full list of commands that can take advantage of the manifest document:</p>
<ul>
<li><code>af push</code>: Allows you to specify multiple services. Pushes with information from the manifest. If no manifest is found, it will ask if you want to create one after the interaction is finished.</li>
<li><code>af stats</code>, <code>af update</code>, <code>af start</code>, <code>af stop</code>: If no app name is given, it operates on the app(s) described by the manifest.</li>
<li><code>af update</code>: Syncs changes from the root of the app if a manifest is present.</li>
<li><code>af start</code>: Starts the app in a multi-app deployment in the proper order (taking dependencies into account).</li>
<li><code>af stop</code>: Stops multi-app deployments by shutting down each app in the reverse of the order in which they were started.</li>
<li><code>af restart</code>: See <code>af stop</code> and <code>af start</code>.</li>
<li><code>af delete</code>: Delete the app</li>
</ul>
<p>Note: For multi-app hierarchies, these will operate only on the sub-app you’re in, rather than always operating on every app in the hierarchy. To operate on every app, invoke the command from the root of the hierarchy.</p>
<h3 id="create_manifest">Creating a Manifest</h3>
<p>The easiest way to get going is to generate a manifest document from basic app info. If you haven’t pushed your app yet, you can start with <code>af push</code> as usual, which will ask if you want to save the configurations as a manifest document:</p>
<pre>$ af push
Would you like to deploy from the current directory? [Yn]:
Application Name: php-example
Detected a PHP Application, is this correct? [Yn]:
Application Deployed URL [php-example.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'php-example'? [yN]:
Create services to bind to 'php-example'? [yN]: y
1: mongodb
2: mysql
3: postgresql
What kind of service?: 2
Specify the name of the service [mysql-example]:
Create another? [yN]:
Would you like to save this configuration? [yN]: y
Manifest written to manifest.yml.
Creating Application: OK
Creating Service [mysql-example]: OK
Binding Service [mysql-example]: OK
Uploading Application:
  Checking for available resources: OK
  Packing application: OK
  Uploading (1K): OK
Push Status: OK
Staging Application 'php-example': OK
Starting Application 'php-example': OK
</pre>
<p>As you can see, just before pushing, we saved the deployment configurations in <code>manifest.yml</code> in the same directory. Let’s take a peek at the file:</p>
<pre>---
applications:
  .:
    name: php-example
    framework:
      name: php
      info:
        mem: 128M
        description: PHP Application
        exec:
    url: ${name}.${target-base}
    mem: 128M
    instances: 1
    services:
      mysql-398b1:
        type: mysql
</pre>
<p>The manifest document has captured all of the configuration that we entered above for the app push into a description of the app deployment. Once you have a <code>manifest.yml</code> file, you can modify it however you'd like, as it’s meant to be human-editable. The structure of the document is freeform, so if you want to define arbitrary values and use them throughout your document, you can.</p>
<p>Now if we try pushing again, <code>af push</code> will use this to automate everything:</p>
<pre>$ af delete php-example
Provisioned service [mysql-398b1] detected, would you like to delete it? [yN]: y
Deleting application [php-example]: OK
Deleting service [mysql-398b1]: OK

$ af push
Would you like to deploy from the current directory? [Yn]:
Pushing application 'php-example'...
Creating Application: OK
Creating Service [mysql-398b1]: OK
Binding Service [mysql-398b1]: OK
Uploading Application:
  Checking for available resources: OK
  Packing application: OK
Uploading (1K): OK
Push Status: OK
Staging Application 'php-example': OK
Starting Application 'php-example': OK
</pre>
<p>You can also use <code>af manifest</code> to create a manifest without pushing. <code>af manifest</code> will let you create more complex manifests describing multiple applications in a single hierarchy.</p>
<p>Now that you have a manifest document, you don’t really have to do anything else if you don’t want to get fancy. It’ll passively improve <code>af</code>’s user interface experience for the commands listed above: <code>af push</code> will be interaction-free, making deployment much easier, and many other commands will be efficient to invoke.</p>
<h3 id="child_manifest">Child Manifests</h3>
<p>A manifest document can inherit properties from a parent manifest like so:</p>
<pre>inherit: path/to/parent.yml</pre>
<p>This slurps in everything from the parent document ensuring that properties defined in the child manifest are deep-merged with the parent. The symbols are resolved after this merge has taken place, so any properties you set in the child manifest may be used in properties set in the parent.</p>
<p>This allows you to provide the basic information, such as service bindings and framework information, in a "base" manifest, which can be "filled in" via a child manifest. For example:</p>
<ul>
<li>Having various child manifests for different deployment modes (e.g. debug, local, public) that extend base app information provided by a "base" manifest.</li>
<li>Packaging the basic configuration along with your app, which users can extend with their own manifest to override your settings or fill in the blanks for their own deployment.</li>
</ul>
<h3 id="symbol_res">Symbol Resolution</h3>
<p>There are currently two special symbols:</p>
<ul>
<li><code>target-base</code>: The base URL of your target. For example, targeting <code>api.appfog.com</code> means a <code>target-base</code> value of <code>appfog.com</code>.</li>
<li><code>random-word</code>: A random string of characters. This is useful for making sure your URLs are unique.</li>
</ul>
<p>Otherwise, symbol resolution simulates lexical scoping, so you can define arbitrary properties, which can be overridden by child manifests or in a nested hash.</p>
<p>For example, the following parent:</p>
<pre>applications:
  ./foo:
    name: bar
    url: ${name}.${target-base}
</pre>
<p>...combined with this child manifest:</p>
<pre>applications:
  ./foo:
    name: baz
</pre>
<p>...and with a target of <code>api.appfog.com</code>, will result in a <code>url</code> of <code>baz.appfog.com</code> when using the child manifest, and <code>bar.appfog.com</code> when using the parent.</p>
<h3 id="multi_manifest">Multi-App Manifests</h3>
<p>Manifests also present a way to deploy multiple apps with a single push command. Let’s say you have a modular app comprised of several independent parts, for example, a publisher and a subscriber. You’ll want the subscriber to start before the publisher, so it doesn’t miss anything that was published. It’s best to have these two apps defined as parts of a whole, so you can specify this dependency. You can do this with multi-app manifest documents.</p>
<p>Our <code>publisher</code> app will publish messages every second, with the message starting at 0 and increasing for every iteration. The subscriber will simply collect the messages it receives in the order they came in, and display them to the user.</p>
<p>To start with, you may want to arrange your apps like so:</p>
<pre>./parent-app
./parent-app/publisher
./parent-app/subscriber
</pre>
<p>This will make using the manifest document more natural.</p>
<p>Switch to the <code>parent-app</code> directory and use <code>af manifest</code> to create your manifest document:</p>
<pre>$ cd parent-app
parent-app $ af manifest
Configure for which application? [.]: ./publisher
Application Name: publisher
Detected a PHP Application, is this correct? [Yn]:
Application Deployed URL [publisher.aws.af.cm]: publisher-${random-word}.${target-base}
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'publisher'? [yN]:
Create services to bind to 'publisher'? [yN]: y
1: mongodb
2: mysql
3: postgresql
What kind of service?: 2
Specify the name of the service [mysql-example]:
Create another? [yN]:
Configure for another application? [yN]: y
Application path?: ./subscriber
Application Name: subscriber
Detected a PHP Application, is this correct? [Yn]:
Application Deployed URL [subscriber.aws.af.cm]: subscriber-${random-word}.${target-base}
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'subscriber'? [yN]: y
1: mysql-example
Which one?: 1
Bind another? [yN]:
Create services to bind to 'subscriber'? [yN]:
Manifest written to manifest.yml.
</pre>
<p>In this single interactive session we’ve configured a manifest that defines two PHP apps, using a single MySQL service. We’re using URLs with a bit of randomness (provided by the special random-word symbol) to ensure uniqueness.</p>
<p>There’s one thing missing, though. We didn’t specify any dependencies between the apps. If we were to start it now, we could lose some data if the publisher starts before the subscriber:</p>
<pre>parent-app $ af push
Would you like to deploy from the current directory? [Yn]:
Pushing application 'publisher'...
# ...
Starting Application 'publisher': OK
Pushing application 'subscriber'...
# ...
Starting Application 'subscriber': OK

parent-app $ curl subscriber-bf872.aws.af.cm
Received: ["5", "6", "7", "8", "9"]
</pre>
<p>As you can see, we’ve lost some data here. In the time between the publisher starting and the subscriber starting, the subscriber has missed four messages.</p>
<p>We can fix this by editing the <code>manifest.yml</code> document to indicate that the publisher depends on the subscriber being started:</p>
<pre>---
applications:
./publisher:
# ...
depends-on: ./subscriber
./subscriber:
# ...
</pre>
<p>Now let’s delete both apps and retry.</p>
<pre>parent-app $ af delete publisher
Deleting application [publisher]: OK

parent-app $ af delete subscriber
Deleting application [subscriber]: OK

parent-app $ af push
Would you like to deploy from the current directory? [Yn]:
Pushing application 'subscriber'...
# ...
Starting Application 'subscriber': OK
Pushing application 'publisher'...
# ...
Starting Application 'publisher': OK
</pre>
<p>As you can see, now the subscriber starts before the publisher, so we shouldn’t have any data loss this time.</p>
<pre>parent-app $ curl subscriber-bf872.aws.af.cm
Received: ["1", "2", "3", "4", "5", "6", "7"]</pre>
<h3>AFIGNORE</h3>
<p>You can create a <code>.afignore</code> file in your app's root directory to tell <code>af push</code> and <code>af update</code> to skip files and directories, much like <code>.gitignore</code> for git.</p>
<p>You can set rules in the following ways:</p>
<ul>
<li>Specify exact file names.</li>
<li>Use wildcard patterns.</li>
<li>Specify directories by appending a '/' (this will include subdirectories).</li>
</ul>
<p>You can also reverse an ignore rule by beginning the line with a <code>!</code>.</p>
<p>Blank lines and lines beginning with <code>#</code> are ignored.</p>
<p>Here's a sample <code>.afignore</code> file:</p>
<pre># ignore local config
config.local

# ignore dot files
.*

# ignore assets directory
assets/

# don't ignore assets/necessary.css
!assets/necessary.css

# don't ignore assets/js/ directory
!assets/js/<br /><br /></pre>
<h3 id="zip_files">ZIP Files</h3>
<p>AppFog uses ZIP files to transfer content between the platform and your local machine. If you have a ZIP in your current directory when you use the `push` command, the Gem will only upload the ZIP file and ignore any other content in the directory. <strong>It is important to not use ZIPs in your code</strong>.</p>
