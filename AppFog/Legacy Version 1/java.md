{{{
  "title": "Languages And Frameworks: Java",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#javaversions">Supported Java Versions</a></li>
<li><a href="#deploy">Deploying Java Apps</a></li>
<li><a href="#custom-jvm-params">Custom JVM Parameters</a></li>
</ul>
<h3 id="javaversions">Supported Java Versions</h3>
<p>For a list of runtimes that AppFog supports run:</p>
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
<h2 id="deploy">Deploying Java Apps</h2>
<p>You can deploy most Java apps by simply generating a <code>WAR</code> file, then running <code>af push</code> from the target directory.</p>
<h2 id="custom-jvm-params">Custom JVM Parameters</h2>
<p>You can add custom JVM parameters like <code>-Duser.timezone</code> by specifiying <code>JAVA_OPTS</code> as an environment variable:</p>
<pre>$ af env-add &lt;app-name&gt; JAVA_OPTS=&lt;value&gt;
</pre>
<p>You can also include the <code>$HOME</code> variable to point to the Tomcat's <code>lib</code> directory.</p>
