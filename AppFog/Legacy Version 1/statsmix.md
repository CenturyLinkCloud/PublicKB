{{{
  "title": "Add-ons: StatsMix",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://www.statsmix.com/">StatsMix</a> makes it easy to track, chart, and share application and business metrics.</p>
<p>Use StatsMix to:</p>
<ul>
<li>Log every time a particular event happens (such as a user creating a new blog post)</li>
<li>View a real-time chart of these application events in StatsMix's web UI</li>
<li>Share the charts with users inside and outside your organization</li>
<li>Create and share custom dashboards that aggregate multiple metrics together
<ul>
<li><a href="http://www.statsmix.com/d/0e788d59208900e7e3bc">Example dashboard</a></li>
<li><a href="http://www.statsmix.com/example-embedded">Example embedded dashboard</a></li>
</ul>
</li>
</ul>
<h1>Install StatsMix</h1>
<p>In the "Add-ons" tab in your app console click "Install" for the StatsMix add-on. That’s it!</p>
<p>Next, set up your app to start using the cache. We have documentation for the following languages and frameworks:</p>
<ul>
<li><a href="#rails">Rails</a></li>
<li><a href="#php">PHP</a></li>
</ul>
<p>For other languages and frameworks, check out <a href="http://www.statsmix.com/developers/code_libraries">this page</a>.</p>
<p>For the StatsMix API, go <a href="http://www.statsmix.com/developers">here</a>.</p>
<h1><a id="rails"></a>Rails</h1>
<p>First, install the StatsMix gem:</p>
<p>{: .prettyprint } $ gem install statsmix</p>
<p>Next, configure the gem according to your version of Rails:</p>
<h3>Rails 2</h3>
<p>Add the following to <code>config/environment.rb</code>, then restart the server:</p>
<p>{: .prettyprint } $ config.gem 'statsmix'</p>
<h3>Rails 3</h3>
<p>Add the following to your Gemfile, then restart the server:</p>
<p>{: .prettyprint } $ gem 'statsmix'</p>
<h1>Your API Key</h1>
<p>AppFog keeps your StatsMix API key in an environment variable called <code>STATSMIX_API_KEY</code>, which you can retrieve using the command <code>ENV['STATSMIX_API_KEY']</code>. Populate your API key for the StatsMix gem with this:</p>
<p>{: .prettyprint } $ StatsMix.api<em>key = ENV['STATSMIX</em>API_KEY']</p>
<h1>Using StatsMix to Track Events</h1>
<p>Any time you want to track an event in your app, simply call:</p>
<p>{: .prettyprint } StatsMix.track(name<em>of</em>metric, value = 1, options = {})</p>
<p>If a metric with that name doesn't exist in your account, StatsMix will create one automatically. If the profile isn't set, the metric will use the first <code>profile_id</code> created in your account. (Developer, Basic, and Standard plans only have one profile.)</p>
<h3>Examples</h3>
<p>Track every time a new blog post is created:</p>
<p>{: .prettyprint } # create a stat with the value 1 (default) for the metric called "Blog Posts" StatsMix.track("Blog Posts")</p>
<p>Count the number of new user accounts in the last 24 hours (i.e. run daily in a daily rake task):</p>
<p>{: .prettyprint } count = User.count(:conditions =&gt; ["created_at &gt;= ?", 24.hours.ago]) # create a stat with the value count for the metric called "Daily New Users" StatsMix.track("Daily New Users", count)</p>
<h1>Adding Metadata</h1>
<p>You can optionally "tag" your data with metadata in the <code>:meta</code> option. For example, if you have a file upload utility and want to track what kinds of files you are receiving:</p>
<p>{: .prettyprint } # a user just uploaded a PDF file; track the type of file using metadata StatsMix.track("File Uploads", 1, {:meta =&gt; {"file type" =&gt; "PDF"}})</p>
<p>You can include multiple key-value pairs in the same stat:</p>
<p>{: .prettyprint } StatsMix.track("File Uploads", 1, {:meta =&gt; {"file type" =&gt; "PDF", "size" =&gt; "1 mb", "country of origin" =&gt; "Absurdistan"}})</p>
<h1>Adding Your Own Identifier</h1>
<p>If you need the ability to update a stat after the fact, you can pass in a unique identifier <code>ref_id</code> (scoped to that metric).</p>
<p>For example, perhaps you want to update the number of users every hour instead of every day. If you pass in the date as <code>ref_id</code>, StatsMix will check whether a stat with that <code>ref_id</code> already exists for that metric. If found, StatsMix will update instead of inserting.</p>
<p>{: .prettyprint } count = User.count(:conditions =&gt; ["created<em>at &gt;= ?", Time.now.strftime("%Y-%m-%d")]) # create/update a stat using today"s date as the unique identifier StatsMix.track("Daily New Users", count, {:ref</em>id =&gt; Time.now.strftime("%Y-%m-%d")})</p>
<h3>Additional Options</h3>
<p>If you’d like to change the timestamp of a stat, pass in the parameter <code>generated_at</code>.</p>
<p>{: .prettyprint } # backdate the stat to yesterday StatsMix.track("Blog Posts", 1, {:generated_at =&gt; 1.days.ago})</p>
<p>Higher level StatsMix accounts can have additional profiles. A profile can be described as a grouping or "bucket" of metrics. For example, an agency may want to create a profile for each customer.</p>
<p>If you are tracking metrics with the same name in two different profiles, you must specify which profile to use with <code>profile_id</code>. (If you don't specify <code>profile_id</code>, StatsMix will default to the first profile in your account.)</p>
<p>{: .prettyprint } StatsMix.track("Blog Posts", 1, {:profile_id =&gt; 789})</p>
<p>You can find the profile ID in StatsMix by creating a metric and looking at the API Details under Code Snippets in the Data &amp; API section. (It will also be in the URL as /<code>profiles/123/metrics/456</code> - in this case the profile id is 123.)</p>
<h3>Limitations</h3>
<p>If you hit a plan level limit (i.e. you go over the number of API requests available to your account), the API will return a 403 Forbidden error and an explanation.</p>
<p>The number of API requests and profiles you can create is based on the type of account you have. For example, Standard plans are limited to 300,000 API requests per month. You can see the current options on StatsMix's <a href="http://www.statsmix.com/home/plans">pricing page</a>.</p>
<h3>Local Setup</h3>
<p>When running StatsMix in development, you can tell StatsMix to either ignore calls to it altogether or funnel them all into a single test metric.</p>
<p>For ignoring calls altogether, just put the following in a configuration file such as environment.rb or an initializer:</p>
<p>{: .prettyprint } StatsMix.ignore = true</p>
<p>For logging to a test metric, add this instead:</p>
<p>{: .prettyprint } StatsMix.test<em>metric</em>name = "My Test Metric"</p>
<p>This routes all <code>StatsMix.track</code> calls to "My Test Metric" regardless of the metric name passed.</p>
<p>Note: If StatsMix.ignore is set, then the test metric will not be used unless StatsMix.ignore is first reset to false.</p>
<h1><a id="php"></a>PHP</h1>
<p>You can get 98% of our functionality by copying &amp; pasting the examples below.</p>
<p>The basic pattern:</p>
<p>{: .prettyprint .linenums} require "StatsMix.php"; StatsMix::set<em>api</em>key(getenv("STATSMIX<em>API</em>KEY"); StatsMix::track($name<em>of</em>metric,$value = 1,$options = array());</p>
<p>Push a stat with the value 1 (default) to a metric called "My First Metric":</p>
<pre><code>StatsMix::track("My First Metric");
</code></pre>
<p>Push the value 20:</p>
<pre><code>StatsMix::track("My First Metric",20);
</code></pre>
<p>Add metadata via the "meta" option in <code>$options</code> - you can use this to add granularity to your stats. This example tracks file uploads by file type.</p>
<p>{: .prettyprint } StatsMix::track("File Uploads", 1, array('meta' =&gt; array("file type" =&gt; "PDF")));</p>
<p>If you need the ability to update a stat after the fact (i.e. you're updating the same stat several times a day), you can pass in a unique identifier called <code>ref_id</code>, which is scoped to the metric (so you can use the same identifier across metrics) This example uses the current date (in UTC time) for <code>ref_id</code>.</p>
<p>{: .prettyprint } StatsMix::track("File Uploads", 1, array('ref_id' =&gt; gmstrftime('%Y-%m-%d'), 'meta' =&gt; array("file type" =&gt; "PDF")));</p>
<p>If you need to timestamp the stat for something other than now, pass in a UTC datetime with the key <code>generated_at</code></p>
<p>{: .prettyprint } StatsMix::track("File Uploads", 1, array('generated_at' =&gt; gmstrftime('%Y-%m-%d %H:%I:%S',strtotime('yesterday'))));</p>
<p>To turn off tracking in your development environment:</p>
<p>{: .prettyprint } StatsMix::set_ignore(true);</p>
<p>To redirect all stats in dev environment to a test metric:</p>
<p>{: .prettyprint } StatsMix::set<em>test</em>metric_name("My Test Metric");</p>
<p>If you have multiple profiles in your account, specify which one via <code>profile_id</code>:</p>
<p>{: .prettyprint } StatsMix::track("metric name that may be in multiple profiles", 1, array('profile<em>id' =&gt; "PROFILE</em>ID"));</p>
<p>To create metrics and stats using a more OO approach, check out the classes <strong>SmMetric</strong> and <strong>SmStat</strong> in StatsMix.php. Using them you can do things like this:</p>
<p>Create a metric:</p>
<p>{: .prettyprint .linenums } $metric = new SmMetric; $metric-&gt;name = "My Test Metric"; $metric-&gt;save(); if($metric-&gt;error){ echo "</p>
<p>Error: {$metric-&gt;error}</p>
<p>"; } //view the xml response: echo $metric-&gt;get_response();</p>
<h3>More Documentation</h3>
<p>The StatsMix PHP Library supports all the methods documented <a href="http://www.statsmix.com/developers/documentation">here</a>.</p>
<h3>Contributing to statsmix</h3>
<p>Check out <a href="https://github.com/derekscruggs/PHP-library-for-StatsMix-API">this GitHub repo</a> to contribute.</p>
<h3>Copyright</h3>
<p>Copyright © 2011 StatsMix, Inc. See <a href="https://www.statsmix.com/terms">Terms of Service</a> for further details.</p>
