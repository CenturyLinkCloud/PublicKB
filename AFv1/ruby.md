{{{
  "title": "Languages And Frameworks: Ruby",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#rubyversions">Supported Ruby Versions</a></li>
<li><a href="#bundler">Bundler</a></li>
<li><a href="#gems">Gems and Gemfiles</a></li>
<li><a href="#standalone-ruby">Standalone Apps</a></li>
</ul>
<h3 id="rubyversions">Supported Ruby Versions</h3>
<p>For a list of runtimes that AppFog supports run:</p>
<pre>$ af runtimes

+---------+-------------+---------+
| Name    | Description | Version |
+---------+-------------+---------+
| ruby18  | Ruby 1.8.7  | 1.8.7   |
| ruby192 | Ruby 1.9.2  | 1.9.2   |
| ruby193 | Ruby 1.9.3  | 1.9.3   |
| java    | Java 1.7    | 1.7.0   |
| python2 | python 2.7  | 2.7.3   |
| node04  | nodejs .04  | 0.4.12  |
| node06  | nodejs .06  | 0.6.17  |
| node08  | nodejs .08  | 0.8.14  |
| node10  | nodejs .10  | 0.10.29 |
| php     | PHP 5.3     | 5.3.10  |
| php54   | PHP 5.4     | 5.4.33  |
| php55   | PHP 5.5     | 5.5.17  |
| php56   | PHP 5.6     | 5.6.1   |
+---------+-------------+---------+
</pre>
<p>Ruby 1.8.7 is the default Ruby runtime.</p>
<p>To use Ruby 1.9.3, for example, add the <code>af --runtime ruby193</code> option when you push your code:</p>
<pre>$ af push &lt;appname&gt; --runtime ruby193
</pre>
<h3 id="bundler">Bundler</h3>
<p><a href="http://gembundler.com/">Bundler</a> is required for any ruby app with gem dependencies. Run <code>bundle install</code> each time you modify your Gemfile and before you make an <code>af push</code> or <code>af update</code> command. A populated vendor/cache directory will be used if included in your application. If missing, gems will be compiled/added to your app whenever you update. Apps with a large number of gem dependencies may try to <code>bundle package</code> to speed up the staging process.</p>
<p><a href="https://github.com/jbarnette/isolate">Isolate</a> is not well-supported on AppFog.</p>
<h3 id="gems">Gems and Gemfiles</h3>
<p>AppFog requires a valid <code>Gemfile</code> <strong>and</strong> <code>Gemfile.lock</code> in your app's root directory to successfully match your dependencies.</p>
<p>The following Gemfile feature aren't supported yet:</p>
<ul>
<li>platform-conditional gems (some binary packages are supported)</li>
<li>private git repositories (use vendor/cache instead)</li>
</ul>
<p>AppFog currently only offers one app server for Sinatra and Rails apps: Thin. If you're using Bundler, and nothing in your app's bundle requires Thin, VCAP cannot safely start your app using it. For Rails in such cases, it will fall back to running your app using '<code>rails server</code>', which uses WEBrick. For best performance and results, use Thin.</p>
<h3 id="standalone-ruby">Standalone apps</h3>
<p>Standalone apps requiring provisioned services are not autoconfigured at this time. Explicit connection management is required and we recommend including the <code>cf-runtime</code> gem in your Gemfile and wiring the connections up yourself.</p>
<pre>client = CFRuntime::CloudApp.running_in_cloud? ? CFRuntime::RedisClient.create : Redis.new
</pre>
<p>For a complete working reference, see our sample <a href="https://github.com/appfog/af-ruby-resque">resque app</a>.</p>
