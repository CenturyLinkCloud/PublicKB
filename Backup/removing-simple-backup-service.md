{{{
  "title": "Removing Simple Backup Service",
  "date": "03-16-2016",
  "author": "Justin Withington",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": false
}}}

In order to remove Simple Backup Service from your system, please follow the instructions below for Windows and Linux accordingly.

**Windows**

1. Navigate to the Windows Control Panel
2. Click on the 'Uninstall a Program' option
3. Select the SimpleBackupService Program
4. Click the Uninstall button and confirm your selection

**Linux**

1. Enter the following text in the Linux Command Line:

```
service simplebackupservice stop
rm -rf /opt/simplebackupservice
rm /etc/init.d/simplebackupservice

if [ -f /etc/redhat-release ];
then
# CentOS and RHEL
chkconfig --del simplebackupservice > /dev/null 2>&1
elif [ -f /etc/debian_version ];
then
# Debian and Ubuntu
update-rc.d -f simplebackupservice remove > /dev/null 2>&1
else
exit 1
fi
```
