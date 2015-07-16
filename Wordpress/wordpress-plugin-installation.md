{{{
  "title": "WordPress Plugin Installation",
  "date": "07-15-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

### IMPORTANT NOTECenturyLink Cloud WordPress hosting is currently in a Limited Beta program with specific customers by invitation only and is not intended for production usage.During the Limited Beta there is no production Service Level Aggreement.--

CenturyLink Cloud WordPress sites use Git to deploy new WordPress code including new plugins.

In order to activate a plugin you will need to download a WordPress Plugin and upload it into the Master branch of the Centurylink Git repository provided to you during your CenturyLink Cloud Wordpress site creation. This will then force a refresh of your WordPress blog and allow you to activate and configure the plugin.

**NOTE:** These instructions assume the following...

* The Git CLI is installed
* A working knowledge of Git usage

##Deploying a WordPress Plugin Using the Git CLI

1. [Clone your WordPress Git Repo](wordpress-clone-push-gitlab.md "Clone your WordPress Git Repo")

2. Open the wp-content folder.

  ![](../images/wp_plugin_installation/wp_plugin_installation_01.png "wp_plugin_installation_01.png")

3. Open the plugins folder.

  ![](../images/wp_plugin_installation/wp_plugin_installation_02.png "wp_plugin_installation_02.png")

4. Download the WordPress Plugin you want to install.

  _In this example we will be installing Akismet_.

5. Locate the local folder the plugin was downloaded to and copy it into the plugins folder of your cloned GitHub repository.

  ![](../images/wp_plugin_installation/wp_plugin_installation_03.png "wp_plugin_installation_03.png")

  You will end up with the following...

  ![](../images/wp_plugin_installation/wp_plugin_installation_04.png "wp_plugin_installation_04.png")

6. Inside your repo, at the command line, running **_git status_** will now show you uncommited changes.

  ![](../images/wp_plugin_installation/wp_plugin_installation_05.png "wp_plugin_installation_05.png")

7. Commit your changes using the **_git add_** command.

  _In this example we will run git add * to add all files to the repo_

  ![](../images/wp_plugin_installation/wp_plugin_installation_06.png "wp_plugin_installation_06.png")

8. Running **_git status_** will show new files to commit.

  ![](../images/wp_plugin_installation/wp_plugin_installation_07.png "wp_plugin_installation_07.png")

9. Run **_git commit_** to commit files.

  ![](../images/wp_plugin_installation/wp_plugin_installation_08.png "wp_plugin_installation_08.png")

10. An editor will open. Insert a comment and save the file.

  ![](../images/wp_plugin_installation/wp_plugin_installation_09.png "wp_plugin_installation_09.png")

11. The CLI will then output file creation.

  ![](../images/wp_plugin_installation/wp_plugin_installation_10.png "wp_plugin_installation_10.png")
  
12. Run **_git push_** to push changes back to your Git Repository and force a restart of your WordPress site.

  ![](../images/wp_plugin_installation/wp_plugin_installation_11.png "wp_plugin_installation_11.png")

13. In your WordPress installation expand _Plugins_.

  ![](../images/wp_plugin_installation/wp_plugin_installation_12.png "wp_plugin_installation_12.png")

14. Next to your installed plugin click _Activate_

  ![](../images/wp_plugin_installation/wp_plugin_installation_13.png "wp_plugin_installation_13.png")

14. Your plugin is now installed.
