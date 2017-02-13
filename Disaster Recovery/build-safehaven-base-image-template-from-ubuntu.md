{{{
  "title": "SafeHaven 3.0/3.1/3.1.1 - Build a base-image template from scratch using Ubuntu 14",
  "date": "9-21-2015",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview:
This document covers the creation of a SafeHaven 3.0/3.1 base image. This base image, once complete, should be converted to template in both the Production and Disaster Recovery Data Centers so that the appropriate amount of SRN and CMS appliances can be deployed from the source template. The base-image template is the same for either SRN or CMS appliances, they are configured for their particular roles during the post-deployment run of the ClusterConfigurator.exe within the SafeHaven Executable bundle. **Note that these links are valid for the current 3.1 GA release only, and may or may not reflect the most recent codebase.**

### Template Creation:
1. Build a 2 vCPU/4GB vRAM Ubuntu 14 image within the desired data centers.

2. Login via SSH. Run `uname -r` to determine the kernel version. **The desired kernel version for SafeHaven 3.1 is 3.13.0-44 currently**.
   * If the kernel is lower, run:
     `apt-get install linux-image-3.13.0-44-generic linux-headers-3.13.0-44-generic -y`
   * Next run `update-grub` and **reboot**. After reboot, `uname -r` should show the correct kernel.  
   * If the kernel is higher (i.e 3.13.0-83), run:
      `apt-get remove linux-image-3.13.0-83-generic linux-headers-3.13.0-83-generic -y` the output will show you the other installed kernels, which are likely to be lower. If that is the case, repeat the command `apt-get remove linux-image-3.13-XX-generic linux-headers-3.13-XX-generic -y`

   * You may see that the grub has been updated as there are no more linux entries, in which case you must install the .44 image.

   * Run: `apt-get install linux-image-3.13.0-44-generic linux-headers-3.13.0-44-generic -y` and once that is complete, run `update-grub`. Reboot the machine and check that `uname -r` returns
      3.13.0-44 as the current kernel. Note that iSCSI servers are tied to the kernel so if you forget to do this step, you will need to rebuild iSCSI after downgrading the kernel.

3. Download the "base installers" package.
      `https://www.dropbox.com/sh/7837hqfwe31wzrh/AAAcE46WjfNGtgFucXot2t5ha/SH3.1.1-u1/baseInstaller-SafeHaven3.1.1-u1.tar.gz?dl=0`

4. Untar the downloaded file by running:
      `tar xvfz baseInstaller-SafeHaven3.1.1-u1.tar.gz?dl=0` (tar xvz Saf (using tab to autocomplete name should be easier))

5. Remove the downloaded .gz `rm -rf Safehaven-(tab)` (optional).

6. Change to the baseImages folder `cd baseImages`.

7. Run the "install" script for Ubuntu, in this instance it would be:
      `./InstallfromUB14x64.sh`

8. Then run the buildcodes. Both of these scripts should be re-run if you find you have a kernel mismatch down the road, as the builcodes will configure iSCSI services.
      `./buildCodes.Ubuntu1404`

9. Change to your root directory. The fastest way to do this is to issue: the `cd ~` command.

10. Download the full kernel from the SafeHaven links. Current 3.1 GA-June26 release can be found below:
      `wget https://www.dropbox.com/sh/7837hqfwe31wzrh/AACqNounvhwEUeKP8UMBRE4Ma/SH3.1.1-GA-Dec15-2015/SafeHaven3.1.1-GA_full_kernel-3.13.0-44-generic_12-16-2015_bin.tar.gz?dl=0`

11. Extract the archive, ensuring to use the "-C /" flag so that the necessary code will be written/overwritten in an upgrade:
      `tar xvfz SafeHaven3.1.1-GA_full_kernel-3.13.0-44-generic...etc.gz -C /`

12. Reboot your server.

13. Move to the SafeHaven directory: `cd /usr/lib/datagardens`

14. Verify that you are running the expected version of safehaven:
    `cat syntropy_version` and `cat utils_version`. The syntropy and utils version should match on all nodes of the cluster. The results of both of these commands should match the expected output (i.e., Syntropy/utils_version = `SafeHaven3.1.1-GA, DataGardens Inc. 2015`).
