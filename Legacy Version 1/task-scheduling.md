{{{
  "title": "Customize: Task Scheduling",
  "date": "1-28-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog allows you to execute scheduled tasks using a "background worker" (also referred to as a "standalone" or container-less application) in almost any language that AppFog supports.</p>
<p>You may want to set one up to auto-scale your app depending on it's load, or dump logs at a certain time of day.</p>
<p>This is an easy way to create a cron job that runs at a specific time each day and performs essential tasks.</p>
<h4>Background Worker Examples</h4>
<p>Check out the examples below to learn how to create your own scheduled application.</p>
<ul>
<li><a href="#task-scheduling-ruby">Ruby</a></li>
<li><a href="#task-scheduling-python">Python</a></li>
</ul>
<h3 id="task-scheduling-ruby">Ruby</h3>
<p>You can use the <code>rufus-scheduler</code> <a href="https://github.com/jmettraux/rufus-scheduler">gem</a> with a standalone ruby app, for example, to run cron-like jobs using an incredibly simple syntax. The examples in the GitHub repo demonstrates this:</p>
<pre>require 'rubygems'
require 'rufus/scheduler'

scheduler = Rufus::Scheduler.start_new

scheduler.in '20m' do
  puts "order ristretto"
end

scheduler.at 'Thu Mar 26 07:31:43 +0900 2009' do
  puts 'order pizza'
end

scheduler.cron '0 22 * * 1-5' do
  # every day of the week at 22:00 (10pm)
  puts 'activate security system'
end

scheduler.every '5m' do
  puts 'check blood pressure'
end
</pre>
<p>Some examples of commands you could run include:</p>
<ul>
<li>Pinging a URL in another app that induces a database backup.</li>
<li>Clear cache.</li>
<li>Perform web-scraping within a set of domains.</li>
<li>Email a particular subset of your users.</li>
</ul>
<h4>Example Standalone App on AppFog</h4>
<p>First, we’ll make a simple Ruby file (<code>portland.rb</code>) that simply outputs "Portland: life is just better here" every five seconds:</p>
<pre>loop {
    puts "Portland: life is just better here"
    sleep 5
}
</pre>
<p>Next, run <code>af push</code> from the app's directory (we'll call the app "portlandrules"). When it asks you if you’re deploying a standalone app, respond "yes," and you can then specify which runtime the app is in and which start command you want to use with the app. (If it asks if you’re deploying a specific language or framework like Rails or Django, respond "no.")</p>
<p>In this case, the start command is <code>ruby portland.rb</code>.</p>
<pre>$ af push portlandrules
Would you like to deploy from the current directory? [Yn]:
Detected a Standalone Application, is this correct? [Yn]:
1: java
2: node04
3: node06
4: php
5: python2
6: ruby18
7: ruby192
8: ruby193
Select Runtime [ruby18]: 6
Selected ruby18
Start Command: ruby portland.rb
1: AWS US East - Virginia
2: AWS EU West - Ireland
3: AWS Asia SE - Singapore
4: HP AZ 2 - Las Vegas
Select Infrastructure: 1
Application Deployed URL [None]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [128M]:
How many instances? [1]:
Bind existing services to 'portlandrules'? [yN]:
Create services to bind to 'portlandrules'? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Uploading Application:
  Checking for available resources: OK
  Packing application: OK
  Uploading (0K): OK
Push Status: OK
Staging Application 'portlandrules': OK
Starting Application 'portlandrules': OK
</pre>
<p>At this point, you can test whether it's working by checking the app's logs:</p>
<pre>$ af logs portlandrules
====&gt; /logs/staging.log &lt;====

# Logfile created on 2012-09-20 21:40:27 +0000 by logger.rb/25413
Auto-reconfiguration disabled because app does not use Bundler.
Please provide a Gemfile.lock to use auto-reconfiguration.

====&gt; /logs/stdout.log &lt;====

Portland: life is just better here
Portland: life is just better here
Portland: life is just better here
Portland: life is just better here
</pre>
<h3 id="task-scheduling-python">Python</h3>
<p>An alternative in Python is <a href="http://packages.python.org/APScheduler/">Advanced Python Scheduler</a>.</p>
