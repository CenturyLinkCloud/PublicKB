{{{
  "title": "Application Specific: Deploying Grails 2.4",
  "date": "1-23-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}


<p>It involves some minor hacking around in order to use Grails 2.4 on AppFog, because the platform has Tomcat 6 running as default for our users. However, we recently added the ability to use Tomcat 7 and Servlet 3 together!</p>
<p>You'll need to perform the following steps to get it up and running.</p>
<ol>
<li>
<p>Use <code>git clone https://github.com/appfog/af-java-tomcat7.git</code> to copy the code off of GitHub.</p>
<p>Alternatively, you can create the app at the <a href="https://console.appfog.com/apps/new">web console</a> using Tomcat7+Servlet3 jumpstart and use <code>af pull</code> to save it locally.</p>
</li>
<li><a href="http://grails.org/doc/latest/guide/gettingStarted.html#requirements">Build your Grails 2.4 app separately.</a></li>
<li>When you have your WAR file created, you'll need to remove all files underneath the Tomcat jumpstart's <code>webapps/ROOT</code> directory, copy the WAR file to that same <code>ROOT</code> directory, then deploy that app there.
<p>Example below.</p>
<pre>..$ rm -rf tomcatjumpstart/webapps/ROOT/*
..$ mv grailsapp/target/helloworld.war tomcatjumpstart/webapps/ROOT
..$ cd tomcatjumpstart/webapps/ROOT
../tomcatjumpstart/webapps/ROOT$ jar -xvf &lt;appname&gt;.war
../tomcatjumpstart/webapps/ROOT$ cd ../../
../tomcatjumpstart$ af push grailsapp --runtime java</pre>
</li>
</ol>
<p>Don't forget to choose Java as the runtime, the start command should be <code>bin/startup.sh</code>, and make sure you give it a URL (or you'll have nothing to go to!). When it's done it should get something like the following.</p>
<pre>../tomcatjumpstart$ af push grailsapp --runtime java
Would you like to deploy from the current directory? [Yn]:
Detected a Standalone Application, is this correct? [Yn]:
1: clr20
2: clr40
3: java
4: node04
5: node06
6: node08
7: node10
8: php
9: php54
10: php55
11: php56
12: python2
13: ruby18
14: ruby192
15: ruby193
Select Runtime [java]:
Selected java
Start Command: bin/startup.sh
1: CLC - Santa Clara
2: AWS US East - Virginia
3: AWS EU West - Ireland
4: AWS Asia SE - Singapore
Select Infrastructure: 2
Application Deployed URL [None]: grailsapp.aws.af.cm
Memory reservation (128M, 256M, 512M, 1G, 2G) [512M]:
How many instances? [1]:
Bind existing services to 'grailsapp'? [yN]:
Create services to bind to 'grailsapp'? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Uploading Application:
  Checking for available resources: OK
  Processing resources: OK
  Packing application: OK
  Uploading (16K): OK
Push Status: OK
Staging Application 'grailsapp': OK
Starting Application 'grailsapp': OK</pre>
