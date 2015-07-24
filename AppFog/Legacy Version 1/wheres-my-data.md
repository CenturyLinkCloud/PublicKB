{{{
  "title": "Account Specific: Where's my data?",
  "date": "1-27-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>AppFog changed the resource thresholds for free plans on February 19, 2014: <a href="http://blog.appfog.com/changes-to-appfog-free-plans/">Please read more about that here</a>. As part of that change, free plan users now have a limit of two service bindings for their apps. The previous limit for service bindings was eight. If you are on a free plan and previously had more than two service bindings, please read the following to help you recover your data.</p>
<h3>Recovering Data</h3>
<p>In order to recover data from a service binding, you'll need to use the <code>af</code> command line tool to create a tunnel. Keep in mind, though, each tunnel you create consumes one of your two available service bindings and one of your two application slots. This means you can only access two services at any one time, whether through a tunnel or one of your running applications.</p>
<p>Our recommendation is to export you data prior to restarting any of your applications via af tunnel.</p>
<h3>Questions:</h3>
<ul>
<li><a href="#servicelimit">Can I create more than two services?</a></li>
<li><a href="#morethantwo">I had more than two services. Did I lose what I had beyond the allowed two?</a></li>
<li><a href="#didyoudelete">Did you delete any services or data associated with those services which existed on my account?</a></li>
<li><a href="#caniaccess">Can I still access all my data?</a></li>
<li><a href="#morethantwoapps">Can I run more than two applications at a time?</a></li>
<li><a href="#morethantwoapps">Does Caldecott count as an application?</a></li>
<li><a href="#runcald">How can I run Caldecott if I have two applications running already?</a></li>
<li><a href="#upgrade">How can I run more than two applications at a time?</a></li>
</ul>
<h3 id="servicelimit">Can I create more than two services?</h3>
<p>You cannot create additional services once you have reached the limit of two services.</p>
<h3 id="morethantwo">I had more than two services. Did I lose what I had beyond the allowed two?</h3>
<p>If you had more than two services before the maintenance, you still do.</p>
<h3 id="didyoudelete">Did you delete any services or data associated with those services which existed on my account?</h3>
<p>We did not delete any services, nor their associated data.</p>
<h3 id="caniaccess">Can I still access all my data?</h3>
<p>You can access all of the data you had prior to the maintenance.</p>
<h3 id="morethantwoapps">Can I run more than two applications at a time? Does Caldecott count as an application?</h3>
<p>You CANNOT run more than two applications at the same time. You CAN run up to two applications at any given time as long as you don't exceed the ram limit of 512MB.</p>
<p>You can create as many applications as you want, as long as you either stop all running applications or set the number of running applications to one. In order to create additional applications, first stop all apps (you may leave one of your applications running if you want). You should then be able to create an additional application.</p>
<p>Caldecott does count as an application and the ram it requires (64MB) counts toward your total ram used.</p>
<h3 id="runcald">How can I run Caldecott if I have two applications running already?</h3>
<p>Our tunneling feature (Caldecott) requires its own running application, in order to communicate with a service. If you have two running applications in addition to Caldecott, you must first stop at least one of the applications, then you can start the tunneling process using Caldecott to access your data. Once the tunneling process is complete, you must stop your Caldecott application, at which point you can start up the other application.</p>
<p>For example - on your account you have <code>app1</code>, <code>app2</code>, and <code>caldecott</code> set up. Currently <code>app1</code> and <code>app2</code> are running but you need to tunnel to your services. So you choose to stop <code>app1</code> via this command: <code>$ af stop app1</code> and then you start the tunnel like so: <code>$ af tunnel service2-mysql</code>. Once you're done with that, then you stop the tunnel application and start the app up again like so: <code>$ af start app1</code> And that's it!</p>
<h3 id="upgrade">How can I run more than two applications at a time?</h3>
<p>If you require more than two running applications (including the application used by our tunneling feature), or more than 512M of memory, or more than two services, you will need to <a href="http://www.appfog.com/products/appfog/pricing/">upgrade to one of our paid plans</a>.</p>
