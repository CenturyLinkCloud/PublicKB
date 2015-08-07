{{{
  "title": "Getting Started with AppFog’s Command Line",
  "date": "1-25-2015",
  "author": "Originally Posted On AppFog",
  "attachments": [],
  "contentIsHTML": false
}}}

[AppFog](http://www.ctl.io/appfog) provides a cloud-based hosting service for your favorite web application stack. You can get servers setup and ready for your code in under a minute using our command line tools or our web console–the choice is yours. Today, we’re going to walk through deploying a WordPress app using af, the command line interface to AppFog.

To get started, you’re going to need a beta account and af. If we haven’t already let you into our private beta, add your email to our list at [appfog](http://www.ctl.io) and we’ll add you in no time!

<code>af</code> is based on vmc, the [CloudFoundry](http://cloudfoundry.org/index.html) command line tool and is distributed as a RubyGem. To install af, you will need [Ruby](https://www.ruby-lang.org/en/) and [RubyGems](https://rubygems.org/). If these are available, then run

<pre><code>$ gem install af</code></pre>

Now you’re ready to login!

<pre><code>
$ af login
Email: jeremy@appfog.com
Password: *********
Successfully logged into [https://api.appfog.com]
</code></pre>

Next, you’re going to need some code to deploy. Luckily, we have prepared a CloudFoundry-ready WordPress sample at [https://github.com/phpfog/af-sample-wordpress](https://github.com/phpfog/af-sample-wordpress). If git is available on your system, then run

<pre><code>
$ git clone https://github.com/phpfog/af-sample-wordpress.git
$ cd af-sample-wordpress
</code></pre>

If you’d rather not use git, you can download a zip archive from [https://github.com/phpfog/af-sample-wordpress/](https://github.com/phpfog/af-sample-wordpress/).

Now let’s push our code to AppFog, name it my-first-app and give it a MySQL database. First, we need to call af push to create our app and upload our code.

<pre><code>
$ af push my-first-app --url my-first-app.aws.af.cm
Creating Application: OK
Uploading Application:
  Checking for available resources: OK
  Processing resources: OK
  Packing application: OK
  Uploading (127K): OK
Push Status: OK
Staging Application: OK
Starting Application: OK
</code></pre>

<code>af</code> detected that we are pushing PHP code and staged and deployed it using Apache 2, but it still needs to connect to a database so let’s ask af to create a MySQL database and bind it to our app.

<pre><code>
$ af create-service mysql --bind my-first-app
Creating Service [mysql-cff71]: OK
Binding Service: OK
Stopping Application: OK
Staging Application: OK
Starting Application: OK
And you’re done! You can now visit your new WP app at http://my-first-app.aws.af.cm/ (or whichever url you chose).
</code></pre>

That’s all for now. You can learn more about af by running af help or asking a question at [support.appfog.com](http://support.appfog.com).
