{{{
  "title": "Resizing Disks in Linux Virtual Machines",
  "date": "7-24-2014",
  "author": "Luke Bakken",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>Server resource requirements change frequently as environments scale, with storage being the most often re-sized aspect of the environment. The Tier 3 control portal provides a self-service function to accommodate increased storage demands without any reboot necessary. Non-boot and swap disks on a Linux VM will automatically be expanded and have their file systems expanded to reflect expanded storage.</p>

<h3>Steps</h3>
<ol>

<li><p>All compute/storage allocations are managed through the "<strong>Settings</strong>" tab on the Virtual Server view. Once you have clicked "<strong>Settings</strong>", click on the "<strong>Resources</strong>" tab. Once on the "<strong>Resources</strong>"
  tab, you may use the sliders to adjust the appropriate disk allocation. In the following screen shot, the <code>/boot</code> and <code>(swap)</code> disks are highlighted in red by the control portal to show that they will not have their file system
  expanded when the disk size changes.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/s88qmief1inemes/?name=default-disks.PNG" alt="default-disks.PNG" />
</p>
</li>
<li>
<p>To resize the / disk and file system, simply move the slider to the right to your desired disk size:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/mdt0ja1htxe2bzg/?name=resize-root-to-24gb.PNG" alt="resize-root-to-24gb.PNG" />
</p>
</li>
<li>
<p>The disk will be expanded and will have the file system expanded. Once the blueprint completes, you can verify this by using the <code>df -h</code> command:</p>
<code>root@ubuntu12:~# df -h<br />Filesystem Size Used Avail Use% Mounted on<br />/dev/sdc   24G  1.8G 21G   8%   /<br />udev       489M 12K  489M  1%   /dev<br />tmpfs      200M 224K 199M  1%   /run<br />none       5.0M 0    5.0M  0%   /run/lock<br />none       498M 0    498M  0%   /run/shm<br />/dev/sda1  495M 52M  418M  12%  /boot</code>
<p>Output may be slightly different based on your Linux distribution, however, <code>/dev/sdc</code> will always have the root file system on it.</p>
</li>
</ol>
