{{{
  "title": "Redhat machines report they are not registered to RHN when running 'yum'",
  "date": "11-25-2014",
  "author": "James Morris",
  "attachments": []
}}}

<p>When running 'yum' on a Redhat machine deployed on CenturyLink Cloud you may receive the message</p>
<p><strong>"This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register."</strong>
</p>
<p>This message is normal and does not indicate any problem, as machines we deploy are themselves not registered to RHN, but rather they connect to repositories within our Redhat Update&nbsp;Infrastructure (RHUI). &nbsp;All base packages for the RHEL distribution
  in question should be available via the RHUI entitlement installed on your machine at build time. &nbsp;&nbsp;</p>
<p>If for some reason your machine is not able to download packages from our RHUI system, please contact our support team to investigate.</p>

