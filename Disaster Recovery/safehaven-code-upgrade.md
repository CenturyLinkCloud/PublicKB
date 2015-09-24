{{{
  "title": "SafeHaven: Code update",
  "date": "9-9-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview:
This document will instruct engineers on updating minor released of SafeHaven deployments. Not that major releases (i.e. 3.0 to 3.1 will require a complete rebuilt and re-replication of all data)

### Walkthrough:
  1. ###### CHECK THE CURRENT VERSION OF THE CODE
  2. ssh as root into the SafeHaven Nodes
    1. For SRN’s : In the root directory
    2. Run "cat sbd_version"
  3. For SRN and CMS: cd /usr/lib/datagardens
    1. Run "cat syntropy_version"
    2. Run "cat "utils_version"
    3. Run "cat cms_version"
  4. KILL THE SERVICES
    1. ssh as root into the CMS:
    2. run killall -9 manager
    3. run ps aux |grep manager to make sure manager is not running anymore
    4. ssh as root into the SRN:
    5. run killall -9 voffice
    6. run ps aux |grep voffice to make sure voffice is not running anymore

  1. ###### UPDATE THE CODE
    1. UPDATE THE SYNTROPY ON THE SAFEHAVEN NODES (CMS and SRN)
    ssh as root into the Nodes:
    2. SYNTROPY AND UTILS UPDATE: (NO REBOOT REQUIRED)
    3. (.i.e wget https://www.dropbox.com/s/77jqlocmn12e94b/SafeHaven3.0.1u9_nosbd_05-07-2015_bin.tar.gz?dl=0) - Please verify link correspond to the release you are updating.
    3. Get the latest syntropy and utils code from dropbox (same as above, ensure that the download matches your release)
    4. Run "tar xvfz SafeHaven3.0.1u9_nosbd_05-07-2015_bin.tar.gz?dl=0 –C /" for each binary
    5. UPDATE THE SBD ON THE SRN’s (SRN REBOOT REQUIRED - NOT DONE ALWAYS)

  1. KERNEL VERSION CHECK:
    1. ssh as root into the SRN:
    2. Check the kernel version on the SRN’s:
    3. Run “uname –r” or “uname -a”
    4. The kernel version needs to be 3.13.0-44-generic.
    Update/downgrade the Kernel Version to 3.13.0-44-generic (apt-get remove linux-kernal-3.13.0-55-generic (or -48-generic) or apt-get install linux-headers-3.13.0-44-generic)
    5. Reboot the SRN
    6. Run “uname –r” or “uname -a” and verify the kernel version again
NOTE: If the kernel version is later than 3.13.0-44-generic, downgrade it to 3.13.0-44-generic.

###### SBD UPDATE:
  1. Get the latest sbd code from dropbox
  2. wget https://www.dropbox.com/s/knr87xj7s2ik8j1/sbd2_cowonly_13485_kernel_3.13.0-44-generic_bin.tar.gz?dl=0
  3. tar xvzf sbd2_cowonly_13056_kernel_3.13.0-44-generic_bin.tar.gz?dl=0 -C /
  4. Reboot and confirm and make sure the sbd can be loaded by running “sbdm version”
  5. INSTALL SCST SERVICE:
  6. Get the baseInstaller from dropbox if it is not there already
  7. wget https://www.dropbox.com/s/ka3c4kb20ybth95/baseInstaller-3.0.1u1.tar.gz?dl=0
  8. tar xvfz baseInstaller-3.0.1u1.tar.gz?dl=0
  9. cd /baseInstaller/ scst/scst-3.0.0-Ubuntu1404# ./scst_install.sh
  10. cd /baseInstaller/scst/scst-3.0.0-Ubuntu1404# service scst restart
  11. Confirm scst is working by running “scstadmin –list_target”

### Final Steps:
  1. Log in to the CMS, where you will be prompted to restart the services before successful login will occur.
  2. Once in CMS, restart any stopped SRN services.
  3. Verify release version by running "cat /var/syntropy" and "cat /var/utils_version" on each updated SRN and "cat /var/cms_version" on the CMS.

  Final install Note- the same steps can be completed in a single command by running the same process and untarring the full kernel for the new release rather than running SBD/Syntropy especially. This will apply to minor releases, wherein bug fixes are more likely to be centered around either component (i.e. using https://www.dropbox.com/sh/b7nkdp0t6uga02k/AACDB_ZwEOLkVGjVkcPumHKSa/SafeHaven3.1.0-GA_full_kernel-3.13.0-44-generic_06-26-2015_bin.tar.gz?dl=0)

RE-CONFIRM THE VERSION OF SYNTROPY AND SBD AGAIN
NOTE: SRN REBOOT CAN HAVE A SERIOUS IMPACT ON THE CUSTOMER’S ENVIRONMENT SO IT IS STRONGLY RECOMMENDED TO PLEASE CONFIRM WITH THE DATAGARDENS TEAM BEFORE REBOOTING THE SRN’s (AT LEAST FOR NOW).
NOTE: DO NOT USE THE DROPBOX LINKS MENTIONED IN THIS DOCUMENT, these are sample 3.0 links. Please check with the SafeHaven/Onboarding team prior to completing this action and do so under strict guidance (though taking a snapshot prior will mitigate any potential risk).

IMPORTANT NOTE: it is very important to run an update-grub command after upgrading/downloading kernels as the scstadmin services are tied to the kernal number and will not function properly if not updated and then rebooted.
