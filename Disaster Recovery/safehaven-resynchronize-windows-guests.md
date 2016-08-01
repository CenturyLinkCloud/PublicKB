{{{
  "title": "SafeHaven: Resynchronize Windows Guests",
  "date": "07-13-2016",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Article Overview
Sometimes, due to improper error states or corruption, it may be necessary to resychronize Production data. Rather than rebuilding the protection group, there is an easy way to accomplish this using the built-in SafeHaven "Tools" prompt.

### Detailed Steps

1. Open the "Tools" prompt under the Start Menu-> "SafeHaven DRaaS..." folder.

2. Open the DgSyncEx.exe prompt by typing `DgSyncEx.exe`. Press Enter. (Typing dgs and pressing the tab key should also auto-complete the command).

3. In the DgSyncEx prompt, type `select disk 0`.

4. Type `set progress 0`.

5. Repeat the same for disk 1, 2, or any other remaining Production disk. (Note that one does not select the replica iSCSI disks.)

6. Type `sync report` for a detailed view of the resynchronization progress (or `DgSyncEx.exe sync report` if prompt exited). When all disks reach 100%, confirm that they are in a clean state by issuing the `list` command from the prompt or `DgSyncEx.exe list` in a new tools prompt.
