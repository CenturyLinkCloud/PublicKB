{{{
  "title": "Add-ons: MemCachier",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://www.memcachier.com/">MemCachier</a> is an implementation of the <a href="http://memcached.org/">Memcache</a> in-memory key/value store used for caching data. It is a key technology in modern web apps for scaling and reducing server loads. The MemCachier add-on manages and scales clusters of memcache servers so you can focus on your app. Tell us how much memory you need and get started for free instantly. Add capacity later as you need it.</p>
<p>The information below will quickly get you up and running with the MemCachier add-on for AppFog. For information on the benefits of MemCachier and how it works, please refer to the more extensive <a href="http://www.memcachier.com/documentation/memcache-user-guide/">User Guide</a>.</p>
<h4>Install MemCachier</h4>
<p>In the “Add-ons” tab in your app console click “Install” for the MemCachier add-on. That’s it!</p>
<p>Next, set up your app to start using the cache. We have documentation for the following languages and frameworks:</p>
<ul>
<li><a href="#ruby">Ruby</a></li>
<li><a href="#rails">Rails</a></li>
<li><a href="#django">Django</a></li>
<li><a href="#php">PHP</a></li>
<li><a href="#java">Java</a></li>
<li><a href="#local">Local Setup</a></li>
<li><a href="#upgrade">Upgrading and Downgrading</a></li>
<li><a href="#support">Support</a></li>
</ul>
<p>Your credentials may take up to three (3) minutes to be synced to our servers. You may see authentication errors if you start using the cache immediately.</p>
<h3 id="ruby">Ruby</h3>
<p>Start by adding the <a href="https://github.com/memcachier/memcachier-gem">memcachier</a> and <a href="http://github.com/mperham/dalli">dalli</a> gems to your <code>Gemfile</code>.</p>
<pre>gem 'memcachier'
gem 'dalli'</pre>
<p>Then bundle install:</p>
<pre>$ bundle install</pre>
<p><code>Dalli</code> is a Ruby memcache client, and the <code>memcachier</code> gem modifies the environment (<code>ENV</code>) such that the environment variables set by MemCachier will work with Dalli. Once these gems are installed you can start writing code. The following is a basic example showing get and set.</p>
<pre>require 'dalli'
require 'memcachier'
cache = Dalli::Client.new
cache.set("foo", "bar")
puts cache.get("foo")</pre>
<p>Without the <code>memcachier</code> gem, you’ll need to pass the proper credentials to <code>Dalli</code>:</p>
<pre>cache = Dalli::Client.new(ENV["MEMCACHIER_SERVERS"].split(","),
                    {:username =&gt; ENV["MEMCACHIER_USERNAME"],
                     :password =&gt; ENV["MEMCACHIER_PASSWORD"]})</pre>
<h3 id="rails">Rails</h3>
<p>Start by adding the <a href="https://github.com/memcachier/memcachier-gem">memcachier</a> and <a href="http://github.com/mperham/dalli">dalli</a> gems to your <code>Gemfile</code>.</p>
<pre>gem 'memcachier'
gem 'dalli'</pre>
<p>Then bundle install:</p>
<pre>$ bundle install</pre>
<p><code>Dalli</code> is a Ruby memcache client, and the <code>memcachier</code> gem modifies the environment (<code>ENV</code>) such that the environment variables set by MemCachier will work with <code>Dalli</code>. Once these gems are installed you’ll want to configure the Rails <code>cache_store</code> appropriately. Modify <code>config/environments/production.rb</code> with the following:</p>
<pre>config.cache_store = :dalli_store</pre>
<p>From here you can use the following code examples to use the cache in your Rails app:</p>
<pre>Rails.cache.write("foo", "bar")
puts Rails.cache.read("foo")</pre>
<p>Without the <code>memcachier</code> gem, you’ll need to pass the proper credentials to <code>Dalli</code> in <code>config/environments/production.rb</code>:</p>
<pre>config.cache_store = :dalli_store, ENV["MEMCACHIER_SERVERS"].split(","),
                    {:username =&gt; ENV["MEMCACHIER_USERNAME"],
                     :password =&gt; ENV["MEMCACHIER_PASSWORD"]}</pre>
<h4>Testing</h4>
<p>To test locally you can simply use the rails console:</p>
<pre>rails console
&gt;&gt; Rails.cache.write('memcachier', 'rocks')
=&gt; true
&gt;&gt; Rails.cache.read('memcachier')
=&gt; "rocks"</pre>
<h3 id="django">Django</h3>
<p>MemCachier has been tested with the <code>pylibmc</code> memcache client, but the default client doesn’t support SASL authentication. Run the following commands on your local machine to install the necessary pips:</p>
<pre>$ sudo port install libmemcached
$ LIBMEMCACHED=/opt/local pip install pylibmc
$ pip install django-pylibmc-sasl</pre>
<p>Be sure to update your <code>requirements.txt</code> file with these new requirements (note that your versions may differ from what’s below):</p>
<pre>pylibmc==1.2.2
django-pylibmc-sasl==0.2.4</pre>
<p>Next, configure your <code>settings.py</code> file the following way:</p>
<pre>os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '')
os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

CACHES = {
  'default': {
    'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
    'LOCATION': os.environ.get('MEMCACHIER_SERVERS', ''),
    'TIMEOUT': 500,
    'BINARY': True,
  }
}</pre>
<p>From here you can start writing cache code in your Django app:</p>
<pre>from django.core.cache import cache
cache.set("foo", "bar")
print cache.get("foo")</pre>
<h3 id="php">PHP</h3>
<p>Start by downloading the <a href="https://github.com/ronnywang/PHPMemcacheSASL">PHPMemcacheSASL</a> library. From here you can start writing cache code in your PHP app:</p>
<pre>include('MemcacheSASL.php');
$server_pieces = explode(':', getenv("MEMCACHIER_SERVERS"))
$m = new MemcacheSASL;
$m-&gt;addServer($server_pieces[0], $server_pieces[1]);
$m-&gt;setSaslAuthData(getenv("MEMCACHIER_USERNAME"), getenv("MEMCACHIER_PASSWORD"));

$m-&gt;add("foo", "bar");
echo $m-&gt;get("foo");</pre>
<p>Or, check out <a href="https://github.com/ceslami/PHPMemcacheSASL">this fork of PHPMemcacheSASL</a> modified specifically for use with AppFog, by AppFog user <a href="https://github.com/ceslami">ceslami</a>.</p>
<p>The more common PHP memcache clients, <a href="http://www.php.net/manual/en/book.memcache.php">Memcache</a> and <a href="http://www.php.net/manual/en/book.memcached.php">Memcached</a>, don’t support SASL authentication at this time and can’t be used with MemCachier.</p>
<h3 id="java">Java</h3>
<p>For Java we recommend using the <a href="https://code.google.com/p/spymemcached/">SpyMemcached</a> client. We also recommend using the <a href="https://maven.apache.org/">Apache Maven</a> build manager for working with Java app. If you aren’t using <code>maven</code> and are instead using <a href="https://ant.apache.org/">Apache Ant</a> or your own build system, then simply add the <code>spymemcached</code> jar file as a dependency of your app.</p>
<p>For <code>maven</code> however, start by configuring it to have the proper <code>spymemcached</code> repository:</p>
<pre>&lt;repository&gt;
  &lt;id&gt;spy&lt;/id&gt;
  &lt;name&gt;Spy Repository&lt;/name&gt;
  &lt;layout&gt;default&lt;/layout&gt;
  &lt;url&gt;http://files.couchbase.com/maven2/&lt;/url&gt;
  &lt;snapshots&gt;
    &lt;enabled&gt;false&lt;/enabled&gt;
  &lt;/snapshots&gt;
&lt;/repository&gt;</pre>
<p>Then add the <code>spymemcached</code> library to your dependencies:</p>
<pre>&lt;dependency&gt;
  &lt;groupId&gt;spy&lt;/groupId&gt;
  &lt;artifactId&gt;spymemcached&lt;/artifactId&gt;
  &lt;version&gt;2.8.1&lt;/version&gt;
  &lt;scope&gt;provided&lt;/scope&gt;
&lt;/dependency&gt;</pre>
<p>Once your build system is configured, you can start adding caching to your Java app:</p>
<pre>import java.io.IOException;
import net.spy.memcached.AddrUtil;
import net.spy.memcached.MemcachedClient;
import net.spy.memcached.ConnectionFactoryBuilder;
import net.spy.memcached.auth.PlainCallbackHandler;
import net.spy.memcached.auth.AuthDescriptor;

public class Foo {
  public static void main(String[] args) {
    AuthDescriptor ad = new AuthDescriptor(new String[] { "PLAIN" },
        new PlainCallbackHandler(System.getenv("MEMCACHIER_USERNAME"),
            System.getenv("MEMCACHIER_PASSWORD")));

    try {
      MemcachedClient mc = new MemcachedClient(new ConnectionFactoryBuilder()
          .setProtocol(ConnectionFactoryBuilder.Protocol.BINARY)
          .setAuthDescriptor(ad).build(), AddrUtil.getAddresses(System
          .getenv("MEMCACHIER_SERVERS") + ":11211"));
      mc.set("foo", "bar");
      System.out.println(mc.get("foo"));
    } catch (IOException ioe) {
      System.err.println("Couldn't create a connection to MemCachier: \nIOException "
              + ioe.getMessage());
    }
  }
}</pre>
<p>You may wish to look the <code>spymemcached</code> <a href="http://dustin.github.com/java-memcached-client/apidocs/">JavaDocs</a> or some more <a href="https://code.google.com/p/spymemcached/wiki/Examples">example code</a> to help in using MemCachier effectively.</p>
<h3 id="libsupport">Library Support</h3>
<p>MemCachier will work with any memcached binding that supports <a href="https://en.wikipedia.org/wiki/Simple_Authentication_and_Security_Layer">SASL authentication</a> and the <a href="https://code.google.com/p/memcached/wiki/MemcacheBinaryProtocol">binary protocol</a>. We have tested MemCachier with the following language bindings, although the chances are good that other SASL binary protocol packages will also work.</p>
<table class="table table-bordered table-striped">
<thead>
<tr>
<td>Language</td>
<td>Bindings</td>
</tr>
</thead>
<tbody>
<tr>
<td>Ruby</td>
<td>dalli</td>
</tr>
<tr>
<td>Python</td>
<td>pylibmc</td>
</tr>
<tr>
<td>Django</td>
<td>django-pylibmc</td>
</tr>
<tr>
<td>PHP</td>
<td>PHPMemcacheSASL</td>
</tr>
<tr>
<td>Java</td>
<td>spymemcached</td>
</tr>
</tbody>
</table>
<h3 id="local">Local Setup</h3>
<p>To test against your AppFog app locally, you'll need to run a local memcached process. MemCachier can only run in AppFog. But because MemCachier and memcached speak the same protocol, you shouldn’t have any issues testing locally. Installation depends on your platform.</p>
<h4>Ubuntu</h4>
<pre>$ sudo apt-get install memcached</pre>
<h4>Mac OS X (with Homebrew)</h4>
<pre>$ brew install memcached</pre>
<h4>Windows</h4>
<p>Please refer to <a href="http://www.codeforest.net/how-to-install-memcached-on-windows-machine">these instructions</a>.</p>
<p>For further information and resources (such as the memcached source code) please refer to the <a href="http://memcached.org/">Memcache.org homepage</a>.</p>
<p>To run memcached simply execute the following command:</p>
<pre>$ memcached -v</pre>
<h3 id="upgrade">Upgrading and Downgrading</h3>
<p>Changing your plan, either by upgrading or downgrading, requires no code changes. Your cache won’t be lost, either. Upgrading and downgrading Just Works™.</p>
<h3 id="support">Support</h3>
<p>You can submit all Memcachier support and runtime issues to <a href="http://support.appfog.com">AppFog Support</a> and any non-support related issues or product feedback to <a href="https://www.memcachier.com/contact">Contact Memcachier</a>.</p>
<p>Memcachier reports issues related to service at <a href="http://status.memcachier.com/">Memcachier Status</a>.</p>
