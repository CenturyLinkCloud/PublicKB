{{{
  "title": "SafeHaven: Gracefully Shutdown SRN Node",
  "date": "10-29-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### OVERVIEW

Rebooting an SRN without taking the proper steps for a graceful shutdown can cause problems with the protection groups residing on said SRN, the most common is reconstitution failure, which renders protection groups in an inactive or error state. This guide will walkthrough the steps required for a proper SRN shutdown. Note that stopping/restarting services does not have the same potential and as such can be performed at any time.

### WALKTHROUGH

1.	Login to SRN and  kill the voffice service: `Killall -9  voffice`

2.	Login to guest vm and disconnect from the iSCSI target: 

  a.	Windows: Disconnect from Iscsi target from Iscsi initiator.

  b.	Linux: `iscsiadm –m node –u`

3.	Login to SRN via SSH

4.	Remove the Iscsi targets:

  a.	`scstadmin -list_target`

  b.	Perform the following command with each IQN pasted into the <target name> field: `scstadmin -rem_target <the target name> -driver iscsi`

5.	Deactivate the Pluns (logical volumes) for the protection groups:
  a. Run `lvscan`
  b. Run `vgchange –an <VG name>` using the volume names, for each volume.
  c. Run `lvscan` again to make sure all volumes have been deactivated (lvscan should show all as "inactive"). If you are unable to deactivate a volume, run `kpartx -d /dev/sbd0` then `kpartx -d /dev/sbd1` (use all sbd's from 0 onward)

6.	Clear all the sbd’s : `sbdmAllClear` (or individually clear sbd's: `sbdm /dev/sbd<number> clear` similar to step 5c).

7.	Reboot the SRN

8.	After rebooting the SRN, make sure that the Protection Groups are reconstituted and in "running state" and that the Guest connects to the targets again. On the Production (source) VM, run `DgSyncEx.exe list` from the SafeHaven Tools Command Prompt to make sure sync is intact. Check `lvscan` to make sure that the logical volumes are active, and run `scstadmin –list_target` to verify that the iSCSI targets are being presented.

9. (Optional) Create a new checkpoint.
