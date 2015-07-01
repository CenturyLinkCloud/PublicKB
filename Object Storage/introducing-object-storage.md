{{{
  "title": "Introducing Object Storage",
  "date": "1-7-2015",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Description</h3>
<p>CenturyLink Cloud now has a robust, geo-distributed Object Storage service capable of storing any type of digital content. Perfect for data backups, media distribution, and file transfers, the CenturyLink Cloud Object Storage is Amazon S3-compatible and accessible from the
  CenturyLink Cloud Control Portal or via API.</p>
<h3>Audience</h3>
<ul>
  <li>All Users</li>
</ul>
<h3>FAQ</h3>
<p><strong>Q: &nbsp;Is this software home-grown or is this based on a commercial product?</strong>
</p>
<p><strong>A:&nbsp;</strong>CenturyLink Cloud Object Storage is based on <a href="http://basho.com/riak-cloud-storage/">Riak CS Enterprise</a> from Basho and will be deployed across CenturyLink Cloud data centers.</p>
<div></div>
<p><strong>Q: &nbsp;What are the key vocabulary terms for Object Storage?</strong>
</p>
<p><strong>A: </strong>Object storage is deployed in a series of "regions" which include data centers for each CenturyLink Cloud geography (US, Canada, Europe). Note that as of this time, Object Storage is only available in Canada.&nbsp;Object Storage uses "buckets"
  to hold "objects." Buckets are flat (no hierarchy) and can contain an unlimited number of objects and unlimited amount of storage. "Access Control Lists" (ACLs) describe permissions to a bucket and the objects within it. Object Storage "users" are associated
  with a given region and have an "access key ID" and "secret access key" which act as the user's username and password for accessing storage.</p>
<div></div>
<p><strong>Q: &nbsp;How do Object Storage users relate to CenturyLink Cloud users?</strong>
</p>
<p><strong>A:&nbsp;</strong>Object Storage users are distinct from CenturyLink Cloud users, but all reside under CenturyLink Cloud accounts. A CenturyLink Cloud user may create multiple Object Storage users that have different access to their buckets. For example, you can create "application
  users" that a web application uses to retrieve objects from buckets.</p>
<div></div>
<p><strong>Q: &nbsp;What kind of data belongs in Object Storage?</strong>
</p>
<p><strong>A:</strong> Object Storage is for key-value data. It is a schema-less repository that can store large objects (up to 5 GB) and is perfect for archive data, Microsoft Office documents and more.</p>
<div></div>
<p><strong>Q: Do I need to replicate my data between data centers?</strong>
</p>
<p><strong>A</strong>: No. Objects uploaded to Object Storage are automatically replicated between data centers in a given region. Object Storage is accessed through a domain that is geo-aware and will route you to the closest data center that has
  your data.</p>
<div></div>
<p><strong>Q: How available is my data within a given data center?</strong>
</p>
<p><strong>A:&nbsp;</strong>Each data center contains a "ring" of servers that maintain copies of the objects. If any server fails, there is no interruption of service as the servers simply re-balance and distribute the objects evenly across the remaining
  servers in the ring. This provides a very high availability of data within a given data center.</p>
<div></div>
<p><strong>Q: How do I interact with Object Storage?</strong>
</p>
<p><strong>A:&nbsp;</strong>Bucket Administrators can use the CenturyLink Cloud Control Portal to create users, create buckets, and secure buckets. Object users and developers have their choice of numerous best-of-breed tools for interfacing with objects.</p>
<div></div>
<p><strong>Q: So what exact do I do in the Control Portal vs. 3rd party tools?</strong>
</p>
<p><strong>A</strong>: The following breakdown explains what is available in the Control Portal and what you should use 3rd party tools for:</p>
<table>
  <tbody>
    <tr>
      <th>Capability</th>
      <th>Control Portal</th>
      <th>3rd Party Tool</th>
    </tr>
    <tr>
      <td>&nbsp;Create user</td>
      <td>&nbsp;x</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;List all buckets for user</td>
      <td>&nbsp;x</td>
      <td>&nbsp;x</td>
    </tr>
    <tr>
      <td>&nbsp;Create a bucket</td>
      <td>&nbsp;x</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Delete a bucket</td>
      <td>&nbsp;x</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;View bucket ACLs (permissions)</td>
      <td>&nbsp;x&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Set bucket ACLs (permissions)</td>
      <td>&nbsp;x</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;See bucket region</td>
      <td>&nbsp;x&nbsp;</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;See bucket owner name</td>
      <td>&nbsp;x&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Add object to bucket</td>
      <td>&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Delete object in bucket</td>
      <td>&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;View object ACLs (permissions)</td>
      <td>&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Set object ACLs (permissions)&nbsp;</td>
      <td>&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
    <tr>
      <td>&nbsp;Do multi-part upload for large objects</td>
      <td>&nbsp;</td>
      <td>x&nbsp;</td>
    </tr>
  </tbody>
</table>
<p><strong>Q: Can I list all the buckets that I have access to, even if I'm not the owner?</strong>
</p>
<p><strong>A</strong>: No. The Object Storage API for retrieving bucket lists only returns buckets where the user is the owner. Users can use the Control Portal to view buckets across all users in an account.</p>
<div></div>
<p><strong>Q: What are those built-in role types (All Users, Authenticated Users) for?</strong>
</p>
<p><strong>A</strong>: These built in ACLs make it easy to share access with a broad population. While you can add individual users to your bucket -- and those users can then interface with that bucket via the API -- you also may want to make a bucket (or
  object) public by giving "All Users" a "Read" permission. This would let public Internet users list the contents of a bucket or view an individual object. The "Authenticated Users" ACL lets any user with a valid Object Storage access key ID interact
  with the selected object.</p>
