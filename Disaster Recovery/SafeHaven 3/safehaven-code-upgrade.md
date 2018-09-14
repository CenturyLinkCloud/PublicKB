{{{
  "title": "SafeHaven: Code update",
  "date": "5-24-2018",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview:
This document instruct engineers on updating minor released of SafeHaven deployments. Note that major releases (i.e. 3.0 to 3.1) require a complete rebuilt and re-replication of all data.

### Code Version Check
1. Check the current version of the code.

2. ssh as root into the SafeHaven Nodes
   * For SRN’s : In the root directory.
     * Run "cat sbd_version".
  * For SRN and CMS: cd /usr/lib/datagardens
    * Run "cat syntropy_version".
    * Run "cat "utils_version".
    * Run "cat cms_version".

4. Kill the services.
   * ssh as root into the CMS:
     * run killall -9 manager
     * run ps aux |grep manager to make sure manager is not running anymore
   * ssh as root into the SRN:
     * run killall -9 voffice
     * run ps aux |grep voffice to make sure voffice is not running anymore

### Update the Code
1. UPDATE THE SYNTROPY ON THE SAFEHAVEN NODES (CMS and SRN)
    ssh as root into the Nodes:

2. SYNTROPY AND UTILS UPDATE: (NO REBOOT REQUIRED)
   * (.i.e., wget https://www.dropbox.com/s/77jqlocmn12e94b/SafeHaven3.0.1u9_nosbd_05-07-2015_bin.tar.gz?dl=0). Please verify link correspond to the release you are updating.

3. Get the latest syntropy and utils code from dropbox (same as above, ensure that the download matches your release).
   * Run "tar xvfz SafeHaven3.0.1u9_nosbd_05-07-2015_bin.tar.gz?dl=0 –C /" for each binary
   * UPDATE THE SBD ON THE SRN’s (SRN REBOOT REQUIRED - NOT DONE ALWAYS).

### Kernel Version Check
1. ssh as root into the SRN.

2. Check the kernel version on the SRN’s:
   * Run “uname –r” or “uname -a”.
   * The kernel version needs to be 3.13.0-44-generic. Update/downgrade the Kernel Version to 3.13.0-44-generic (apt-get remove linux-kernal-3.13.0-55-generic (or -48-generic) or apt-get install linux-headers-3.13.0-44-generic).
   * Reboot the SRN
   * Run “uname –r” or “uname -a” and verify the kernel version again.
   * NOTE: If the kernel version is later than 3.13.0-44-generic, downgrade it to 3.13.0-44-generic.

### SBD Update
1. Get the latest sbd code from dropbox.
   * wget https://www.dropbox.com/s/knr87xj7s2ik8j1/sbd2_cowonly_13485_kernel_3.13.0-44-generic_bin.tar.gz?dl=0
   * tar xvzf sbd2_cowonly_13056_kernel_3.13.0-44-generic_bin.tar.gz?dl=0 -C /

2. Reboot.
   * Confirm and make sure the sbd can be loaded by running “sbdm version”.

3. Install SCST Services.
   * Get the baseInstaller from dropbox, if it is not there already.
   * wget https://www.dropbox.com/s/ka3c4kb20ybth95/baseInstaller-3.0.1u1.tar.gz?dl=0
   * tar xvfz baseInstaller-3.0.1u1.tar.gz?dl=0
   * cd /baseInstaller/ scst/scst-3.0.0-Ubuntu1404# ./scst_install.sh
   * cd /baseInstaller/scst/scst-3.0.0-Ubuntu1404# service scst restart
   * Confirm scst is working by running “scstadmin –list_target”

### Final Steps:
1. Log in to the CMS.
   * You will be prompted to restart the services before successful login occurs.

2. Once in CMS, restart any stopped SRN services.

3. Verify release version by running "cat /var/syntropy" and "cat /var/utils_version" on each updated SRN and "cat /var/cms_version" on the CMS.

4. Final install Note- the same steps can be completed in a single command by running the same process and untarring the full kernel for the new release rather than running SBD/Syntropy especially. This applies to minor releases, in which bug fixes are more likely to be centered around either component (i.e., using https://www.dropbox.com/sh/b7nkdp0t6uga02k/AACDB_ZwEOLkVGjVkcPumHKSa/SafeHaven3.1.0-GA_full_kernel-3.13.0-44-generic_06-26-2015_bin.tar.gz?dl=0)

RE-CONFIRM THE VERSION OF SYNTROPY AND SBD AGAIN

NOTE: SRN REBOOT CAN HAVE A SERIOUS IMPACT ON THE CUSTOMER’S ENVIRONMENT SO IT IS STRONGLY RECOMMENDED TO PLEASE CONFIRM WITH THE DATAGARDENS TEAM BEFORE REBOOTING THE SRN’s (AT LEAST FOR NOW).

NOTE: DO NOT USE THE DROPBOX LINKS MENTIONED IN THIS DOCUMENT, these are sample 3.0 links. Please check with the SafeHaven team prior to completing this action and do so under strict guidance (though taking a snapshot prior will mitigate any potential risk).

IMPORTANT NOTE: it is very important to run an update-grub command after upgrading/downloading kernels as the scstadmin services are tied to the kernal number and will not function properly if not updated and then rebooted.
