{{{
  "title": "Installing Wordpress Plugins",
  "date": "04-05-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

<h3>Installing Wordpress Plugins</h3>

CenturyLink Cloud WordPress sites use http://www.github.com to deploy new WordPress code including new plugins.

In order to activate a plugin you will need to download a WordPress Plugin and upload it into the Master branch of the GitHub repository provided to you during your CenturyLink Cloud Wordpress installation. This will then force a refresh of your WordPress blog and allow you to activate and configure the plugin.

**NOTE:** _These instructions assume a working knowledge of GitHub usage and will utilize Windows and the GitHub for Windows Application to sync a new plugin directly to the Master Branch._

**1. Open GitHub, right click your cloned repository, and select Open in Explorer.**

![](../images/installing-wordpress-plugins_1.png "installing-wordpress-plugins_1.png")

**2. Open the wp-content folder.**

![](../images/installing-wordpress-plugins_2.png "installing-wordpress-plugins_2.png")

**3. Open the plugins folder.**

![](../images/installing-wordpress-plugins_3.png "installing-wordpress-plugins_3.png")

**4. Download the WordPress Plugin you want to install.**

In this example we will be installing _Akismet_.

**5. Locate the local folder the plugin was downloaded to and copy it into the plugins folder of your GitHub repository.**

![](../images/installing-wordpress-plugins_4.png "installing-wordpress-plugins_4.png")

You will end up with the following...

![](../images/installing-wordpress-plugins_5.png "installing-wordpress-plugins_5.png")

**6. In the GitHub Client you will now see _Uncommitted Changes_**

![](../images/installing-wordpress-plugins_6.png "installing-wordpress-plugins_6.png")

**7. Click _Show_ to expand the view and see local changes to the repository.**

![](../images/installing-wordpress-plugins_7.png "installing-wordpress-plugins_7.png")

**8. In the right pane you will see a list of changes that can be committed to GitHub.**

![](../images/installing-wordpress-plugins_8.png "installing-wordpress-plugins_8.png")

**9. Add a comment and click _Commit to master_.**

![](../images/installing-wordpress-plugins_9.png "installing-wordpress-plugins_9.png")

**10. In the upper right hand corner click _Sync_ to upload the commited changes to GitHub.**

![](../images/installing-wordpress-plugins_10.png "installing-wordpress-plugins_10.png")

**11. On http://www.github.com you will now the plugin in the plugins directory.**

![](../images/installing-wordpress-plugins_11.png "installing-wordpress-plugins_11.png")

**12. In your WordPress installation expand _Plugins_.**

![](../images/installing-wordpress-plugins_12.png "installing-wordpress-plugins_12.png")

**13. Next to your installed plugin click _Activate_**

![](../images/installing-wordpress-plugins_13.png "installing-wordpress-plugins_13.png")

**14. Your plugin is now installed.**
