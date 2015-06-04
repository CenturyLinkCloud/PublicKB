{{{
  "title": "Services: PostgreSQL",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog provides a PosgreSQL service that's accessible to apps that are running on any of the supported runtimes and frameworks.</p>
<ul>
<li><a href="#vcap">VCAP_SERVICES</a></li>
<li><a href="#php">PHP</a></li>
<li><a href="#ruby">Ruby</a></li>
</ul>
<h3 id="vcap">The VCAP_SERVICES Environment Variable</h3>
<p>When you provision and bind a service to your app, AppFog creates an environment variable called <code>VCAP_SERVICES</code>. For apps that can't be automatically configured, you can find the information your app needs to connect to the database in this variable.</p>
<p>This variable contains a JSON document with a list of all credentials and connection information for the bound services.</p>
<p>Here's an example that of the environment variable for an app that has a PostgreSQL service bound to it:</p>
<pre>{"postgresql-9.1":[
    {
        "name":"postgresql-5633b",
        "label":"postgresql-9.1",
        "plan":"free",
        "tags":["postgresql","postgresql-9.1","relational"],
        "credentials":{
            "name":"d19a133d77da6470383d825e0bc56f7a7",
            "host":"10.0.48.220",
            "hostname":"10.0.48.220",
            "port":5432,
            "user":"ub3df122ceb05491899e0f227634a859f",
            "username":"ub3df122ceb05491899e0f227634a859f",
            "password":"p0d09ed1578024aebb700057d398cd24b"
        }
    }
]}
</pre>
<p>You can use your app's language-specific facility to call the environment variable.</p>
<p>In Java:</p>
<pre>java.lang.System.getenv("VCAP_SERVICES")
</pre>
<p>In Ruby:</p>
<pre>ENV['VCAP_SERVICES']
</pre>
<p>In Javascript:</p>
<pre>process.env.VCAP_SERVICES
</pre>
<p>In Python:</p>
<pre>os.getenv("VCAP_SERVICES")
</pre>
<p>In PHP:</p>
<pre>getenv("VCAP_SERVICES")
</pre>
<h3 id="php">PHP</h3>
<p>Connecting your PHP app to a bound PostgreSQL service is simple:</p>
<pre>$services_json = json_decode(getenv("VCAP_SERVICES"),true);
$postgresql_config = $services_json["postgresql-9.1"][0]["credentials"];

$username = $postgresql_config["username"];
$password = $postgresql_config["password"];
$hostname = $postgresql_config["hostname"];
$port = $postgresql_config["port"];
$db = $postgresql_config["name"];

$link = pg_connect("host=$hostname port=$port dbname=$db user=$username password=$password");
</pre>
<h3 id="ruby">Ruby</h3>
<p>Connecting your Ruby app to a bound PostgreSQL service is simple:</p>
<pre>require "pg"

services = JSON.parse(ENV['VCAP_SERVICES'])
postgresql_key = services.keys.select { |svc| svc =~ /postgresql/i }.first
postgresql = services[postgresql_key].first['credentials']
postgresql_conn = {:host =&gt; postgresql['hostname'], :port =&gt; postgresql['port'], :username =&gt; postgresql['user'], :password =&gt; postgresql['password'], :dbname =&gt; postgresql['name']}
connection = PG.connect(postgresql_conn)
</pre>
