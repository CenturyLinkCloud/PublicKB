{{{
  "title": "Languages And Frameworks: Grails Building and Deployment",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="http://grails.org/">Grails</a> is a framework for rapidly developing web apps that can be deployed to any Java servlet container, such as Tomcat. Based on the dynamic language <a href="http://groovy.codehaus.org/">Groovy</a> and the <a href="http://www.springframework.org/">Spring</a> framework, it brings the paradigm of Convention over Configuration to the Java platform with the expressiveness of a Java-like dynamic language.</p>
<p><strong>Note</strong>: Users that want to deploy their own <strong>Grails 2.4</strong> app should take a look at <a href="grails-building-and-deployment.md">this article</a>.</p>
<p>This guide assumes that you already have Java and <a href="http://grails.org/Installation">Grails</a> installed and know how to build a simple Grails app. That’s all you need to start working with AppFog.</p>
<ul>
<li><a href="#grails-services">Services</a></li>
<li><a href="#deployment">Deployment</a></li>
<li><a href="#further-reading">Further Reading</a></li>
</ul>
<h3 id="grails-services">Services</h3>
<p>AppFog provides a rich set of services, all of which can be used by Grails apps: MySQL, PostgreSQL, MongoDB, Redis, and RabbitMQ. Each of these services has a corresponding Grails plug-in. When these plug-ins are installed, you don’t have to configure any connection settings for the associated AppFog service - it’s done all automatically when your app is deployed. And when you first deploy your app with af-push, Grails will ask you whether you want to create and bind the relevant services based on which plug-ins you have installed.</p>
<h4>SQL services</h4>
<p>Currently, you can either use MySQL or Postgres on AppFog if you want a relational database for your app. All you need to access them is the <a href="http://grails.org/plugin/hibernate">Hibernate plug-in</a>, which is included by default in all new Grails apps. You also need to make sure that the relevant driver is available to your app, for example by declaring it in <code>BuildConfig.groovy</code>:</p>
<pre>grails.project.dependency.resolution = {
    ...
    dependencies {
        runtime "mysql:mysql-connector-java:5.1.18"
        ...
    }
}
</pre>
<p>and that the JDBC driver class is set in <code>DataSource.groovy</code>:</p>
<pre>environments {
    production {
        dataSource {
            driverClassName = "com.mysql.jdbc.Driver"
            ...
        }
    }
}
</pre>
<p>In this case, we’re going to deploy the app for the standard production environment, but you could easily set up a ‘cloud’ or similar environment. Also, you can easily configure the JDBC URL, username and password for the production environment to point to a local MySQL database because those settings are overridden when the app is deployed to AppFog.</p>
<p>To use the key-value store <a href="http://redis.io/">Redis</a>, you need to either install the <a href="http://grails.org/plugin/redis">Redis plug-in</a> or <a href="http://grails.org/plugin/redis-gorm">Redis for GORM</a>. As with the SQL stores, when you deploy your app to AppFog it will automatically use whichever Redis service has been bound to it.</p>
<p>The former plug-in provides low-level access to Redis via a <code>redis</code> bean, while the latter allows you to map GORM domain classes to Redis. See the <a href="http://grails.github.com/inconsequential/redis/manual/index.html">plug-in documentation</a> for more information.</p>
<h4>MongoDB</h4>
<p>To use the document store <a href="http://www.mongodb.org/">MongoDB</a>, just install the <a href="http://grails.org/plugin/mongodb">MongoDB</a> plug-in.</p>
<p>The MongoDB plug-in for Grails allows you to map GORM entities to MongoDB Collections. It also provides a low-level API for accessing the MongoDB driver for Java directly. Refer to the <a href="http://grails.github.com/inconsequential/mongo/manual/index.html">plug-in documentation</a> for more information.</p>
<h3 id="deployment">Deployment</h3>
<p>Deploying your Grails app to AppFog is simple. Just generate your <code>.war</code> file, then push:</p>
<pre>$ grails prod war
| Done creating WAR target/af-java-grails-example-0.1.war
$ cd target
$ af push
Would you like to deploy from the current directory? [Yn]:
Application Name: grails-example
Detected a Java SpringSource Grails Application, is this correct? [Yn]:
1: AWS US East - Virginia
2: AWS EU West - Ireland
3: AWS Asia SE - Singapore
Select Infrastructure: 1
Application Deployed URL [grails-example.aws.af.cm]:
Memory reservation (128M, 256M, 512M, 1G, 2G) [512M]:
How many instances? [1]:
Bind existing services to 'grails-example'? [yN]:
Create services to bind to 'grails-example'? [yN]: y
1: mongodb
2: mysql
3: postgresql
What kind of service?: 2
Specify the name of the service [mysql-6dc25]:
Create another? [yN]:
Would you like to save this configuration? [yN]:
Creating Application: OK
Creating Service [mysql-6dc25]: OK
Binding Service [mysql-6dc25]: OK
Uploading Application:
  Checking for available resources: OK
  Processing resources: OK
  Packing application: OK
  Uploading (11K): OK
Push Status: OK
Staging Application 'grails-example': OK
Starting Application 'grails-example': OK
</pre>
<h3 id="further-reading">Further Reading</h3>
<p>For more information, check out <a href="http://docs.cloudfoundry.org/buildpacks/java/gsg-grails.html">Cloud Foundry's documentation on Grails</a>.</p>
