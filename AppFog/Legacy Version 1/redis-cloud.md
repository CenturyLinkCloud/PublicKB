{{{
  "title": "Add-ons: Redis Cloud",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://redis-cloud.com">Redis Cloud</a> is a fully-managed service for running your Redis dataset. You can quickly and easily get your apps up and running with Redis Cloud on AppFog. You can then add as many Redis databases as you need (each running in a dedicated process, in a non-blocking manner) and increase or decrease the memory size of your plan without affecting your existing data. You can easily import an existing dataset to any of your Redis Cloud databases, from your AWS S3 account or from any other Redis server. Daily backups are performed automatically and in addition, you can backup your dataset manually at any given time.</p>
<p>Note: Redis Cloud is currently only available on our AWS US-East infrastructure.</p>
<h3>Install Redis Cloud</h3>
<p>In the "Add-ons" tab on your app console click "Install" for the Redis Cloud add-on. That’s it!</p>
<p>Once Redis Cloud has been added, you will notice a new environment variable: <code>REDISCLOUD_URL</code> in the <code>Env variables</code> tab on your app console, containing the username, password, hostname and port of your first Redis Cloud database.</p>
<p>Note: as database provisioning is carried out asynchronously, please wait until the creation and initialization of the database is complete. This process shouldn't take more than 60 seconds. You're ready to go when the "hostname" value in the <code>REDISCLOUD_URL</code> environment variable is different than your "localhost".</p>
<p>Next, setup your app to start using the Redis Cloud add-on. In the following sections we have documented the interfaces with several languages and frameworks supported by AppFog.</p>
<ul>
<li><a href="#rediscloud-ruby">Ruby</a></li>
<li><a href="#rediscloud-rails">Rails</a></li>
<li><a href="#rediscloud-sinatra">Sinatra</a></li>
<li><a href="#rediscloud-java">Java</a></li>
<li><a href="#rediscloud-python">Python</a></li>
<li><a href="#rediscloud-django">Django</a></li>
<li><a href="#rediscloud-php">PHP</a></li>
<li><a href="#rediscloud-node">Node.js</a></li>
</ul>
<h3 id="rediscloud-ruby">Using Redis from Ruby</h3>
<p>The <a href="https://github.com/redis/redis-rb">redis-rb</a> is a very stable and mature redis client and the easiest way to access Redis from Ruby.</p>
<p>Install redis-rb:</p>
<pre>$ gem install redis</pre>
<h4 id="rediscloud-rails">Configuring Redis from Rails</h4>
<p>For Rails 2.3.3 up to Rails 3.0, update the <code>config/environment.rb</code> to include the redis gem:</p>
<pre>config.gem 'redis' </pre>
<p>For Rails 3.0 and above, update the <code>Gemfile</code>:</p>
<pre>gem 'redis'  </pre>
<p>And then install the gem via Bundler:</p>
<pre>$ bundle install</pre>
<p>Lastly, create a new <code>redis.rb</code> initializer in <code>config/initializers/</code> and add the following code snippet:</p>
<pre>uri = URI.parse(ENV["REDISCLOUD_URL"])
$redis = Redis.new(:host =&gt; uri.host, :port =&gt; uri.port, :password =&gt; uri.password)</pre>
<h4 id="rediscloud-sinatra">Configuring Redis on Sinatra</h4>
<p>Add this code snippet to your configure block:</p>
<pre>configure do
    . . .
    require 'redis'
    uri = URI.parse(ENV["REDISCLOUD_URL"])
    REDIS = Redis.new(:host =&gt; uri.host, :port =&gt; uri.port, :password =&gt; uri.password)
    . . .
end</pre>
<h4>Using Redis on Unicorn</h4>
<p>No special setup is required when using Redis Cloud with a Unicorn server. Users running Rails apps on Unicorn should follow the instructions in the <a href="#rediscloud-rails">Configuring Redis from Rails</a> section and users running Sinatra apps on Unicorn should follow the instructions in the <a href="#rediscloud-sinatra">Configuring Redis on Sinatra</a> section.</p>
<h4>Testing (Ruby)</h4>
<pre>redis.set("foo", "bar")
# =&gt; "OK"
redis.get("foo")
# =&gt; "bar"</pre>
<h3 id="rediscloud-java">Using Redis from Java</h3>
<p><a href="https://github.com/xetorthio/jedis">Jedis</a> is a blazingly small, sane and easy to use Redis java client. You can download the latest build from <a href="https://github.com/xetorthio/jedis/releases">github</a> or use it as a maven dependency:</p>
<pre>&lt;dependency&gt;
    &lt;groupId&gt;redis.clients&lt;/groupId&gt;
    &lt;artifactId&gt;jedis&lt;/artifactId&gt;
    &lt;version&gt;2.0.0&lt;/version&gt;
    &lt;type&gt;jar&lt;/type&gt;
    &lt;scope&gt;compile&lt;/scope&gt;
&lt;/dependency&gt;</pre>
<p>Configure connection to your Redis Cloud service using <code>REDISCLOUD_URL</code> environment variable and the following code snippet:</p>
<pre>try {
        URI redisUri = new URI(System.getenv("REDISCLOUD_URL"));
        JedisPool pool = new JedisPool(new JedisPoolConfig(),
                redisUri.getHost(),
                redisUri.getPort(),
                Protocol.DEFAULT_TIMEOUT,
                redisUri.getUserInfo().split(":",2)[1]);
} catch (URISyntaxException e) {
           // URI couldn't be parsed.
} </pre>
<h4>Testing (Java)</h4>
<pre>Jedis jedis = pool.getResource();
jedis.set("foo", "bar");
String value = jedis.get("foo");
// return the instance to the pool when you're done
pool.returnResource(jedis);</pre>
<p>(example taken from Jedis docs).</p>
<h3 id="rediscloud-python">Using Redis from Python</h3>
<p><a href="https://github.com/andymccurdy/redis-py">redis-py</a> is the most common client to access Redis from Python.</p>
<p>Use pip to install it:</p>
<pre>$ pip install redis</pre>
<p>Configure connection to your Redis-Cloud service using <code>REDISCLOUD_URL</code> environment variable and the following code snippet:</p>
<pre>import os
import urlparse
import redis
url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)</pre>
<h4>Testing (Python):</h4>
<pre>&gt;&gt;&gt; r.set('foo', 'bar')
True
&gt;&gt;&gt; r.get('foo')
'bar'</pre>
<h4 id="rediscloud-django"><a href="https://github.com/sebleier/django-redis-cache">Django-redis-cache</a></h4>
<p>Redis can be used as the back-end cache for Django.</p>
<p>To do so, install django-redis-cache:</p>
<pre>$ pip install django-redis-cache</pre>
<p>Next, configure your <code>CACHES</code> in the <code>settings.py</code> file:</p>
<pre>import os
import urlparse
redis_url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
CACHES = {
    'default': {
    'BACKEND': 'redis_cache.RedisCache',
    'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
    'OPTIONS': {
        'PASSWORD': redis_url.password,
        'DB': 0,
    }
  }
}</pre>
<h4>Testing (Django)</h4>
<pre>from django.core.cache import cache
cache.set("foo", "bar")
print cache.get("foo")</pre>
<h3 id="rediscloud-php">Using Redis from PHP</h3>
<p><a href="https://github.com/nrk/predis">Predis</a> is a flexible and feature-complete PHP client library for Redis.</p>
<p>Instructions for installing the <a href="https://github.com/nrk/predis">Predis</a> library can be found <a href="https://github.com/nrk/predis#how-to-use-predis">here</a>.</p>
<p>Loading the library to your project should be straightforward:</p>
<pre>&lt;?php
// prepend a base path if Predis is not present in your "include_path".
require 'Predis/Autoloader.php';
Predis\Autoloader::register();</pre>
<p>Configure connection to your Redis Cloud service using <code>REDISCLOUD_URL</code> environment variable and the following code snippet:</p>
<pre>$redis = new Predis\Client(array(
    'host' =&gt; parse_url($_ENV['REDISCLOUD_URL'], PHP_URL_HOST),
    'port' =&gt; parse_url($_ENV['REDISCLOUD_URL'], PHP_URL_PORT),
    'password' =&gt; parse_url($_ENV['REDISCLOUD_URL'], PHP_URL_PASS),
));</pre>
<h4>Testing (PHP)</h4>
<pre>$redis-&gt;set('foo', 'bar');
$value = $redis-&gt;get('foo');</pre>
<h3 id="rediscloud-node">Using Redis from Node.js</h3>
<p><a href="https://github.com/mranney/node_redis">node_redis</a> is a complete Redis client for node.js.</p>
<p>You can install it with:</p>
<pre>$ npm install redis</pre>
<p>Configure connection to your Redis-Cloud service using <code>REDISCLOUD_URL</code> environment variable and the following code snippet:</p>
<pre>var redis = require('redis');
var url = require('url');
var redisURL = url.parse(process.env.REDISCLOUD_URL);
var client = redis.createClient(redisURL.port, redisURL.hostname, {no_ready_check: true});
client.auth(redisURL.auth.split(":")[1]);</pre>
<h4>Testing (Node.js)</h4>
<pre>client.set('foo', 'bar');
client.get('foo', function (err, reply) {
    console.log(reply.toString()); // Will print `bar`
});</pre>
<h3>Dashboard</h3>
<p>Our dashboard presents all performance and usage metrics of your Redis Cloud service on a single screen, as shown below:</p>
<p><img class="screenshot" src="https://s3.amazonaws.com/redis-cloud-appfog/doc/appfog-dashbord-redis.jpeg" alt="" /></p>
<p>To access your Redis Cloud dashboard, simply click the "Manage" button of the RedisCloud add-on in the "Add-ons" tab on your app console.</p>
<p>You can then find your dashboard under the <code>MY DATABASES</code> menu.</p>
<h3>Adding Redis databases to your app</h3>
<p>Redis Cloud allows you to add multiple Redis databases, each running in a dedicated process, in a non-blocking manner (i.e. without interfering with your other databases). You can create as many databases as you need.</p>
<p>Your first Redis database is created automatically upon launching the Redis Cloud add-on and its URL and credentials are maintained in <code>REDISCLOUD_URL</code> environment variable.</p>
<p>To add more databases, simply access your Redis Cloud add-on by clicking the "Manage" button and then click the <code>New DB</code> button in the <code>MY DATABASES &gt; Manage</code> page.</p>
<p>Warning: The Redis Cloud console will provide you a new URL for connecting to your new Redis database.</p>
<h3>Pricing</h3>
<p>The Redis Cloud AppFog add-on is in beta phase and is currently offered for free.</p>
<h3>Support</h3>
<p>All Redis Cloud support and runtime issues should be submitted to <a href="http://support.appfog.com">AppFog Support</a>. You may <a href="https://redislabs.com/contact" target="_blank&quot;">Contact Redis Labs</a> with any non-support related issues or product feedback.</p>
<h3>Additional resources</h3>
<ul>
<li><a href="http://redis-cloud.com/redis/developers">Developers Resources</a></li>
<li><a href="http://redis.io/documentation">Redis Documentation</a></li>
</ul>
