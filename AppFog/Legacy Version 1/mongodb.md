{{{
  "title": "Services: MongoDB",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Connection Pool Memory Allocation (10MB maximum for MongoDB, Redis, and RabbitMQ Service Instances) Concurrent Connections (20 maximum for MongoDB, Redis and RabbitMQ) Total Database Storage (based on maximum available service instances) Storage per Database (maximum for MySQL or PostgreSQL service instances) Service Instances (maximum)</p>
<table>
<tbody>
<tr>
<td> </td>
<td><center>Basic</center></td>
<td><center>Developer</center></td>
<td><center>Silver</center></td>
<td><center>Gold</center></td>
<td><center>Platinum</center></td>
</tr>
<tr>
<td><center>Maximum Number of Service Instances</center></td>
<td><center>8</center></td>
<td><center>8</center></td>
<td><center>16</center></td>
<td><center>64</center></td>
<td><center>128</center></td>
</tr>
<tr>
<td><center>Maximum Total Database Storage</center></td>
<td><center>2GB</center></td>
<td><center>4GB</center></td>
<td><center>16GB</center></td>
<td><center>128GB</center></td>
<td><center>512GB</center></td>
</tr>
<tr>
<td><center>Maximum Database Storage Per Instance</center></td>
<td><center>250MB</center></td>
<td><center>500MB</center></td>
<td><center>1GB</center></td>
<td><center>2GB</center></td>
<td><center>4GB</center></td>
</tr>
<tr>
<td><center>Connection Pool Memory Allocation<br />(10MB Maximum)</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
</tr>
<tr>
<td><center>Concurrent Connections<br />(20 Maximum)</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
<td><center>Yes</center></td>
</tr>
</tbody>
</table>
<p> </p>
<p>AppFog provides a MongoDB service that's accessible to apps that are running on any of the supported runtimes and frameworks.</p>
<ul>
<li><a href="#ruby">Ruby</a></li>
<li><a href="#node">Node.js</a></li>
<li><a href="#walkthrough">Node.js with MongoDB Walkthrough</a></li>
<li><a href="#php">PHP</a></li>
</ul>
<h3 id="ruby">Ruby</h3>
<p>You can use the <a href="http://mongomapper.com/">MongoMapper ORM</a> to adapt your Ruby app to access the AppFog MongoDB service.</p>
<h3>Gemfile</h3>
<p>First, add the MongoMapper gem, as well as BSON for serialization of JSON-like documents, which is necessary for interfacing with the MongoDB Ruby driver:</p>
<pre>gem 'mongo_mapper'
gem 'bson_ext'
</pre>
<p>And install the gems:</p>
<pre>$ gem install mongo_mapper
$ gem install bson_ext </pre>
<h3>Rails</h3>
<p>For a Rails app, modify the production section of your app's <code>config/mongo.yml</code> to set credentials, host, and port by parsing the JSON-formatted <code>VCAP_SERVICES</code> environment variable:</p>
<pre>production:
host: &lt;%= JSON.parse(ENV['VCAP_SERVICES'])['mongodb-1.8'].first['credentials']['hostname'] rescue 'localhost' %&gt;
port: &lt;%= JSON.parse( ENV['VCAP_SERVICES'] )['mongodb-1.8'].first['credentials']['port'] rescue 27017 %&gt;
database:  &lt;%= JSON.parse( ENV['VCAP_SERVICES'] )['mongodb-1.8'].first['credentials']['db'] rescue 'tutorial_db' %&gt;
username: &lt;%= JSON.parse( ENV['VCAP_SERVICES'] )['mongodb-1.8'].first['credentials']['username'] rescue '' %&gt;
password: &lt;%= JSON.parse( ENV['VCAP_SERVICES'] )['mongodb-1.8'].first['credentials']['password'] rescue '' %&gt;
</pre>
<p>For other Ruby apps, use the <code>JSON.parse()</code> code to extract the information you need to construct a <a href="http://www.mongodb.org/display/DOCS/Connections">MongoDB connection string</a> from the <code>VCAP_SERVICES</code> environment variable.</p>
<h4>Bundle</h4>
<pre>$ bundle package
$ bundle install
</pre>
<h4>Deploy</h4>
<p>When <code>af</code> asks if you want to bind any services, enter <code>y</code> and choose <code>mongodb</code> from the menu. Provide a name for the service or accept the default:</p>
<pre>$ af push --runtime ruby193
    Would you like to deploy from the current directory? [Yn]:
    Application Name: test
    Application Deployed URL [test.aws.af.cm]:
    Detected a Sinatra Application, is this correct? [Yn]:
    Memory Reservation (64M, 128M, 256M, 512M, 1G) [256M]:
    Creating Application: OK
    Would you like to bind any services to 'test'? [yN]: y
    Would you like to use an existing provisioned service [yN]? N
    The following system services are available
    1: mongodb
    2: mysql
    3: postgresql
    Please select one you wish to provision: 1
    Specify the name of the service [mongodb-example1]:
    Creating Service: OK
    Binding Service [mongodb-example1]: OK
    Uploading Application:
        Checking for available resources: OK
        Processing resources: OK
        Packing application: OK
    Uploading (8K): OK
    Push Status: OK
    Staging Application: OK
    Starting Application: OK
</pre>
<h3 id="node">Node.js</h3>
<p>Before you begin, make sure you have <a href="http://nodejs.org/">Node.js</a> and <a href="http://www.mongodb.org/">MongoDB</a> installed on your development computer.</p>
<h4>Setup</h4>
<p>Start <code>mongod</code> in your local environment:</p>
<pre>$ mongod </pre>
<h4>Push</h4>
<p>Push your Node.js app to AppFog and bind a new MongoDB service to it:</p>
<pre>$ af push
    Would you like to deploy from the current directory? [Yn]:
    Application Name: mongo-node-example
    Application Deployed URL [mongo-node-example.aws.af.cm]:
    Detected a Node.js Application, is this correct? [Yn]:
    Memory Reservation (64M, 128M, 256M, 512M, 1G) [64M]:
    Creating Application: OK
    Would you like to bind any services to 'mongo-node-example'? [yN]: y
    The following system services are available
    1: mongodb
    2: mysql
    3: postgresql
    Please select one you wish to provision: 1
    Specify the name of the service [mongodb-example1]:
    Creating Service: OK
    Binding Service [mongodb-example1]: OK
    Uploading Application:
        Checking for available resources: OK
        Packing application: OK
        Uploading (0K): OK
    Push Status: OK
    Staging Application: OK
    Starting Application: OK
</pre>
<h4>Configure MongoDB</h4>
<p>Next, update your app to use the MongoDB connection information and credentials, both locally and on AppFog, by adding the following code to the beginning of <code>app.js</code>:</p>
<pre>if(process.env.VCAP_SERVICES){
    var env = JSON.parse(process.env.VCAP_SERVICES);
    var mongo = env['mongodb-1.8'][0]['credentials'];
}
else{
    var mongo = {
    "hostname":"localhost",
    "port":27017,
    "username":"",
    "password":"",
    "name":"",
    "db":"db"
    }
}

var generate_mongo_url = function(obj){
    obj.hostname = (obj.hostname || 'localhost');
    obj.port = (obj.port || 27017);
    obj.db = (obj.db || 'test');

    if(obj.username &amp;&amp; obj.password){
        return "mongodb://" + obj.username + ":" + obj.password + "@" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
    else{
        return "mongodb://" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
}

var mongourl = generate_mongo_url(mongo);
</pre>
<p>The if statement provides two different sets of information, depending on whether the app is running locally or on AppFog. <code>generate_mongo_url</code> creates appropriate connection information for MongoDB, which is then assigned to <code>mongourl</code>.</p>
<p>Your app is now configured for MongoDB.</p>
<p>Need a more detailed walkthrough? Keep reading.</p>
<h2 id="walkthrough">Node.js with MongoDB Walkthrough</h2>
<p>Before you start, make sure:</p>
<ul>
<li>You have <a href="https://console.appfog.com/signup">an AppFog account</a>.</li>
<li>The <code>af</code> command line tool is installed on your development computer.</li>
<li><a href="http://nodejs.org/">Node.js</a> is installed on your development computer.</li>
<li><a href="http://www.mongodb.org/">MongoDB</a> is installed on your development computer.</li>
</ul>
<h4>Setup</h4>
<p>Start <code>mongod</code> in your local environment with the following command:</p>
<p><code>$ mongod </code></p>
<p>Confirm that Node.js is installed correctly by starting the interactive javascript console:</p>
<pre>$ node </pre>
<p>Hit <code>Control-C</code> to exit.</p>
<p>Confirm that Node Package Manager (NPM) is installed:</p>
<pre>$ npm -v
1.0.6
</pre>
<p>Log in to AppFog:</p>
<pre>$ af login
</pre>
<h4>Write a Basic Node.js App</h4>
<p>We'll write a basic Node.js app called <code>mongo-node-example</code>.</p>
<p>First, create a directory and change into it:</p>
<pre>$ mkdir mongo-node-example
$ cd mongo-node-example
</pre>
<p>Create a file <code>app.js</code> with the following code:</p>
<pre>var port = (process.env.VMC_APP_PORT || 3000);
var host = (process.env.VCAP_APP_HOST || 'localhost');
var http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World\n');
}).listen(port, host);
</pre>
<p>This creates a Node.js web server using <code>port 3000</code> on <code>localhost</code> that responds to any <code>HTTP</code> request with the string “Hello World”.</p>
<p>Start the Node.js web server locally:</p>
<pre>$ node app.js
</pre>
<p>In another terminal window send a request:</p>
<pre>$ curl localhost:3000
Hello World
</pre>
<p>Alternatively, browse to <code>http://localhost:3000</code> to see the response from the web server.</p>
<p>Hit <code>Control-C</code> in the first terminal window to stop the web server.</p>
<h4>Deploy</h4>
<p>Next, push the application to AppFog. Hit <code>Enter</code> to accept the defaults, but enter a unique name for the app and set up a <code>mongodb</code> service:</p>
<pre>$ af push
Would you like to deploy from the current directory? [Yn]:
Application Name: mongo-node-example
Application Deployed URL [mongo-node-example.aws.af.cm]:
Detected a Node.js Application, is this correct? [Yn]:
Memory Reservation (64M, 128M, 256M, 512M, 1G) [64M]:
Creating Application: OK
Would you like to bind any services to 'mongo-node-example'? [yN]: y
The following system services are available
1: mongodb
2: mysql
3: postgresql
4: rabbitmq
5: redis
Please select one you wish to provision: 1
Specify the name of the service [mongodb-example1]:
Creating Service: OK
Binding Service [mongodb-example1]: OK
Uploading Application:
    Checking for available resources: OK
    Packing application: OK
    Uploading (0K): OK
Push Status: OK
Staging Application: OK
Starting Application: OK
</pre>
<h4>Test</h4>
<pre>$ curl mongo-node-example.aws.af.cm
Hello World
</pre>
<h4>Add MongoDB Configuration</h4>
<p>Your app is now deployed and has a new <code>mongodb</code> service bound to it, but it's not using the service yet. Next, we'll configure the app to use the MongoDB connection information and credentials, both locally and on AppFog.</p>
<p>Add the following code to the beginning of <code>app.js</code>:</p>
<pre>if(process.env.VCAP_SERVICES){
    var env = JSON.parse(process.env.VCAP_SERVICES);
    var mongo = env['mongodb-1.8'][0]['credentials'];
}
else{
    var mongo = {
        "hostname":"localhost",
        "port":27017,
        "username":"",
        "password":"",
        "name":"",
        "db":"db"
    }
}

var generate_mongo_url = function(obj){
    obj.hostname = (obj.hostname || 'localhost');
    obj.port = (obj.port || 27017);
    obj.db = (obj.db || 'test');

    if(obj.username &amp;&amp; obj.password){
        return "mongodb://" + obj.username + ":" + obj.password + "@" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
    else{
        return "mongodb://" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
}

var mongourl = generate_mongo_url(mongo);
</pre>
<p>The if statement provides two different sets of information, depending on whether the app is running locally or on AppFog. <code>generate_mongo_url</code> creates appropriate connection information for MongoDB, which is then assigned to <code>mongourl</code>.</p>
<h4>Test your app locally</h4>
<pre>$ node app.js </pre>
<p>In another terminal:</p>
<pre>$ curl localhost:3000
</pre>
<p>The app should return the string “Hello World”.</p>
<h4>Deploy your update</h4>
<pre>$ af update mongo-node-example <br />Uploading Application: <br />  Checking for available resources: OK <br />  Packing application: OK <br />  Uploading (1K): OK <br />Push Status: OK <br />Stopping Application: OK <br />Staging Application: OK <br />Starting Application: OK</pre>
<h4>Test your app on AppFog</h4>
<p><code><code><code>$ curl mongo-node-example.aws.af.cm Hello World </code></code></code></p>
<h4>Add MongoDB Functionality</h4>
<p>Next, install the MongoDB native drivers locally and update the app to use MongoDB.</p>
<p>Install MongoDB native drivers locally:</p>
<p><code><code><code>$ npm install mongodb </code></code></code></p>
<p>This creates a new local directory called <code>node_modules</code> in the app's root.</p>
<p>In <code>app.js</code>, create a new function called <code>record_visit</code> that stores the server request to MongoDB:</p>
<pre>var record_visit = function(req, res){
    /* Connect to the DB and auth */
    require('mongodb').connect(mongourl, function(err, conn){
        conn.collection('ips', function(err, coll){
            /* Simple object to insert: ip address and date */
            object_to_insert = { 'ip': req.connection.remoteAddress, 'ts': new Date() };

            /* Insert the object then print in response */
            /* Note the _id has been created */
            coll.insert( object_to_insert, {safe:true}, function(err){
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write(JSON.stringify(object_to_insert));
            res.end('\n');
            });
        });
    });
}
</pre>
<p>The <code>.connect</code> method connects to MongoDB using either the local or AppFog <code>mongourl</code>. Then the <code>.collection('ips', ...)</code> method adds the request information to the data that will be committed.</p>
<p>Update the <code>http.createServer</code> method so that it calls the <code>record_visit</code> function when the server request is made:</p>
<pre>http.createServer(function (req, res) {
    record_visit(req, res);
}).listen(port, host);
</pre>
<h4>Test your app locally</h4>
<p><code><code><code>$ node app.js </code></code></code></p>
<p>and from another terminal:</p>
<pre>$ curl localhost:3000
{"ip":"127.0.0.1","ts":"2011-12-29T23:22:38.192Z","_id":"4efcf63ecab9a5b41e000001"}
</pre>
<p>Hit <code>Control-C</code> in the first terminal to stop the web server.</p>
<h4>Test your app on AppFog</h4>
<pre>$ af update mongo-node-example
$ curl mongo-node-example.aws.af.cm
{"ip":"127.0.0.1","ts":"2011-12-29T23:24:25.199Z","_id":"4efcf6a927996b5f79000001"}
</pre>
<p>Create a function <code>print_visits</code> that prints the last ten visits/requests:</p>
<pre>var print_visits = function(req, res){
    /* Connect to the DB and auth */
    require('mongodb').connect(mongourl, function(err, conn){
        conn.collection('ips', function(err, coll){
            coll.find({}, {limit:10, sort:[['_id','desc']]}, function(err, cursor){
                cursor.toArray(function(err, items){
                    res.writeHead(200, {'Content-Type': 'text/plain'});
                    for(i=0; i&lt;items.length;i++){
                        res.write(JSON.stringify(items[i]) + "\n");
                    }
                    res.end();
                });
            });
        });
    });
}
</pre>
<p>Update the <code>createServer</code> method to call the new <code>print_visits</code> function:</p>
<pre>http.createServer(function (req, res) {
    params = require('url').parse(req.url);
    if(params.pathname === '/history') {
        print_visits(req, res);
    }
    else{
        record_visit(req, res);
    }
}).listen(port, host);
</pre>
<p>Web server requests will either add the current visit to MongoDB (the default) or, if url includes “/history”, output the last ten visits.</p>
<h4>Test your app locally</h4>
<pre>$ curl localhost:3000
{"ip":"127.0.0.1","ts":"2011-12-29T23:44:30.254Z","_id":"4efcfb5e2f9d30481f000003"}
$ curl localhost:3000/history
{"ip":"127.0.0.1","ts":"2011-12-29T23:44:30.254Z","_id":"4efcfb5e2f9d30481f000003"}
{"ip":"127.0.0.1","ts":"2011-12-29T23:31:39.339Z","_id":"4efcf85b2f9d30481f000002"}
{"ip":"127.0.0.1","ts":"2011-12-29T23:31:26.678Z","_id":"4efcf84e2f9d30481f000001"}
{"ip":"127.0.0.1","ts":"2011-12-29T23:22:38.192Z","_id":"4efcf63ecab9a5b41e000001"}
</pre>
<p>Stop the application locally and update it on AppFog.</p>
<pre>$ af update mongo-node-example
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
Uploading (8K): OK
Push Status: OK
Stopping Application: OK
Staging Application: OK
Starting Application: OK
</pre>
<h4>Test your app on AppFog</h4>
<pre>$ curl mongo-node-example.aws.af.cm/history
{"ip":"127.0.0.1","ts":"2011-12-29T23:49:46.738Z","_id":"4efcfc9acbfffadc0b000001"}
{"ip":"127.0.0.1","ts":"2011-12-29T23:24:25.199Z","_id":"4efcf6a927996b5f79000001"}
</pre>
<h3 id="php">PHP</h3>
<p>Connecting your PHP app to a bound MongoDB service is simple:</p>
<pre>$services_json = json_decode(getenv("VCAP_SERVICES"),true);
$mongo_config = $services_json["mongodb-1.8"][0]["credentials"];

$username = $mongo_config["username"];
$password = $mongo_config["password"];
$hostname = $mongo_config["hostname"];
$port = $mongo_config["port"];
$db = $mongo_config["db"];
$name = $mongo_config["name"];

$connect = "mongodb://${username}:${password}@${hostname}:${port}/${db}";
$m = new Mongo($connect);
$db = $m-&gt;selectDB($db);
</pre>
<h3>Links</h3>
<p>For another complete sample app for a Node.js app with MongoDB, check out <a href="https://github.com/appfog/af-node-sample-mongodb">our GitHub repo</a>.</p>
<p>For more information, check out <a href="http://docs.cloudfoundry.com/services/mongodb/nodejs-mongodb.html">Cloud Foundry's documentation on MongoDB</a>.</p>
