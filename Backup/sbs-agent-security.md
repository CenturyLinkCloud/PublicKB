{{{
  "title": "SBS Agent Security Configurations",
  "date": "11-8-2019",
  "author": "John Gerger",
  "keywords": ["backup", "clc", "cloud", "restore", "sbs"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

Simple Backup Service Agent Security Configurations
===================================================

The Backup agent's UI is password protected and restricted to 'localhost' viewing by default. This document describes how to customize the username, password, and agent binding IP address.

When SimpleBackupService is installed, the application is secured by the default username and password.

The default values are:  
* Username: sbs  
* Password: backup

The username, password and agent binding IP address can be customized by editing the ``sbs-agent.properties`` file located in the Simple Backup Service install directory.

``/opt/simplebackupservice`` on Linux

``C:\Program Files\simplebackupservice`` on Windows

The file contains the following text:
```
#Uncomment the two below lines to set custom username and password
#security.user.name=sbs 
#security.user.password=backup

#Uncomment to change the Network address to which the agent should bind to, default is 127.0.0.1
#To open agent ui for all ip ranges, set to 0.0.0.0
#server.address=127.0.0.1
```
Simply remove the hash symbol from the lines you wish to change and replace the text after the “=“ symbols on those lines with the values of your choice. You can bind the server.address property to one of the sever's IP addresses, or set it to 0.0.0.0 to allow access to all the server's IP addresses. Be sure to save the file with these changes and [restart the Simple Backup Service](restarting-simple-backup-service.md) agent for the changes to take affect.
