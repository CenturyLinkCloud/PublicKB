{{{
  "title": "Languages And Frameworks: Drupal",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog does not yet have a persistent data storage system, though we're working on it. This means that the file system is volatile and any data that needs to be persistent should be included in the code base (by making all changes in a local development environment) or offloaded to a database or an external storage system like Amazon's S3. You can find a tutorial on just how to do that <a href="http://blog.appfog.com/how-to-use-amazon-s3-for-persistent-file-storage-on-appfog/">here</a>.</p>
<h2>Services</h2>
<p>You can connect your PHP app to AppFog services by using the <code>VCAP_SERVICES</code> environment variable, which becomes available to your app when you bind a service to it. You can access the variable in PHP like this:</p>
<pre>getenv('VCAP_SERVICES')</pre>

<h2 id="drupal">Drupal</h2>
<p>The following is a step-by-step guide to deploying a Drupal app to AppFog.</p>
<h3>Download Drupal</h3>
<p><a href="http://drupal.org/project/download/">Download Drupal</a>, unzip it to a new directory, and change into that directory.</p>
<p>Then create your <code>settings.php</code> file:</p>
<pre>$ cp ./sites/default/default.settings.php ./sites/default/settings.php</pre>
<h3>Services</h3>
<p>In <code>settings.php</code>, replace <code>$databases = array();</code> with:</p>
<pre>$services = getenv('VCAP_SERVICES');
$services_json = json_decode($services,true);
$mysql_config = $services_json["mysql-5.1"][0]["credentials"];
$databases['default']['default'] = array(
    'driver' =&gt; 'mysql',
    'database' =&gt; $mysql_config["name"],
    'username' =&gt; $mysql_config["user"],
    'password' =&gt; $mysql_config["password"],
    'host' =&gt; $mysql_config["hostname"],
    'port' =&gt; $mysql_config["port"],
);
</pre>
<h3>Deploy to AppFog</h3>
<p>Push your code, making sure to create and bind a new MySQL service to the app:</p>
<pre>$ af push</pre>
<h3>Finish the Drupal Install</h3>
<p>Point your browser to your app's install script, in this case drupal-example.aws.af.cm/install.php. That should take you through the rest of the install process.</p>
<h2>Further Development</h2>
<p>AppFog does not yet have a persistent data storage system, though we're working on it. This means that the file system is volatile and any changes made to the file system by the app will be lost on an app start, stop, or deploy.</p>
<p>This means you should do any development that makes changes to the file system in a local development environment and then push those changes to AppFog using an <code>af update</code>. You can sync any database changes by tunneling.</p>
