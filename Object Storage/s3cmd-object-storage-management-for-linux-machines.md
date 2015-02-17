{{{
  "title": "S3CMD - Object Storage Management for Linux Machines",
  "date": "10-27-2014",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>S3CMD is a Linux utility that can be used to interact and manage your <a href="http://www.tier3.com/products/object-storage" target="_blank">CenturyLink Cloud Object Storage</a> buckets. While S3CMD is included in many package managers, it is best to manually configure
  the official repository to ensure that you are using the latest version.</p>
<p>First, you will need to create a user and object storage bucket from within the CenturyLink Cloud Control Portal:</p>
<ol>
  <li>Navigate to “Object Storage” under the “Services” tab of <a href="https://control.tier3.com/">https://control.tier3.com</a>
  </li>
  <li>Click “Create User” and fill out the required fields.
    <a><img src="https://t3n.zendesk.com/attachments/token/9hcvz1o9trzgsjt/?name=bucketusercreation.JPG" alt="bucketusercreation.JPG" />
    </a>
  </li>
  <li>Switch to the “Buckets” tab and click “Create Bucket”. Enter the bucket name and select the owner from the drop-down menu. If you need to add additional users or modify the permissions, you can click on the buck et name after it has been generated to
    make said modifications.</li>
</ol>
<p>
  <a><img src="https://t3n.zendesk.com/attachments/token/mo4fnodxuvhzhpk/?name=bucketcreation.JPG" alt="bucketcreation.JPG" />
  </a>
</p>
<p><strong>To add the repository to a CentOS or RHEL machine</strong> (note, both instructions assume you are running as root- you will need to add “sudo” where appropriate if not logged in as root):</p>
<ol>
  <li>Install wget if not already installed by entering the command: <strong>yum install wget&nbsp;–y</strong>
  </li>
  <li>Enter the command: <strong>cd /etc/yum.repos.d</strong>
  </li>
  <li>Download the appropriate file for your distribution:</li>
  <ol>
    <li>For CentOS/RHEL 5 enter the command “<strong>wget </strong><a href="http://s3tools.org/repo/CentOS_5/s3tools.repo"><strong>http://s3tools.org/repo/RHEL_5/s3tools.repo</strong></a>” (without quotes)</li>
    <li>For CentOS/RHEL 6 enter the command “<strong>wget </strong><a href="http://s3tools.org/repo/RHEL_6/s3tools.repo"><strong>http://s3tools.org/repo/RHEL_6/s3tools.repo</strong></a>” (without quotes)</li>
  </ol>
  <li>Enter the command: <strong>yum install s3cmd -y</strong>
  </li>
</ol>
<p><strong>To add the repository to a Ubuntu/Debian machine:</strong>
</p>
<ol>
  <li>Install wget&nbsp;if not already installed by entering the command: <strong>apt-get install wget&nbsp;–y</strong>
  </li>
  <li>Import the signing key by entering the command: <strong>wget -O - -q http://s3tools.org/repo/deb-all/stable/s3tools.key | apt-key add -</strong>
  </li>
  <li>Add the repository by entering the command: <strong><strong>wget -O/etc/apt/sources.list.d/s3tools.list&nbsp;</strong><a href="http://s3tools.org/repo/deb-all/stable/s3tools.list"><strong>http://s3tools.org/repo/deb-all/stable/s3tools.list</strong></a>
    </strong>
  </li>
  <li>Refresh your packages and install by entering the command: <strong>apt-get update &amp;&amp; apt-get install s3cmd</strong>
  </li>
</ol>

<h5>Once S3CMD has been installed, it must be configured to use CenturyLink Cloud’s Object Storage:</h5>
<ol>
  <ol>
    <li>S3CMD stores its settings in a configuration file. You can either run s3cmd&nbsp;–configure&nbsp;to launch an interactive&nbsp;configuration generation tool, or specify a&nbsp;pre-existing file.&nbsp;You will be prompted for both your Access Key&nbsp;and
      your Secret Key, which can be found by clicking on the appropriate username in the CenturyLink Cloud Control Panel, under the Services-&gt; Object Storage Section.</li>
    <li>
      <a><img src="https://t3n.zendesk.com/attachments/token/wzvex9kpccjeuge/?name=bucketsecret.JPG" alt="bucketsecret.JPG" />
      </a>
    </li>
    <li>Enter your encryption password.</li>
    <li>Hit enter as the default path to gpg should be correct.</li>
    <li>Select “Yes” for HTTPS unless explicitly directed otherwise.</li>
    <li>You will then be asked to test your settings- select NO as it WILL fail.</li>
    <li>Select “Yes” when prompted to save your configuration file.</li>
    <li>The .s3cfg file will be created in your users home directory- open it with your favorite text editor, in this example we will use VIM. Enter the command: <strong>vi ~/.s3cfg</strong>
    </li>
    <li>In the configuration file, change the following fields with the appropriate CenturyLink Cloud data center (in this example, we are using Canada- but an American data center would be us.tier3.io, UK would be uk.tier3.io, etc.)</li>
  </ol>
</ol>
<pre>host_base = ca.tier3.io

host_bucket = %(bucket)s.ca.tier3.io</pre>

<p>Alternatively, you can modify and save the following file and then specify s3cmd to use it by entering the command <strong>s3cmd&nbsp;–c /path/to/config file</strong>
</p>
<p><strong>Sample configuration file, bolded items must be edited:</strong>
</p>
<pre>[default]

<strong>access_key = YOUR_ACCESS_KEY_HERE</strong>

bucket_location = US

cloudfront_host = cloudfront.amazonaws.com

cloudfront_resource = /2010-07-15/distribution

default_mime_type = binary/octet-stream

delete_removed = False

dry_run = False

enable_multipart = False

encoding = UTF-8

encrypt = False

follow_symlinks = False

force = False

get_continue = False

gpg_command = /usr/local/bin/gpg

gpg_decrypt = %(gpg_command)s -d --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s

gpg_encrypt = %(gpg_command)s -c --verbose --no-use-agent --batch --yes --passphrase-fd %(passphrase_fd)s -o %(output_file)s %(input_file)s

<strong>gpg_passphrase = password</strong>

guess_mime_type = True

<strong>host_base = ca.tier3.io</strong>

<strong>host_bucket = %(bucket)s.ca.tier3.io</strong>

human_readable_sizes = False

list_md5 = False

log_target_prefix =

preserve_attrs = True

progress_meter = True

proxy_host = localhost

proxy_port = 8080

recursive = False

recv_chunk = 4096

reduced_redundancy = False

<strong>secret_key = YOUR_SECRET_KEY_HERE</strong>

send_chunk = 4096

simpledb_host = sdb.amazonaws.com

skip_existing = False

socket_timeout = 300

urlencoding_mode = normal

<strong>use_https = False</strong>

verbosity = WARNING

</pre>
<h5>Using S3CMD:</h5>
<p>Now that S3cmd has been configured, you can issue normal commands and interact with your storage. Run S3cmd&nbsp;–-man for a full list of commands.</p>
<p>Make a bucket with <code><strong>s3cmd mb s3://my-new-bucket-name</strong></code>
</p>
<p>List the contents of a bucket with <strong>s3cmd ls s3://my-new-bucket-name</strong>
</p>
<p>Upload a file <strong>s3cmd&nbsp;put testfile.xml&nbsp;s3://my-new-bucket-name/testfile.xml</strong>
</p>
<p>Download/Retrieve a file <strong>s3cmd&nbsp;get s3://my-new-bucket-name/testfile.xml testfile_modified.xml&nbsp;</strong>
</p>




<p>Look for the second article in this series which will discuss using advanced S3cmd features such as rsync and encryption!</p>