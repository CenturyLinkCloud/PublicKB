{{{
  "title": "Gathering Information for Troubleshooting Lync Issues",
  "date": "11-12-2014",
  "author": "Eric Schubert",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description (goal/purpose)</strong>
</p>
<p>A guide to troubleshooting Lync issues. This guide will help you gather the necessary information to open a trouble ticket with Lumen Cloud if you are having an issue with Lync. This information is required in order for the Managed Services team to troubleshoot
  the issue.</p>
<p><strong>Audience</strong>
</p>
<ul>
  <li>Microsoft Lync Managed Services Customers</li>
</ul>
<p>Before gathering the information below, determine the following:</p>
<ul>
  <li>Is the issue affecting all users, multiple users&nbsp;or 1 user?</li>
  <li>If all users, proceed to opening a ticket.</li>
  <li>If multiple users&nbsp;– was there a conference or meeting or something that ties these users together? Can you reproduce the issue?</li>
  <li>If one user, does the user have the issue once, sometimes or all the time?</li>
  <li>If&nbsp; sometimes or all the time&nbsp;– does the user have the issue when connected to a different network? (home, office, coffeshop)</li>
  <li>If the user has the issue in multiple locations&nbsp;– does the user have the issue with multiple devices/clients? (iphone, ipad, android, mac, pc)</li>
</ul>
<p><strong>Information needed:</strong>
</p>
<p>Prior to opening a ticket with Lumen Cloud, please gather the following information:</p>
<ul>
  <li><strong>Name, SIP&nbsp;Address, OS and client&nbsp;and if applicable,&nbsp;Lync Phone number</strong>
  </li>
</ul>
<p><strong>call info:</strong>
</p>
<ul>
  <li><strong>Inbound or Outbound</strong>
  </li>
  <li><strong>PSTN call? Dial-in Conference call? Lync Conference?, Lync Call?</strong>
  </li>
  <li><strong>Number of the party calling/being called/exact time</strong>
  </li>
  <li><strong>What was the symptom? Poor quality/disconnected/unable to connect/unable to login/unable to join meetings/search or address book not working…</strong>
  </li>
  <li><strong>Any error messages in the client? Please send screen shots or type the error exactly.</strong>
  </li>
  <li><strong>Gather the logs from the client. Turn on logging and attempt to replicate the problem. Or just configure all clients to have logging on by default as some issues will be difficult to replicate.</strong>
  </li>
</ul>
<p><strong>Enable Logging on the Lync Client</strong> <strong>for Windows</strong>
</p>
<p>From the Lync Client Click on Tools – Options – General
  <br />Under the Logging section check Turn on logging in Lync and Turn on Windows Event logging for Lync
  <br />Click OK
  <br />Restart Lync Client
  <br />Attempt&nbsp; to replicate the issue
  <br />Logs can be found in &lt;username&gt;\tracing
  <br />There will typically be a searchable error in there a clue to point you further in troubleshooting.</p>
<p><strong>Enable Logging on the Lync Client</strong> <strong>for Mac</strong>
</p>
<p>From the Lync Client Click on Lync&nbsp;– Preferences&nbsp;– General
  <br />Under the Logging section check Turn on logging for troubleshooting.
  <br />Restart Lync Client
  <br />Attempt&nbsp; to replicate the issue
  <br />The logs are located in users/username/library/logs/Microsoft-Lync-0.log. (The zero increments as the log file grow.)
  <br />There will typically be a searchable error in there a clue to point you further in troubleshooting.</p>
<p><strong>Enable Logging on the Lync Mobile Client</strong> <strong>for iOS</strong>
</p>
<p>From the Lync Mobile Client - My Info screen&nbsp;tap Options
  <br />Under the&nbsp;Other section tap Logging. Toggle off to on for Enable Logging
  <br />Restart Lync Mobile Client
  <br />Attempt&nbsp; to replicate the issue
  <br />Return to My Info&nbsp;– Options&nbsp;– Other&nbsp;– Logging. There will be a Send Log Files button. Tap it and send an email with the attached log files to yourself. Attach these logs to the ticket.
  <br />There will typically be a searchable error in there a clue to point you further in troubleshooting.</p>
<p>This guide provides the reader with the tools needed to successfully troubleshoot and track down the precise error for virtually any Lync issue.</p>
<p><strong>Enable Logging on the Lync Mobile Client</strong> <strong>for Andriod</strong>
</p>
<p>On the Android device, after a user is signed in, press the hardware menu button and tap Options in the menu. On the Options screen, check if the Logging option is turned on. If not, turn on the Logging option, sign out, and then sign in again.
  <br />Restart Lync Mobile Client
  <br />Attempt&nbsp; to replicate the issue
  <br />Return to the Options Menu. Options&nbsp;– Other&nbsp;– Logging. There will be a Send Log Files button. Tap it and send an email with the attached log files to yourself. Attach these logs to the ticket.
  <br />There will typically be a searchable error in there a clue to point you further in troubleshooting.</p>
<p><strong>Gather all the information and log files and submit a ticket.</strong>
</p>
<p>After you have all the above information, open a ticket with the NOC by sending an email to Lumen Cloud support. Existing Managed Services customers will have this address. Alternatively, Log onto the Control Portal <a href="https://control.tier3.com/">https://control.tier3.com</a>  and click Support.</p>
<p>In your ticket request include all the above information and attach all log files gathered. This information will be used to troubleshoot the issue.</p>
