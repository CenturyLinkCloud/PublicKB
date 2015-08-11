{{{
  "title": "Getting Started With AppFog v1: Cloud Image Hosting for WordPress on AppFog",
  "date": "1-25-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>As stated before, non-persistent storage for uploadable media assets and files, which are desirable and often required of a solution like WordPress, can slow down your site-building efforts. Sure, you can upload updated versions of your WordPress app from your local machine and have the media stay permanently, but what if you're creating new content everyday? What if you just need to upload a new image or two? You may find that the aforementioned time consuming and ultimately counterintuitive method goes against the quick n' simple process of uploading images to the admin back-end.</p>
<p>Luckily, there is a solution to this problem. AppFog customers can upload images to WordPress almost seamlessly the way the popular blog software has intended by making a once-time install process of one of two different plugins. One is by installing the Jetpack plugin and using its Photon module, and the other is by using the Cloudinary plugin. I have outlined the step-by-step install process for both of these below.</p>
<hr />
<h3>Using Jetpack</h3>
<p>Jetpack is a very robust plugin package created by WordPress.com that actually contains 30 smaller plugins, or "modules", that range from the trivial to the indispensable. One of these module features is called <strong>Photon</strong>, and it allows image files to be stored on WordPress.com's cloud servers. All it takes is a WordPress.com account (which takes less than 30 seconds to sign up for) in addition to a WordPress app installation and the Jetpack plugin.</p>
<h5>Installing WordPress on your AppFog Account</h5>
<ol>
<li>Set up WordPress on your AppFog account.</li>
<li>Visit the AppFog Colsole at <a href="https://console.appfog.com/">https://console.appfog.com/</a> and click on the <strong>New App</strong> button.</li>
<li>Select PHP WordPress (under "Step 1: Choose an application").</li>
<li>Choose an infrastructure (under "Step 2: Choose an infrastructure").</li>
<li>Choose a subdomain under "Step 3".</li>
<li>Wait for app to install. Once done, you will be redirected to the Mission Control page of the control.</li>
<li>Click on the <strong>Visit Live Site</strong> button in the upper right.</li>
<li>Go through the onscreen prompts to configure your WordPress blog.</li>
</ol>
<h5>Downloading your WordPress App</h5>
<p>In your computer's command line interface tool, download your app's source code by using <code>af pull &lt;appname&gt; [path]</code>.</p>
<h5>Getting a WordPress Account</h5>
<p>Sign up for an account at <a href="http://www.wordpress.com">http://www.wordpress.com</a>, and remember username/email and password.</p>
<h5>Downloading the Jetpack Plugin to your Local Computer</h5>
<ol>
<li>In your web browser, visit <a href="http://wordpress.org/plugins/jetpack/installation/">http://wordpress.org/plugins/jetpack/installation/</a> and download the latest version.</li>
<li>Unzip plugin files to the WordPress app directory on your local machine, specifically to this path: <code>/wordpress/wp-content/plugins/</code>.</li>
</ol>
<h5>Uploading your WordPress Application</h5>
<p>Go back to your CLI and update your WordPress app (with the Jetpack plugin inside the plugins folder) with this: <code>af update &lt;appname&gt; [--path]</code>.</p>
<h5>Activating Jetpack</h5>
<ol>
<li>Open up your WordPress site in a web browser, and log in to your admin backend by going to <code>&lt;yourdomain.com&gt;/wp-admin/</code>.</li>
<li>Once you're in, navigate to the Plugins section and find Jetpack by WordPress.com on the list. Click <strong>Activate</strong>.</li>
<li>You should now see a banner at the top of the page stating "Your Jetpack is almost ready!". Click the <strong>Connect to WordPress.com</strong> button.</li>
<li>Enter the WordPress.com username/email and password credentials you acquired in step #3.</li>
<li>Navigate to the Jetpack section of the WP admin back-end, and click on <strong>Settings</strong> in the left-hand navigation.</li>
<li>Scroll down to the <strong>Photon</strong> module, and click on the <strong>Activate</strong> link to the right.</li>
</ol>
<p>That's it! Your images will now be served dynamically from the global WordPress.com cloud.</p>
<hr />
<h3>Using Cloudinary</h3>
<p>Cloudinary is a powerful add-on available to all AppFog users that can streamlines all your image management needs, even if you don't necessarily use WordPress. With WordPress, though, you can easily integrate it to host images to the cloud. And through Cloudinary's own console dashboard, you access your media gallery and perform several cool operations on your images, which include easy resizing &amp; cropping, scaling, shaping, and applying different effects and filters.</p>
<h5>Installing WordPress on your AppFog Account</h5>
<ol>
<li>Visit the <a href="https://console.appfog.com/">AppFog Web Console</a>, and click on the <strong>New App</strong> button.</li>
<li>Select PHP WordPress (under "Step 1: Choose an application").</li>
<li>Choose an infrastructure (under "Step 2: Choose an infrastructure").</li>
<li>Choose a subdomain under "Step 3".</li>
<li>Wait for app to install. Once done, you will be redirected to the <strong>Mission Control</strong> page of the control.</li>
<li>Click on the <strong>Visit Live Site</strong> button in the upper right.</li>
<li>Go through the onscreen prompts to configure your WordPress blog.</li>
</ol>
<h5>Installing Cloudinary</h5>
<ol>
<li>Go back to the <a href="https://console.appfog.com/">AppFog Web Console</a>.</li>
<li>Open the WordPress app page.</li>
<li>Click on the <strong>Add-ons</strong> tab in the left-hand navigation.</li>
<li>Scroll down to the <strong>Cloudinary</strong> section and click the <strong>Install</strong> button underneath.</li>
<li>Once Cloudinary is finished installing, <strong>Manage</strong> and <strong>Delete</strong> buttons should appear. Click on <strong>Manage</strong>.</li>
<li>You can manage your email and password settings by going to <strong>Settings</strong> &gt; <strong>Users</strong> in the Cloudinary console.</li>
</ol>
<h5>Downloading your WordPress App</h5>
<p>In your computer's command line interface tool, download your app's source code by using <code>af pull &lt;appname&gt; [path]</code>.</p>
<h5>Download the Cloudinary Plugin to your Local Computer</h5>
<ol>
<li>In your web browser, visit <a href="https://wordpress.org/plugins/cloudinary-image-management-and-manipulation-in-the-cloud-cdn/">https://wordpress.org/plugins/cloudinary-image-management-and-manipulation-in-the-cloud-cdn/</a> and download the latest version.</li>
<li>Unzip plugin files to the WordPress app directory on your local machine, specifically to this path: <code>/wordpress/wp-content/plugins/</code>.</li>
</ol>
<h5>Uploading your WordPress Application</h5>
<p>Go back to your CLI and update your WordPress app (with the Jetpack plugin inside the plugins folder) with this: <code>af update &lt;appname&gt; [--path]</code>.</p>
<h5>Activating the Cloudinary Plugin</h5>
<ol>
<li>Visit the Cloudinary Dashboard at <a href="https://cloudinary.com/console">https://cloudinary.com/console</a> and copy the Cloudinary_URL. It should be in this format: cloudinary://api_key:api_secret@cloud_name. The components in that string, the api_key, the api_secret, and the cloud_name can all be found under Environment Variable on the Cloudinary console homepage.</li>
<li>Open up your WordPress site in a web browser, and log in to your admin back-end by going to <code>&lt;yourdomain.com&gt;/wp-admin/</code>.</li>
<li>Open the Cloudinary link on the lefthand side, and paste the Cloudinary_URL in the field provided and click <strong>Update Settings</strong>.</li>
<li>To use, open up a new or existing Post and click on the <strong>Cloudinary Upload/Insert</strong> button, and upload images.</li>
</ol>
<p>And you're done! Your images will now be served dynamically from the Cloudinary cloud if you use the <strong>Cloudinary Upload/Insert</strong> option instead of the default media library. Please keep in mind that there are storage limits by using the free version of Cloudinary.</p>
