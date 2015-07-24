{{{
  "title": "Add-ons: CloudMailin",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<h3>Install CloudMailin</h3>
<p>In the "Add-ons" tab in your app console click "Install" for the CloudMailin add-on. That's it!</p>
<h3>Receive Email</h3>
<p>Cloudmailin can receive email and forward them to your app by performing a POST to a specific page.</p>
<p>Log in to the Cloudmailin console by clicking "Manage" on the add-on in your PHP Fog app console.</p>
<p>Go to "Edit Target" and specify the address in your application that will receive the emails via an HTTP POST (e.g. /mail.php).</p>
<p>Here's the code that goes into that page:</p>
<pre>&lt;?php
    $from = $_POST['from'];
    $to = $_POST['to'];
    $plain_text = $_POST['plain'];

    header("Content-type: text/plain");

    if ($to == getenv("CLOUDMAILIN_FORWARD_ADDRESS")) {
        header("HTTP/1.0 200 OK");
        echo('success');
        }else{
        header("HTTP/1.0 403 OK");
        echo('user not allowed here');
    }

    exit;
?&gt;</pre>
<p>That's it! Now any email sent to your CloudMailin email address will forward to your app. You can always check to see what your CloudMailin email address is by going to the "Env. Variables" tab in your AppFog app console and looking for the <code>CLOUDMAILIN_FORWARD_ADDRESS</code>, or by logging in to CloudMailin directly.</p>
<p>You can set up your custom domain emails to forward, too. You can find information on that <a href="http://docs.cloudmailin.com/receiving_email/forwarding_and_custom_domains/">here</a>.</p>
