{{{
  "title": "CURL and Proxy API",
  "date": "1-29-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><em>Note: If you see any errors on this page, please let us know at support@appfog.com</em></p>
<p><a href="#manipulation">Existing Resources - Manipulating Them and Gathering Data</a> <br /> <a href="#creation">Creating New Resources</a></p>
<ul>
<li><a href="#create_app">App Creation Resource Notes</a></li>
<li><a href="#create_service">Service Creation Resource Notes</a></li>
</ul>
<p><a href="#examples">CURL Examples</a></p>
<hr />
<h2 id="headers">Authorization and Other Headers</h2>
<p>The API uses 4 types of headers:</p>
<table>
<tbody>
<tr>
<td>
<pre>-H Authorization:$TOKEN</pre>
</td>
<td>This header must contain the alphanumeric value contained in the login token and is needed for every CURL call against the API. For Unix\Linux users, the token is in <strong>.af_token</strong> located in your home folder by default. It is recommended that you export the token to an environment variable when you want to work with the API. This way you can simply call the variable instead of copy/pasting the entire alphanumeric value for each attempt.</td>
</tr>
<tr>
<td>
<pre>-H Content-Type:application/json</pre>
</td>
<td>This must set JSON as the data type being sent to the API when updating app details.</td>
</tr>
<tr>
<td>
<pre>-H Content-Type:applicaton/xml</pre>
</td>
<td>It must be set as XML when uploading code/content to an app.</td>
</tr>
<tr>
<td>
<pre>-H Content-Encoding:gzip</pre>
</td>
<td>This must be set as GZIP when uploading code/content to an app.</td>
</tr>
<tr>
<td>
<pre>-H Proxy-User:sample@domain.tld</pre>
</td>
<td>This must contain the email address of the account with which you want to interact. This header is needed when making changes to a team account. You must be a <a href="teams.md">team member</a> of that account to accomplish this.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="verbs">HTTP Verbs</h2>
<table>
<tbody>
<tr>
<td>GET</td>
<td>Retrieving Resources</td>
</tr>
<tr>
<td>POST</td>
<td>Creating Resources</td>
</tr>
<tr>
<td>PUT</td>
<td>Replacing Resources</td>
</tr>
<tr>
<td>DELETE</td>
<td>Deleting Resources</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="manipulation">Existing Resources - Manipulating Them and Gathering Data</h2>
<p>There are 3 types of resource available from which you may gather information, and 1 which you can directly manipulate. They're all written in JSON. There is one for each user, app, and service. Templates are shown below along with notes.</p>
<table>
<tbody>
<tr>
<td><a href="#user">USER</a></td>
<td>
<pre>{
    "id":,
    "email":"",
    "plan":"",
    "company":"",
    "created_at":"",
    "updated_at":"",
    "uuid":"",
    "deleted_at":"",
    "admin":
}</pre>
</td>
</tr>
<tr>
<td><a href="#service">SERVICE</a></td>
<td>
<pre>{
    "name":"",
    "type":"",
    "vendor":"",
    "provider":"",
    "version":"",
    "tier":"",
    "properties":{},
    "meta":{
        "created":,
        "updated":,
        "tags":["","",""],
        "version":
    },
    "infra":{
        "provider":"",
        "name":""
    }
}</pre>
</td>
</tr>
<tr>
<td><a href="#app">APP</a></td>
<td>
<pre>{
    "name":"",
    "staging":{
        "model":"",
        "stack":""
    },
    "uris":[],
    "instances":,
    "runningInstances":,
    "resources":{
        "memory":,
        "disk":,
        "fds":
    },
    "state":"",
    "services":[],
    "version":"",
    "env":[],
    "meta":{
        "debug":,
        "console":,
        "version":,
        "created":
    },
    "infra":{
        "provider":"",
        "name":""
    }
}</pre>
</td>
</tr>
</tbody>
</table>
<p> </p>
<h3 id="user">User - Existing Resource Notes</h3>
<p>This resource is not editable, but can be provide useful information. The <strong>deleted_at</strong> key value will always be NULL because a deleted user will not have this JSON resource anymore.</p>
<h3 id="service">Service - Existing Resource Notes</h3>
<p>This resource is not editable, but can be provide useful information.</p>
<h3 id="app">App - Existing Resource Notes</h3>
<p>There are 2 versions of this object for each app: STARTED and STOPPED. Changes uploading using this resource must use the stopped version. Either run the stop command through CLI tool or web console, or get the most recent version of this resource and update the <strong>state</strong> key value to STOPPED. Then get the JSON resource of the stopped app.</p>
<p>Editable Resources:</p>
<table>
<tbody>
<tr>
<td>Key</td>
<td>Value Type</td>
<td>Note</td>
</tr>
<tr>
<td><em>name</em></td>
<td>STRING</td>
<td>After editing this, ensure you've updated the URL of the app you want to work on in your CURL command.</td>
</tr>
<tr>
<td><em>uris</em></td>
<td>STRING</td>
<td>More than one URL can be added. They must self-contained strings delimited by commas.</td>
</tr>
<tr>
<td><em>instances</em></td>
<td>Integer</td>
<td> </td>
</tr>
<tr>
<td><em>memory</em></td>
<td>INTEGER</td>
<td> </td>
</tr>
<tr>
<td><em>state</em></td>
<td>STRING</td>
<td>Can only be set to "STARTED" or "STOPPED". Value changes after starting/stopping app.</td>
</tr>
<tr>
<td><em>services</em></td>
<td>STRING</td>
<td>More than one service can be added. They must self-contained strings delimited by commas.</td>
</tr>
<tr>
<td><em>env</em></td>
<td>STRING</td>
<td>More than one environment variable can be added. They must self-contained strings delimited by commas.</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="creation">Creating New Resources</h2>
<p>There is a JSON resource required to create each app and service. The following are templates of each with notes.</p>
<table>
<tbody>
<tr>
<td><a href="#create_user">APP</a></td>
<td>
<pre>{
    "name":"",
    "staging":{
        "framework":"",
        "runtime":""
    },
    "uris":[],
    "instances":,
    "resources":{
        "memory":
    },
    "infra":{
        "provider":""
    }
}</pre>
</td>
</tr>
<tr>
<td><a href="#create_service">SERVICE</a></td>
<td>
<pre>{
    "type":"",
    "tier":"",
    "vendor":"",
    "version":"",
    "infra":{
        "provider":""
    },
    "name":""
}</pre>
</td>
</tr>
</tbody>
</table>
<p> </p>
<h3 id="create_app">App Creation Resource Notes</h3>
<table>
<tbody>
<tr>
<td>Key</td>
<td>Value Type</td>
<td>Notes</td>
</tr>
<tr>
<td><em>name</em></td>
<td>STRING</td>
<td> </td>
</tr>
<tr>
<td><em>framework</em></td>
<td>STRING</td>
<td>
<table>
<tbody>
<tr>
<td colspan="3">Accepted values:</td>
</tr>
<tr>
<td>sinatra</td>
<td>java_web</td>
<td>lift</td>
</tr>
<tr>
<td>grails</td>
<td>wsgi</td>
<td>node</td>
</tr>
<tr>
<td>django</td>
<td>otp_rebar</td>
<td>play</td>
</tr>
<tr>
<td>php</td>
<td>spring</td>
<td>rails3</td>
</tr>
<tr>
<td>rack</td>
<td>standalone</td>
<td> </td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><em>runtime</em></td>
<td>STRING</td>
<td>
<table>
<tbody>
<tr>
<td colspan="4">Accepted values:</td>
</tr>
<tr>
<td>ruby18</td>
<td>ruby192</td>
<td>ruby193</td>
<td> </td>
</tr>
<tr>
<td>java</td>
<td>python2</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td>node04</td>
<td>node06</td>
<td>node08</td>
<td>node10</td>
</tr>
<tr>
<td>php</td>
<td>php54</td>
<td>php55</td>
<td>php56</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><em>uris</em></td>
<td>STRING</td>
<td>More than one URL can be added. They must self-contained strings delimited by commas.</td>
</tr>
<tr>
<td><em>instances</em></td>
<td>INTEGER</td>
<td> </td>
</tr>
<tr>
<td><em>memory</em></td>
<td>INTEGER</td>
<td> </td>
</tr>
<tr>
<td><em>infra</em></td>
<td>STRING</td>
<td>
<table>
<tbody>
<tr>
<td colspan="2">Accepted values:</td>
</tr>
<tr>
<td>aws</td>
<td>clc-uc01</td>
</tr>
<tr>
<td>eu-aws</td>
<td>ap-aws</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<p> </p>
<h3 id="create_service">Service Creation Resource Notes</h3>
<table>
<tbody>
<tr>
<td>Key Name</td>
<td>Type of Value</td>
<td>Note</td>
</tr>
<tr>
<td><em>type</em></td>
<td>STRING</td>
<td>
<table>
<tbody>
<tr>
<td>Accepted values:</td>
<td>free</td>
</tr>
</tbody>
</table>
</td>
</tr>
<tr>
<td><em>tier</em></td>
<td>STRING</td>
<td> </td>
</tr>
<tr>
<td><em>vendor</em></td>
<td>STRING</td>
<td> </td>
</tr>
<tr>
<td><em>version</em></td>
<td>STRING</td>
<td> </td>
</tr>
<tr>
<td><em>provider</em></td>
<td>STRING</td>
<td> </td>
</tr>
<tr>
<td><em>name</em></td>
<td>STRING</td>
<td>
<table>
<tbody>
<tr>
<td colspan="2">Accepted values:</td>
</tr>
<tr>
<td>aws</td>
<td>clc-uc01</td>
</tr>
<tr>
<td>eu-aws</td>
<td>ap-aws</td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<p> </p>
<p>Some of the key values vary depending on the type of service you want to start up. The values for each are below.</p>
<table>
<tbody>
<tr>
<td> </td>
<td><em>type</em></td>
<td><em>vendor</em></td>
<td><em>version</em></td>
</tr>
<tr>
<td>MySQL</td>
<td>database</td>
<td>mysql</td>
<td>5.1</td>
</tr>
<tr>
<td>PostgreSQL</td>
<td>database</td>
<td>postgresql</td>
<td>9.1</td>
</tr>
<tr>
<td>MongoDB</td>
<td>document</td>
<td>mongodb</td>
<td>1.8</td>
</tr>
<tr>
<td>MongoDB 2</td>
<td>document</td>
<td>mongodb2</td>
<td>2.4.8</td>
</tr>
<tr>
<td>RabbitMQ</td>
<td>generic</td>
<td>rabbitmq</td>
<td>2.</td>
</tr>
<tr>
<td>Redis</td>
<td>generic</td>
<td>rabbitmq</td>
<td>2.2</td>
</tr>
</tbody>
</table>
<hr />
<h2 id="examples">CURL Examples</h2>
<p>GET Call for an App</p>
<pre>curl -X GET \
-H Authorization:$TOKEN \
https://api.appfog.com/apps/hello_world

{"name":"hello_world","staging":{"model":"sinatra","stack":"ruby192"},"uris":["hello-world.uc01.clc.af.cm","www.example-domain.tld"],"instances":2,"runningInstances":2,"resources":{"memory":128,"disk":1024,"fds":256},"state":"STARTED","services":["my_database"],"version":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-1","env":["MY_ENV=example_string"],"meta":{"debug":null,"console":false,"version":20,"created":XXXXXXX379},"infra":{"provider":"clc-uc01","name":"clc-uc01"}}
</pre>
<p>POST Call to Create an App</p>
<pre>curl -X POST \
-H Authorization:$TOKEN \
-H Content-Type:application/json \
https://api.appfog.com/apps \
-d '{"name":"hello_world","staging":{"framework":"sinatra","runtime":null},"uris":["hello-world.uc01.clc.af.cm","www.example-domain.tld"],"instances":2,"resources":{"memory":128},"infra":{"provider":"clc-uc01"}}'

{"result":"success","redirect":"http://bhvu5gugln.uc01.clc.af.cm/apps/hello_world","infra":{"provider":"clc-uc01","name":"clc-uc01"}}
</pre>
<p>PUT Call to Increase App Memory</p>
<pre>curl -X PUT \
-H Authorization:$TOKEN \
https://api.appfog.com/apps/hello_world \
-d '{"name":"hello_world","staging":{"model":"sinatra","stack":"ruby192"},"uris":["hello_world.uc01.clc.af.cm"],"instances":2,"runningInstances":0,"resources":{"memory":256,"disk":1024,"fds":256},"state":"STARTED","services":["my_database"],"version":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-1","env":["MY_ENV=example_string"],"meta":{"debug":null,"console":false,"version":2,"created":XXXXXXXXXX},"infra":{"provider":"clc-uc01","name":"clc-uc01"}}'

{"name":"hello_world","staging":{"model":"sinatra","stack":"ruby192"},"uris":["hello_world.uc01.clc.af.cm"],"instances":2,"runningInstances":0,"resources":{"memory":256,"disk":1024,"fds":256},"state":"STARTED","services":["my_database"],"version":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-1","env":["MY_ENV=example_string"],"meta":{"debug":null,"console":false,"version":3,"created":XXXXXXXXXX},"infra":{"provider":"clc-uc01","name":"clc-uc01"}}</pre>
<p>DELETE Call to Delete an App</p>
<pre>curl -X DELETE \
-H Authorization:$TOKEN \
https://api.appfog.com/apps/hello_world</pre>
