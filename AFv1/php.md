{{{
  "title": "Languages And Frameworks: PHP",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#custom">Custom PHP App</a></li>
<li><a href="#php_ini">php.ini</a></li>
<li><a href="#docroot">Document Root</a></li>
</ul>
<h2>Supported Versions</h2>
<p>For the most reliable experience, make sure you have the same version of PHP installed on your local development environment as the target AppFog instance. You can check the available runtimes by running:</p>
<pre>$ af runtimes

+---------+-------------+---------+
| Name    | Description | Version |
+---------+-------------+---------+
| ruby18  | Ruby 1.8.7  | 1.8.7   |
| ruby192 | Ruby 1.9.2  | 1.9.2   |
| ruby193 | Ruby 1.9.3  | 1.9.3   |
| java    | Java 1.7    | 1.7.0   |
| python2 | python 2.7  | 2.7.3   |
| node04  | nodejs .04  | 0.4.12  |
| node06  | nodejs .06  | 0.6.17  |
| node08  | nodejs .08  | 0.8.14  |
| node10  | nodejs .10  | 0.10.29 |
| php     | PHP 5.3     | 5.3.10  |
| php54   | PHP 5.4     | 5.4.33  |
| php55   | PHP 5.5     | 5.5.17  |
| php56   | PHP 5.6     | 5.6.1   |
+---------+-------------+---------+
</pre>
<p>AppFog supports PHP with the <code>Apache Web Server 2.2.22</code> and <code>mod_php</code>. You can take a closer look at the PHP and Apache configurations for your runtime here:</p>
<pre> <a href="http://php_info.aws.af.cm/">PHP 5.3</a>, <a href="http://php_info54.aws.af.cm/">PHP 5.4</a>, <a href="http://php_info55.aws.af.cm/">PHP 5.5</a>, <a href="http://php_info56.aws.af.cm/">PHP 5.6</a></pre>
<h2>Persistent Data Storage</h2>
<p>AppFog does not yet have a persistent data storage system. This means that any files created or updated while the application is running are volatile and will be lost if the application is restarted or crashes. The only files that are persisted between application (re)starts are those that are uploaded with the <code>af push</code> or <code>af update</code> commands. The best practice for persisting files created while an application is running is to store them in a native AppFog database or external storage system like Amazon's S3 or ClearDB. You can find a tutorial on how to do that <a href="http://blog.appfog.com/how-to-use-amazon-s3-for-persistent-file-storage-on-appfog/">here</a>.  </p>
<p>The <a href="http://12factor.net">12factor.net</a> website provides a helpful guide on how to build fault-tolerant, redundant cloud-based applications.</p>
<h2>Services</h2>
<p>You can connect your PHP app to AppFog services by using the <code>VCAP_SERVICES</code> environment variable, which becomes available to your app when you bind a service to it. You can access the variable in PHP like this:</p>
<pre>getenv('VCAP_SERVICES')
</pre>

<h2 id="custom">Custom PHP App</h2>
<h3>Create the App</h3>
<p>Create a directory for the app and change into it:</p>
<pre>$ mkdir php-example
$ cd php-example
</pre>
<p>Create an <code>index.php</code> file with the following:</p>
<pre>&lt;?php echo "Hello world!"; ?&gt;
</pre>
<h3>Deploy to AppFog</h3>
<pre>$ af push php-example
Would you like to deploy from the current directory? [Yn]:
Detected a PHP Application, is this correct? [Yn]:
Application Deployed URL [php-example.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'php-example'? [yN]:
Create services to bind to 'php-example'? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Uploading Application:
    Checking for available resources: OK
    Packing application: OK
    Uploading (0K): OK
Push Status: OK
Staging Application 'php-example': OK
Starting Application 'php-example': OK

$ af curl php-example.aws.af.cm
Hello world!%
</pre>
<h2 id="php_ini">php.ini</h2>
<p>AppFog does not support direct access to <code>php.ini</code>. However, the <code>AllowOverride</code> directive in <code>php.ini</code> is set to "<code>All</code>" which enables you to set the values of the directives in your <code>.htaccess</code> or in your PHP file via <code>ini_set()</code>.</p>
<h3>Setting Values <code>.htaccess</code></h3>
<p>Setting the value of a directive in <code>.htaccess</code> is easy. Simply place the following line of code in your <code>.htaccess</code> file, and insert the name and value of the directive you want to use:</p>
<pre>php_value &lt;name&gt; &lt;value&gt;
</pre>
<p>For more information on this topic, check out the following references:</p>
<ul>
<li><a href="http://php.net/manual/en/configuration.changes.php">How to change configuration settings</a></li>
<li><a href="http://davidwalsh.name/php-values-htaccess">Set php.ini Values Using .htaccess</a></li>
</ul>
<h3>Setting Values Using <code>ini_set()</code></h3>
<p>Please consult the <a href="http://www.php.net/manual/en/function.ini-set.php">PHP manual on <code>ini_set()</code></a>.</p>
<h2 id="docroot">Document Root</h2>
<p>You can modify your document root adding the following into your <code>.htaccess</code>:</p>
<pre>RewriteEngine on
RewriteCond %{HTTP_HOST} ^domain.com$ [NC,OR]
RewriteCond %{HTTP_HOST} ^www.domain.com$
RewriteCond %{REQUEST_URI} !public/
RewriteRule (.*) /public/$1 [L]
</pre>
