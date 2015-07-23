{{{
  "title": "Add-ons: Searchify",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://www.searchify.com">Searchify</a> is an add-on that provides hosted full-text search.</p>
<p>Searchify allows developers to easily add search to their applications, without having to deal with Solr or Lucene, and without the hassle of configuring and hosting your own search infrastructure. Searchify is fast. Most search queries will be answered in under 100 milliseconds. Searchify offers true real-time search, so documents added are immediately searchable. Searchify is a drop-in replacement for existing IndexTank users.</p>
<p>Searchify has client libraries for <a href="http://www.searchify.com/documentation/php-client">PHP</a>, <a href="http://www.searchify.com/documentation/ruby-client">Ruby</a>, <a href="http://www.searchify.com/documentation/python-client">Python</a>, <a href="http://www.searchify.com/documentation/java-client">Java</a>, and others, all of which communicate with Searchify's <a href="http://www.searchify.com/documentation/api">REST API</a>.</p>
<h3>Install Searchify</h3>
<p>In the "Add-ons" tab in your app console click "Install" for the Searchify add-on. That's it!</p>
<p>Installing the Searchify add-on creates an account with Searchify associated with your PHP Fog account. By default, it will contain one empty index called "idx" which you can use or delete and replace.</p>
<p>This will also add an environment variable called <code>SEARCHIFY_API_URL</code> in the "Env. Variables" in your app console. This contains the private API URL used to access the newly provisioned Searchify service from your app.</p>
<h3>Set up your local development environment</h3>
<p>The <code>SEARCHIFY_API_URL</code> environment variable holds the private URL you'll use to access the Searchify service from within a local environment. Developers will typically create one search index for testing and one for production.</p>
<p>The next step is to install the appropriate language client library to develop locally with Searchify.</p>
<h3>Installing the client library</h3>
<p>You can access Searchify using the IndexTank client library.</p>
<h4>Installing the IndexTank Client</h4>
<p>Full PHP client documentation and download links are available <a href="http://www.searchify.com/documentation/php-client">here</a>.</p>
<p>Once you've installed the client library, you can use it to add documents to your index as well as to perform searches. The following code sample demonstrates basic document indexing and searching.</p>
<pre>&lt;?php
    include_once "indextank.php";

    $API_URL = getenv('SEARCHIFY_API_URL');

    $client = new Indextank_Api($API_URL);
    $index = $client-&gt;get_index("&lt;YOUR INDEX NAME&gt;");
?&gt;
</pre>
<p>Once you have an instance of the client all you need is the content you want to index. The simplest way to add a document is sending that content in a single field called "text":</p>
<pre>&lt;?php
    $text = 'this is a text';
    $doc_id = 1234;
    $index-&gt;add_document($doc_id, array('text'=&gt;$text));
?&gt;
</pre>
<p>That's it, you've indexed a document! You can now search the index for any indexed document by simply providing the search query:</p>
<pre>&lt;?php
    $query = "&lt;YOUR QUERY&gt;";
    $res = $index-&gt;search($query);

    echo $res-&gt;matches . " results\n";
    foreach($res-&gt;results as $doc) {
      print_r($doc);
      echo "\n";
    }
?&gt;
</pre>
<p>An index may be deleted and re-created anytime to clean it up, either from code as shown below or from Searchify's <a href="http://www.searchify.com/dashboard">dashboard</a>:</p>
<h4>Deleting an index</h4>
<pre>&lt;?php
    include_once "indextank.php";
    $API_URL = getenv('SEARCHIFY_API_URL');

    $client = new Indextank_Api($API_URL);
    $index = $client-&gt;get_index("&lt;YOUR INDEX NAME&gt;");
    $index-&gt;delete_index();
?&gt;
</pre>
<h4>Creating a new index</h4>
<pre>&lt;?php
    $client = new Indextank_Api($API_URL);

    // This parameter allows you to create indices with public search enabled.
    // Default is false.
    $public_search_enabled = false;
    $index = $client-&gt;create_index("&lt;YOUR INDEX NAME&gt;", $public_search_enabled);

    while (!$index-&gt;has_started()) {
      sleep(1);
    }
?&gt;
</pre>
<h4>Dashboard</h4>
<p>The Searchify dashboard allows you to manage indices, allowing you to create, delete, and search indices. Custom scoring functions can also be configured. The dashboard can be accessed by visiting the PhpFog app console, and selecting Searchify.</p>
<h4>Plans</h4>
<p>Searchify offers plans based on the number of documents stored. If you outgrow the limits of your current Searchify plan, you can change to a larger plan. A list of all plans available can be found <a href="http://www.searchify.com/plans">here</a>.</p>
<h3>Further Reading</h3>
<p>For more information on the features available from Searchify, including faceting, geolocation, snippets, autocomplete, and custom scoring functions, please see the documentation at <a href="http://www.searchify.com/documentation">www.searchify.com/documentation</a>.</p>
