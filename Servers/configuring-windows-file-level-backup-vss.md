{{{
  "title": "Configuring Windows File-level Backup (VSS)",
  "date": "10-26-2021",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>Microsoft's Volume Shadow Copy Service (VSS) is a framework which allows for&nbsp;backup operations to be performed without interrupting operations&nbsp;and generally does not cause perceivable performance degradation. While there are limitations and
  best-practices for VSS (i.e. high transaction environments, locked files, or non-VSS aware applications) the VSS service is a simple and effective way to provide an additional layer of granular protection and self-service restore operations. The most
  common use case for VSS is enabling revision history and backup for file servers. This article will demonstrate the configuration of both backup and restores on Windows Server 2008. The same principles apply to all versions of Windows Server and Desktop
  operating systems.</p>
<p><strong>While VSS is a powerful tool for retaining file versions, it is not a full-featured backup solution! It is meant to augment your overall backup strategy, but is NOT a technology that should be solely relied upon for enterprise backup and recovery. The Lumen Cloud's team of Solution Architects can assist in building an&nbsp;</strong><strong>encompassing backup and Disaster Recovery solution to meet your business requirements.</strong>
</p>
<p>To enable VSS, open Windows Explorer and browse to the volume you wish to protect. Right-click the volume and select “Properties.” You will see a tab entitled “Shadow Copies.”</p>

<p>By default, VSS is disabled. Click the “Enable” button to begin- an information dialog box will appear, to continue enabling VSS, select the “Yes” option. It is important to heed the warning presented by Microsoft, echoing the use cases outlined in this
  introduction of this article: <strong>“The default settings are not appropriate for servers that have high I/O load. For heavily used servers, you should manually configure shadow copies and place the storage area on a volume that will not be shadow copied”. </strong>Again,
  if you require a backup solution for a high-performance server, The Lumen Cloud's Solution Architects can assist you in designing an appropriate backup solution.</p>

<p>Once you have clicked “Yes”, you will see a time stamp noting the first successful shadow copy. By clicking the “Settings” button, you can configure both the storage limits as well as the snapshot schedule. The default configuration does not have a storage
  limit and takes snapshots at 7:00A.M and 12:00P.M.</p>
<p>To set a storage limit, select the “Use Limit” radio button and input an integer value for the size limit (in megabytes). You can use the “Details” button if you would like to specify a separate volume for VSS snapshot storage. In this example, we limit
  the consumption to 2GB.</p>

<p>Use the “Schedule” button to adjust the default schedules. In the initial view, you can change the two pre-defined schedules. Create additional schedules using the “New” button, or delete existing schedules using the “Delete” button.</p>

<p>If you would like to change the snapshot frequency, click the “Advanced” button, and check the “Repeat Task” checkbox. In this example, we will take VSS snapshots every 15 minutes during business hours.</p>

<p><strong>Performing a restore:</strong>
</p>
<p>To perform a restore of a deleted or modified file, right-click on the parent folder and select “Properties.” Navigate to the “Previous Versions” tab.</p>

<p>From this dialog, you can either open the folder to restore individual files or sub-folders, or restore the entire folder. If you wish to restore a single file, select “Open” and then copy and paste the previous version of the desired file to a new location.</p>
<p>If you wish to restore the entire folder- you will be presented with a warning. <strong>Please proceed with caution as the restore operation will replace the current version of the folder on your machine.</strong>
</p>
