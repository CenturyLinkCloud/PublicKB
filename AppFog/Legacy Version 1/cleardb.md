{{{
  "title": "Add-ons: ClearDB",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": false
}}}

<h4>Intro</h4>
<p><a href="https://www.cleardb.com">ClearDB</a> is a hosted <a href="http://www.mysql.com/">MySQL</a> service that allows you to create as large of a database as necessary for your application while having peace of mind that your data is safe, and fault tolerant.</p>
<h4>Why use ClearDB</h4>
<p>ClearDB can make sure you have enough room for growth with your application. If your database is expected to be larger than your AppFog account allotments or you, just want assurance that your data will be persistent, ClearDB can help to mediate these concerns.</p>
<h4>Install ClearDB</h4>
<p>In the AppFog console, select the application you wish to setup. Navigate to the “Add-ons” tab and click “Install” for the ClearDB add-on.</p>
<h4>Using ClearDB</h4>
<p>Installing the ClearDB add-on automatically sets an environment variable for your app called <code>CLEARDB_DATABASE_URL</code>. This variable includes the full URI including the hostname, database path, username and password.</p>
<p>The following code demonstrates how to parse the environment variable:</p>
<pre>$url=parse_url(getenv("CLEARDB_DATABASE_URL"))
mysql_connect(
    $server = $url["host"],
    $username = $url["user"],
    $password = $url["pass"]);
    $db=substr($url["path"],1);
    mysql_select_db($db);
?&gt;</pre>
<h4>ClearDB DashBoard</h4>
<p>To access your ClearDB dashboard, simply click the "Manage" button under ClearDB from the "Add-ons" tab on your app console.</p>
<h4>Additional Resources</h4>
<p><a href="http://www.cleardb.com/developers">ClearDB Documentation</a></p>
<p>[MySQL AppFog Documentation](mysql.md)</p>
<p><a href="http://dev.mysql.com/doc/">MySQL Documentation</a></p>
