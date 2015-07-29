{{{
  "title": "Add-ons: Logentries",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="https://logentries.com/">Logentries</a> provides Log Management and System Intelligence as a Service. Logentries is a simple and powerful solution for log management. It provides an easy to use interface so that you can quickly understand what is happening in your log data and ultimately your applications. Setup one of the client libraries below in a matter of minutes and start sending logs to Logentries from your AppFog application.</p>
<h3>Install Logentries</h3>
<p>In the "Add-ons" tab on your app console click "Install" for the Logentries add-on. Then add the appropriate library below and you're done!</p>
<p>Once Logentries has been added, you will notice a new enironment variable: <code>LOGENTRIES_TOKEN</code> in the <code>Env variables</code> tab on your app console, containing a Token UUID that is used by the client library to locate your logfile on Logentries.</p>
<p>Next, setup your app to start using the Logentries add-on. In the following sections we have documented the interfaces with several languages and frameworks supported by AppFog.</p>
<ul>
<li><a href="#logentries-ruby">Ruby</a></li>
<li><a href="#logentries-rails">Rails</a></li>
<li><a href="#logentries-sinatra">Sinatra</a></li>
<li><a href="#logentries-php">PHP</a></li>
<li><a href="#logentries-nodejs">NodeJS</a></li>
<li><a href="#logentries-java">Java</a></li>
<li><a href="#logentries-python">Python</a></li>
</ul>
<h3 id="logentries-ruby">Using Logentries from Ruby</h3>
<p>There are two Logentries rubygems, for Rails and Sinatra.</p>
<h4 id="logentries-rails">Configuring Logentries from Rails</h4>
<p>For Rails, update the <code>gemfile</code> to include the logentries gem:</p>
<pre>gem 'le' </pre>
<p>And then install the gem via Bundler:</p>
<pre>$ bundle install</pre>
<p>Enter the following in <code>config/environment.rb</code>:</p>
<pre>Rails.logger = Le.new(ENV.fetch('LOGENTRIES_TOKEN'))</pre>
<p>Lastly, write some log events:</p>
<pre>Rails.logger.info("Hello Logentries. I'm an info message")</pre>
<h4 id="logentries-sinatra">Configuring Logentries on Sinatra</h4>
<p>For Sinatra, update the <code>gemfile</code> to include the logentries gem:</p>
<pre>gem 'sinatra-logentries'</pre>
<p>And then install the gem via Bunlder:</p>
<pre>$ bundle install</pre>
<p>Enter the following in your <code>app.rb</code> file:</p>
<pre>require 'sinatra-logentries'

configure do
    Sinatra::Logentries.token = ENV.fetch('LOGENTRIES_TOKEN')
end</pre>
<p>Lastly, write some log events:</p>
<pre>logger.info("Hello Logentries, I'm an info message.")</pre>
<h3 id="logentries-php">Using Logentries from PHP</h3>
<p>Get the <a href="https://github.com/logentries/le_php/archive/master.zip">PHP library</a> from their Github repository.</p>
<p>Unzip it into your applications root directory.</p>
<p>Enter this line at the top of a PHP file from which you wish to log (adjust if you unzipped elsewhere):</p>
<pre>require dirname(__FILE__) . '/le_php-master/logentries.php';</pre>
<p>Lastly, write some log events:</p>
<pre>$log-&gt;Info("Hello Logentries, I'm an info message");
$log-&gt;Warn("Hey Logentries, I'm a warning");</pre>
<h3 id="logentries-nodejs">Using Logentries from NodeJS</h3>
<p>For NodeJS, install the Logentries library with npm in your apps directory:</p>
<pre>npm install node-logentries</pre>
<p>Enter the following at the top of your <code>app.js</code> file:</p>
<pre>var logentries = require('node-logentries');
var log = logentries.logger({
    token:process.env.LOGENTRIES_TOKEN
});</pre>
<p>Lastly, write some log events:</p>
<pre>log.info("Hey Logentries, I'm an info message")</pre>
<h3 id="logentries-java">Using Logentries from Java</h3>
<h2>Maven Users</h2>
<p>Place this in your pom.xml:</p>
<pre>&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;log4j&lt;/groupId&gt;
        &lt;artifactId&gt;log4j&lt;/artifactId&gt;
        &lt;version&gt;1.2.17&lt;/version&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;com.logentries&lt;/groupId&gt;
        &lt;artifactId&gt;logentries-appender&lt;/artifactId&gt;
        &lt;version&gt;RELEASE&lt;/version&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;</pre>
<h2>Manual Install</h2>
<p>Download the plugin .jar file <a href="http://search.maven.org/#search|gav|1|g:&quot;com.logentries&quot; AND a:&quot;logentries-appender&quot;">here</a> and place it in your <code>WEB-INF/lib</code> folder.</p>
<p>Then, if you don't already have it, download log4j from <a href="https://logging.apache.org/log4j/1.2/download.html">here</a> and place it in your <code>WEB-INF/lib</code> folder.</p>
<h2>Configuration</h2>
<p>The last file you need is the log4j config which you can download <a href="https://raw.githubusercontent.com/logentries/le_java/master/configFiles/log4j.xml.example">here</a>. Be sure to place this on your classpath. A simple way to do this is to put it in your src folder.</p>
<p>Lastly, write some log events, below is a sample Java class configured to use log4j.</p>
<pre>import org.apache.log4j.*;

public class HelloLogentries
{
    private static Logger log = LogManager.getRootLogger();

    public static void main(String[] args)
    {
        log.info("Hello Logentries, I'm from AppFog");
    }
}</pre>
<h3 id="logentries-python">Using Logentries from Python</h3>
<p>For Python, place the following in your <code>requirements.txt</code> file, so it can be installed using pip:</p>
<pre>git+git://github.com/logentries/le_python.git</pre>
<p>Configure the library in your code with the following lines:</p>
<pre>from logentries import LogentriesHandler
import logging,os

log = logging.getLogger('mylogger')
log.addHandler(LogentriesHandler(os.getenv("LOGENTRIES_TOKEN")))</pre>
<p>Lastly, write some log events</p>
<pre>log.info("Hello Logentries, I'm an info message")
log.warning("Im quite important")</pre>
<h3>Support</h3>
<p>All Logentries support issues should be submitted to <a href="mailto:support@logentries.com">Logentries Support</a> or via the Logentries in-app Support widget in the left sidebar.</p>
<h3>Additional resources</h3>
<ul>
<li><a href="http://logentries.com/doc/appfog">Logentries AppFog Documentation</a></li>
</ul>
