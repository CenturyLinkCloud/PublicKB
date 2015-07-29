{{{
  "title": "Languages And Frameworks: Python",
  "date": "1-30-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<ul>
<li><a href="#wsgi">WSGI</a></li>
<li><a href="#dependencies">Dependencies</a></li>
<li><a href="#services">Services</a></li>
</ul>
<p>AppFog currently supports Python 2.7.3. You can check the available runtimes by running <code>af runtimes</code>.</p>
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
<h1 id="wsgi">WSGI</h1>
<p>AppFog supports Python by serving apps through the <a href="http://wsgi.readthedocs.org/en/latest/index.html">WSGI</a> protocol using <a href="http://gunicorn.org/">Gunicorn</a>.</p>
<p>By convention, the entry point for non-django applications should be in a file named <code>wsgi.py</code> in the base directory and should contain a function named <code>application</code> with 2 parameters for the wsgi <code>environ</code> and <code>start_response</code>. The full gunicorn command will be something like <code>gunicorn -c gunicorn.config wsgi:application</code>, where the generated config file will include the port your application will bind to. For django applications, the wsgi.py file is not required. Unfortunately, the file your app is bootstrapped through (wsgi.py) and name of your application function is not customizable on AppFog.</p>
<h1 id="dependencies">Dependencies</h1>
<p>AppFog uses <code>pip</code> (1.1) and <code>virtualenv</code> to deploy apps. You can define the package prequisites of your Python app in a top-level <a href="https://pip.pypa.io/en/1.1/requirements.html">requirements.txt</a> file, which <code>pip</code> uses to install dependencies. Dependencies will be downloaded and re-cached into your package whenever you update your app. In cases where your requirements take an exceptionally long time to download or compile, you have as an option the ability to bundle your requirements along with your application code, which will speed up the staging process for your app.</p>
<pre>$ pip bundle -r requirements.txt app.pybundle
</pre>
<p>For more details, see the <a href="http://www.pip-installer.org/en/1.1/usage.html#bundles">pip docs</a>.</p>
<h2>Limitations</h2>
<p>There is currently a known issue with Python apps that include many dependencies. We are working on a solution to this that should be available very soon.</p>
<h2 id="services">Services</h2>
<p>You can connect your Python app to AppFog services by using the <code>VCAP_SERVICES</code> environment variable, which becomes available to your app when you bind a service to it.</p>
