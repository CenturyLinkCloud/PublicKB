{{{
  "title": "SafeHaven 3.1: Removing Stuck Test Failover Clones",
  "date": "9-21-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
If there is corruption within a Protection Group (see companion article on determining corruption) or other issues within the cluster, occasionally a Test-Failover clone will fail and require manual cleanup. The following commands walk you through removing the clone and protection group. They will need to be completely re-created once they have been removed, as a corrupt Protection Group is unusable.

### Walkthrough
1. Stop CMS and SRN services.
   * Log in CMS, run the following commands.
   * Kill the process: `killall -9 manager`
   * Make sure the process is killed with the command: `ps -ef|grep manager`

2. Log into Prod SRNx and DR SRNx.
   * Login to both SRNs.
   * Kill the process: `killall -9 voffice`
   * Make sure the process is killed with the command: `ps -ef|grep voffice`
   * Repeat on all nodes.

3. Clean the target.
   * Run `scstadmin -list_target`.
   * Copy the desied IQN     .
   * Run `scstadmin -rem_target <pasted IQN name> -driver iscsi`.

4. Clean the device .		
   * `vgs` to list all volume groups.
   * `vgchange -a n <vg name>`
   * `vgremove <vg name> -f`

5. `kpartx -d /dev/sbdx` (where x is the number of your PG SBD group, found either through CMS GUI or following the steps below).
   * Login to srn and do the following.
   * `cd /var/syntropy/dvol`
   * `ls`
   * `cat protectiongroupname/protectiongroup.dvol`
   * `ms_sbd_device to get /dev/sbd#`

6. `sbdm /dev/sbdx clear` (where x is the number of the PG SBD group).

7. Clean Logical Volume.
   * `lvs` to list
   * If yes, then `lvremove:/dev/$volumegroupname$ $(Storage Pool Name$)/$protection group name$`.

   *(Most have a snap volume and a PG volume. It is easiest to do lvremove /dev/vol group/PG-name* *and you will be prompted to choose y/n for each volume in the event of a mistake.)*

   * OPTIONAL COMMAND (Not currently required): `dd if=/dev/zero of=/dev/<volume group name>/<protection group name> bs=4M`

8. Clean Physical Volumes.
   * pvs to list
   * If volumes exist, then execute
   * `pvremove /dev/mapper/xxx`

9. Clean the folders and files.
   * `cd /var/syntropy/`
   * `ls`
   * cd into every directory, delete any files with the PG name  (associated bitmaps, pluns, targets, dvol. Some of these are directories so use rm `-rf` rather than simply `rm`). If you have a unique name, it is easiest to cd into each directory and simply `rm -rf <Protection Group Name*>`. Then re-run `ls` to verify that the appropriate entries have been deleted.

  10. Login to CMS and re-start services when prompted.
     * Manually restart SRN services (right click on SRN, "start").
     * Then, rebuild Protection Groups as required.
