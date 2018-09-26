{{{
  "title": "SafeHaven: Gracefully Shutdown SRN Node",
  "date": "10-29-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### OVERVIEW
Rebooting an SRN without taking the proper steps for a graceful shutdown can cause problems with the protection groups residing on the SRN. The most common is reconstitution failure, which renders protection groups in an inactive or error state. This guide walks you through the steps required for a proper SRN shutdown. Note that stopping/restarting services does not have the same potential and ,as such, can be performed at any time.

### WALKTHROUGH
1. Login to SRN and  kill the voffice service with the `Killall -9  voffice` command.

2. Login to the guest vm and disconnect from the iSCSI target:
   * Windows: Disconnect from Iscsi target from Iscsi initiator.
   * Linux: `iscsiadm –m node –u`

3. Login to SRN via SSH.

4. Remove the Iscsi targets:
   * `scstadmin -list_target`
   * Perform the following command with each IQN pasted into the <target name> field: `scstadmin -disable_target <the target name> -driver iscsi`

5. Deactivate the Pluns (logical volumes) for the protection groups:
   * Run `lvscan`.
   * Run `vgchange –an <VG name>` using the volume names, for each volume.
   * Run `lvscan` again to make sure all volumes have been deactivated (lvscan should show all as "inactive"). If you are unable to deactivate a volume, run `kpartx -d /dev/sbd0`. Then `kpartx -d /dev/sbd1` (use all sbd's from 0 onward).

6. Clear all the sbd’s : `sbdAllClear` (or individually clear sbd's: `sbdm /dev/sbd<number> clear` similar to part 3 of Step 5).

7. Clear the bitmaps with `sbdFlushAllBitmaps`.

8. Reboot the SRN.

9. After rebooting the SRN, make sure that the Protection Groups are reconstituted and in "running state" and that the Guest connects to the targets again. On the Production (source) VM, run `DgSyncEx.exe list` from the SafeHaven Tools Command Prompt to make sure sync is intact. Check `lvscan` to make sure that the logical volumes are active, and run `scstadmin –list_target` to verify that the iSCSI targets are being presented.

10. (Optional) Create a new checkpoint.
