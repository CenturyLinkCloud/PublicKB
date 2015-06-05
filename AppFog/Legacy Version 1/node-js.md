{{{
  "title": "Languages And Frameworks: Node.js",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#node-supported-versions">Supported Versions</a></li>
<li><a href="#node-deployment">Deployment</a></li>
<li><a href="#node-dep-mgmt">Dependency Management</a></li>
<li><a href="#node-npm-problems">Potential Problems with NPM</a></li>
<li><a href="#node-coffee-script">CoffeeScript</a></li>
<li><a href="#node-walkthrough">"Hello World" Walkthrough</a></li>
</ul>
<h3 id="node-supported-versions">Supported Versions</h3>
<p>For the most reliable development experience, make sure you have the same runtime version of Node.js used on your local development environment as your target AppFog instance. You can check the available runtimes by executing this command:</p>
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
<p>You can download and install the <a href="https://github.com/joyent/node/tags">specific version of Node.js</a>.</p>
<p>The default Node.js runtime version is Node 0.10.22, however you can specify a different runtime version when you deploy by using the runtime flag. For example, to use Node 0.6.17:</p>
<pre>$ af push --runtime=node06
</pre>
<h2 id="node-deployment">Deployment</h2>
<p>When you deploy a Node.js app to AppFog, the stager runs the first of the following files it finds:</p>
<ul>
<li>server.js</li>
<li>app.js</li>
<li>index.js</li>
<li>main.js</li>
<li>application.js</li>
</ul>
<p>Alternatively, you can specify the startup file in your <code>package.json</code> file, by specifying the <code>start</code> command under the <code>scripts</code> key:</p>
<pre>{
    "name": "test-app",
    "version": "0.0.1",
    "scripts": {
        "start": "node server.js"
    }
    ....
}
</pre>
<h2 id="node-dep-mgmt">Dependency Management</h2>
<p>AppFog supports <a href="https://npmjs.org/">npm</a> (Node Package Manager).</p>
<p>You can install your dependencies to your local machine in one of two ways: directly or by using a <code>package.json</code> file that names all of your dependencies.</p>
<p>Direct installation of <code>express</code>, for example, would look like this:</p>
<pre>$ npm install express
</pre>
<p>Or you can have a <code>package.json</code> file that names the dependency:</p>
<pre>{
    "name":"hello-node",
    "version":"0.0.1",
    "dependencies":{
        "express":""
    }
}
</pre>
<p>Once you have the <code>package.json</code> file ready, you can simply run:</p>
<pre>$ npm install
</pre>
<p>This will install all of the packages named in <code>package.json</code>.</p>
<p>Both of these installation methods will create a directory called <code>node_modules</code> which will include the entire contents of all of your dependencies. When you deploy your code with an <code>af push</code>, AppFog simply uploads your app, including the entire <code>node_modules</code> directory.</p>
<h3>NPM Shrinkwrap</h3>
<p>AppFog also supports <a href="https://npmjs.org/doc/shrinkwrap.html">npm shrinkwrap</a>. This means that you can instruct AppFog to rebuild the modules, which you'll want to do if your app has any native dependencies, for example.</p>
<p>To make use of this feature, simply run:</p>
<pre>$ npm shrinkwrap
</pre>
<p>This command looks at your <code>node_modules</code> directory and generates an <code>npm-shrinkwrap.json</code> file, which reflects the whole tree of dependencies with fixed versions. This functions as a snapshot of your app's dependencies in much the same way that <code>Gemfile.lock</code> does for Ruby apps. This file guarantees that AppFog provides the exact node module versions to avoid compatibility issues.</p>
<p>If you deploy your app with those conditions in place, AppFog will install the node modules to the app during the staging process. If the require node module doesn't work with the node engine that the app is running on, however, AppFog will not install the module.</p>
<h4 id="node-npm-problems">Potential Problems with NPM</h4>
<p>Users have reported issues with their npm installs failing. This is due to the format of the npm-shrinkwrap.json file being used.</p>
<p>While a valid shrinkwrap file, those formatted as follows should not be used:</p>
<p><code> "dependencies": { "qs": { "version": "0.6.5", "from": "qs@0.6.5" }, </code></p>
<p>This will result in the npm installer attempting to install a package <code>qs@qs@0.6.5</code>, due to the installer prepending the dependency name to the "from" attribute.</p>
<p>Instead, the following format should be used instead.</p>
<p><code> "dependencies": { "qs": { "version": "0.6.5", "from" : "0.6.5" }, </code></p>
<h2 id="node-coffee-script">CoffeeScript</h2>
<p>You can deploy a <a>CoffeeScript</a> Node app to AppFog by using a shim file to load the CoffeeScripts.</p>
<p>Assuming you have two files, <code>app.coffee</code> and <code>app.js</code>, <code>app.js</code> can simply look like this:</p>
<pre>require('coffee-script');
require('./app')
</pre>
<p>The <code>app.coffee</code> file is what you would normally run with <code>coffee app.coffee</code>. Make sure <code>coffee-script</code> is also in your <code>node-modules</code> directory. Requiring the <code>coffee-script</code> module will enhance node's <code>require</code> functionality and compile the coffee files at require time.</p>
<h2 id="node-walkthrough">"Hello World" Walkthrough</h2>
<p>The following is a step-by-step guide to writing and deploying a “hello world” Node.js web server app with the <a href="http://expressjs.com/">Express</a> web module:</p>
<h3>Create the App</h3>
<p>Create a directory for the app and change into it:</p>
<pre>$ mkdir hello-node
$ cd hello-node
</pre>
<p>Create a <code>package.json</code> file with the following contents:</p>
<pre>{
    "name":"hello-node",
    "version":"0.0.1",
    "dependencies":{
        "express":""
    }
}
</pre>
<p>Use <code>npm</code> (Node Package Manager) to install the dependencies named in <code>package.json</code>:</p>
<pre>$ npm install
</pre>
<p>Create a file called <code>app.js</code> with the following code:</p>
<pre>var express = require('express')
var app = express()

app.get('/', function (req, res) {
  res.send('Hello from AppFog!')
})

app.listen(process.env.VCAP_APP_PORT || 3000)
</pre>
<p>Notice that AppFog passes the listen port for your app in an environment variable, accessed by <code>process.env.VCAP_APP_PORT</code>.</p>
<h3>Deploy the App</h3>
<pre>$ af login
</pre>
<p>Push the app. You can hit <code>Enter</code> to accept the defaults at most of the prompts, but be sure to enter a unique <code>URL</code> for the app. Here's an example push:</p>
<pre>$ af push
Would you like to deploy from the current directory? [Yn]:
Application Name: hello-node
Detected a Node.js Application, is this correct? [Yn]:
Application Deployed URL [hello-node.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [64M]:
How many instances? [1]:
Bind existing services to 'hello-node'? [yN]:
Create services to bind to 'hello-node'? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
    Uploading (255K): OK
Push Status: OK
Staging Application 'hello-node': OK
Starting Application 'hello-node': OK
</pre>
<p>Hit the app in your browser, <code>http://hello-node.aws.af.cm</code>, in this example.</p>
<h2 id="express">Environments in Express</h2>
<p>Express supports arbitrary environments, like <code>production</code> and <code>development</code>. You can use the <code>configure()</code> method to set different configurations under the different environments. Here, we'll bind a <code>mongodb</code> service to the app to demonstrate.</p>
<h3>Bind Service</h3>
<p>Use the <code>af create-service &lt;service&gt; &lt;name&gt; &lt;app&gt;</code> command to create the <code>mongodb</code> service and bind it in one step:</p>
<pre>$ af create-service mongodb mongo-example hello-node
Creating Service: OK
Binding Service [mongo-example]: OK
Stopping Application 'hello-node': OK
Staging Application 'hello-node': OK
Starting Application 'hello-node': OK
</pre>
<h3>Add MongoDB Configuration</h3>
<p>Your app now has a new <code>mongodb</code> service bound to it, but it's not using the service yet. Next, we’ll configure the app to use the MongoDB connection information and credentials, both locally and on AppFog.</p>
<p>Add the following code to the beginning of <code>app.js</code>, right after the line <code>var express = require('express');</code>:</p>
<pre>var express = require('express');
var mongo;
app.configure('development', function(){
    mongo = {
        "hostname":"localhost",
        "port":27017,
        "username":"",
        "password":"",
        "name":"",
        "db":"db"
    }
});
app.configure('production', function(){
    var env = JSON.parse(process.env.VCAP_SERVICES);
    mongo = env['mongodb-1.8'][0]['credentials'];
});

var generate_mongo_url = function(obj){
    obj.hostname = (obj.hostname || 'localhost');
    obj.port = (obj.port || 27017);
    obj.db = (obj.db || 'test');

    if(obj.username &amp;&amp; obj.password){
        return "mongodb://" + obj.username + ":" + obj.password + "@" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }else{
        return "mongodb://" + obj.hostname + ":" + obj.port + "/" + obj.db;
    }
}

var mongourl = generate_mongo_url(mongo);
</pre>
<p>Now the app is set to connect to the local <code>mongodb</code> server when it's in <code>development</code> mode. In production mode, it's set to connect to the AppFog service that's bound to the app, by parsing <code>VCAP_SERVICES</code> variable.</p>
<h3>Add MongoDB Functionality</h3>
<p>Next, install the MongoDB native drivers locally and update the app to use MongoDB.</p>
<p>Install MongoDB native drivers locally:</p>
<pre>$ npm install mongodb
</pre>
<p>This adds a new local directory called <code>mongodb</code> in the <code>node_modules</code> directory.</p>
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
<p>Update the <code>app.get</code> method so that it calls the <code>record_visit</code> function when the server request is made:</p>
<pre>app.get('/', function(req, res) {
    record_visit(req, res);
});
app.listen(process.env.VCAP_APP_PORT || 3000);
</pre>
<h3>Test Your App Locally</h3>
<pre>$ mongod
</pre>
<p>and from another terminal:</p>
<pre>$ node app.js
</pre>
<p>and from a third terminal:</p>
<pre>$ curl localhost:3000
{"ip":"127.0.0.1","ts":"2011-12-29T23:22:38.192Z","_id":"4efcf63ecab9a5b41e000001"}
</pre>
<p>Hit <code>Control-C</code> in the first terminal to stop the web server.</p>
<h3>Production Environment Variable</h3>
<p>Next, add the <code>NODE_ENV</code> environment variable to the app deployment and set it to <code>production</code> so that Express knows to run the app in <code>production</code> mode:</p>
<pre>$ af env-add hello-node NODE_ENV=production
Adding Environment Variable [NODE_ENV=production]: OK
Stopping Application 'hello-node': aOK
Staging Application 'hello-node': OK
Starting Application 'hello-node': OK
</pre>
<h3>Test Your App on AppFog</h3>
<pre>$ af update hello-node
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
    Uploading (1M): OK
Push Status: OK
Stopping Application 'hello-node': OK
Staging Application 'hello-node': OK
Starting Application 'hello-node': OK

$ curl hello-node.aws.af.cm
{"ip":"127.0.0.1","ts":"2011-12-29T23:24:25.199Z","_id":"4efcf6a927996b5f79000001"}
</pre>
