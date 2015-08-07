{{{
  "title": "Add-ons: IronMQ",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Install IronMQ</h3>
<p>In the "Add-ons" tab in your app console click "Install" for the IronMQ add-on. That's it!</p>
<h3>Authentication</h3>
<p>You need two things to authenticate and tell IronMQ which project to attach your queues to:</p>
<pre>Token: IRON_MQ_TOKEN

Project ID: IRON_WORKER_PROJECT_ID</pre>
<p>You can find these environment variables in the "Env. Variables" tab in your app console. You can also access these variables in PHP through the <code>getenv()</code> function.</p>
<h3>The Basics</h3>
<p>There are three basic actions you can perform on a message queue:</p>
<ul>
<li>Put a message into a queue.</li>
<li>Get a message out of a queue.</li>
<li>Delete the message you got out of the queue when you're done with it. (If you don't delete the message, it will go back into the queue after a timeout.)</li>
</ul>
<p>These three simple actions are the main actions you'll typically use. Here's some sample code using our client that shows how to use these functions.</p>
<pre>// Get package here: https://github.com/iron-io/iron_mq_php
require_once "IronMQ.class.php"

$ironmq = new IronMQ(array(
'token' =&gt;getenv('IRON_MQ_TOKEN'),
'project_id' =&gt; getenv('IRON_WORKER_PROJECT_ID')
));

// Put a message on the queue
$ironmq-&gt;postMessage("my_queue", "Hello world");

// Get a message
$msg = $ironmq-&gt;getMessage("my_queue");

// Delete the message
$ironmq-&gt;deleteMessage("my_queue", $message_id);</pre>
<p>For more information please visit the <a href="http://dev.iron.io/mq/">IronMQ Reference Page.</a></p>
