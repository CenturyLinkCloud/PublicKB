{{{
  "title": "Using Managed Backup Client",
  "date": "10-26-2021",
  "author": "John Gerger",
  "attachments": [],
  "contentIsHTML": false
}}}

**Managed Backup went End of Sale 6/25/19; all existing subscriptions will still continue to function.**

**You will not be able to add Managed Backup to new servers, but it can be removed from existing servers.**

### Overview

While Control Portal allows for turning Managed Backup on and off for a given server, getting details about the status of recent backups or changing the target of the backups using an exclusions list are not yet supported through this interface. This functionality is provided, however, by the Netbackup Client installed on the server itself. After gaining access to the server remotely through either RDP on Windows or SSH on Linux, you can use the following instructions to review status or set paths for exclusion. For help using the Netbackup Client for exclusions or viewing status, you may also contact the Lumen Client Service Center at 1-888-638-6771.

### Using Netbackup Client

#### Reviewing Backup Status

Netbackup Client can be used to obtain the status of recent backups on both Windows and Linux machines.

##### **Windows**

Windows offers both a GUI client as well as information on the command line.

1. To use the GUI, launch the *Netbackup Client Job Tracker* via the Start Menu. Make sure to use **Run as Administrator**, as it will be required to launch this app. This interface will show the most recent backup and status, as well as the start and end time. Click the **Previous** or **Next** buttons to show other completed backups.

2. For the command line tool, you can run the bpclimagelist command as follows ``C:\Program Files\VERITAS\NetBackup\bin\bpclimagelist.exe -client &lthostname&gt``. This will display a list of the successful backups that have occurred for the past 14 days, which correlates with the 2 weeks of retention on the backups. If any dates are missing, this is an indicator of a backup that did not occur or failed. (In these cases, notification has been sent to the Operations Support Team at the time of failure to remedy the failed backup.)

##### **Linux**

Linux provides the bpclimagelist command that can be ran as follows ``/usr/openv/netbackup/bin/bpclimagelist -client <hostname> -b``. This will display a list of the successful backups that have occurred for the past 14 days, which correlates with the 2 weeks of retention on the backups. If any dates are missing, this is an indicator of a backup that did not occur or failed. (In these cases, notification has been sent to the Operations Support Team at the time of failure to remedy the failed backup.)

#### Setting Exclusion Rules

NetBackup provides for the ability to exclude or filter data from a backup job while it is running. A backup job is created with a defined include list for the policy and in the case Lumen Cloud Managed Backup, includes the entire volume for all disks by default. By creating an exclude list, it is possible to remove entries from the backup job which would normally be covered by the running job. It is recommended to utilize small, simple exclude lists where possible as they will add additional processing overhead.

The primary cases for defining an exclude list are when you would like to do the following:

- Exclude data that would cause the backup to exit with a partial success code (e.g. locked temp file).

- Prevent backup of junk data that has limited utility for system recovery (e.g., live database files that should be backed up with an agent, or using a script to export data to another directory).

- Prevent backup of data htat does not require frequent backup (e.g., Archive directory).

- Lower the total usage resulting in lower billing.

The exclude list can be modified for both Windows and Linux machines.

##### Windows

Custom excludes can be set up using the NetBackup Client in Windows.

1. Open the Netbackup client via the Start Menu (*Netbackup 7.x Start < Symantec Netbackup < Backup, Archive and Restore*).

2. Navigate to *File < Netbackup Client Properties* then to the *Exclude List* tab.

3. Enter a file or path name including the asterisk as a wildcard and click the **Add** button to add it to the list.

##### Linux

Custom excludes are configured in Linux by adding a line to the ``/usr/openv/netbackup/exclude_list file``

1. Open the ``/usr/openv/netbackup/exclude_list`` using ``vi`` (or your favorite Linux text editor).

2. Add the directories to be excluded.<br /><br />e.g., You might add the following paths to the exclude_list:

``/data02/apphome/crmprd/purging/``

``/data02/apphome/crmprd/appjobs/filter/Neolane\*``

``/data02/apphome/crmprd/ temp``

3. Save the file and quit (``:wq!`` in ``vi``).
