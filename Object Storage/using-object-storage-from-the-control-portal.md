{{{
  "title": "Using Object Storage from the Control Portal",
  "date": "1-7-2015",
  "author": "Richard Seroter",
  "attachments": []
}}}

<h3>Description</h3>
<p>Tier 3 now has a robust, geo-distributed Object Storage service capable of storing any type of digital content. Perfect for data backups, media distribution, and file transfers, the Tier 3 Object Storage is Amazon S3-compatible and accessible from the
  Tier 3 Control Portal or via API. &nbsp;<strong>This KB article explains how to interact with Object Storage from the Tier 3 Control Portal.</strong>
</p>
<h3>Audience</h3>
<ul>
  <li>Bucket Administrators</li>
</ul>
<h3>Actions Supported in the Tier 3 Control Portal</h3>
<p>Below, each action available in the Control Portal is explained and demonstrated.</p>
<h4>Create Object Storage Users</h4>
<ol>
  <li>Navigate to Object Storage from the top navigation menu.
    <p><img src="https://t3n.zendesk.com/attachments/token/ym2it3jg0o4gtr4/?name=objectstorage-control01.png" alt="objectstorage-control01.png" />
    </p>
  </li>
  <li>On the Object Storage page, switch to the&nbsp;<strong>Users</strong> tab.
    <p><img src="https://t3n.zendesk.com/attachments/token/ilqiwxbdk0srypc/?name=objectstorage-control02.png" alt="objectstorage-control02.png" />
    </p>
  </li>
  <li>Click the&nbsp;<strong>create user</strong> button and enter the user's details. The <strong>name</strong> field should contain a friendly alphanumeric identifier for the user. Enter an&nbsp;<strong>email&nbsp;</strong>address for the user. Note that
    this value must be unique across the platform and can't be reused. &nbsp;Additionally, this email can be a bogus and non-functional email. We don't use this email for anything except to assure uniqueness. &nbsp;You will not be contacted using this
    email. Finally, choose which Object Storage region to add this user to. Click&nbsp;<strong>save</strong>.
    <p><img src="https://t3n.zendesk.com/attachments/token/xpcaevihuzwhyji/?name=objectstorage-control03.png" alt="objectstorage-control03.png" />
    </p>
  </li>
  <li>Click the created user record to view the&nbsp;<strong>access key id&nbsp;</strong>and&nbsp;<strong>secret access key&nbsp;</strong>values which act as the username and password for this Object Storage user.
    <p><img src="https://t3n.zendesk.com/attachments/token/m0yxppkprm3yemx/?name=objectstorage-control04.png" alt="objectstorage-control04.png" />
    </p>
  </li>
</ol>
<h4>&nbsp;</h4>
<h4>Reset Object Storage User Key</h4>
<ol>
  <li>Navigate to the record for the chosen Object Storage user.</li>
  <li>Click the <strong>reset user key</strong> button.
    <p><img src="https://t3n.zendesk.com/attachments/token/tjytdkntw0sskhw/?name=objectstorage-control05.png" alt="objectstorage-control05.png" />
    </p>
  </li>
  <li>Refresh the page to see the new&nbsp;<strong>secret access key</strong>.&nbsp;</li>
</ol>
<h4>&nbsp;</h4>
<h4>Create a New Object Storage Bucket and View Bucket Details</h4>
<ol>
  <li>Navigate to the Object Storage service page and locate the&nbsp;<strong>Buckets</strong> tab. Click the&nbsp;<strong>create bucket&nbsp;</strong>button.
    <p><img src="https://t3n.zendesk.com/attachments/token/20uwulrzexej84r/?name=objectstorage-control06.png" alt="objectstorage-control06.png" />
    </p>
  </li>
  <li>Enter a&nbsp;<strong>bucket name</strong> value.The name has to start and end with lowercase letters or numbers, and can only contain lowercase letter, numbers, dashes, and dots. This value must be unique across the entire region. Next, select an&nbsp;<strong>owner&nbsp;</strong>from
    the list of Object Storage users created in the account. The owner is an important decision as the API retrieves lists of buckets by the owner name. Click the&nbsp;<strong>save&nbsp;</strong>button to create the bucket. If the name of the bucket is
    not unique, you will receive an alert asking you to choose a new bucket name.
    <p><img src="https://t3n.zendesk.com/attachments/token/qxax5zp3r4u8922/?name=objectstorage-control07.png" alt="objectstorage-control07.png" />
    </p>
  </li>
  <li>View the list of all buckets created by all users in this Tier 3 account. Note that for each item in the list below, you can see the name of the bucket, the owner of the bucket (in the text below the bucket name), the region of the bucket, size of the
    bucket, and estimated cost of the bucket.
    <p><img src="https://t3n.zendesk.com/attachments/token/t0stb2nc9fxxyyn/?name=objectstorage-control08.png" alt="objectstorage-control08.png" />
    </p>
  </li>
  <li>Click on a bucket name to view the details of the bucket. This page shows read-only details such as the bucket name, owner, region and API URL. It also contains the list of active permissions associated with the bucket.
    <p><img src="https://t3n.zendesk.com/attachments/token/ysyk1pasfkusxod/?name=objectstorage-control09.png" alt="objectstorage-control09.png" />
    </p>
  </li>
</ol>

<h4>Manage Object Storage Permissions</h4>
<ul>
  <li>View the details for an individual bucket.</li>
  <li>Click the&nbsp;<strong>permissions&nbsp;</strong>section to activate the&nbsp;<strong>customize permissions</strong> view.
    <p><img src="https://t3n.zendesk.com/attachments/token/djembukgimufntu/?name=objectstorage-control10.png" alt="objectstorage-control10.png" />
    </p>
  </li>
  <li>Click&nbsp;<strong>add grantee</strong> to update the Access Control List (ACL) for this bucket. This list shows all of the users in this Tier 3 account, and two built in groups,&nbsp;<strong>All Users&nbsp;</strong>and&nbsp;<strong>Authenticated Users</strong>.
    When you add&nbsp;<strong>All Users</strong> to a bucket -- and give it read permissions -- you are giving public Internet access to the bucket. If you add the&nbsp;<strong>Authenticated Users&nbsp;</strong>group to the bucket, then any Object Storage
    user can access the bucket.
    <p><img src="https://t3n.zendesk.com/attachments/token/ivmmb4xsodl5ynt/?name=objectstorage-control11.png" alt="objectstorage-control11.png" />
    </p>
  </li>
  <li>For any existing user, you can modify their permissions by selecting/de-selecting checkboxes associated with each permission. Note that the bucket owner always has full control. To delete the user from the grantee list, click the red "x" at the far
    right of the record. Changes made to a bucket are instantly committed. For instance, if you add&nbsp;<strong>All Users</strong> with read permissions, then the buckets (and contained objects) are immediately available to anyone. Likewise, if you use
    a 3rd party tool to manage Object Storage, changes to the grantee list are instantly visible in the Control Portal.
    <p><img src="https://t3n.zendesk.com/attachments/token/lbwk8yusxor66tb/?name=objectstorage-control12.png" alt="objectstorage-control12.png" />
    </p>
  </li>
</ul>

