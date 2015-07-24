{{{
  "title": "Add-ons: MemCached-Cloud",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://redislabs.com/memcached-cloud">Memcached Cloud</a> is a fully-managed service that operates your Memcached in a reliable and fail-safe manner. Your dataset is constantly replicated, so if a node fails, an automatic failover mechanism guarantees that your data is served without interruption. Memcached Cloud provides various data persistence options as well as remote backups for disaster recovery purposes. You can quickly and easily get your apps up and running with Memcached Cloud through its add-on for AppFog, just tell us how much memory you need and start using your Memcached bucket instantly.</p>
<p>A Memcached bucket is created in seconds and from that moment on, all operations are fully automated. The service completely frees developers from dealing with nodes, clusters, server lists, scaling and failure recovery, while guaranteeing absolutely no data loss.</p>
<h2>Getting Started</h2>
<p>In the "Add-ons" tab on your app console click "Install" for the <code>Memcached Cloud</code> add-on. That's it!</p>
<p>Once <code>Memcached Cloud</code> has been added, you will notice three new enironment variables: <code>MEMCACHEDCLOUD_SERVERS</code>, <code>MEMCACHEDCLOUD_USERNAME</code>, <code>MEMCACHEDCLOUD_PASSWORD</code> in the <code>Env variables</code> tab on your app console, containing the servers and credentials of your first <code>Memcached Cloud</code> bucket.</p>
<p>Next, setup your app to start using the Memcached Cloud add-on. In the following sections we have documented the interfaces with several languages and frameworks supported by AppFog.</p>
<ul>
<li><a href="#ruby">Ruby</a></li>
<li><a href="#rails">Rails</a></li>
<li><a href="#sinatra">Sinatra</a></li>
<li><a href="#unicorn">Unicorn</a></li>
<li><a href="#java">Java</a></li>
<li><a href="#python">Python</a></li>
<li><a href="#django">Django</a></li>
<li><a href="#php">PHP</a></li>
</ul>
<h2><a id="ruby"></a>Using Memcached with Ruby</h2>
<p><a href="https://github.com/mperham/dalli">Dalli</a> is a high performance, pure Ruby client for accessing Memcached servers that uses binary protocol.</p>
<h3><a id="rails"></a>Configuring Memcached on Rails</h3>
<p>To use Dalli with Rails 3.x, update your gems with:</p>
<pre>:::ruby
gem 'dalli'  </pre>
<p>And then install the gem via Bundler:</p>
<pre>:::ruby
bundle install</pre>
<p>Lastly, add the following line in your <code>config/environments/production.rb</code>:</p>
<pre>:::ruby
config.cache_store = :dalli_store, ENV[MEMCACHEDCLOUD_SERVERS].split(','), { :username =&gt; ENV[MEMCACHEDCLOUD_USERNAME], :password =&gt; ENV[MEMCACHEDCLOUD_PASSWORD] }</pre>
<h3><a id="sinatra"></a>Configuring Memcached on Sinatra</h3>
<p>Add this code snippet to your configure block:</p>
<pre>:::ruby
configure do
    . . .
    require 'dalli'

    $cache = Dalli::Client.new(ENV[MEMCACHEDCLOUD_SERVERS].split(','), :username =&gt; ENV[MEMCACHEDCLOUD_USERNAME], :password =&gt; ENV[MEMCACHEDCLOUD_PASSWORD])
    . . .
end</pre>
<h3><a id="unicorn"></a>Using Memcached on Unicorn</h3>
<p>No special setup is required when using Memcached Cloud with a Unicorn server. Users running Rails apps on Unicorn should follow the instructions in the <a href="#rails">Configuring Memcached from Rails</a> section and users running Sinatra apps on Unicorn should follow the instructions in the <a href="#sinatra">Configuring Memcached on Sinatra</a> section.</p>
<h3>Testing from Ruby</h3>
<pre>:::ruby
$cache.set("foo", "bar")
# =&gt; true
$cache.get("foo")
# =&gt; "bar"</pre>
<h2><a id="java"></a>Using Memcached with Java</h2>
<p><a href="https://code.google.com/p/spymemcached/">spymemcached</a> is a simple, asynchronous, single-threaded Memcached client written in Java. You can download the latest build from: <a href="https://code.google.com/p/spymemcached/downloads/list">https://code.google.com/p/spymemcached/downloads/list</a>. If you are using <code>Maven</code>, start by adding the following repository:</p>
<pre>:::java
&lt;repositories&gt;
    &lt;repository&gt;
      &lt;id&gt;spy&lt;/id&gt;
      &lt;name&gt;Spy Repository&lt;/name&gt;
      &lt;layout&gt;default&lt;/layout&gt;
      &lt;url&gt;http://files.couchbase.com/maven2/&lt;/url&gt;
      &lt;snapshots&gt;
        &lt;enabled&gt;false&lt;/enabled&gt;
      &lt;/snapshots&gt;
    &lt;/repository&gt;
&lt;/repositories&gt;</pre>
<p>Next, specify the actual artifact as follows:</p>
<pre>:::java
&lt;dependency&gt;
  &lt;groupId&gt;spy&lt;/groupId&gt;
  &lt;artifactId&gt;spymemcached&lt;/artifactId&gt;
  &lt;version&gt;2.8.9&lt;/version&gt;
  &lt;scope&gt;provided&lt;/scope&gt;
&lt;/dependency&gt;</pre>
<p>Configure the connection to your Memcached Cloud service by using the <code>MEMCACHEDCLOUD</code> <code>Env variables</code> as shown in the following code snippet:</p>
<pre>:::java
try {
    AuthDescriptor ad = new AuthDescriptor(new String[] { "PLAIN" },
        new PlainCallbackHandler(System.getenv("MEMCACHEDCLOUD_USERNAME"), System.getenv("MEMCACHEDCLOUD_PASSWORD")));

    MemcachedClient mc = new MemcachedClient(
              new ConnectionFactoryBuilder()
                  .setProtocol(ConnectionFactoryBuilder.Protocol.BINARY)
                  .setAuthDescriptor(ad).build(),
          AddrUtil.getAddresses(System.getenv("MEMCACHEDCLOUD_SERVERS")));

} catch (IOException ex) {
    // the Memcached client could not be initialized.
} </pre>
<h3>Testing from Java</h3>
<pre>:::java
mc.set("foo", 0, "bar");
Object value = mc.get("foo");</pre>
<h2><a id="python"></a>Using Memcached with Python</h2>
<p><a href="https://github.com/jaysonsantos/python-binary-memcached">bmemcached</a> is a pure, thread safe, python module to access memcached via binary protocol.</p>
<p>Use <code>pip</code> to install it:</p>
<pre>:::term
pip install python-binary-memcached</pre>
<p>Configure the connection to your Memcached Cloud service using the <code>MEMCACHEDCLOUD``Env variables</code> and the following code snippet:</p>
<pre>:::python
import os
import urlparse
import bmemcached
import json

mc = bmemcached.Client(os.environ.get('MEMCACHEDCLOUD_URL').split(','), os.environ.get('MEMCACHEDCLOUD_USERNAME'), os.environ.get('MEMCACHEDCLOUD_PASSWORD'))</pre>
<h3>Testing from Python</h3>
<pre>:::python
mc.set('foo', 'bar')
print client.get('foo')</pre>
<h3><a id="django"></a>Using Memcached with Django</h3>
<p>Memcached Cloud can be used as a Django cache backend with <a href="https://github.com/jaysonsantos/django-bmemcached">django-bmemcached</a>.</p>
<p>To do so, install django-bmemcached:</p>
<pre>:::term
pip install django-bmemcached</pre>
<p>Next, configure your <code>CACHES</code> in the <code>settings.py</code> file:</p>
<pre>:::python
import os
import urlparse
import json

CACHES = {
    'default': {
        'BACKEND': 'django_bmemcached.memcached.BMemcached',
        'LOCATION': os.environ.get('MEMCACHEDCLOUD_URL').split(','),
        'OPTIONS': {
                    'username': os.environ.get('MEMCACHEDCLOUD_USERNAME'),
                    'password': os.environ.get('MEMCACHEDCLOUD_PASSWORD')
            }
    }
}</pre>
<h3>Testing from Django</h3>
<pre>:::python
from django.core.cache import cache
cache.set("foo", "bar")
print cache.get("foo")</pre>
<h2><a id="php"></a>Using Memcached with PHP</h2>
<p><a href="https://github.com/ronnywang/PHPMemcacheSASL">PHPMemcacheSASL</a> is a simple PHP class with SASL support.</p>
<p>Include the class in your project and configure a connection to your Memcached Cloud service using the <code>MEMCACHEDCLOUD``Env variables</code> and the following code snippet:</p>
<pre>&lt;?php
include('MemcacheSASL.php');

$mc = new MemcacheSASL;
list($host, $port) = explode(':', $_ENV['MEMCACHEDCLOUD_SERVERS']);
$mc-&gt;addServer($host, $port);
$mc-&gt;setSaslAuthData($_ENV['MEMCACHEDCLOUD_USERNAME'], $_ENV['MEMCACHEDCLOUD_PASSWORD']);</pre>
<h3>Testing from PHP</h3>
<pre>$mc-&gt;add("foo", "bar");
echo $mc-&gt;get("foo");</pre>
<h2>Memcached Cloud Dashboard</h2>
<p>Our dashboard displays all of the performance and usage metrics for your Memcached Cloud service on a single screen, as shown in the following screenshot:</p>
<p><img title="" src="https://s3.amazonaws.com/paas-docs/memcached-cloud/appfog+-+mem.png" alt="Dashboard" /></p>
<p>To access your Memcached Cloud dashboard, simply click the "Manage" button of your Memcached Cloud add-on in the "Add-ons" tab on your app console.</p>
<p>You can then find your dashboard under the <code>MY BUCKETS</code> menu.</p>
<h2>Pricing</h2>
<p>The Memcached Cloud AppFog add-on is in beta phase and is currently offered for free.</p>
<h2>Adding Memcached Buckets to Your Plan</h2>
<p>Memcached Cloud allows you to add multiple Memcached buckets to your plan, each running in a dedicated process and in a non-blocking manner (i.e. without interfering with your other buckets). You can create as many buckets as you need.</p>
<p>Your first Memcached bucket is provisioned automatically upon launching the Memcached Cloud add-on. Its servers and credentials are maintained with the <code>MEMCACHEDCLOUD</code> env. vars. To add more buckets, simply access your Memcached Cloud console and click the <code>Add Bucket</code> button in the <code>MY BUCKETS &gt; Manage</code> page.</p>
<p>Your new Memcached bucket's server and credentials will be displayed in the Memcached Cloud console.</p>
<h2>Support</h2>
<p>All Memcached Cloud support and runtime issues should be submitted to <a href="http://support.appfog.com">AppFog Support.</a></p>
<p>Any non-support related issues or product feedback is welcome via email at <a href="https://redislabs.com/contact">info@redislabs.com</a>.</p>
<h2>Additional Resources</h2>
<ul>
<li><a href="http://redislabs.com/php-memcached">Developers Resources</a></li>
<li><a href="https://code.google.com/p/memcached/wiki/NewStart">Memcached Wiki</a></li>
</ul>
