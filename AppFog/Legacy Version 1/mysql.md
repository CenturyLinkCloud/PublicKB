{{{
  "title": "Services: MySQL",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog provides a MySQL service that's accessible to apps that are running on any of the supported runtimes and frameworks. It's also accessed using the <code>af tunnel</code> command.</p>
<p>It is limited it its total in size based on your chosen subscription plan. When the limit is reached, writes to the database should start failing.</p>
<table>
<tbody>
<tr>
<td> </td>
<td><center>Basic</center></td>
<td><center>Developer</center></td>
<td><center>Silver</center></td>
<td><center>Gold</center></td>
<td><center>Platinum</center></td>
</tr>
<tr>
<td><center>Maximum Number of Service Instances</center></td>
<td><center>8</center></td>
<td><center>8</center></td>
<td><center>16</center></td>
<td><center>64</center></td>
<td><center>128</center></td>
</tr>
<tr>
<td><center>Maximum Total Database Storage</center></td>
<td><center>2GB</center></td>
<td><center>4GB</center></td>
<td><center>16GB</center></td>
<td><center>128GB</center></td>
<td><center>512GB</center></td>
</tr>
<tr>
<td><center>Maximum Database Storage Per Instance</center></td>
<td><center>250MB</center></td>
<td><center>500MB</center></td>
<td><center>1GB</center></td>
<td><center>2GB</center></td>
<td><center>4GB</center></td>
</tr>
</tbody>
</table>
<p> </p>
<p>The AppFog app deployment process can automatically configure your app to use the bound MySQL service. Check the doc page for your app's framework to learn more about auto-reconfiguration.</p>
<p>Some things to remember while working with MySQL on AppFog.</p>
<ol>
<li>AppFog apps should always close database connections and should not use persistent MySQL connections.</li>
<li>Large databases can be very flaky when trying to back them up externally because our MySQL connections are not persistent. Keep file transfers under 200 MB per request.</li>
<li>Your best bet is to use a GUI like <a href="http://www.navicat.com/">Navicat</a> to connect to your database locally.</li>
</ol>
<h3 id="vcap">The VCAP_SERVICES Environment Variable</h3>
<p>When you provision and bind a service to your app, AppFog creates an environment variable called <code>VCAP_SERVICES</code>. For apps that can't be automatically configured, you can find the information your app needs to connect to the database in this variable.</p>
<p>This variable contains a JSON document with a list of all credentials and connection information for the bound services.</p>
<p>Here's an example that of the environment variable for an app that has two MySQL database services bound to it:</p>
<pre>{"mysql-5.1":[
    {
        "name":"mysql-4f700",
        "label":"mysql-5.1",
        "plan":"free",
        "tags":["mysql","mysql-5.1","relational"],
        "credentials":{
            "name":"d6d665aa69817406d8901cd145e05e3c6",
            "hostname":"mysql-node01.us-east-1.aws.af.cm",
            "host":"mysql-node01.us-east-1.aws.af.cm",
            "port":3306,
            "user":"uB7CoL4Hxv9Ny",
            "username":"uB7CoL4Hxv9Ny",
            "password":"pzAx0iaOp2yKB"
        }
    },
    {
        "name":"mysql-f1a13",
        "label":"mysql-5.1",
        "plan":"free",
        "tags":["mysql","mysql-5.1","relational"],
        "credentials":{
            "name":"db777ab9da32047d99dd6cdae3aafebda",
            "hostname":"mysql-node01.us-east-1.aws.af.cm",
            "host":"mysql-node01.us-east-1.aws.af.cm",
            "port":3306,
            "user":"uJHApvZF6JBqT",
            "username":"uJHApvZF6JBqT",
            "password":"p146KmfkqGYmi"
        }
    }
]}
</pre>
<p>You can use your app's language-specific facility to call the environment variable.</p>
<h4>In Java:</h4>
<pre>java.lang.System.getenv("VCAP_SERVICES")
</pre>
<h4>In Ruby:</h4>
<pre>ENV['VCAP_SERVICES']</pre>
<p>or</p>
<pre>JSON.parse(ENV.fetch('VCAP_SERVICES'))</pre>
<h4>In Javascript:</h4>
<pre>process.env.VCAP_SERVICES
</pre>
<h4>In Python:</h4>
<pre>os.getenv("VCAP_SERVICES")
</pre>
<h4>In PHP:</h4>
<pre>getenv("VCAP_SERVICES")
</pre>
<p>You can distinguish between multiple MySQL instances using the value of the <code>name</code> key.</p>
<p>The <code>credentials</code> object contains all of the data you need to connect to MySQL through a driver or library.</p>
<ul>
<li><code>hostname</code> and <code>host</code> have the same value, which is the host where the MySQL server is running.</li>
<li><code>port</code> is the port where MySQL server accepts connections on the host.</li>
<li><code>user</code> and <code>username</code> are the name of the MySQL database user.</li>
<li><code>password</code> is the MySQL password.</li>
<li><code>name</code> is the name of the MySQL database.</li>
</ul>
<h3 id="php">PHP</h3>
<p>Here's a bit more on how to use the <code>VCAP_SERVICES</code> variable to access your MySQL service:</p>
<pre>$services_json = json_decode(getenv("VCAP_SERVICES"),true);
$mysql_config = $services_json["mysql-5.1"][0]["credentials"];

$username = $mysql_config["username"];
$password = $mysql_config["password"];
$hostname = $mysql_config["hostname"];
$port = $mysql_config["port"];
$db = $mysql_config["name"];

$link = mysql_connect("$hostname:$port", $username, $password);
$db_selected = mysql_select_db($db, $link);
</pre>
<h3 id="migration">Migration</h3>
<p>Here's a quick guide on migrating an existing database to an AppFog app.</p>
<h4>Prepare your data</h4>
<p>First, export your MySQL data into a <code>.sql</code> file. If you're using phpMyAdmin, you can just use the export tool. If you're using command line tools like <code>mysqldump</code>, use the following:</p>
<pre>mysqldump -h &lt;hostname&gt; -u &lt;username&gt; -p&lt;Password&gt; &lt;database&gt; &gt; /tmp/mydata.sql
</pre>
<h4>Log in and establish your tunnel</h4>
<pre>$ af login
Attempting login to [https://api.appfog.com]
Email: example@appfog.com
Password: **************
Successfully logged into [https://api.appfog.com]

$ af tunnel
1: exampleapp1-mysql
Which service to tunnel to?: 1
Password: ********
Getting tunnel connection info: OK

Service connection info:
username : uaLDy9EhhvMLq
password : p5Odjf6E5O7uW
name : dc1aaa897343f4eb1aed047ec7c86f19f

Starting tunnel to exampleapp1-mysql on port 10000.
1: none
2: mysql
Which client would you like to start?: 1
</pre>
<p>Check out our <a href="service-database-content-management-tunneling.md">doc on tunneling</a> for more info.</p>
<h4>Import</h4>
<p>At this point, you can access your AppFog MySQL server as if it's a local MySQL instance.</p>
<pre>mysql --protocol=TCP --host=localhost --port=10000 --user=uaLDy9EhhvMLq --password=p5Odjf6E5O7uW dc1aaa897343f4eb1aed047ec7c86f19f
</pre>
<p>Import the data by running this command:</p>
<pre>mysql --protocol=TCP --host=localhost --port=10000 --user=uaLDy9EhhvMLq --password=p5Odjf6E5O7uW dc1aaa897343f4eb1aed047ec7c86f19f &lt; /tmp/mydata.sql
</pre>
