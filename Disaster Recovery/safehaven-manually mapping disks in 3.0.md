{{{
  "title": "SafeHaven 3.0: Manually mapping disks",
  "date": "9-9-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

In SafeHaven 3.0, you may find yourself having to manually map or resync disks. The procedure for doing as such is recommended below:

  1. Open->Start->SafeHaven DraaS...Folder, and select "tools" (while running as administrator)
  2. In the tools menu, type in "DgSyncEX.exe list" which will show the list of source/targe disks and their percentage of replication. If there are disks that are not mapped, or a percentage that is less than 100%, the process must be completed.
  3. First, login to your production VM, and open up the aforementioned SafeHaven Tools program.
  4. Run "DgSynxEx.exe list" to verify the sync progress and health status.
  5. To manually start the disk sync, simply type "DgSyncEx.exe start"
  6. If you find that all your disks must be remapped, you can run the dgcleandiskpairs.bat to remove them all and start over again.
  7. If you sync has partially finished, than you may need to run a storage/check and repair, which is done with the following commands:
    1. DgSyncEx.exe list
    2. DgSyncEx.exe select disk 0
    3. DgSyncEx.exe enable read
    4. DgSyncEx.exe start check

If you should find yourself required to map Individual disks manually (i.e. if there are more than 5 disks which is the max shown in the GUI, then you will need to map them with the command line. This is done through the same tools menu, in the this case we are mapping disk 5 to disk 11- though it is always highly recommended that you verify which disks are being mapped by comparing the contents of disk manager (diskmgmt.msc)).

    1. dgdisksmap 5 11
    2. dgsyncex.exe rescan
    3. dgsyncex.exe select disk 5
    4. dgsyncex.exe set rate 81920

The sync rate command governs the speed at which writes are mirrored to the local cache or local replica, depending on the Protection Type used within a given Protection Group.

Clearing existing mapping can be accomplished by running the "cleanalldiskpairs.bat" files under the SafeHaven tools menu or by removing the appropriate registry key:

  HKLM->SYSTEM->CurrentControlSet->Services->DgRplct->PairList

  Delete Pair X (first two keys after default are disk numbers)

### Warning
  
  IMPROPERLY MAPPING DISKS HAVE THE POTENTIAL TO OVERWRITE PRODUCTION DISKS WITH THE CONTENTS OF OTHER DISKS. ENSURE THAT YOUR DISK MAPPING HAS BEEN VALIDATED IN DISK MANAGER (diskmgmt.msc) OR THAT THIS ACTION IS BEING SUPERVISED BY SAFEHAVEN ENGINEERING OR ONBOARDING ENGINEERING.
