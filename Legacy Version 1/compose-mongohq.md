{{{
  "title": "Add-ons: Compose (MONGOHQ)",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Install Compose</h3>
<p>In the "Add-ons" tab in your app console click "Install" for the Compose add-on. That's it!</p>
<p>Installing the Compose add-on automatically sets an environment variable for your app called <code>MONGOHQ_URL</code>. You can access this in your code with <code>getenv(["MONGOHQ_URL")</code>. This variable includes the full URI including the hostname, database path, username and password. It looks like this:</p>
<pre>mongodb://username:password@host:port/database
</pre>
<p>Using MongoDB from a PHP app is very easy. The required extensions are already installed on all servers, so you can use the Mongo objects from your app immediately. Here is a little sample app you can use to test out your newly created MongoDB:</p>
<pre>&lt;?php
    // connect
    $m = new Mongo(getenv("MONGOHQ_URL"));

    // select a database
    $db = $m-&gt;comedy;

    // select a collection (analogous to a relational database's table)
    $collection = $db-&gt;cartoons;

    // add a record
    $obj = array( "title" =&gt; "Calvin and Hobbes", "author" =&gt; "Bill Watterson" );
    $collection-&gt;insert($obj);

    // add another record, with a different "shape"
    $obj = array( "title" =&gt; "XKCD", "online" =&gt; true );
    $collection-&gt;insert($obj);

    // find everything in the collection
    $cursor = $collection-&gt;find();

    // iterate through the results
    foreach ($cursor as $obj) {
        echo $obj["title"] . "\n";
    }
?&gt;
</pre>
<p>You can find more information on using a MongoDB from a PHP app <a href="http://php.net/manual/en/class.mongodb.php">here</a>.</p>
<h3>Compose Admin Panel</h3>
<p>In the "Add-ons" tab in your app console, click on the "Manage" button for the compose add-on. This will take you to your Compose account where you can make configuration changes and upgrade your Compose account.</p>
<p>For more information, please visit the <a href="https://docs.compose.io/getting-started/compose.html">compose documentation</a>.</p>
