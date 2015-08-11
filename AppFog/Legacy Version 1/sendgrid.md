{{{
  "title": "Add-ons: SendGrid",
  "date": "1-26-2015",
  "author": "Chris Sterling",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><a href="https://sendgrid.com">SendGrid's</a> cloud-based email infrastructure relieves businesses of the cost and complexity of maintaining custom email systems. SendGrid provides reliable delivery, scalability and real-time analytics along with flexible APIs that make custom integration a breeze.</p>
<h3>Install SendGrid</h3>
<p>In the "Add-ons" tab on your app console click "Install" for the SendGrid add-on. That's it!</p>
<p>Once SendGrid has been added, you will notice new environment variables: in the <code>Env variables</code> tab on your app console: <code>SENDGRID_USERNAME</code>, <code>SENDGRID_PASSWORD</code>, <code>SENDGRID_SMTP_HOST</code>.</p>
<p>How to upgrade your SendGrid account:</p>
<ul>
<li>Find the SendGrid add-on and click on "Manage" button:</li>
</ul>
<p><img class="screenshot" src="http://static.sendgrid.com.s3.amazonaws.com/images/appfog/appfog_sso.png" alt="" /></p>
<ul>
<li>On the SendGrid site click on "Change Package" button:</li>
</ul>
<p><img class="screenshot" src="http://static.sendgrid.com.s3.amazonaws.com/images/appfog/appfog_upgrade.png" alt="" /></p>
<ul>
<li>Select a new plan:</li>
</ul>
<p><img class="screenshot" src="http://static.sendgrid.com.s3.amazonaws.com/images/appfog/appfog_select_plan.png" alt="" /></p>
<p>Next, setup your app to start using the SendGrid add-on. In the following sections we have documented the interfaces with several languages and frameworks supported by AppFog.</p>
<ul>
<li><a href="#sendgrid-rails">Ruby/Rails</a></li>
<li><a href="#sendgrid-java">Java</a></li>
<li><a href="#sendgrid-php">PHP</a></li>
<li><a href="#sendgrid-node">Node.js</a></li>
<li><a href="#sendgrid-python">Python</a></li>
</ul>
<h3 id="sendgrid-rails">Ruby on Rails</h3>
<p>You can quickly get started with SendGrid using Ruby on Rails ActionMailer. You will need to edit the ActionMailer settings in <code>config/environment.rb</code> to use SendGrid credentials from environment variables:</p>
<pre>ActionMailer::Base.smtp_settings = {
  :address =&gt; ENV["SENDGRID_SMTP_HOST"],
  :port =&gt; '587',
  :authentication =&gt; :plain,
  :user_name =&gt; ENV["SENDGRID_USERNAME"],
  :password =&gt; ENV["SENDGRID_PASSWORD"],
  :domain =&gt; 'yourdomain.com',
  :enable_starttls_auto =&gt; true
}</pre>
<h3 id="sendgrid-java">Java</h3>
<p>This Java program will build a multi-part MIME email and send it through SendGrid. Java already has built in libraries to send and receive emails. This example uses <a href="https://java.net/projects/javamail/pages/Home">javamail</a>.</p>
<pre>import javax.mail.*;
import javax.mail.internet.*;
import javax.mail.Authenticator;
import javax.mail.PasswordAuthentication;
import java.util.Properties;

public class SimpleMail {

    private static final String SMTP_HOST_NAME = System.getenv("SENDGRID_SMTP_HOST");
    private static final String SMTP_AUTH_USER = System.getenv("SENDGRID_USERNAME");
    private static final String SMTP_AUTH_PWD  = System.getenv("SENDGRID_PASSWORD");

    public static void main(String[] args) throws Exception{
        new SimpleMail().test();
    }

    public void test() throws Exception{
        Properties props = new Properties();
        props.put('mail.transport.protocol', 'smtp');
        props.put('mail.smtp.host', SMTP_HOST_NAME);
        props.put('mail.smtp.port', 587);
        props.put('mail.smtp.auth', 'true');

        Authenticator auth = new SMTPAuthenticator();
        Session mailSession = Session.getDefaultInstance(props, auth);
        // uncomment for debugging infos to stdout
        // mailSession.setDebug(true);
        Transport transport = mailSession.getTransport();

        MimeMessage message = new MimeMessage(mailSession);

        Multipart multipart = new MimeMultipart('alternative');

        BodyPart part1 = new MimeBodyPart();
        part1.setText('This is multipart mail and u read part1');

        BodyPart part2 = new MimeBodyPart();
        part2.setContent('&lt;b&gt;This is multipart mail and u read part2&lt;/b&gt;', 'text/html');

        multipart.addBodyPart(part1);
        multipart.addBodyPart(part2);

        message.setContent(multipart);
        message.setFrom(new InternetAddress('me@myhost.com'));
        message.setSubject('This is the subject');
        message.addRecipient(Message.RecipientType.TO,
            new InternetAddress('someone@somewhere.com'));

        transport.connect();
        transport.sendMessage(message,
        message.getRecipients(Message.RecipientType.TO));
        transport.close();
    }

    private class SMTPAuthenticator extends javax.mail.Authenticator {
        public PasswordAuthentication getPasswordAuthentication() {
            String username = SMTP_AUTH_USER;
            String password = SMTP_AUTH_PWD;
            return new PasswordAuthentication(username, password);
        }
    }
}</pre>
<h3 id="sendgrid-php">PHP</h3>
<p>You can use <a href="https://github.com/sendgrid/sendgrid-php">this</a> library to send emails through SendGrid using PHP. More information about the library can be found <a href="http://sendgrid.com/docs/Code_Examples/php.html">here</a>.</p>
<pre>include 'path/to/sendgrid-php/SendGrid_loader.php';
$ sendgrid = new SendGrid(getenv('SENDGRID_USERNAME'), getenv('SENDGRID_PASSWORD'));
$ mail = new SendGrid\Mail();
$ mail-&gt;
  addTo('foo@bar.com')-&gt;
  setFrom('me@bar.com')-&gt;
  setSubject('Subject goes here')-&gt;
  setText('Hello World!')-&gt;
  setHtml('&lt;strong&gt;Hello World!&lt;/strong&gt;');</pre>
<p>For sending emails using SMTP:</p>
<pre>$ sendgrid-&gt;
smtp-&gt;
  send($mail);</pre>
<p>For sending emails using the Web API:</p>
<pre>$ sendgrid-&gt;
web-&gt;
  send($mail);</pre>
<h3 id="sendgrid-node">Node.js</h3>
<p>SendGrid has a Node.js package that is written and maintained by two core engineers. The code is open source and available on <a href="https://github.com/sendgrid/sendgrid-nodejs">Github</a>.</p>
<p>Add the following settings in package.json file</p>
<pre>{
  "name": "node-sendgrid-example",
  "version": "0.0.1",
  "dependencies": {
    "sendgrid": "1.0.0-rc.1.0"
  },
  "engines": {
    "node": "&gt;= 0.10.x",
    "npm": "1.2.x"
  }
}</pre>
<p>Install SendGrid locally with the following command: <code>npm install</code></p>
<p>To begin using this library, initialize the sendgrid object with your SendGrid credentials:</p>
<pre>var sendgrid  = require('sendgrid')(
  process.env.SENDGRID_USERNAME,
  process.env.SENDGRID_PASSWORD
);</pre>
<p>Send the email.</p>
<pre>sendgrid.send({
  to: 'example@example.com',
  from: 'sender@example.com',
  subject: 'Hello World',
  text: 'Sending email with NodeJS through SendGrid!'
}, function(err, json) {
  if (err) { return console.error(err); }
  console.log(json);
});</pre>
<p>Full documentation of all the features of SendGrid's Node.js package can be found on <a href="https://github.com/sendgrid/sendgrid-nodejs">Github</a>.</p>
<h3 id="sendgrid-python">Python</h3>
<p>Before start writing the code you need to copy the <a href="https://github.com/sendgrid/sendgrid-python/tree/master/sendgrid">SendGrid Python library</a> into your project by placing the files in a sendgrid sub-directory. When you import this library into your app you'll be able to create SendGrid instances and send mail with simple commands. This library allows you to quickly and easily send emails through SendGrid using Python.</p>
<p>At the top of your app's .py file, import the sendgrid library:</p>
<pre>import sendgrid
import os</pre>
<p>Now, from within your app, you can send email with the following few lines:</p>
<pre># make a secure connection to SendGrid
s = sendgrid.Sendgrid(os.environ.get('SENDGRID_USERNAME'), os.environ.get('SENDGRID_PASSWORD'), secure=True)
# make a message object
message = sendgrid.Message("from@mydomain.com",
                           "message subject",
                           "plaintext message body",
                           "&lt;strong&gt;HTML message body&lt;/strong&gt;")
# add a recipient
message.add_to("someone@example.com", "John Doe")</pre>
<p>use the Web API to send your message</p>
<pre>s.web.send(message)</pre>
<p>or use the SMTP API to send your message</p>
<pre>s.smtp.send(message)</pre>
<h3>Dashboard</h3>
<p>SendGrid offers statistics for a number of different metrics to report on what is happening with your messages.</p>
<p><img class="screenshot" src="http://static.sendgrid.com.s3.amazonaws.com/images/delivery_metrics.png" alt="" /></p>
<p>To access your SendGrid dashboard, simply click the "Manage" button of the SendGrid add-on in the "Add-ons" tab on your app console.</p>
<h3>Support</h3>
<p>One of SendGrid's best features is its responsive customer service. You can contact SendGrid 24/7 by phone or web:</p>
<ul>
<li><a href="http://support.sendgrid.com/">http://support.sendgrid.com</a></li>
<li>Toll Free: +1 (877) 969-8647</li>
</ul>
<h3>Additional resources</h3>
<p>Additional resources are available at:</p>
<ul>
<li><a href="http://sendgrid.com/docs/Integrate/index.html">Integrate With SendGrid</a></li>
<li><a href="http://sendgrid.com/docs/Code_Examples/index.html">Code Examples</a></li>
</ul>
