{{{
  "title": "Using Object Storage from 3rd Party Tools",
  "date": "1-7-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>CenturyLink Cloud now has a robust, geo-distributed Object Storage service capable of storing any type of digital content. Perfect for data backups, media distribution, and file transfers, the Object Storage is Amazon S3-compatible and accessible from
  the Control Portal or via API. <strong>This KB article explains how to interact with Object Storage from 3rd party tools.</strong>
</p>
<h3>Audience</h3>
<ul>
  <li>Bucket Administrators</li>
  <li>Object Administrators</li>
  <li>Developers</li>
</ul>
<h3>Using Explorer for Amazon S3&nbsp;on Windows</h3>
<p>CenturyLink Cloud Object Storage is Amazon S3 compatible which means that a host of tools are readily available for maintaining buckets and interacting with bucket objects. <a href="http://www.cloudberrylab.com/">Explorer for Amazon S3</a>&nbsp;is
  a freeware product (that also has a paid version) that works with CenturyLink Cloud Object Storage.</p>
<ul>
  <li><a href="http://www.cloudberrylab.com/free-amazon-s3-explorer-cloudfront-IAM.aspx">Download a copy of Explorer for S3</a> from their product website.</li>
  <li>Install Explorer for Amazon S3 and run the program.
    <p><img src="https://t3n.zendesk.com/attachments/token/hk3EDH82esD9JlHc0XaJ1tCI6/?name=01.png" alt="01.png" />
    </p>
  </li>
  <li>In the Control Portal, navigate to the Object Storage service and view the user record that you plan to configure Explorer for Amazon S3 with. Record the&nbsp;<strong>access key id&nbsp;</strong>and&nbsp;<strong>secret access key</strong>&nbsp;for use
    in the tool.
    <p><img src="https://t3n.zendesk.com/attachments/token/fEYdYbXwcrEGGkfJBtavv318U/?name=02.png" alt="02.png" />
    </p>
  </li>
  <li>Back in Explorer for Amazon S3, click the <strong>File, S3 Compatible</strong> menu option in order to add the connection details for Object Storage.</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/87ta5NWRhlj7cmk0WlGlC84vX/?name=01.png" alt="01.png" /></p>
<ul>
  <li>Enter a friendly name in the&nbsp;<strong>Display Name&nbsp;</strong>field (this does not correspond to any value in CenturyLink Cloud Object Storage), and populate the <strong>Service Point</strong>,&nbsp;<strong>Access Key ID&nbsp;</strong>and&nbsp;<strong>Secret Access Key</strong>    fields with the corresponding values from the Control Portal.
    <p><img src="https://t3n.zendesk.com/attachments/token/QqoxEfC8rImNPstoke3KDODmj/?name=03.png" alt="03.png" />
    </p>
  </li>
  <li>
    <p>Return to the Explorer for Amazon S3 main window and change <strong>Source</strong> to the newly Created Storage Account. Using the drag and drop model of the software or use the Copy command to Upload data to Object Storage.</p>
  </li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/9BDZDWtOfEbqPvaJ64pHAvmI0/?name=05.png" alt="05.png" />
</p>
<ul>
  <li>Permissions can be applied at both the bucket and object level. A user could have "read" rights for the bucket (and thus be able to list objects) but NOT have "read" rights to an individual object (and therefore couldn't open that object).</li>
</ul>
<p><img src="https://t3n.zendesk.com/attachments/token/Cv1ndjweYcJSSc0lMoZgLdpT9/?name=06.png" alt="06.png" />
</p>
<ul>
  <li>Explorer for Amazon S3 also lets users download objects, delete objects, view bucket/object properties, and preview objects.</li>
</ul>