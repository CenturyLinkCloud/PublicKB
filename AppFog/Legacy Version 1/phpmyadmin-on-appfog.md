{{{
  "title": "Services: phpMyAdmin on AppFog",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://www.phpmyadmin.net/home_page/index.php">phpMyAdmin</a> is a free and popular software tool written in PHP that provides a web interface for administration of MySQL databases.</p>
<p>AppFog's phpMyAdmin jumpstart is slightly modified to work better in AppFog's environment. Check out the GitHub repository <a href="https://github.com/appfog/af-php-myadmin">here</a>.</p>
<h2>Install phpMyAdmin</h2>
<h3>1. Create the app.</h3>
<p>Go to <a href="https://console.appfog.com/">the console</a> and click on "Create App" at the top of the screen. Choose the phpMyAdmin jumpstart and pick an infrastructure (make sure to pick the same infrastructure as the database service you want to connect it to). Give the phpMyAdmin app a name and hit the "Create App" button.</p>
<h3>2. Bind the database service.</h3>
<p>Next you'll need to bind your new phpMyAdmin app to the database service you want to manage. On the app's management page, hit the "Services" tab, find the service you want, and hit the "Bind" button.</p>
<h3>3. Secure the app.</h3>
<p>You'll also need to add a password to your phpMyAdmin app. Click on the "Env Variables" tab on the left. Create an environment variable called:</p>
<pre>PMA_PASSWORD
</pre>
<p>You can set the value to whatever you want as your password. Your default phpMyAdmin username is the email address your AppFog account is under, but you can optionally override that to something of your choice by creating another environment variable called <code>PMA_USERNAME</code>.</p>
<p>That's it! Your phpMyAdmin app is ready to go.</p>
<p>One addition you may want to make to the app is to force SSL. You can do this very easily by adding an <code>.htaccess</code> file to the root of the app with a forced redirect from <code>http</code> to <code>https</code>.</p>
