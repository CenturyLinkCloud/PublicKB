{{{
  "title": "Services: Working with VCAP_SERVICES Environment Variables",
  "date": "1-21-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>When you provision and bind a service to your app, AppFog creates an environment variable called <code>VCAP_SERVICES</code>.</p>
<p>This variable contains a JSON document with a list of all credentials and connection information for the bound services.</p>
<p>Here's an example that of the environment variable for an app that has two MySQL database services bound to it:</p>
<pre>{"mysql-5.1":[
    {
        "name":"mysql-4f700",
        "label":"mysql-5.1",
        "plan":"free",
        "tags":["mysql","mysql-5.1","relational"],
        "credentials":{
            "name":"d6d665aa69817406d8901cd145e05e3c6",
            "hostname":"mysql-node01.us-east-1.aws.af.cm",
            "host":"mysql-node01.us-east-1.aws.af.cm",
            "port":3306,
            "user":"uB7CoL4Hxv9Ny",
            "username":"uB7CoL4Hxv9Ny",
            "password":"pzAx0iaOp2yKB"
        }
    },
    {
        "name":"mysql-f1a13",
        "label":"mysql-5.1",
        "plan":"free",
        "tags":["mysql","mysql-5.1","relational"],
        "credentials":{
            "name":"db777ab9da32047d99dd6cdae3aafebda",
            "hostname":"mysql-node01.us-east-1.aws.af.cm",
            "host":"mysql-node01.us-east-1.aws.af.cm",
            "port":3306,
            "user":"uJHApvZF6JBqT",
            "username":"uJHApvZF6JBqT",
            "password":"p146KmfkqGYmi"
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
