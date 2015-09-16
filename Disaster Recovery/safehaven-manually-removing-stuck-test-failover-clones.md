{{{
  "title": "SafeHaven 3.1: Manually removing stuck test failover clones (primarily 3.1)",
  "date": "8-31-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

#### Overview:

If the is corruption (see companion article on determining corruption), or other issues within the cluster, occoassionally the Test-Failover clone will fail and require maunal cleanup. The following commands will walk you through removing the clone and protection group. They will need to be completely re-created once they have been removed as this is due to the corruption issue currently undergoing an emergency sprint to release an update.

#### WALKTHROUGH:

1. Stop CMS and SRN services
  1. Log in CMS, run the following commands
	2. Kill the process: killall -9 manager
	3. Make sure the process is killed with the command: ps -ef|grep manager
2. Log into Prod SRNx and DR SRNx
  1. Login to both SRNs
  2. Kill the process: killall -9 voffice
	3. Make sure the process is killed with the command: ps -ef|grep voffice
	4. Repeat on all nodes.

3. Clean the target
  1. Run scstadmin -list_target
  2. Copy the desied IQN     
	3. Run scstadmin -rem_target <paste IQN name> -driver iscsi

4. Clean the device 		
  1. vgs to list all volume groups
	2. vgchange -a n <vg name>
	3. vgremove <vg name> -f

5. kpartx -d /dev/sbdx (where x is the number of your PG SBD group, either found through the CMS GUI or following the steps below)
    1. login to srn
    2. cd /var/syntropy/dvol
    3. ls
    4. cat protectiongroupname/protectiongroup.dvol
    5. ms_sbd_device to get /dev/sbd#

6. sbdm /dev/sbdx clear

7. Clean Logical Volume
	1. lvs to list
	2. If yes, then
	3. lvremove:
    /dev/$volume group name$ $(Storage Pool Name$)/$protection group name$

    *(Most will have a snap volume and a PG volume so it is easiest to do lvremove /dev/vol group/PG-name* and you will be prompted to choose y/n for each volume in the event you made a mistake.)*

   4.EXTRANEOUS PER SHASHA, BUT KEEPING FOR RECORD: dd if=/dev/zero of=/dev/<volume group name>/<protection group name> bs=4M

8. Clean Physical Volumes
	1. pvs to list
	2. If yes, then
	3. pvremove /dev/mapper/xxx

9. Clean the folders and files
	1. cd /var/syntropy/
	2. ls
	3. cd into every directory, delete any files with the PG name  (associated bitmaps, pluns, targets, dvol. Some of these will be directories so use rm -rf rather than simply rm). If you have a unique name, it is easiest to cd into each directory ane simply rm <Protection Group Name*> and then re-run ls to verify that the appropriate entries have been deleted.
