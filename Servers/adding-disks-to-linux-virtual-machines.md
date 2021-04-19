{{{
  "title": "Adding Disks to Linux Virtual Machines",
  "date": "6-17-2014",
  "author": "Luke Bakken",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>

<p>Server resource requirements change frequently as environments scale, with storage being the most often re-sized aspect of the environment. The Lumen Cloud control portal provides a self-service function to accommodate increased storage demands by allowing you to add disks to your virtual machine. Disks added to a Linux VM will have a file system created as part of the addition process and do not require a server reboot.</p>

<h3>Steps</h3>

<ol>
  <li><p>All compute/storage allocations are managed through the "<strong>Settings</strong>" tab on the Virtual Server view. Once you have clicked "<strong>Settings</strong>", click on the "<strong>Resources</strong>" tab. Once on the "<strong>Resources</strong>" tab, you may use the <strong>"Add Storage Disk"</strong> button to add another disk:</p>
  <p><img src="https://t3n.zendesk.com/attachments/token/bli847kch9laoth/?name=add-storage-disk.PNG" alt="add-storage-disk.PNG" />
  </p>
  </li>
  <li>
  <p>Enter a name for the mount point and move the slider to the right to your desired disk size:</p>
  <p><img src="https://t3n.zendesk.com/attachments/token/elc7wcjvwcv5wie/?name=added-storage-and-sized.PNG" alt="added-storage-and-sized.PNG" />
  </p>
  </li>
  <li>
  <p>When you click <strong>"Save"</strong> the disk will be added. Once the blueprint completes, you can verify by using the <code>df -h</code> command:</p>
  <code>[root@linux-server ~]# df -h<br />Filesystem Size Used Avail Use% Mounted on<br />/dev/sdc   14G  1.1G 13G   9%   /<br />tmpfs      1.9G 0    1.9G  0%   /dev/shm<br />/dev/sda1  495M 57M  414M  12%  /boot<br />/dev/sdd   119G 188M 117G  1%   /data-disk</code>
  <p>Output may be slightly different based on your Linux distribution, however, <code>/dev/sdc</code> will always have the root file system on it.</p>
  </li>
</ol>
