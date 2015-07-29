{{{
  "title": "Languages And Frameworks: WordPress Deployment and Configuration",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h2>Important Reminder</h2>
<p>AppFog does not yet have a persistent data storage system, which is frequently updated by the native WordPress admin console when applying themes, uploading images, or adding modules. Any changes stored on the file system during runtime by WordPress will be lost on an app start, stop, or deploy. To ensure your WordPress website changes are persisted between (re)starts, the recommended best practice is to save file updates in a database or block storage solution.</p>
<p>This means you should do any development that makes changes to the file system in a local development environment and then push those changes to AppFog using an <code>af update</code>. You can find a solutions tutorial about it in our <a href="wordpress.md">WordPress article</a>.</p>
<h2>Services</h2>
<p>Connect your PHP app to AppFog service instances by using the <code>VCAP_SERVICES</code> environment variable, which becomes available to your app when you bind a service to it. You can access the variable in PHP like this:</p>
<pre>getenv('VCAP_SERVICES')
</pre>
<h2 id="wordpress">WordPress</h2>
<p>The following is a step-by-step guide to deploying a WordPress app to AppFog.</p>
<h3>Download Wordpress</h3>
<p><a href="http://wordpress.org/download/">Download WordPress</a>, unzip it to a new directory, and change into that directory.</p>
<p>Then create your <code>wp-config.php</code> file:</p>
<pre>$ cp wp-config-sample.php wp-config.php
</pre>
<h3>Services</h3>
<p>In <code>wp-config.php</code>, replace:</p>
<pre>/** The name of the database for WordPress */
define('DB_NAME', 'database_name_here');

/** MySQL database username */
define('DB_USER', 'username_here');

/** MySQL database password */
define('DB_PASSWORD', 'password_here');

/** MySQL hostname */
define('DB_HOST', 'localhost');
</pre>
<p>with:</p>
<pre>$services = getenv("VCAP_SERVICES");
$services_json = json_decode($services,true);
$mysql_config = $services_json["mysql-5.1"][0]["credentials"];

define('DB_NAME', $mysql_config["name"]);
define('DB_USER', $mysql_config["user"]);
define('DB_PASSWORD', $mysql_config["password"]);
define('DB_HOST', $mysql_config["hostname"]);
define('DB_PORT', $mysql_config["port"]);
</pre>
<h3>Deploy to AppFog</h3>
<pre>$ af push wordpress-example
Would you like to deploy from the current directory? [Yn]:
Detected a PHP Application, is this correct? [Yn]:
Application Deployed URL [wordpress-example.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'wordpress-example'? [yN]:
Create services to bind to 'wordpress-example'? [yN]: y
1: mongodb
2: mysql
3: postgresql
What kind of service?: 2
Specify the name of the service [mysql-d197d]:
Create another? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Creating Service [mysql-d197d]: OK
Binding Service [mysql-d197d]: OK
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
    Uploading (5M): OK
Push Status: OK
Staging Application 'wordpress-example': OK
Starting Application 'wordpress-example': OK
</pre>
<h3>Finish the WordPress Install</h3>
<p>Point your browser to your app's install script, in this case wordpress-example.aws.af.cm/wp-admin/install.php. That should take you through the rest of the install process.</p>
