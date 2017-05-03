{{{
  "title": "SafeHaven-4-Upgrade Procedure for Minor Releases(Syntropy and GUI Console)",
  "date": "05-03-2016",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}
## Article Overview
This article explains how to upgrade SafeHaven software and console.

### Assumption
This article assumes that the existing cluster is 4.0.1 or later. In this example, both Syntropy version and SafeHaven Console version are 4.0.1

![Upgrade](../../images/SH4.0/Upgrade/upgrade_1.png)

### Requirement
I order to prevent possible ongoing jobs failure, please confirm no job is in progress before upgrad.

### Update SafeHaven software (Syntropy)

Click on Administration on tools bar and then click on "Update Code.." from the drop-down menu. 

![Upgrade](../../images/SH4.0/Upgrade/upgrade_2.png)


Input the URL of the update debian file, link (https://download.safehaven.ctl.io/SH-4.0.2/safehaven-4.0.2.deb) under the Download Links section of the SafeHaven 4.0.2 release notes : https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/safehaven-4.0.2-release/.

Then input CMS root Password, click "Update" to start the update

**NOTE**: The latest official SafeHaven is 4.0.2 when this article is been written, if you are running on later version, please contact SafeHaven team for assistance 

![Upgrade](../../images/SH4.0/Upgrade/upgrade_3.png)

After the update is finished, click on "OK" then "OK and Close" to leave the wizard.

![Upgrade](../../images/SH4.0/Upgrade/upgrade_4.png)


### Download the new SafeHaven Console 

Download the latest compatible SafeHaven Console (GUI) from the GUI Package download link (https://download.safehaven.ctl.io/SH-4.0.2/SafeHavenConsole-4.0.2.zip) under the Download Links section of the SafeHaven 4.0.2 release notes : https://www.ctl.io/knowledge-base/disaster-recovery/safehaven-4/safehaven-4.0.2-release/

Unzip the downloaded package and login to the cluster using the new console

Double check if the versions of SafeHaven Console and Syntropy are compatible.

![Upgrade](../../images/SH4.0/Upgrade/upgrade_5.png)

