{{{
  "title": "Run custom script upon failover for Windows PG",
  "date": "07-16-2018",
  "author": "Juan Aristizabal",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
This article explains how to configure custom scripts to run upon failover for Windows Protection Groups.

### Requirements
1. Initial Replication is complete for the Protection Group and checkpoints are available for Failover.

### Assumptions
This article assumes that a SafeHaven cluster has already been created successfully. Both production and recovery SRNs are registered and peered with storage pools claimed correctly. Initial replication has completed and there is at least one checkpoint available. This article assumes that Test Failover has been done successfully.

### Run custom script upon failover for Windows PG
Users may not choose to perform Network Isolation in case of an actual Failover event.

1. RDP to the Windows server on production.

2. Open the folder **C:\Program Files\SafeHaven\startup**, locate the file  **customSecScript.bat** and open it on a text editor. 

3. The file has an example on how to open RDP port on the failover instance. Add your script invokation at the end of the file, also include an echo statement before the command invokation to add a comment on the log file. For instance here is a simple command that creates a file after the failover instance boots up (only the last lines of the file are shown).

```batch
.......
......
echo "Open RDP port in the firewall for all security profiles so that the VM is accessible in the cloud"
powershell -command "Set-NetFirewallRule -DisplayGroup """Remote Desktop""" -Profile Any -Action Allow"
echo "Testing post boot operation"
powershell -command "echo """testing custom script..."" > C:\Users\Administrator\Downloads\onfailover.txt" 
```


4. Save the file and either wait for the periodic checkpoint to kick in or issue a manual checkpoint from the SafeHaven console. 

5. Upon failover or test failover the script **customSecScript.bat** will be executed. You can confirm the commands executed by looking at the contents of the log file **safehavenStartup.txt** located at **C:\Program Files\SafeHaven\startup**.
