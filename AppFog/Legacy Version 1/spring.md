{{{
  "title": "Languages And Frameworks: Spring",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#services-spring">Using AppFog Services In Spring Apps</a></li>
<li><a href="#spring-determining-auto-configure">Determining Whether Your App Can Be Auto-Configured</a></li>
<li><a href="#spring-relational">Relational Database (MySQL and Postgres)</a></li>
<li><a href="#spring-mongo">MongoDB</a></li>
<li><a href="#spring-limits-auto-reconfig">Limitations of Auto-Reconfiguration</a></li>
<li><a href="#spring-opt-out-auto-reconfig">Opting Out of Auto-Reconfiguration</a></li>
<li><a href="#spring-explicit-configure">Explicitly Configuring Your App to Use AppFog Services</a></li>
<li><a href="#spring-conditionalize">Using Spring Profiles to Conditionalize AppFog Configuration</a></li>
<li><a href="#spring-email">Sending Email From Spring Apps Deployed to AppFog</a></li>
<li><a href="#spring-accessing-properties">Accessing AppFog Properties</a></li>
</ul>
<p>In general, there's nothing special you need to do to deploy Spring apps to AppFog. If your Spring app runs on a tc Server or Apache Tomcat, it will also run on AppFog without any changes.</p>
<p>It's usually best to package your Spring app in a <code>*.war</code> file so that <code>af push</code> will automatically detect that it's a Spring app, but you can also deploy it as an exploded directory if you want.</p>
<p>There are, however, a few things about the AppFog environment that might affect how your deployed app runs:</p>
<ul>
<li>
<p>Local disk storage is ephemeral. In other words, local disk storage is not guaranteed to persist for the entire life of the app. This is because AppFog creates a new virtual disk every time you restart your app. Additionally, AppFog restarts all apps after it updates its own environment. This means that, although your app is able to write local files while it is running, the files will disappear after the app restarts. If the files your app is writing are temporary, then this should not be a problem. However, if your app needs the data in the files to persist, then you must use one of the data services to manage the data. In this scenario, MongoDB is a good choice because it is a document-oriented database.</p>
</li>
<li>
<p>AppFog uses Apache Tomcat as its app server, and it runs your app within the root context. This is different from normal Apache Tomcat in which the context path is determined by the name of the <code>*.war</code> file in which the app is packaged.</p>
</li>
<li>
<p>HTTP sessions are not replicated, but HTTP traffic is sticky. This means that if a your app crashes or restarts, the HTTP sessions are lost.</p>
</li>
<li>
<p>External users can access your app only via the URL provided by the <code>af push</code> command (or equivalent STS command). Although your app might be able to internally listen to other ports (such as the JMX port for the MBean server), external users of your app will not be able to listen on these ports.</p>
</li>
</ul>
<h3 id="services-spring">Using AppFog Services In Spring Apps</h3>
<p>If your Spring app requires services (such as a database), you might be able to deploy your app to AppFog without changing a single line of code. In this case, AppFog automatically re-configures the relevant bean definitions to bind them to cloud services. See <a href="#spring-determining-auto-configure">Determining Whether Your App Can Be Auto-Configured</a> for details.</p>
<p>If your Spring app cannot take advantage of AppFog’s auto-reconfiguration feature, or you want more control over the configuration, the additional steps are very simple and easy. See <a href="#spring-explicit-configure">Explicitly Configuring Your App to Use AppFog Services</a>.</p>
<h3 id="spring-determining-auto-configure">Determining Whether Your App Can Be Auto-Configured</h3>
<p>You will likely be able to deploy many of your existing Spring apps to AppFog without changing a single line of code, even in the case that your app needs a service such as a relational database. This is because AppFog automatically detects the type of service your app needs, and if its configuration falls within <a href="#spring-limits-autoreconfig">a small set of limitations</a>, AppFog will automatically reconfigure it so that it binds to service instances that AppFog creates and maintains itself.</p>
<p>With auto-reconfiguration, AppFog creates the database or connection factory itself, using its own values for properties such as host, port, username and so on. For example, if you have a single <code>javax.sql.DataSource</code> bean in your app context that AppFog reconfigures and binds to its own database service, AppFog doesn’t use the username and password and driver URL you originally specified. Rather, it uses its own internal values. This is transparent to the app, which really only cares about having a relational database to which it can write data but doesn’t really care what the specific properties are that created the database.</p>
<p>The following sections describe, for each supported service, the type of bean that AppFog detects if auto-configuration occurs.</p>
<h3 id="spring-relational">Relational Database (MySQL and Postgres)</h3>
<p>Auto-reconfiguration occurs if AppFog detects a <code>javax.sql.DataSource</code> bean. The following snippet of a Spring app context file shows an example of defining this type of bean which AppFog will in turn detect and potentially auto-reconfigure:</p>
<pre>&lt;bean class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close" id="dataSource"&gt;
    &lt;property name="driverClassName" value="org.h2.Driver" /&gt;
    &lt;property name="url" value="jdbc:h2:mem:" /&gt;
    &lt;property name="username" value="sa" /&gt;
    &lt;property name="password" value="" /&gt;
&lt;/bean&gt;
</pre>
<p>The relational database that AppFog actually uses depends on the service instance you explicitly bind to your app when you deploy it: MySQL or Postgres. AppFog creates either a commons DBCP or Tomcat datasource.</p>
<p>AppFog will internally generate values for the following properties: driverClassName, url, username, password, validationQuery.</p>
<h3 id="spring-mongo">MongoDB</h3>
<p>You must be using Spring Data MongoDB 1.0 M4 or later for auto-reconfiguration to work.</p>
<p>Auto-reconfiguration occurs if AppFog detects a <code>org.springframework.data.document.mongodb.MongoDbFactory</code> bean. The following snippet of a Spring app context file shows an example of defining this type of bean which AppFog will in turn detect and potentially auto-reconfigure:</p>
<pre>&lt;mongo:db-factory
    id="mongoDbFactory"
    dbname="pwdtest"
    host="127.0.0.1"
    port="1234"
    username="test_user"
    password="test_pass"  /&gt;
</pre>
<p>AppFog will create a <code>SimpleMOngoDbFactory</code> with its own values for the following properties: <code>host</code>, <code>port</code>, <code>username</code>, <code>password</code>, <code>dbname</code>.</p>
<h3>Redis</h3>
<p>You must be using <a href="http://www.springsource.org/spring-data/redis">Spring Data Redis</a> 1.0 M4 or later for auto-reconfiguration to work.</p>
<p>Auto-reconfiguration occurs if AppFog detects a <code>org.springframework.data.redis.connection.RedisConnectionFactory</code> bean. The following snippet of a Spring app context file shows an example of defining this type of bean which AppFog will in turn detect and potentially auto-reconfigure:</p>
<pre>&lt;bean id="redis"
      class="org.springframework.data.redis.connection.jedis.JedisConnectionFactory"
      p:hostName="localhost" p:port="6379"  /&gt;
</pre>
<p>AppFog will create a <code>JedisConnectionFactory</code> with its own values for the following properties: <code>host</code>, <code>port</code>, <code>password</code>. This means that you must package the Jedis JAR in your app. AppFog does not currently support the JRedis and RJC implementations.</p>
<h3>RabbitMQ</h3>
<p>You must be using <a href="http://www.springsource.org/spring-amqp">Spring AMQP</a> 1.0 or later for auto-reconfiguration to work. Spring AMQP provides publishing, multi-threaded consumer generation, and message converters. It also facilitates management of AMQP resources while promoting dependency injection and declarative configuration.</p>
<p>Auto-reconfiguration occurs if AppFog detects a <code>org.springframework.amqp.rabbit.connection.ConnectionFactory</code> bean. The following snippet of a Spring app context file shows an example of defining this type of bean which AppFog will in turn detect and potentially auto-reconfigure:</p>
<pre>&lt;rabbit:connection-factory
    id="rabbitConnectionFactory"
    host="localhost"
    password="testpwd"
    port="1238"
    username="testuser"
    virtual-host="virthost" /&gt;
</pre>
<p>AppFog will create a <code>org.springframework.amqp.rabbit.connection.CachingConnectionFactory</code> with its own values for the following properties: <code>host</code>, <code>virtual-host</code>, <code>port</code>, <code>username,</code> <code>password</code>.</p>
<h3 id="spring-limits-auto-reconfig">Limitations of Auto-Reconfiguration</h3>
<p>AppFog auto-reconfigures apps only if the following items are true:</p>
<ul>
<li>
<p>You bind only one service instance of a given service type to your app. In this context, MySQL and Postgres are considered the same service type (relational database), so if you have bound both a MySQL and a Postgres service to your app, auto-reconfiguration will not occur.</p>
</li>
<li>
<p>You include only <em>one</em> bean of a matching type in your Spring app context file. For example, you can have only one bean of type <code>javax.sql.DataSource</code>.</p>
</li>
</ul>
<p>Also note that if auto-reconfiguration occurs, but you have customized the configuration of the service (such as the pool size or connection properties), AppFog ignores the customizations.</p>
<h3 id="spring-opt-out-auto-reconfig">Opting Out of Auto-Reconfiguration</h3>
<p>Sometimes you may not want AppFog to auto-reconfigure your Spring app in the ways described in this section. There are two ways to opt out:</p>
<ul>
<li>
<p>When you deploy your app using <code>af</code> or STS, specify that the framework is <code>JavaWeb</code> instead of <code>Spring</code>. Note that in this case your app will not be able to take advantage of the Spring Profiles feature.</p>
</li>
<li>
<p>Use the <code>&lt;cloud:&gt;</code> namespace elements in your Spring app context file to explicitly create a bean that represents a service. This makes auto-reconfiguration unnecessary. See <a href="#spring-explicit-configure">Explicitly Configuring Your App to Use AppFog Services</a></p>
</li>
</ul>
<h3 id="spring-explicit-configure">Explicitly Configuring Your App to Use AppFog Services</h3>
<p>The easiest way to use AppFog services in your Spring apps is to declare the <code>&lt;cloud:&gt;</code> namespace, point it to the AppFog Schema, then use the service-specific elements defined in the <code>&lt;cloud&gt;</code> namespace. For example, with just a single line of XML in your app context file you can create a JDBC data source that you can use in your specific bean definitions. You can configure multiple data sources or connection factories if your app requires it. You can also further configure these cloud services if you want, although it is completely optional because AppFog uses commonplace configuration values to create typical service instances that are adequate for most uses. In sum, using the <code>&lt;cloud:&gt;</code> namespace provides you with as much control as you want over the number and type of AppFog services that your app uses.</p>
<p>The basic steps to update your Spring app to use any of the AppFog services are as follows:</p>
<ul>
<li>
<p>Update your app build process to include a dependency on the <code>org.cloudfoundry.cloudfoundry-runtime</code> artifact. For example, if you use Maven to build your app, the following <code>pom.xml</code> snippet shows how to add this dependency:</p>
<pre>&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.cloudfoundry&lt;/groupId&gt;
        &lt;artifactId&gt;cloudfoundry-runtime&lt;/artifactId&gt;
        &lt;version&gt;0.8.1&lt;/version&gt;
    &lt;/dependency&gt;
    &lt;!-- additional dependency declarations --&gt;
&lt;/dependencies&gt;
</pre>
</li>
<li>
<p>Update your app build process to include the Spring Framework Milestone repository. The following <code>pom.xml</code> snippet shows how to do this in Maven:</p>
<pre>&lt;repositories&gt;
    &lt;repository&gt;
          &lt;id&gt;org.springframework.maven.milestone&lt;/id&gt;
           &lt;name&gt;Spring Maven Milestone Repository&lt;/name&gt;
           &lt;url&gt;http://maven.springframework.org/milestone&lt;/url&gt;
           &lt;snapshots&gt;
                   &lt;enabled&gt;false&lt;/enabled&gt;
           &lt;/snapshots&gt;
    &lt;/repository&gt;
    &lt;!-- additional repository declarations --&gt;
&lt;/repositories&gt;
</pre>
</li>
<li>
<p>In your Spring app, update all app context files that will include the AppFog service declarations, such as a data source, by adding the <code>&lt;cloud:&gt;</code> namespace declaration and the location of the AppFog services Schema, as shown in the following snippet:</p>
<pre>&lt;beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xmlns:cloud="http://schema.cloudfoundry.org/spring"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.1.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-3.1.xsd
        http://schema.cloudfoundry.org/spring
        http://schema.cloudfoundry.org/spring/cloudfoundry-spring.xsd
        &gt;
    &lt;!-- bean declarations --&gt;
&lt;/beans&gt;
</pre>
</li>
<li>
<p>You can now specify the AppFog services in the Spring app context file by using the <code>&lt;cloud:&gt;</code> namespace along with the name of specific elements, such as <code>data-source</code>. AppFog provides elements for each of the supported services: database (MySQL and Postgres), Redis, MongoDB, and RabbitMQ.</p>
<p>The following example shows a simple data source configuration that will be injected into a JdbcTemplate using the <code>&lt;cloud:data-source&gt;</code> element.</p>
<pre>&lt;beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xmlns:cloud="http://schema.cloudfoundry.org/spring"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans-3.1.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context-3.1.xsd
        http://schema.cloudfoundry.org/spring
        http://schema.cloudfoundry.org/spring/cloudfoundry-spring.xsd
        &gt;
    &lt;cloud:data-source id="dataSource" /&gt;
    &lt;bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate"&gt;
      &lt;property name="dataSource" ref="dataSource" /&gt;
    &lt;/bean&gt;
        &lt;!-- additional beans in your app --&gt;
&lt;/beans&gt;
</pre>
</li>
</ul>
<p>When you later deploy the app using <code>af</code> or STS, you bind a specific data service (such as MySQL or Postgres) to it and AppFog creates an instance of the service. Note that in the example above, you did not specify typical data source properties such as <code>driverClassName</code> or <code>url</code> or <code>username</code> - this is because AppFog automatically takes care of those properties for you.</p>
<p>For complete information about all the <code>&lt;cloud:&gt;</code> elements you can use in your Spring app context file to access AppFog services, see the following sections:</p>
<ul>
<li><a href="#clouddata-source"><code>&lt;cloud:data-source&gt;</code>: Configure a JDBC Data Source for Either MySQL or Postgres Databases</a></li>
<li><a href="#cloudmongo-db-factory"><code>&lt;cloud:mongo-db-factory&gt;</code>: Configure a MongoDB Connection Factory</a></li>
<li><a href="#cloudservice-scan"><code>&lt;cloud:service-scan&gt;</code> Injecting Services Into @Autowired Beans</a></li>
<li><a href="#cloudproperties"><code>&lt;cloud:properties&gt;</code> Get AppFog Service Information</a></li>
<li><a href="#cloudredis-connection-factory"><code>&lt;cloud:redis-connection-factory&gt;</code>: Configure a Redis Connection Factory</a></li>
<li><a href="#cloudrabbit-connection-factory"><code>&lt;cloud:rabbit-connection-factory&gt;</code>: Configure a RabbitMQ Connection Factory</a></li>
</ul>
<p>After you have finished specifying all the AppFog services you are going to use in your app, you use the standard AppFog client commands (<code>af</code>, SpringSource Tool Suite, or the Eclipse plugin) to create instances of these services, bind them to your apps, then deploy your apps to AppFog. See <a href="#deploy">Deploying Apps</a> for details on how to use these tools.</p>
<h3 id="clouddata-source"><code>&lt;cloud:data-source&gt;</code></h3>
<p>The <code>&lt;cloud:data-source&gt;</code> element provides an easy way for you to configure a JDBC data source for your Spring app. Later, when you actually deploy the app, you bind a particular database service instance to it, such as MySQL or Postgres.</p>
<p>The following example shows a simple way to configure a JDBC data source that will be injected into a org.springframework.jdbc.core.JdbcTemplate bean:</p>
<pre>&lt;cloud:data-source id="dataSource" /&gt;

    &lt;bean id="jdbcTemplate" class="org.springframework.jdbc.core.JdbcTemplate"&gt;
      &lt;property name="dataSource" ref="dataSource" /&gt;
    &lt;/bean&gt;
</pre>
<p>In the preceding example, note that no specific information about the datasource is supplied, such as the JDBC driver classname, the specific URL to access the database, and the database users. Instead, AppFog will take care of all of that at runtime, using appropriate information from the specific type of database service instance you bind to your app.</p>
<h3>Attributes</h3>
<p>The following table lists the attributes of the <code>&lt;cloud:data-source&gt;</code> element.</p>
<p>AttributeDescriptionType</p>
<table class="table table-bordered table-striped attributes">
<thead></thead>
<tbody>
<tr>
<td>id</td>
<td>The ID of this data source. The JdbcTemplate bean uses this ID when it references the data source.<br /> Default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
<tr>
<td>service-name</td>
<td>The name of the data source service.<br /> You specify this attribute only if you are binding multiple database services to your app and you want to specify which particular service instance binds to a particular Spring bean. The default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
</tbody>
</table>
<h4>Advanced Data Source Configuration</h4>
<p>The section above showed how to configure a very simple JDBC data source; AppFog uses the most common configuration options when it actually creates the data source at runtime. You can, however, specify some of these configuration options using the following two child elements of <code>&lt;cloud:data-source&gt;</code>: <code>&lt;cloud:connection&gt;</code> and <code>&lt;cloud:pool&gt;</code>.</p>
<p>The <code>&lt;cloud:connection&gt;</code> child element takes a single String attribute (properties) that you use to specify connection properties you want to send to the JDBC driver when establishing new database connections. The format of the string must be semi-colon separated name/value pairs (<code>[propertyName=property;]</code>).</p>
<p>The <code>&lt;cloud:pool&gt;</code> child element takes the following two attributes:</p>
<p>AttributeDescriptionTypeDefault</p>
<table class="table table-bordered table-striped attributes">
<thead></thead>
<tbody>
<tr>
<td>pool-size</td>
<td>Specifies the size of the connection pool. Set the value to either the maximum number of connections in the pool, or a range of the minimum and maximum number of connections separated by a dash.</td>
<td>int</td>
<td>Default minimum is 0. Default maximum is 8. These are the same defaults as the Apache Commons Pool.</td>
</tr>
<tr>
<td>max-wait-time</td>
<td>In the event that there are no available connections, this attribute specifies the maximum number of milliseconds that the connection pool waits for a connection to be returned before throwing an exception. Specify `-1` to indicate that the connection pool should wait forever.</td>
<td>int</td>
<td>Default value is `-1` (forever).</td>
</tr>
</tbody>
</table>
<p>The following example shows how to use these advanced data source configuration options:</p>
<pre>&lt;cloud:data-source id="mydatasource"&gt;
    &lt;cloud:connection properties="charset=utf-8" /&gt;
    &lt;cloud:pool pool-size="5-10" max-wait-time="2000" /&gt;
&lt;/cloud:data-source&gt;
</pre>
<p>In the preceding example, the JDBC driver is passed the property that specifies that it should use the UTF-8 character set. The minimum and maximum number of connections in the pool at any given time is 5 and 10, respectively. The maximum amount of time that the connection pool waits for a returned connection if there are none available is 2000 milliseconds (2 seconds), after which the JDBC connection pool throws an exception.</p>
<h3 id="cloudmongo-db-factory"><code>&lt;cloud:mongo-db-factory&gt;</code></h3>
<p>The <code>&lt;cloud:mongo-db-factory&gt;</code> provides a simple way for you to configure a MongoDB connection factory for your Spring app.</p>
<p>The following example shows a MongoDbFactory configuration that will be injected into a <code>org.springframework.data.mongodb.core.MongoTemplate</code> object:</p>
<pre>&lt;cloud:mongo-db-factory id="mongoDbFactory" /&gt;

&lt;bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate"&gt;
    &lt;constructor-arg ref="mongoDbFactory"/&gt;
&lt;/bean&gt;
</pre>
<h4>Attributes</h4>
<p>The following table lists the attributes of the <code>&lt;cloud:mongo-db-factory&gt;</code> element.</p>
<p>AttributeDescriptionType</p>
<table class="table table-bordered table-striped attributes">
<thead></thead>
<tbody>
<tr>
<td>id</td>
<td>The ID of this MongoDB connection factory. The MongoTemplate bean uses this ID when it references the connection factory.<br /> Default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
<tr>
<td>service-name</td>
<td>The name of the MongoDB service. You specify this attribute only if you are binding multiple MongoDB services to your app and you want to specify which particular service instance binds to a particular Spring bean. The default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
<tr>
<td>write-concern</td>
<td>Controls the behavior of writes to the data store. The values of this attribute correspond to the values of the `com.mongodb.WriteConcern` class. If you do not specify this attribute, then no `WriteConcern` is set for the database connections and all writes default to NORMAL.<br /><br /> The possible values for this attribute are as follows:<br /><br />
<ul>
<li>NONE: No exceptions are raised, even for network issues.</li>
<li>NORMAL: Exceptions are raised for network issues, but not server errors.</li>
<li>SAFE: MongoDB service waits on a server before performing a write operation. Exceptions are raised for both network and server errors.</li>
<li>FSYNC\_SAVE: MongoDB service waits for the server to flush the data to disk before performing a write operation. Exceptions are raised for both network and server errors.</li>
</ul>
</td>
<td>String</td>
</tr>
</tbody>
</table>
<h3>Advanced MongoDB Configuration</h3>
<p>The preceding section shows how to configure a simple MongoDB connection factory using default values for the options. This is adequate for many environments. However, you can further configure the connection factory by specifying the optional <code>&lt;cloud:mongo-options&gt;</code> child element of <code>&lt;cloud:mongo-db-factory&gt;</code>.</p>
<p>The <code>&lt;cloud:mongo-options&gt;</code> child element takes the following two attributes:</p>
<p>AttributeDescriptionTypeDefault</p>
<table class="table table-bordered table-striped attributes">
<thead></thead>
<tbody>
<tr>
<td>connections-per-host</td>
<td>Specifies the maximum number of connections allowed per host for the MongoDB instance. Those connections will be kept in a pool when idle. Once the pool is exhausted, any operation requiring a connection will block while waiting for an available connection.</td>
<td>int</td>
<td>10</td>
</tr>
<tr>
<td>max-wait-time</td>
<td>Specifies the maximum wait time (in milliseconds) that a thread waits for a connection to become available.</td>
<td>int</td>
<td>120,000 (2 minutes)</td>
</tr>
</tbody>
</table>
<p>The following example shows how to use the advanced MongoDB options:</p>
<pre>&lt;cloud:mongo-db-factory id="mongoDbFactory" write-concern="FSYNC_SAFE"&gt;
    &lt;cloud:mongo-options connections-per-host="12" max-wait-time="2000" /&gt;
&lt;/cloud:mongo-db-factory&gt;
</pre>
<p>In the preceding example, the maximum number of connections is set to 12 and the maximum amount of time that a thread waits for a connection is 1 second. The WriteConcern is also specified to be the safest possible (<code>FSYNC_SAFE</code>).</p>
<h3 id="cloudredis-connection-factory"><code>&lt;cloud:redis-connection-factory&gt;</code></h3>
<p>The <code>&lt;cloud:redis-connection-factory&gt;</code> provides a simple way for you to configure a Redis connection factory for your Spring app.</p>
<p>The following example shows a <code>RedisConnectionFactory</code> configuration that will be injected into a <code>org.springframework.data.redis.core.StringRedisTemplate object</code>:</p>
<pre>&lt;cloud:redis-connection-factory id="redisConnectionFactory" /&gt;

&lt;bean id="redisTemplate" class="org.springframework.data.redis.core.StringRedisTemplate"&gt;
    &lt;property name="connection-factory" ref="redisConnectionFactory"/&gt;
&lt;/bean&gt;
</pre>
<h4>Attributes</h4>
<p>The following table lists the attributes of the <code>&lt;cloud:redis-connection-factory&gt;</code> element.</p>
<table class="table table-bordered table-striped attributes">
<tbody>
<tr><th>Attribute</th><th>Description</th><th>Type</th></tr>
<tr>
<td>id</td>
<td>The ID of this Redis connection factory. The RedisTemplate bean uses this ID when it references the connection factory. <br />Default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
<tr>
<td>service-name</td>
<td>The name of the Redis service. <br />You specify this attribute only if you are binding multiple Redis services to your app and you want to specify which particular service instance binds to a particular Spring bean. The default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
</tbody>
</table>
<h4>Advanced Redis Configuration</h4>
<p>The preceding section shows how to configure a very simple Redis connection factory; AppFog uses the most common configuration options when it actually creates the factory at runtime. You can, however, change some of these configuration options using the <code>&lt;cloud:pool&gt;</code> child element of <code>&lt;cloud:redis-connection-factory&gt;</code>.</p>
<p>The <code>&lt;cloud:pool&gt;</code> child element takes the following two attributes:</p>
<table class="table table-bordered table-striped attributes">
<tbody>
<tr><th>Attribute</th><th>Description</th><th>Type</th><th>Default</th></tr>
<tr>
<td>pool-size</td>
<td>Specifies the size of the connection pool. Set the value to either the maximum number of connections in the pool, or a range of the minimum and maximum number of connections separated by a dash.</td>
<td>int</td>
<td>Default minimum is 0. Default maximum is 8. These are the same defaults as the Apache Commons Pool.</td>
</tr>
<tr>
<td>max-wait-time</td>
<td>In the event that there are no available connections, this attribute specifies the maximum number of milliseconds that the connection pool waits for a connection to be returned before throwing an exception. Specify `-1` to indicate that the connection pool should wait forever.</td>
<td>int</td>
<td>Default value is `-1` (forever).</td>
</tr>
</tbody>
</table>
<p>The following example shows how to use these advanced Redis configuration options:</p>
<pre>&lt;cloud:redis-connection-factory id="myRedisConnectionFactory"&gt;
    &lt;cloud:pool pool-size="5-10" max-wait-time="2000" /&gt;
&lt;/cloud:redis-connection-factory&gt;
</pre>
<p>In the preceding example, the minimum and maximum number of connections in the pool at any given time is 5 and 10, respectively. The maximum amount of time that the connection pool waits for a returned connection if there are none available is 2000 milliseconds (2 seconds), after which the Redis connection pool throws an exception.</p>
<h3 id="cloudrabbit-connection-factory"><code>&lt;cloud:rabbit-connection-factory&gt;</code></h3>
<p>The <code>&lt;cloud:rabbit-connection-factory&gt;</code> provides a simple way for you to configure a RabbitMQ connection factory for your Spring app.</p>
<p>The following complete example of a Spring app contenxt file shows a <code>RabbitConnectionFactory</code> configuration that will be injected into a <code>rabbitTemplate</code> object. The example also uses the <code>&lt;rabbit:&gt;</code> namespace to perform RabbitMQ-specific configurations, as explained after the example:</p>
<pre>&lt;beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:mvc="http://www.springframework.org/schema/mvc"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:rabbit="http://www.springframework.org/schema/rabbit"
       xmlns:cloud="http://schema.cloudfoundry.org/spring"
       xsi:schemaLocation="http://www.springframework.org/schema/mvc   http://www.springframework.org/schema/mvc/spring-mvc-3.0.xsd
           http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
           http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-3.0.xsd
           http://www.springframework.org/schema/rabbit http://www.springframework.org/schema/rabbit/spring-rabbit-1.0.xsd
           http://schema.cloudfoundry.org/spring http://schema.cloudfoundry.org/spring/cloudfoundry-spring.xsd"&gt;

    &lt;!-- Obtain a connection to the RabbitMQ via cloudfoundry-runtime: --/&gt;
    &lt;cloud:rabbit-connection-factory id="rabbitConnectionFactory" /&gt;

    &lt;!-- Set up the AmqpTemplate/RabbitTemplate: --/&gt;
    &lt;rabbit:template id="rabbitTemplate"
        connection-factory="rabbitConnectionFactory" /&gt;

    &lt;!-- Request that queues, exchanges and bindings be automatically declared on the broker: --/&gt;
    &lt;rabbit:admin connection-factory="rabbitConnectionFactory"/&gt;

    &lt;!-- Declare the "messages" queue: --/&gt;
    &lt;rabbit:queue name="messages" durable="true"/&gt;

    &lt;!-- additional beans in your app --/&gt;

&lt;/beans&gt;
</pre>
<p>In the preceding example, note the definition and location of the <code>&lt;rabbit:&gt;</code> namespace at the top of the XML file. This namespace is then used to configure RabbitTemplate and RabbitAdmin objects as the main entry points to Spring AMQP and to declare a queue called <code>messages</code> within the RabbitMQ broker.</p>
<p>See <a href="#rabbit-and-spring">RabbitMQ And Spring: Additional Programming Information</a> for additional information about using RabbitMQ in your Spring apps.</p>
<h4>Attributes</h4>
<p>The following table lists the attributes of the <code>&lt;cloud:rabbit-connection-factory&gt;</code> element.</p>
<table class="table table-bordered table-striped attributes">
<tbody>
<tr><th>Attribute</th><th>Description</th><th>Type</th></tr>
<tr>
<td>id</td>
<td>The ID of this RabbitMQ connection factory. The RabbitTempalte bean uses this ID when it references the connection factory. <br />Default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
<tr>
<td>service-name</td>
<td>The name of the RabbitMQ service. <br />You specify this attribute only if you are binding multiple RabbitMQ services to your app and you want to specify which particular service instance binds to a particular Spring bean. The default value is the name of the bound service instance.</td>
<td>String</td>
</tr>
</tbody>
</table>
<h4>Advanced RabbitMQ Configuration</h4>
<p>The preceding section shows how to configure a very simple RabbitMQ connection factory; AppFog uses the most common configuration options when it actually creates the factory at runtime. You can, however, change some of these configuration options using the <code>&lt;cloud:rabbit-options&gt;</code> child element of <code>&lt;cloud:rabbit-connection-factory&gt;</code>.</p>
<p>The <code>&lt;cloud:rabbit-options&gt;</code> child element defines one attribute called <code>channel-cache-size</code> which you can set to specify the size of the channel cache size. The default value is 1.</p>
<p>The following example shows how to use these advanced RabbitMQ configuration options:</p>
<pre>&lt;cloud:rabbit-connection-factory id="rabbitConnectionFactory" &gt;
    &lt;cloud:rabbit-options channel-cache-size="10" /&gt;
&lt;/cloud:rabbit-connection-factory&gt;
</pre>
<p>In the preceding example, the channel cache size of the RabbitMQ connection factory is set to 10.</p>
<h3 id="cloudservice-scan"><code>&lt;cloud:service-scan&gt;</code></h3>
<p>The <code>&lt;cloud:service-scan&gt;</code> element scans all services bound to the app and creates a Spring bean of an appropriate type for each one that has been annoted with the <code>@org.springframework.beans.factory.annotation.Autowired</code> annotation. The <code>&lt;cloud:service-scan&gt;</code> element acts as a cloud equivalent of <code>&lt;context:component-scan&gt;</code> in core Spring, which scans the CLASSPATH for beans with certain annotations and creates a bean for each.</p>
<p>The <code>&lt;cloud:service-scan&gt;</code> is especially useful during the initial phases of app development, because you can get immediate access to service beans without explicitly adding a <code>&lt;cloud:&gt;</code> element to your Spring app context file for each new service that you bind.</p>
<p>The <code>&lt;cloud:service-scan&gt;</code> element has no attributes or child elements; for example:</p>
<pre> &lt;cloud:service-scan /&gt;
</pre>
<p>In your Java code, you must annotate each dependency with <code>@Autowired</code> so that a bean of the corresponding service is automatically created. For example:</p>
<pre>package cf.examples;

import org.springframework.beans.factory.annotation.Autowired;

....

@Autowired DataSource dataSource;
@Autowired ConnectionFactory rabbitConnectionFactory;
@Autowired RedisConnectionFactory redisConnectionFactory;
@Autowired MongoDbFactory mongoDbFactory;

...
</pre>
<p>Use of only the <code>@Autowired</code> annotation is adequate if you have bound only one service of each service type to your app. If you bind more than one (for example, you bind two different MySQL service instances to the same app) then you must also use the <code>@Qualifier</code> annotation to match the Spring bean with the specific service instance.</p>
<p>For example, assume you bound two MySQL services (named <code>inventory-db</code> and <code>pricing-db</code>) to your app; use the <code>@Qualifier</code> annotation as shown in the following example to specify which service instance applies to which Spring bean:</p>
<pre>@Autowired @Qualifier("inventory-db") DataSource inventoryDataSource;
@Autowired @Qualifier("pricing-db") DataSource pricingDataSource;
</pre>
<h3 id="cloudproperties"><code>&lt;cloud:properties&gt;</code></h3>
<p>The <code>&lt;cloud:properties&gt;</code> element exposes basic information about the app and its bound services as properties. Your app can then consume these properties using the Spring property placeholder support.</p>
<p>The <code>&lt;cloud:properties&gt;</code> element has just a single attribute (<code>id</code>) which specifies the name of the Properties bean. Use this ID as a reference to <code>&lt;context:property-placeholder&gt;</code> which you can use to hold all the properties exposed by AppFog. You can then use these properties in your other bean defintions.</p>
<p>Note that if you are using Spring Framework 3.1 (or later), these properties are automatically available without having to include <code>&lt;cloud:properties&gt;</code> in your app context file.</p>
<p>The following example shows how to use this element in your Spring app context file:</p>
<pre>&lt;cloud:properties id="cloudProperties" /&gt;

&lt;context:property-placeholder properties-ref="cloudProperties" /&gt;

&lt;bean class="com.mchange.v2.c3p0.ComboPooledDataSource"&gt;
    &lt;property name="user"
              value="${cloud.services.mysql.connection.username}" /&gt;
...
&lt;/bean&gt;
</pre>
<p>In the preceding example, <code>cloud.services.mysql.connection.username</code> is one of the properties exposed by AppFog.</p>
<p>For a complete list of properties exposed by AppFog, as well as a more detailed example, see <a href="#spring-accessing-properties">Accessing AppFog Properties</a>.</p>
<h3 id="rabbit-and-spring">RabbitMQ And Spring: Additional Programming Information</h3>
<p>This section provides additional information about using RabbitMQ in your Spring apps that you deploy to AppFog. This section is not intended to be a complete tutorial on RabbitMQ and Spring; for that, see the following resources:</p>
<ul>
<li><a href="http://www.rabbitmq.com/getstarted.html">RabbitMQ Tutorials</a> cover the basics of creating messaging in your apps.</li>
<li><a href="http://www.rabbitmq.com/download.html">Download</a>, <a href="http://www.rabbitmq.com/install.html">install</a> and <a href="http://www.rabbitmq.com/configure.html">configure</a> RabbitMQ.</li>
<li><a href="http://static.springsource.org/spring-amqp/docs/1.0.x/reference/html/">Spring AMPQ reference documentation</a></li>
</ul>
<p>The RabbitMQ service is accessed through the <a href="http://www.amqp.org/">AMQP protocol</a> (versions 0.8 and 0.9.1) and your app will need access to a AMQP client library in order to use the service. The Spring AMQP project enables AMQP apps to be built using Spring constructs.</p>
<p>The following sample <code>pom.xml</code> file shows RabbitMQ dependencies and repositories in addition to the <code>cloudfoundry-runtime</code> dependency described above:</p>
<pre>&lt;repositories&gt;
    &lt;repository&gt;
          &lt;id&gt;org.springframework.maven.milestone&lt;/id&gt;
           &lt;name&gt;Spring Maven Milestone Repository&lt;/name&gt;
           &lt;url&gt;http://maven.springframework.org/milestone&lt;/url&gt;
           &lt;snapshots&gt;
                   &lt;enabled&gt;false&lt;/enabled&gt;
           &lt;/snapshots&gt;
    &lt;/repository&gt;
&lt;/repositories&gt;

&lt;dependency&gt;
    &lt;groupId&gt;cglib&lt;/groupId&gt;
    &lt;artifactId&gt;cglib-nodep&lt;/artifactId&gt;
    &lt;version&gt;2.2&lt;/version&gt;
&lt;/dependency&gt;

&lt;dependency&gt;
    &lt;groupId&gt;org.springframework.amqp&lt;/groupId&gt;
    &lt;artifactId&gt;spring-rabbit&lt;/artifactId&gt;
    &lt;version&gt;1.0.0.RC2&lt;/version&gt;
&lt;/dependency&gt;

&lt;dependency&gt;
    &lt;groupId&gt;org.cloudfoundry&lt;/groupId&gt;
    &lt;artifactId&gt;cloudfoundry-runtime&lt;/artifactId&gt;
    &lt;version&gt;0.7.1&lt;/version&gt;
&lt;/dependency&gt;
</pre>
<p>Then update your app controller/logic as follows:</p>
<ul>
<li>
<p>Include the messaging libraries:</p>
<pre>import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.amqp.core.AmqpTemplate;
</pre>
</li>
<li>
<p>Read and write messages as shown in the following Java code snippets:</p>
<pre>@Controller
public class HomeController {
   @Autowired AmqpTemplate amqpTemplate;
   @RequestMapping(value = "/")
   public String home(Model model) {
       model.addAttribute(new Message());
       return "WEB-INF/views/home.jsp";
   }
   @RequestMapping(value = "/publish", method=RequestMethod.POST)
   public String publish(Model model, Message message) {
       // Send a message to the "messages" queue
       amqpTemplate.convertAndSend("messages", message.getValue());
       model.addAttribute("published", true);
       return home(model);
   }
   @RequestMapping(value = "/get", method=RequestMethod.POST)
   public String get(Model model) {
       // Receive a message from the "messages" queue
       String message = (String)amqpTemplate.receiveAndConvert("messages");
       if (message != null)
           model.addAttribute("got", message);
       else
           model.addAttribute("got_queue_empty", true);
       return home(model);
}
</pre>
</li>
</ul>
<h3 id="spring-conditionalize">Using Spring Profiles to Conditionalize AppFog Configuration</h3>
<p>The preceding sections describe how to use the <code>&lt;cloud:&gt;</code> namespace to easily configure services (such as data sources and RabbitMQ connection factories) for Spring apps deployed to AppFog. However, you might not always want to deploy your apps to AppFog; for example, you might sometimes want to use a local environment to test the app during iterative development. In this case, it would be useful to <em>conditionalize</em> the app configuration so that only specific fragments are activated when a certain condition is true. Setting up such conditionalized configuration makes your app portable to many different environments so that you do not have to manually change the configuration when you deploy it to, for example, your local environment and then to AppFog. To enable this, use the Spring <em>profiles</em> feature, available in Spring Framework 3.1 or later.</p>
<p>The basic idea is that you group the configuration for a specific environment using the profile attribute of a nested <code>&lt;beans&gt;</code> element in the appropriate Spring app context file. You can create your own custom profiles, but the ones that are most relevant in the context of AppFog are <code>default</code> and <code>cloud</code>.</p>
<p>When you deploy a Spring app to AppFog, AppFog automatically enables the <code>cloud</code> profile. This allows for a pre-defined, convenient location for AppFog-specific app configuration. You should then group all specific usages of the <code>&lt;cloud:&gt;</code> namespace within the <code>cloud</code> profile block to allow the app to run outside of AppFog environments. You then use the <code>default</code> profile (or a custom profile) to group the non-AppFog configuration that will be used if you deploy your app to a non-AppFog environment.</p>
<p>Here is an example of a Spring <code>MongoTemplate</code> being populated from two alternately configured connection factories. When running on AppFog (<code>cloud</code> profile), the connection factory is automatically configured. When not running on AppFog (<code>default</code> profile), the connection factory is manually configured with the connection settings to a running MongoDB instance.</p>
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans  xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:cloud="http://schema.cloudfoundry.org/spring"
        xmlns:jdbc="http://www.springframework.org/schema/jdbc"
        xmlns:util="http://www.springframework.org/schema/util"
        xmlns:mongo="http://www.springframework.org/schema/data/mongo"
        xsi:schemaLocation="http://www.springframework.org/schema/data/mongo
          http://www.springframework.org/schema/data/mongo/spring-mongo-1.0.xsd
          http://www.springframework.org/schema/jdbc
          http://www.springframework.org/schema/jdbc/spring-jdbc-3.1.xsd
          http://schema.cloudfoundry.org/spring
          http://schema.cloudfoundry.org/spring/cloudfoundry-spring.xsd
          http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans-3.1.xsd
          http://www.springframework.org/schema/util
          http://www.springframework.org/schema/util/spring-util-3.1.xsd"&gt;

        &lt;bean id="mongoTemplate" class="org.springframework.data.mongodb.core.MongoTemplate"&gt;
           &lt;constructor-arg ref="mongoDbFactory" /&gt;
        &lt;/bean&gt;

        &lt;beans profile="default"&gt;
           &lt;mongo:db-factory id="mongoDbFactory" dbname="pwdtest" host="127.0.0.1" port="27017" username="test_user" password="efgh" /&gt;
        &lt;/beans&gt;

        &lt;beans profile="cloud"&gt;
           &lt;cloud:mongo-db-factory id="mongoDbFactory" /&gt;
        &lt;/beans&gt;

&lt;/beans&gt;
</pre>
<p>Note that the <code>&lt;beans profile="value"&gt;</code> element is nested inside the standard root <code>&lt;beans&gt;</code> element. The MongoDB connection factory in the <code>cloud</code> profile uses the <code>&lt;cloud:&gt;</code> namespace, the connection factory configuration in the <code>default</code> profile uses the <code>&lt;mongo:&gt;</code> namespace. You can now deploy this app to the two different environments without making any manual changes to its configuration when you switch from one to the other.</p>
<p>See the <a href="http://blog.springsource.com/2011/02/11/spring-framework-3-1-m1-released/">SpringSource Blog</a> for additional information about using Spring Profiles, a new feature in Spring Framework 3.1.</p>
<h3 id="spring-email">Sending Email From Spring Apps Deployed to AppFog</h3>
<p>In order to prevent spam and other abuse, SMTP is blocked from apps running in AppFog. However, your apps can still send email when deployed to AppFog, as described in this section.</p>
<p>Service providers, such as <a href="http://sendgrid.com/">SendGrid</a>, can send email on your behalf via HTTP web services, which is an option you can use when deploying your app to AppFog. If, however, you also run your app inside your datacenter, you might want to use your corporate SMTP servers in that case. This is a good example of using <a href="#spring-conditionalize">Spring Profiles</a> to conditionalize how your app sends email, depending on where exactly the app happens to be deployed. This makes your app portable to different environments without you having to manually update its configuration.</p>
<p>The following snippet of a Spring app context shows how to specify that your app should use SendGrid to send email when the app is running in AppFog; note the use of the <code>cloud</code> profile:</p>
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans  xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:cloud="http://schema.cloudfoundry.org/spring"

    ...

    &lt;beans profile="cloud"&gt;
       &lt;bean name="mailSender" class="example.SendGridMailSender"&gt;
          &lt;property name="apiUser" value="youremail@domain.com" /&gt;
          &lt;property name="apiKey" value="secureSecret" /&gt;
       &lt;/bean&gt;
    &lt;/beans&gt;

   ...

    &lt;!-- additional beans in your app --&gt;

&lt;/beans&gt;
</pre>
<p>In the example, <code>example.SendGridMailSender</code> is the Spring bean that sends email using the SendGrid service provider; however, this bean will only be activated when your app is deployed to AppFog. If your app is actually running inside your datacenter, then your default email server is used.</p>
<h3 id="spring-accessing-properties">Accessing AppFog Properties</h3>
<p>AppFog exposes a number of app and service properties directly into its deployed apps. Your deployed app can in turn consume these properties. The properties exposed by AppFog include basic information about the app, such as its name and the Cloud provider, and detailed connection information for all services currently bound to the app.</p>
<p>Service properties generally take one of the following forms:</p>
<pre>cloud.services.{service-name}.connection.{property}
cloud.services.{service-name}.{property}
</pre>
<p>where <code>{service-name}</code> refers to the name you gave the service when you bound it to your app at deploy time. The specific connection properties that are available depend on the type of service; see the table at the end of this section for the complete list.</p>
<p>For example, assume that in <code>af</code> you created a Postgres service called <code>my-postgres</code> and then bound it to your app; AppFog exposes the following properties about this service that your app in turn can consume:</p>
<pre>cloud.services.my-postgres.connection.host
cloud.services.my-postgres.connection.hostname
cloud.services.my-postgres.connection.name
cloud.services.my-postgres.connection.password
cloud.services.my-postgres.connection.port
cloud.services.my-postgres.connection.user
cloud.services.my-postgres.connection.username
cloud.services.my-postgres.plan
cloud.services.my-postgres.type
</pre>
<p>For convenience, if you have bound just one service of a given type to your app, AppFog creates an alias based on the service type instead of the service name. For example, if only one MySQL service is bound to an app, the properties will take the form <code>cloud.services.mysql.connection.{property}</code>. AppFog uses the following aliases in this case:</p>
<ul>
<li><code>mysql</code></li>
<li><code>mongodb</code></li>
<li><code>postgresql</code></li>
<li><code>rabbitmq</code></li>
<li><code>redis</code></li>
</ul>
<p>If you want to use these AppFog properties in your app, use a Spring property placholder inside of a <code>cloud</code> profile; Spring profiles are briefly described in <a href="#spring-conditionalize">Using Spring Profiles to Conditionalize AppFog Configuration</a>.</p>
<p>For example, assume that you have bound a MySQL service called <code>spring-mysql</code> to your app, but your app requires a c3p0 connection pool instead of the connection pool provided by AppFog. But you still want to use the same connection properties defined by AppFog for the MySQL service, in particular the username and password and JDBC URL. The following Spring app context snippet shows how you might implement this:</p>
<pre>&lt;beans profile="cloud"&gt;
   &lt;bean id="c3p0DataSource" class="com.mchange.v2.c3p0.ComboPooledDataSource" destroy-method="close"&gt;
      &lt;property name="driverClass" value="com.mysql.jdbc.Driver" /&gt;
      &lt;property name="jdbcUrl"
                value="jdbc:mysql://${cloud.services.spring-mysql.connection.host}:${cloud.services.spring-mysql.connection.port}/${cloud.services.spring-mysql.connection.name}" /&gt;
      &lt;property name="user" value="${cloud.services.spring-mysql.connection.username}" /&gt;
      &lt;property name="password" value="${cloud.services.spring-mysql.connection.password}" /&gt;
   &lt;/bean&gt;
&lt;/beans&gt;
</pre>
<p>The following table lists all the app and service properties that AppFog exposes to deployed apps. In the property names, <code>{service-name}</code> refers to the actual name of the bound service.</p>
<p>cloud.app.nameNot applicable.The name of the app.</p>
<table class="table table-bordered table-striped attributes">
<thead>
<tr><th>Property</th><th>Associated Service Type</th><th>Description</th></tr>
</thead>
<tbody>
<tr>
<td>cloud.provider.url</td>
<td>Not applicable.</td>
<td>The URL of the cloud hosting your app, such as <tt>cloudfoundry.com</tt>.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.db</td>
<td>MongoDB</td>
<td>Name of the database that AppFog created.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.host</td>
<td>MongoDB</td>
<td>Name or IP address of the host on which the MongoDB server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.hostname</td>
<td>MongoDB</td>
<td>Name or IP address of the host on which the MongoDB server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.name</td>
<td>MongoDB</td>
<td>Name of the user that connects to the MongoDB database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.password</td>
<td>MongoDB</td>
<td>Password of the user that connects to the MongoDB database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.port</td>
<td>MongoDB</td>
<td>Listen port of the MongoDB server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.username</td>
<td>MongoDB</td>
<td>Name of the user that connects to the MongoDB database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.plan</td>
<td>MongoDB</td>
<td>Pay plan for the service, such as <tt>free</tt>.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.type</td>
<td>MongoDB</td>
<td>Name and version of the MongoDB server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.name</td>
<td>MySQL</td>
<td>Name of the MySQL database that AppFog created.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.host</td>
<td>MySQL</td>
<td>Name or IP address of the host on which the MySQL server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.hostname</td>
<td>MySQL</td>
<td>Name or IP address of the host on which the MySQL server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.port</td>
<td>MySQL</td>
<td>Listen port of the MySQL server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.user</td>
<td>MySQL</td>
<td>Name of the user that connects to the MySQL database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.username</td>
<td>MySQL</td>
<td>Name of the user that connects to the MySQL database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.password</td>
<td>MySQL</td>
<td>Password of the user that connects to the MySQL database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.plan</td>
<td>MySQL</td>
<td>Pay plan for the service, such as <tt><tt>free.</tt></tt></td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.type</td>
<td>MySQL</td>
<td>Name and version of the MySQL server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.name</td>
<td>Postgres</td>
<td>Name of the Postgres database that AppFog created.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.host</td>
<td>Postgres</td>
<td>Name or IP address of the host on which the Postgres server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.hostname</td>
<td>Postgres</td>
<td>Name or IP address of the host on which the Postgres server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.port</td>
<td>Postgres</td>
<td>Listen port of the Postgres server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.user</td>
<td>Postgres</td>
<td>Name of the user that connects to the Postgres database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.username</td>
<td>Postgres</td>
<td>Name of the user that connects to the Postgres database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.password</td>
<td>Postgres</td>
<td>Password of the user that connects to the Postgres database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.plan</td>
<td>Postgres</td>
<td>Pay plan for the service, such as <tt>free</tt>.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.type</td>
<td>Postgres</td>
<td>Name and version of the Postgres server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.url</td>
<td>RabbitMQ</td>
<td>URL used to connect to the AMPQ broker. URL includes the host, port, username, and so on.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.plan</td>
<td>RabbitMQ</td>
<td>Pay plan for the service, such as <tt><tt>free.</tt></tt></td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.type</td>
<td>RabbitMQ</td>
<td>Name and version of the RabbitMQ server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.host</td>
<td>Redis</td>
<td>Name or IP address of the host on which the Redis server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.hostname</td>
<td>Redis</td>
<td>Name or IP address of the host on which the Redis server is running.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.port</td>
<td>Redis</td>
<td>Listen port of the Redis server.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.name</td>
<td>Redis</td>
<td>Name of the user that connects to the Redis database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.connection.password</td>
<td>Redis</td>
<td>Password of the user that connects to the Redis database.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.plan</td>
<td>Redis</td>
<td>Pay plan for the service, such as <tt>free</tt>.</td>
</tr>
<tr>
<td>cloud.services.{<em>service-name</em>}.type</td>
<td>Redis</td>
<td>Name and version of the Redis server.</td>
</tr>
</tbody>
</table>
