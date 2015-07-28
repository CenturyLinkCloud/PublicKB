{{{
  "title": "Add-ons: IronWorker",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Install IronWorker</h3>
<p>In the "Add-ons" tab in your app console click "Install" for the IronWorker add-on. That's it!</p>
<h3>Integrate IronWorker</h3>
<p>Just copy <a href="https://github.com/iron-io/iron_worker_php/blob/master/IronWorker.class.php">IronWorker.class.php</a> and include it in your script:</p>
<pre>&lt;?php
require_once "IronWorker.class.php"</pre>
<h3>Create a Worker</h3>
<p>When you install IronWorker, the installer creates two environment variables set with the necessary credentials. Create a worker and pass in those credentials like this:</p>
<pre class="prettyprint linenums:3 linenums">$worker = new IronWorker(array(
'token' =&gt; getenv('IRON_WORKER_TOKEN'),
'project_id' =&gt; getenv('IRON_WORKER_PROJECT_ID')
));
</pre>
<p>Here's an example worker:</p>
<pre>&lt;?php
echo "Hello PHP World!\n";</pre>
<p>We'll call this worker "HelloWorld.php".</p>
<h3>Upload Your Worker</h3>
<p>Here's how to take the example above, zip it up, and upload it to IronWorker.</p>
<pre>&lt;?php
# Zip single file:
IronWorker::createZip(dirname(__FILE__), array('HelloWorld.php'), 'worker.zip', true);
$res = $iw-&gt;postCode('HelloWorld.php', 'worker.zip', 'HelloWorld');</pre>
<h3>Queue Your Worker</h3>
<pre>&lt;?php
$task_id = $iw-&gt;postTask('HelloWorld');</pre>
<p>Your worker should start in a few seconds.</p>
<h3>Schedule Your Worker</h3>
<p>If you want to run your code more than once or run it in regular intervals, you can schedule it:</p>
<pre>&lt;?php
# 3 minutes from now
$start_at = time() + 3*60;

# Run task every 2 minutes, repeat 10 times
$iw-&gt;postScheduleAdvanced('HelloWorld', array(), $start_at, 2*60, null, 10);</pre>
<h3>Check the Status of Your Worker</h3>
<p>Use the <code>getTaskDetails()</code> method.</p>
<pre>&lt;?php
$task_id = $iw-&gt;postTask('HelloWorld');
$details = $iw-&gt;getTaskDetails($task_id);

echo $details-&gt;status; # prints 'queued', 'complete', 'error' etc.</pre>
<h3>And More...</h3>
<p>You can also pass payloads to your tasks, set progress status, logs, etc. For more information, check out some of these resources:</p>
<ul>
<li><a href="https://github.com/iron-io/iron_worker_php">IronWorker on GitHub</a></li>
<li><a href="http://iron-io.github.com/iron_worker_php/">IronWorker PHP Reference Documentation</a></li>
<li><a href="https://github.com/iron-io/iron_worker_php/wiki">IronWorker PHP Wiki</a></li>
<li><a href="http://docs.iron.io/">Full Documentation on Iron.io</a></li>
</ul>
