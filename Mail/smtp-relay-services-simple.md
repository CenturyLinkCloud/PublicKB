{{{
  "title": "SMTP Relay Services (Simple)",
  "date": "12-2-2014",
  "author": "jw@tier3.com",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>SMTP Relay Services (Simple)</strong>
</p>
<p>SMTP Relay can be used to do application level email relay without the need of managing your own SMTP server/service. The current offering is prices at $0.10 per 1000 emails sent via the service and billed at the account level.&nbsp;</p>
<p>You can sign up for the service easily by going to the Contol Portal &gt; Services &gt; SMTP Relay. From here you can create an SMTP relay account by doing the following:</p>
<ul>
  <li>Click the "Create SMTP Relay" button.</li>
  <li>It will create a user to be used on the service and will be listed with an alias, password, status such as:<img src="https://t3n.zendesk.com/attachments/token/govwacy5fnuzexs/?name=smtp-relay-user.png" alt="smtp-relay-user.png" />
  </li>
  <li>Now you can connect to the SMTP relay service from your virtual servers at Tier 3.</li>
</ul>
<div>&nbsp;</div>
<div><strong>Connect to the SMTP Relay Service</strong>
</div>
<div><strong>&nbsp;</strong>
</div>
<div>Connecting to the SMTP service is very easy as it is done via port 25 from inside the Tier 3 Cloud. Here are the settings:</div>
<div>
  <ul>
    <li>SMTP Host: relay.t3mx.com</li>
    <li>SMTP Host Port: 25</li>
    <li>User: (what is provided in your control portal as the alias)</li>
    <li>Password: (what is provided in your control portal)</li>
  </ul>
  <div>&nbsp;</div>
  <div>You will also need to add SPF record as follows:&nbsp;<strong>v=spf1 ip4:66.150.160.0/24</strong>
  </div>
  <div><strong>&nbsp;</strong>
  </div>
  <div><strong>API's for SMTP Relay Provisioning:</strong>
  </div>
  <div>&nbsp;</div>
  <div>Here are the links to the provisioning service for the SMTP Relay that can be used to manage SMTP relay accounts and get invalid addresses such as bounce backs:</div>
  <div>&nbsp;</div>
  <div>
    <ul>
      <li><a href="http://help.tier3.com/entries/20345643-overview">Overview</a>
      </li>
      <li><a href="http://help.tier3.com/entries/20340072-create-alias">Create Alias</a>
      </li>
      <li><a href="http://help.tier3.com/entries/20350261-list-aliases">List Aliases</a>
      </li>
      <li><a href="http://help.tier3.com/entries/20345653-disable-alias">Disable Alias</a>
      </li>
      <li><a href="http://help.tier3.com/entries/20345668-remove-alias">Remove Alias</a>
      </li>
      <li><a href="http://help.tier3.com/entries/20345683-get-invalid-addresses">Get Invalid Addresses</a>&nbsp;</li>
    </ul>
  </div>
  <div><strong>&nbsp;</strong>
  </div>
  <div><strong>RHEL Compatible Postfix Basic Setup</strong>
  </div>
  <div><strong><br /></strong>Install pre-reqs:</div>
  <div>
    <pre> &gt; sudo yum install cyrus-sasl{,-plain}</pre>
  </div>
  <div></div>
  <div></div>
  <div>As root create the file /etc/postfix/smtp_sasl_password_maps with the following content (substituting your alias and password):</div>
  <div></div>
  <div><strong><strong></strong></strong>
    <pre>relay.t3mx.com    <strong>$alias</strong>:<strong>$password</strong></pre>
    <div>
      <div>
        <br />Create a hash of your password map:</div>

      <div></div>

      <div><strong></strong>
        <pre>&gt; sudo postmap /etc/postfix/smtp_sasl_password_maps</pre>
        <div>
          <br />Add the following lines to your /etc/postfix/main.cf:</div>
        <div>
          <pre>smtp_sasl_auth_enable = yes<br />smtp_sasl_password_maps = hash:/etc/postfix/smtp_sasl_password_maps<br />smtp_sasl_security_options = noanonymous<br />relayhost = relay.t3mx.com</pre>
        </div>
      </div>
    </div>
    <div></div>
    <div>Restart postfix and test:</div>
    <div></div>
    <div><strong><strong></strong></strong>
      <pre>&gt; sudo /sbin/service postfix restart</pre>
    </div>
    <strong></strong>
  </div>
  <div><strong></strong>
  </div>
  <div><strong></strong>
  </div>
  <div><strong></strong>
  </div>
</div>