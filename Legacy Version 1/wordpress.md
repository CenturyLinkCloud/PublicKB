{{{
  "title": "Getting Started With AppFog v1: WordPress",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>WordPress is the most-used content management systems on the internet today, accounting for an unbelievable 22.0% of the top 10 million websites, and on a total of over 60 million websites as of August 2013. Although when it was initially developed in 2003 to be a blogging platform, its ease of use, ability to add third-party plugins, and scalability has made it popular for nearly every use under the sun in the succeeding years.</p>
<p>We at AppFog recognize the appeal of WordPress. The advantages of cloud computing and PaaS are numerous. However, due to the non-persistent filesystem, the ephemeral nature of uploaded media assets and files can be frustrating, especially in the case of having a WordPress hosted with AppFog. One can upload an image, a theme update, or a new plugin then that asset can be gone five minutes later.</p>
<p>Rest assured, there are ways to run a working, up-to-date, and highly active WordPress install on AppFog! It involves these three steps.</p>
<ol>
<li><a href="#install">Installing WordPress on your local computer.</a></li>
<li><a href="#update_local">Update its core, themes, and plugins.</a></li>
<li><a href="#upload">Upload the app and database to AppFog.</a></li>
<li><a href="#keep_updated">Keep it up-to-date.</a></li>
</ol>
<hr />
<h2 id="install">Part One: Install WordPress Locally</h2>
<p>Getting a basic WordPress site on a local machine is pretty straightforward. You will need to set up a server environment to run PHP and MySQL, then <a href="http://www.wordpress.org/download/">download the latest version of WordPress</a>. You can run it on just about any type of a desktop/laptop or server operating system, and instructions can often be found just a Google search away. For your convenience, I've selected web links with thorough installation instructions for Windows, Mac OS, and Ubuntu.</p>
<h3>Windows</h3>
<p>There are a plethora of solutions for getting the environment set up to run WordPress on Windows XP, Vista, 7, or 8. My personal favorite is by using XAMPP (which stands for Cross-platform, Apache, MySQL, PHP and Perl), for which I've placed the link first.</p>
<ul>
<li>WPMU Dev: <a href="http://premium.wpmudev.org/blog/how-to-install-WordPress-locally-for-pcwindows-with-xampp/">How to Install WordPress Locally for PC/Windows with XAMPP</a></li>
<li>WordPress Codex: <a href="http://codex.wordpress.org/Installing_WordPress#Easy_5_Minute_WordPress_Installation_on_Windows">Easy 5 Minute WordPress Installation on Windows</a></li>
<li>WP Explorer: <a href="http://www.wpexplorer.com/install-WordPress-in-windows-wamp/">Installing WordPress On Windows Locally With WAMP</a></li>
</ul>
<h3>OS X</h3>
<p>A nice Mac-based solution is through a compilation of Mac, Apache, MySQL, and PHP called MAMP.</p>
<ul>
<li>WP Beginner: <a href="http://www.wpbeginner.com/wp-tutorials/how-to-install-WordPress-locally-on-mac-using-mamp/">How to Install WordPress Locally on Mac using MAMP</a></li>
<li>WordPress Codex: <a href="http://codex.wordpress.org/Installing_WordPress_Locally_on_Your_Mac_With_MAMP">Installing WordPress Locally on Your Mac With MAMP</a></li>
</ul>
<h3>Ubuntu</h3>
<p>Flavors of Linux distributions are more varied than there are types of ice cream at your local Baskin Robins. One of the most popular Linux distros is Ubuntu, and the WordPress installation for it are simple.</p>
<ul>
<li>WP Explorer: <a href="http://www.wpexplorer.com/locally-install-WordPress-on-ubuntu/">Install WordPress On Ubuntu Locally With LAMP</a></li>
</ul>
<p>Once you have carefully followed the instructions and can verify that WordPress is running smoothly on your local machine, you can proceed to the next step.</p>
<hr />
<h2 id="update_local">Part Two: Update Core, Themes, and Plugins</h2>
<p>Now you can customize your local WordPress install by adding new themes (the look and feel of your website) and plugins (third-party code extensions that provide your WordPress install with expanded functionality). Consult the latest WordPress documentation for more information on this.</p>
<p>Once you have your local WordPress site running the way you wish it to on a live, public environment (e.g., on AppFog). make sure you have the latest version of, not only your WordPress core files, but of all themes and plugins you may have added. This can be done by directing your web browser to your local install's admin back-end at <code>/wp-admin/update-core.php</code>.</p>
<p>Next, you should make a backup copy of your <em>wp-config.php</em> that's located in your root WordPress directory. You will need to do some modifications to it in the final step.</p>
<p>You can more information on image hosting with WordPress on AppFog in our <a href="cloud-image-hosting-for-wordpress-on-appfog.md">Cloud Image Hosting for WordPress on AppFog</a> article.</p>
<hr />
<h2 id="upload">Part Three: Deploy your WordPress Site to AppFog</h2>
<p>Instructions on how to how to complete this task can be found on our support site via the links below. Remember to open the <em>wp-config.php</em> and modify the pieces of the code used to connect to the database with the <em>VCAP_SERVICES</em> environment variable.</p>
<ul>
<li>AppFog: <a href="wordpress-deployment-and-configuration.md">WordPress Deployment and Configuration</a></li>
<li>AppFog: <a href="service-database-content-management-tunneling.md">Service/Database Content Management (Tunneling)</a></li>
</ul>
<hr />
<h2 id="keep_updated">Part Four: Stay Current with WordPress Updates</h2>
<p>As some of the most widely-used website software in the world, it's no surprise that WordPress is a major target to attackers, whom work tirelessly to find vulnerabilities in the code. AppFog strongly advises to update to the very latest available versions of the WordPress core code, themes, and plugins to minimize your chances of being compromised.</p>
