{{{
  "title": "Languages And Frameworks: Flask",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The following is a step-by-step guide to writing and deploying a "hello world" Python Flask app:</p>
<h3>Create the App</h3>
<p>Create a directory for the app and change into it:</p>
<pre>$ mkdir flask-example
$ cd flask-example
</pre>
<h3>Prepare Your Environment</h3>
<p><!--- Create a <code>virtualenv</code> environment:</p>

<pre>$ virtualenv venv
New python executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
</pre>

<p>---></p>
<p>Note: There is currently an issue with using <code>virtualenv</code> in an app directory, so we'll use a workaround.</p>
<pre>$ mkdir ../flask-example-venv
$ virtualenv ../flask-example-venv
New python executable in ../flask-example-venv/bin/python
Installing setuptools............done.
Installing pip...............done.
</pre>
<p>Activate the environment:</p>
<pre>$ . ../flask-example-venv/bin/activate
(flask-example-venv) $
</pre>
<p>Use <code>pip</code> to install Flask:</p>
<pre>(flask-example-venv) $ pip install Flask
Downloading/unpacking Flask
Downloading Flask-0.9.tar.gz (481Kb): 481Kb downloaded
Running setup.py egg_info for package Flask
Downloading/unpacking Werkzeug&gt;=0.7 (from Flask)
Downloading Werkzeug-0.8.3.tar.gz (1.1Mb): 1.1Mb downloaded
Running setup.py egg_info for package Werkzeug
Downloading/unpacking Jinja2&gt;=2.4 (from Flask)
Downloading Jinja2-2.6.tar.gz (389Kb): 389Kb downloaded
Running setup.py egg_info for package Jinja2
Installing collected packages: Flask, Werkzeug, Jinja2
Running setup.py install for Flask
Running setup.py install for Werkzeug
Running setup.py install for Jinja2
Successfully installed Flask Werkzeug Jinja2
Cleaning up...
</pre>
<p>Create a file called <code>wsgi.py</code> with the following code:</p>
<pre>from flask import Flask, Request, Response
application = app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
</pre>
<h3>Test Your App Locally</h3>
<pre>(flask-example-venv) $ python wsgi.py
 * Running on http://127.0.0.1:5000/
</pre>
<p>In another terminal:</p>
<pre>$ curl 127.0.0.1:5000
Hello World!%
</pre>
<h3>Prepare Your App for Deployment on AppFog</h3>
<p>Create a <code>requirements.txt</code> file with the following:</p>
<pre>flask==0.8
</pre>
<h3>Deploy to Appfog</h3>
<pre>af push flask-example
Would you like to deploy from the current directory? [Yn]:

Detected a Python WSGI Application, is this correct? [Yn]:
Application Deployed URL [flask-example.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [64M]:
How many instances? [1]:
Bind existing services to 'flask-example'? [yN]:
Create services to bind to 'flask-example'? [yN]:
Would you like to save this configuration? [yN]:

Creating Application: OK
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
    Uploading (10M): OK
Push Status: OK
Staging Application 'flask-example': OK
Starting Application 'flask-example': OK
</pre>
<h3>Test Your App on AppFog:</h3>
<pre>$ curl flask-example.aws.af.cm
Hello World!%
</pre>
<h3>Connect Your App to Services</h3>
<p>Now we'll connect Flask to a MongoDB service provided by AppFog.</p>
<h3>Bind Service</h3>
<p>Use the <code>af create-service &lt;service&gt; &lt;name&gt; &lt;app&gt;</code> command to create the <code>mongodb</code> service and bind it in one step:</p>
<pre>$ af create-service mongodb mongo-example flask-example
Creating Service: OK
Binding Service [mongo-example]: OK
Stopping Application 'flask-example': OK
Staging Application 'flask-example': OK
Starting Application 'flask-example': OK
</pre>
<h3>Add MongoDB Configuration</h3>
<p>Your app now has a new <code>mongodb</code> service bound to it, but it's not using the service yet. Next, we’ll configure the app to use the MongoDB connection information and credentials, both locally and on AppFog.</p>
<p>First, add this to <code>requirements.txt</code>:</p>
<pre>pymongo==2.1.1
</pre>
<p>Then add the following to the beginning of <code>wsgi.py</code>:</p>
<pre>import time
import sys
import os
import json
</pre>
<p>And add the following to the end, right before <code>if __name__ == '__main__':</code></p>
<pre>@app.route('/mongo')
def mongotest():
    from pymongo import Connection
    uri = mongodb_uri()
    conn = Connection(uri)
    coll = conn.db['ts']
    coll.insert(dict(now=int(time.time())))
    last_few = [str(x['now']) for x in coll.find(sort=[("_id", -1)], limit=10)]
    body = "\n".join(last_few)
    return Response(body, content_type="text/plain;charset=UTF-8")

def mongodb_uri():
    services = json.loads(os.getenv("VCAP_SERVICES", "{}"))
    if services:
        creds = services['mongodb-1.8'][0]['credentials']
        uri = "mongodb://%s:%s@%s:%d/%s" % (
            creds['username'],
            creds['password'],
            creds['hostname'],
            creds['port'],
            creds['db'])
        print &gt;&gt; sys.stderr, uri
        return uri
    else:
        uri = "mongodb://localhost:27017"
</pre>
<p>We also need to install <code>pymongo</code> for our local test:</p>
<pre>$ pip install pymongo
Downloading/unpacking pymongo
Downloading pymongo-2.2.1.tar.gz (230Kb): 230Kb downloaded
Running setup.py egg_info for package pymongo

Installing collected packages: pymongo
Running setup.py install for pymongo
...
Successfully installed pymongo
Cleaning up...
</pre>
<h3>Test Your App Locally</h3>
<pre>(flask-example-venv) $ python wsgi.py
 * Running on http://127.0.0.1:5000/
</pre>
<p>In another terminal:</p>
<pre>$ curl 127.0.0.1:5000/mongo
1342592886%
</pre>
<h3>Deploy to AppFog</h3>
<pre>$ af update flask-example
Uploading Application:
    Checking for available resources: OK
    Processing resources: OK
    Packing application: OK
    Uploading (10M): OK
Push Status: OK
Stopping Application 'flask-example': OK
Staging Application 'flask-example': OK
Starting Application 'flask-example': OK
</pre>
<h3>Test Your App on AppFog</h3>
<pre>$ curl flask-example.aws.af.cm/mongo
1342483543%
</pre>
