{{{
  "title": "S3CMD - Object Storage Management for Linux Machines",
  "date": "03-25-2015",
  "author": "Brian Button",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>S3CMD is a Linux command line utility that can be used to interact with and manage your <a href="../Object Storage">CenturyLink Cloud Object Storage</a> buckets and data, Access Control Lists (ACLs), and associated metadata. S3CMD is an advanced tool to be used for accessing object storage, so care should be taken.</p>

<ul>
    <li class="scroll-to-link"><a href="#install">Installing S3CMD</a>
    </li>
    <li class="scroll-to-link"><a href="#configure">Configuring S3CMD for CenturyLink Object Storage</a>
    </li>
    <li class="scroll-to-link">
        <a href="#usage">Using S3CMD</a>
    </li>
    <li class="scroll-to-link">
    <a href="#version">Special note about S3CMD versions</a>
</ul>

<h4><a id="install">Installing S3CMD</a></h4>
<p>Before you can use S3CMD, you'll need to make sure it is installed. At the command line, enter the following: <strong>which s3cmd</strong> . If this command gives  no output, then you do not have S3CMD installed and need to add it. </p>

<p>The simplest way to add it is to use the package manager for your version of Linux, probably either <strong>yum</strong> or <strong>apt</strong>. While S3CMD is included in many package managers, it is best to manually configure
  the official repository to ensure that you are using the latest version.

<p><strong>To add the repository to a CentOS or RHEL machine</strong> (note, both instructions assume you are running as root - you will need to add “sudo” where appropriate if not logged in as root):</p>
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
  <li>Add the repository by entering the command: <strong><strong>wget -O /etc/apt/sources.list.d/s3tools.list&nbsp;</strong><a href="http://s3tools.org/repo/deb-all/stable/s3tools.list"><strong>http://s3tools.org/repo/deb-all/stable/s3tools.list</strong></a>
    </strong>
  </li>
  <li>Refresh your packages and install by entering the command: <strong>apt-get update &amp;&amp; apt-get install s3cmd</strong>
  </li>
</ol>

<h4><a id="configure">Configuring S3CMD</a></h4>
Once S3CMD has been installed, it must be configured to use CenturyLink Cloud’s Object Storage.
<ol>
  <ol>
    <li>S3CMD stores its settings in a configuration file. You can either run <strong>s3cmd&nbsp;–configure&nbsp;</strong> to launch an interactive&nbsp;configuration generation tool, or specify a pre-existing file. You will need both your Access Key and
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
    <li>The .s3cfg file will be created in your users home directory- open it with your favorite text editor, in this example we will use <strong>vi</strong>. Enter the command: <strong>vi ~/.s3cfg</strong>
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

<p>To begin using S3CMD, you'll need have an object storage user and a bucket, which you can create through the CenturyLink Cloud Control Portal: </p>
<ol>
  <li>Navigate to “Object Storage” under the “Services” tab of <a href="https://control.ctl.io/">https://control.ctl.io</a>
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
</pre>
<h4><a id="usage">Using S3CMD</a></h4>
<p>Now that S3cmd has been configured, you can issue normal commands and interact with your storage. Run S3cmd&nbsp;–-man for a full list of commands.</p>
<p>Make a bucket with <code><strong>s3cmd mb s3://my-new-bucket-name</strong></code>
</p>
<p>List the contents of a bucket with <strong>s3cmd ls s3://my-new-bucket-name</strong>
</p>
<p>Upload a file <strong>s3cmd&nbsp;put testfile.xml&nbsp;s3://my-new-bucket-name/testfile.xml</strong>
</p>
<p>Download/Retrieve a file <strong>s3cmd&nbsp;get s3://my-new-bucket-name/testfile.xml testfile_modified.xml&nbsp;</strong>
</p>
<h4><a id="version">Special note about S3CMD versions</a></h4>
<p>
S3CMD is an active open-source project, and as such is frequently updated. Depending on the version of S3CMD you installed, the default authentication strategy may have changed. Using the incorrect authentication strategy will result in <strong>403 Not Authorized</strong> errors for some requests to object storage. You can tell which version of S3CMD you have by running the command <strong>s3cmd --version</strong> and inspecting the output. If the version is before <strong>1.5.0</strong> then s3cmd will operate correctly.
</p>
<p>
If your version is <strong>1.5.0</strong> or newer, then there are two ways to make this work correctly again. The first is to provide the <strong>--signature-v2</strong> argument to S3CMD, for example like <strong>s3cmd --signature-v2 ls</strong>. The argument tells S3CMD to revert to the original authentication strategy. The more permanent change is to add <strong>signature_v2 = True</strong> to the bottom of your .s3cfg file. That will force S3CMD to use the original authentication strategy every time the command is run.
</p>

</br>

<p>Look for the second article in this series which will discuss using advanced S3cmd features such as rsync and encryption!</p>
