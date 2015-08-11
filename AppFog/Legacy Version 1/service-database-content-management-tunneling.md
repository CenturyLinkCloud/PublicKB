{{{
  "title": "Services: Service and Database Content Management (Tunneling)",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>You can interact with your provisioned services interactively by using the <code>af tunnel</code> command. This deploys an app to your account called Caldecott, which is a <code>TCP</code> proxy over <code>HTTPS</code>. Caldecott creates a tunnel that connects a port on your local computer to the service in AppFog. The <code>af tunnel</code> command uploads the Caldecott app to your AppFog instance, sets up the tunneling, and offers to start a standard client on your computer to work with the service. This can be useful for managing your services as well as for debugging.</p>
<ul>
<li><a href="#prereqs">Prerequisites</a></li>
<li><a href="#tunneling">Tunneling</a></li>
<li><a href="#3rd-party-tools">Third-party Tools</a></li>
<li><a href="#more-info">More about the Tunnel Command</a></li>
<li><a href="#errors">Errors</a></li>
</ul>
<h3 id="prereqs">Prerequisites</h3>
<ul>
<li>Caldecott comes installed with the af gem.</li>
<li>Caldecott starts a client program for the service you want to access, for example <code>mysql</code> for <code>MySQL</code> or <code>psql</code> for <code>PostgreSQL</code>. The client must be installed on your computer and be on the execution <code>PATH</code> so that Caldecott scripts can start it. If you want to use a different client, Caldecott will display the connection information and credentials you will need to connect to the service. The following table shows the client programs Caldecott can start for each service.</li>
</ul>
<table class="table table-bordered table-striped" style="margin-left: auto; margin-right: auto;">
<tbody>
<tr><th>Service</th><th>Client</th></tr>
<tr>
<td>MongoDB</td>
<td><tt>mongo</tt></td>
</tr>
<tr>
<td>MySQL</td>
<td><tt>mysql</tt></td>
</tr>
<tr>
<td>PostgreSQL</td>
<td><tt>psql</tt></td>
</tr>
<!---
<tr>
<td>rabbitmq</td>
<td><i>none</i></td>
</tr>

<tr>
<td>Redis</td>
<td><tt>redis-cli</tt></td>
</tr>
---></tbody>
</table>
<h3 id="tunneling">Tunneling</h3>
<p>Get a list of your services by using the <code>af services</code> command:</p>
<pre>$ af services
</pre>
<p>Which should return something like this:</p>
<pre>============== System Services ==============

+------------+---------+-----------------------------+
| Service    | Version | Description                 |
+------------+---------+-----------------------------+
| mongodb    | 1.8     | MongoDB NoSQL store         |
| mysql      | 5.1     | MySQL database service      |
| postgresql | 9.1     | PostgreSQL database service |
+------------+---------+-----------------------------+

=========== Provisioned Services ============

+-----------------------+------------+
| Name                  | Service    |
+-----------------------+------------+
| exampleapp1-mysql     | mysql      |
| exampleapp2-mysql     | mysql      |
| exampleappmongodb     | mongodb    |
| example-postgres      | postgresql |
+-----------------------+------------+
</pre>
<p>Create a tunnel to the service with <code>af tunnel &lt;service&gt;</code>. For example:</p>
<pre>$ af tunnel exampleapp1-mysql
</pre>
<p>The first time you create a tunnel, <code>af</code> uploads Caldecott to your Cloud:</p>
<pre>Uploading Application:
Checking for available resources: OK
Processing resources: OK
Packing application: OK
Uploading (1K): OK
Push Status: OK
Binding Service [exampleapp1-mysql]: OK
Staging Application: OK
Starting Application: OK
</pre>
<p>Then Caldecott creates the tunnel and prompts you to start a client. Here's an example session with <code>mysql</code>.</p>
<pre>Starting tunnel to exampleapp1-mysql on port 10000.
1: none
2: mysql
3: mysqldump
Which client would you like to start?: 2
Launching 'mysql --protocol=TCP --host=localhost --port=10000
--user=um4rwWyhwa07B --password=pBiBlqjINB6cmdd368741dbc1945cfb62315565efcf1b5'

Welcome to the MySQL monitor.  Commands end with ; or \g.
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
.
.
.
mysql&gt;
</pre>
<p>When you exit the client, <code>af</code> disconnects the tunnel.</p>
<h3 id="3rd-party-tools">Using Third-party Tools</h3>
<p>For the last step, if you choose the <code>1: none</code> or if Caldecott doesn't have a default client for the service, you can simply leave the terminal window open. You can then start your preferred client in another window by using the provided "Service connection info".</p>
<pre>Service connection info:
  username : uz2Nrj2p20TXA
  password : p1tmyq30ZhjgQ
  name     : ddc26c09b7a7d4a1b88dacf445a7c9f87
  infra    : aws

Starting tunnel to exampleapp1-mysql on port 10000.
1: none
2: mysql
3: mysqldump
Which client would you like to start?: 1
Open another shell to run command-line clients or
use a UI tool to connect using the displayed information.
Press Ctrl-C to exit...
</pre>
<p>Leaving that terminal session open, simply start your client. Here's an example with MySQL Workbench:</p>
<p>Launch Workbench. On the left, you’ll see "Open Connection to Start Querying". Below that, click on "New Connection" to get started. This will bring up a new menu where we’ll input the necessary information.</p>
<p>For the "Connection Name", you can use whatever you want.</p>
<p>For "Hostname", you need to use your "localhost", and for the "port number", use what was given to you in the command line (where it says Starting tunnel to on port ). Port 10000 is the default.</p>
<p>The username and password are in the output of the <code>af tunnel</code> command under "Service connection info".</p>
<p>The "Default Schema" can be whatever you want, just like the "Connection Name".</p>
<p>Click on "OK", and it will take you back to the main screen, where you can click on your newly formed connection under the "Open Connection to Start Querying" header. Double-click on the connection you just made and that's it!</p>
<p>Once you're done, hit <code>Ctrl-C</code> to exit <code>af</code> and close the tunnel.</p>
<h3 id="more-info">More about the Tunnel Command</h3>
<p>You can simply enter the <code>af tunnel</code> command and respond to the prompts to create a tunnel. The command allows you to select from a list of existing provisioned services, so you don't need to know the service's name ahead of time.</p>
<p>The full syntax of the <code>af tunnel</code> command is:</p>
<pre>af tunnel [&lt;servicename&gt;] [--port &lt;portnumber&gt;] [&lt;clientcmd&gt;]
</pre>
<p>The <code>&lt;servicename&gt;</code> argument is the name of the service, as shown by the <code>af services</code> command. If you exclude <code>&lt;servicename&gt;</code>, <code>af</code> provides a list of existing services to choose from.</p>
<p>The <code>&lt;portnumber&gt;</code> parameter is the port to use on the local machine. By default, <code>af</code> chooses an available port in the <code>10000</code> range.</p>
<p>The <code>&lt;clientcmd&gt;</code> argument is the name of the client program to start. Only the client names shown in the table in the <a href="#prereqs">Prerequisites</a> section are supported for this argument.</p>
<h3 id="errors">Errors</h3>
<pre>terminate called after throwing an instance of 'std::runtime_error'
  what():  Encryption not available on this event-machine
ERROR 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 0
Aborted</pre>
<p>Install the <em>openssl-devel</em> or <em>libssl-dev</em> package. Then, try installing your <em>eventmachine</em> gem with:</p>
<p><code>sudo gem install eventmachine -- --with-openssl-dir=/path/to/openssl</code></p>
<p>Use <code>which openssl</code> to determine the location of your <em>openssl</em> install and put that path in your command. In my case it was:</p>
<p><code>sudo gem install eventmachine -- --with-openssl-dir=/usr/bin/openssl</code>.</p>
