{{{
  "title": "Languages And Frameworks: Ruby on Rails",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#rails30">Rails 3.0</a></li>
<li><a href="#rails31">Rails 3.1</a></li>
<li><a href="#rails-console">Rails Console</a></li>
<li><a href="#rake-db-seed">rake db:seed</a></li>
<li><a href="#autoreconfig">Auto-reconfiguration</a></li>
</ul>
<p>AppFog currently only offers one app server for Rails apps: Thin. If you're using Bundler, and nothing in your app's bundle requires Thin, VCAP cannot safely start your app using it. For Rails in such cases, it will fall back to running your app using '<code>rails server</code>', which uses WEBrick. For best performance and results, use Thin.</p>
<h3 id="rails30">Rails 3.0</h3>
<p>Ruby on Rails app deployments on AppFog automatically recognize MySQL. For other services, you'll need to access the <code>VCAP_SERVICES</code> environment variable. </p>
<p>Make sure to use the correct version of the MySQL2 gem in your Gemfile:</p>
<pre># If you use a different database in development, hide it from AppFog
group :development do
gem 'sqlite3'
end

# Rails 3.0 requires version less than 0.3 of mysql2 gem
group :production do
gem 'mysql2', '&lt; 0.3'
end
</pre>
<h3>Bundle your app:</h3>
<pre>$ bundle package
$ bundle install
</pre>
<p>Deploy:</p>
<pre>$ af push
</pre>
<h3 id="rails31">Rails 3.1</h3>
<p>Rails 3.1 introduces the asset pipeline. To get the asset pipeline working on AppFog, precompile your assets in your development environment. This compiles them into <code>public/assets</code>, at which point you can tweak the production environment configuration before excuting a normal <code>af push</code>.</p>
<h4>Gemfile</h4>
<pre># If you use a different database in development, hide it from AppFog.
group :development do
gem 'sqlite3'
end

# Rails 3.1 can use the latest mysql2 gem.
group :production do
gem 'mysql2'
end
</pre>
<h4>Bundle your app:</h4>
<pre>$ bundle package
$ bundle install
</pre>
<h4>Configs</h4>
<p>In <code>config/environments/production.rb</code>, change</p>
<pre>config.server_static_assets = false
</pre>
<p>to</p>
<pre>config.server_static_assets = true
</pre>
<h4>Assets</h4>
<p>Pre-compile your asset pipeline:</p>
<pre>$ bundle exec rake assets:precompile
</pre>
<h4>Version Control System</h4>
<p>Commit the current configuration to your version control system. Consider including: + <code>Gemfile.lock</code> + gems packaged into <code>vendor/cache</code> + assets compiled into <code>public/assets</code>.</p>
<h4>Deploy</h4>
<pre>$ af push
</pre>
<h3>Services</h3>
<p>AppFog automatically creates and binds a new MySQL service with the Ruby on Rails jumpstart, and the app is <a href="#autoreconfig">automatically reconfigured</a> to connect to the service. </p>
<h3 id="rails-console">Rails Console</h3>
<p>To use the Rails console with your database service, tunnel into the service, and choose 'none' when it asks you which client to start:</p>
<pre>$ af tunnel ror-example-mysql
Binding Service [ror-example-mysql]: OK
Stopping Application 'caldecott-aws': OK
Staging Application 'caldecott-aws': OK
Starting Application 'caldecott-aws': OK
Getting tunnel connection info: OK

Service connection info:
  username : uKaJETLlNmkrs
  password : pYfnUUY3L5jLU
  name     : d77261f24bbae4c889d0a231b3e70a763
  infra    : aws

Starting tunnel to ror-example-mysql on port 10000.
1: none
2: mysql
3: mysqldump
Which client would you like to start?: 1
Open another shell to run command-line clients or
use a UI tool to connect using the displayed information.
Press Ctrl-C to exit...
</pre>
<p>Next, create another database section in your <code>config/database.yml</code> file with the service connection info in the <code>af tunnel</code> output:</p>
<pre>proxied-appfog:
adapter: mysql2
database : d77261f24bbae4c889d0a231b3e70a763
username : uKaJETLlNmkrs
password : pYfnUUY3L5jLU
port: 10000
host: 127.0.0.1
</pre>
<p>Finally, in a another terminal, run <code>rails console</code>, passing in the database environment you created:</p>
<pre>$ RAILS_ENV=proxied-appfog rails console
</pre>
<p>That's it, you now have a Rails console proxied to your AppFog database service!</p>
<h2 id="rake-db-seed">rake db:seed</h2>
<p>This assumes that you have your Rails app set up, and you have a MySQL service bound to it.</p>
<h4>Tunnel to your bound MySQL service</h4>
<p>Use the af tunnel command to connect to the MySQL service that's bound to your Rails app. When prompted, enter '1' for no client.</p>
<pre>$ af tunnel
1: rails-mysql-example
Which service to tunnel to?: 1
Getting tunnel connection info: OK

Service connection info:
username : &lt;username&gt;
password : &lt;password&gt;
name : &lt;db-name&gt;

Starting tunnel to rails-mysql-example on port 10000.
1: none
2: mysql
3: mysqldump
Which client would you like to start?: 1
Open another shell to run command-line clients or
use a UI tool to connect using the displayed information.
Press Ctrl-C to exit...
</pre>
<p>You now have a secure tunnel set up to your MySQL service through which you can run <code>rake db:seed</code>.</p>
<h4>Create a new section in your <code>config/database.yml</code> file</h4>
<pre>proxied-appfog:
adapter: mysql2
database: &lt;db-name&gt;
username: &lt;username&gt;
password: &lt;password&gt;
port: 10000
host: 127.0.0.1
</pre>
<h4>Run <code>rake db:seed</code></h4>
<p>Start with a simple <code>seeds.rb</code> file that just creates one record in your database to test that it works.</p>
<p>Then, leaving open the terminal window with the tunnel running in it, open a new terminal window and run:</p>
<pre>$ RAILS_ENV=proxied-appfog rake db:seed
</pre>
<p>If all goes well, you should have a log file in your <code>log/</code> directory called <code>proxied-appfog.log</code> that shows the SQL commands running from your <code>seeds.rb</code> file.</p>
<pre>$ af files ror-example logs/
startup.log                               8.2K
stdout.log                                  0B
proxied-appfog.log                          0B
</pre>
<h3 id="autoreconfig">Auto-reconfiguration</h3>
<p>Ruby on Rails apps deployed on AppFog support auto-reconfiguration for relational database services. This means you can deploy a Rails app on AppFog without changing a single line of code.</p>
<p>AppFog automatically reconfigures Rails apps by modifying the production settings in your <code>config/database.yml</code> file during staging.</p>
<p>While it’s fairly common to put these types of connections in a Rails Initializer File, auto-reconfiguration should work just as well if you create the connection somewhere else within your app.</p>
<p>When your Rails app is staged for deployment, AppFog makes two modifications:</p>
<ul>
<li>Adds an additional <code>cf-autoconfig</code> gem to your Bundle.</li>
<li>Adds an Initializer file to <code>config/initializers</code> that ensures that all dynamic class modification is done prior to loading other Initializers (and thus before your app executes).</li>
</ul>
<h4>Limitations</h4>
<p>Auto-reconfiguration only works if there's exactly one service of a given service type bound to your app. For example, you can only bind only one relational database service (e.g. MySQL or Postgres) to an app.</p>
<p>If your app doesn’t follow these limitations, AppFog won't auto-reconfigure your app.</p>
<p>The auto-reconfiguration mechanism also expects typical Ruby apps. If your app configuration is complex, it may not work. In those cases, you can opt out of auto-reconfiguration:</p>
<h4>Opting out of auto-reconfiguration</h4>
<p>AppFog offers a few ways to opt out of the auto-reconfiguration mechanism.</p>
<ul>
<li>Create a file in your Rails app called <code>config/cloudfoundry.yml</code>. Add the entry <code>autoconfig: false</code>.</li>
<li>Include the <code>cf-runtime</code> gem in your app's <code>Gemfile</code>.</li>
</ul>
<h3>Further Reading</h3>
<p>For more technical details about how auto-reconfiguration works on AppFog, check out <a href="http://blog.cloudfoundry.com/2012/03/12/using-cloud-foundry-services-with-ruby-part-1-auto-reconfiguration/">this blog post</a>.</p>
