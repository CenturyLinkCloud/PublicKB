{{{
  "title": "The AF CLI Tool: Push, Pull, and Update Commands",
  "date": "1-24-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

<p>This lines out some details to how the <code>push</code>, <code>pull</code>, and <code>update</code> commands should work.</p>
<h4>PUSH</h4>
<h4><code>af push {app}</code></h4>
<p>The command <code>push</code> ZIPs the content in the current directory and uploads it to the environment. For more information on the structure of a app, visit our [Application Configuration](application-configuration-using-manifest-files-and-afignore.md) article. If you have a ZIP file located within this directory, it can cause the problems lined out in the [Application Configuration](ZIP files) section of that article. An example for an application called <code>user-php</code> is below.</p>
<pre>user@localhost: ~/af/apps/my_test_php_app$ af push user-php
Would you like to deploy from the current directory? [Yn]: y
Detected a PHP Application, is this correct? [Yn]: y
1: CLC - Santa Clara
2: AWS US East - Virginia
3: AWS EU West - Ireland
4: AWS Asia SE - Singapore
Select Infrastructure: 2
Application Deployed URL [derek-php.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Create services to bind to 'derek-php'? [yN]: n
Would you like to save this configuration? [yN]: n
Creating Application: OK
Uploading Application:
  Checking for available resources: OK
  Packing application: OK
  Uploading (0K): OK
Push Status: OK
Staging Application 'user-php': OK
Starting Application 'user-php': OK</pre>
<h4>PULL</h4>
<h4><code>af pull {app}</code></h4>
<p>The command <code>pull</code> bundles content currently running on the platform and downloads it as a ZIP file. It is then automatically extracted to a file named after the app under the local directory. An example for an application called <code>user-php</code> is below.</p>
<pre>user@localhost:~/af/apps$ af pull user-php
Pulling last pushed source code: OK

user@localhost:~/af/apps$ ls
user-php  my_test_php_app
user@localhost:~/af/apps$ cd user-php/
user@localhost:~/af/apps/user-php$ ls
index.php</pre>
<h4>UPDATE</h4>
<h4><code>af update {app}</code></h4>
<p>The command <code>update</code> updates the specified application with the <strong>all</strong> content in your current directory. If you have a ZIP file located within this directory, it can cause the problems lined out in the <a href="application-configuration-using-manifest-files-and-afignore.md">ZIP Files</a> section of our Application Configuration article above. An example for an application called <code>user-php</code> is below.</p>
<pre>user@localhost:~/af/apps$ ls
user-php  my_test_php_app
user@localhost:~/af/apps$ cd user-php/
user@localhost:~/af/apps/derek-php$ af update user-php
Uploading Application:
  Checking for available resources: OK
  Packing application: OK
  Uploading (0K): OK
Push Status: OK
Stopping Application 'user-php': OK
Staging Application 'user-php': OK
Starting Application 'user-php': OK</pre>
