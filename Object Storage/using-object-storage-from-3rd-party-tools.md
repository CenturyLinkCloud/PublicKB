{{{
  "title": "Using Object Storage from 3rd Party Tools",
  "date": "12-2-2015",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
CenturyLink Cloud now has a robust, geo-distributed Object Storage service capable of storing any type of digital content. Perfect for data backups, media distribution, and file transfers, the Object Storage is Amazon S3-compatible and accessible from the Control Portal or via API. CenturyLink Cloud Object Storage is Amazon S3 compatible, which means that a host of tools are readily available for maintaining buckets and interacting with bucket objects.

### Audience
* Bucket Administrators
* Object Administrators
* Developers

### Prerequisites
* Have already created an Object Storage user account in the Control Portal
* Have already created a new bucket or have access permissions to an existing bucket

### Using Cloudberry Explorer for Amazon S3
[Explorer for Amazon S3](http://www.cloudberrylab.com/) is a freeware tool for Windows (a paid version also available) that works with CenturyLink Cloud Object Storage.

1. [Download and Install a copy of Explorer for S3.](http://www.cloudberrylab.com/free-amazon-s3-explorer-cloudfront-IAM.aspx)

2. In the Control Portal, navigate to the Object Storage service and view the user record that you want to configure Explorer for Amazon S3 with. Copy/save the **access key id** and **secret access key**.

    ![object storage users control](../images/using-object-storage-from-3rd-party-tools-06.png)

3. Capture the service point for object storage.  They are as follows:

    * Canada: canada.os.ctl.io

4. Back in Explorer for Amazon S3, click the **File, New S3 Compatible Account** menu option in order to add the connection details for Object Storage.

    ![new s3 compatible account](../images/using-object-storage-from-3rd-party-tools-01.png)

5. Specify name, service point, access and secret keys to register the new S3 Compatible Storage account.

    ![s3 compatible account input](../images/using-object-storage-from-3rd-party-tools-02.png)

6. Return to the Explorer for Amazon S3 main window and using the drag and drop model of the software (or the Copy command) upload data to Object Storage.

    ![cloudberry bucket list](../images/using-object-storage-from-3rd-party-tools-03.png)

    ![cloudberry copy UI](../images/using-object-storage-from-3rd-party-tools-04.png)

7. Permissions can be applied at both the bucket and object level. Customers should review the documentation for information on apply ACL policies.

    ![cloudberry ACLs](../images/using-object-storage-from-3rd-party-tools-05.png)

8. Explorer for Amazon S3 also lets users download objects, delete objects, view bucket/object properties, and preview objects.

### Using CyberDuck on Mac OS X
[CyberDuck](//cyberduck.io/?l=en) is a freeware product for Mac OS X (paid version also available) that works with CenturyLink Cloud Object Storage.

1. [Download a copy of CyberDuck for OS X](//update.cyberduck.io/Cyberduck-4.7.2.zip) from the product website.

2. Install CyberDuck and run the program. It looks like this when it starts up without any **Connections** (aka: Service Points or Servers) configured.

    ![cyberduck new install](../images/cyberduck-new-install.png)

3. In the Control Portal, navigate to the Object Storage service and view the user record that you want to configure CyberDuck to use. Record the **Access Key ID** and the **Secret Access Key** for use in the tool.

    ![object storage user record edited](../images/object-storage-user-record-edited.png)

4. Also you will need the **Service Point** (aka server) where your bucket exists (or will exist). In the Control Portal, on the Object Storage bucket listing page, either create a new bucket, or click on an existing bucket. When the **Bucket Info and Settings** page is displayed, copy/save the portion of the **bucket URL** that follows the bucket name. In this example, the bucket **Service Point** (server name) is: **canada.os.ctl.io**

    ![object storage bucket info](../images/object-storage-bucket-info-and-settings.png)

5. Back in CyberDuck, click the **Open Connection** icon (upper left corner) in order to configure the connection details for your Object Storage bucket. Select **S3 (Amazon Simple Storage)** from the drop down. In the **Server** field, enter the name of the **Service point**. Leave Port field set to **443**. Populate the **Username** field with your **Access Key ID** and populate the **Password** field with your **Secret Access key**.

    ![cyberduck setup connection](../images/cyberduck-setup-connection.png)

6. After you have configured the Object Storage connection, CyberDuck will list the available buckets at that **Connection**. You can double-click on a bucket to upload files or even drag-and-drop files into the bucket.

    ![cyberduck established connection](../images/cyberduck-established-connection.png)

7. Now that CyberDuck is configured to quickly connect to your CenturyLink Cloud Object Storage account and access the stored buckets, you should bookmark the account for easy access. Click the **Bookmark icon** to navigate to the Bookmark page.

    ![cyberduck bookmark page](../images/cyberduck-bookmark-page.png)

8. Click the **Add Connection button** to add this Object Storage account to your Bookmarks.

    ![cyberduck bookmark added](../images/cyberduck-bookmark-added.png)

9. Permissions can be applied at both the bucket and object level. A user could have **FULL ACCESS** rights for the bucket (and thus be able to add and remove objects) but only have **READ** rights to an individual object (and therefore couldn't update that object).

    ![cyberduck bucket permissions](../images/cyberduck-bucket-permissions.png)

    ![cyberduck object permissions](../images/cyberduck-object-permissions.png)
