{{{
  "title": "Using SAML for Single-Sign-On to the CenturyLink Platform Control Portal",
  "date": "10-13-2014",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>CenturyLink Cloud supports the use of Security Assertion Markup Language (SAML) for exchanging user authentication data as XML between trusted parties. This industry standard protocol empowers our customers to use their <strong>own</strong> identity management system
  for authenticating users of the CenturyLink Cloud Control Portal.</p>
<p>SAML has three main parties: the user, the identity provider (IdP), and service provider (SP). The IdP is the repository that holds identity information. The SP is the party that wants to authenticate a particular user who is using an application.</p>
<p>The SAML flow occurs as follows:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/lvelbw7wuayx1yb/?name=saml01.png" alt="saml01.png" />
</p>
<ol>
  <li>The enterprise user of the CenturyLink Cloud hits a URL that is dedicated to their account. The user is asked how they would like to log into the system and they choose SAML.</li>
  <li>The web application contacts the CenturyLink Cloud SAML service to initiate the SAML message exchange.</li>
  <li>The CenturyLink Cloud SP &nbsp;sends a digitally signed SAML authentication request to the enterprise IdP. This IdP takes the user's Kerberos token and validates them as a user on the enterprise network.&nbsp;</li>
  <li>The IdP returns a signed (and optionally, encrypted) SAML authentication response message to the CenturyLink Cloud SP. This message includes a Name ID assertion and that value is matched to a User record in the CenturyLink Cloud.</li>
  <li>The user is logged into the CenturyLink Cloud and operates under the roles and permissions assigned to their CenturyLink Cloud user account.</li>
</ol>
<p>The steps below walk through the process of building an entire SSO and SAML scenario based on Microsoft Active Directory Federation Services as the IdP proxy. If you already have an identity provider, you can skip to step #3 where trust is established
  between CenturyLink Cloud and the IdP.</p>
<p><strong>Steps:&nbsp;</strong>
</p>
<div><strong>1. Provision server to act as Identity Provider.</strong>
</div>
<ul>
  <li>Log into the CenturyLink Cloud Control Portal and choose to create a new Blueprint. This takes you to the Blueprint Designer wizard.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/ibkzd7s7a1eiawp/?name=saml02.png" alt="saml02.png" />
  </li>
  <li>Include a single (Windows Server 2008 or above) server to the Bluepriint and add packages to<strong> Install DNS</strong>,<strong> Install Active Directory</strong>, <strong>Reboot</strong>,<strong> Install IIS</strong>, and<strong> Add a Public IP</strong>.
    The DNS and Active Directory packages give us a custom domain to work with, and an identity directory for our user records. Microsoft Internet Information Services (IIS) provides a web application host for the Active Directory Federation Services
    (ADFS) web services used later on. Finally, the public IP address exposes our server to the public internet where applications (like the CenturyLink Cloud Control Portal) can access it for a SAML exchange.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/iwardtgt0md86ub/?name=saml03.png" alt="saml03.png" />
  </li>
  <li>Publish the Blueprint and then locate it in the Blueprint library. Click the <strong>Deploy Blueprint </strong>button to initiate the provisioning process.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/y7ykjphvipevaxg/?name=saml04.png" alt="saml04.png" />
  </li>
  <li>On the "Customize Blueprint" step of the deployment wizard, the user is asked to provide deploy-time build parameters such as the server password, host network, and Active Directory domain name. Note a few key values: first, the <strong>Primary DNS</strong>    value <em>must be equal to the name of the server being created</em>. Recall that we are added DNS services to the server itself, so THIS is the domain that the new server should use for resolution. The <strong>Domain Name </strong>parameter typically
    contains the full name of the domain (including a suffix such as ".com") while the Net BIOS Name omits the suffix.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/s6a6babbwyz6cgt/?name=saml05.png" alt="saml05.png" />
  </li>
  <li>Complete the deployment process and wait for the new server to be built by the CenturyLink Cloud Blueprint engine.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/40kzokenuhefjg1/?name=saml06.png" alt="saml06.png" />
  </li>
  <li>Locate the server in the designated group and confirm its DNS value and public IP address.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/urbtqbzxjfpzjzk/?name=saml07.png" alt="saml07.png" />
  </li>
</ul>
<div><strong>2. Install and configure Active Directory Federation Services.</strong>
</div>
<ul>
  <li>Open client VPN software and connect to the CenturyLink Cloud network. Once authenticated, create a Remote Desktop session to the target server. In the Server Manager, confirm the installation of DNS, Active Directory, and IIS.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/zw73lohdl71fyzf/?name=saml08.png" alt="saml08.png" />
  </li>
  <li>In order to issue certificates easily from this server, install the<strong> Certificate Services</strong> role on the server. Choose the <strong>Certificate Authority</strong>&nbsp;role, select <strong>Enterprise CA</strong>, set this to a <strong>Root CA</strong>,
    and create a new private key. Finish the wizard.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/ii8wm8sp1du3eb7/?name=saml09.png" alt="saml09.png" />
  </li>
  <li>Open the IIS Manager, click the host name, and locate the <strong>Server Certificates</strong>&nbsp;feature.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/krjaljf6u8rwnvj/?name=saml10.png" alt="saml10.png" />
  </li>
  <li>Double-click the <strong>Server Certificates </strong>icon and select the option on the right to <strong>Create Domain Certificate</strong>. On the first page of the wizard choose the common name (it could be a wildcard entry like "*.tier3samldemo.com")
    and organizational details.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/reorahcosfefwgy/?name=saml11.png" alt="saml11.png" />
  </li>
  <li>On the next page of the wizard, choose the Certificate Authority and set the friendly name of the certificate.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/codn2xcaxidksij/?name=saml12.png" alt="saml12.png" />
  </li>
  <li>After completing the wizard (and creating a certificate that should show up in the Certificates MMC as a <strong>Personal</strong> certificate for the Computer account), right-click the Default Web Site in the IIS Manager and choose <strong>Edit Bindings</strong>.
    Here, we set the site to use our new certificate for SSL.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/bownmh9yfwndaau/?name=saml13.png" alt="saml13.png" />
  </li>
  <li>For users working with Windows Server 2008 or Windows Serve 2008 R2, <a href="http://www.microsoft.com/en-us/download/details.aspx?id=10909" target="_blank">download ADFS 2.0 from the Microsoft website</a>. Windows Server 2012 comes with ADFS pre-installed.
    Run the ADFS Setup Wizard.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/tyfztrw28p8vry5/?name=saml14.png" alt="saml14.png" />
  </li>
  <li>Select the <strong>Federation server </strong>role, and complete the short wizard. Once the wizard installs prerequisite software and finishes installing ADFS 2.0, choose the option to launch the ADFS Configuration Wizard.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/dbrlictlpumk8wi/?name=saml15.png" alt="saml15.png" />
  </li>
  <li>Choose to <strong>Create a new Federation Service</strong>, a <strong>Stand-alone federation server</strong>, and notice that the wizard pulls in the name of the certificate set for SSL in IIS.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/m1gncqt4ioc6ljd/?name=saml16.png" alt="saml16.png" />
  </li>
  <li>When the wizard completes, notice the new ADFS configuration options.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/xbr3sv8dgdbszyc/?name=saml17.png" alt="saml17.png" />
  </li>
  <li>Before proceeding, add a new user to the Active Directory. In the Server Manager, expand the <strong>Active Directory Domain Services</strong>&nbsp;node, then <strong>Active Directory Users and Computers</strong>, and then the domain.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/zzkbryfitpffwci/?name=saml31.png" alt="saml31.png" />
  </li>
  <li>Right-click on the <strong>Users </strong>node and select <strong>New</strong>, then <strong>User. </strong>Add the details of this new user and save the settings.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/ydfqxfzie9gc0hf/?name=saml32.png" alt="saml32.png" />
  </li>
</ul>
<div><strong>3. Create trust relationship with CenturyLink Cloud.</strong>
</div>
<ul>
  <li>Prior to starting this step, <strong>contact the CenturyLink Cloud NOC to acquire the public certificate</strong> that validates the message coming from CenturyLink Cloud.</li>
  <li>In the ADFS 2.0 Management console (or whatever IdP service that's being used), create a new Relying Party Trust. This is where the settings from the CenturyLink Cloud are added to the local IdP so that it recognizes the SAML authentication request and can
    validate the inbound signature.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/7wrwwf8wrpnankf/?name=saml18.png" alt="saml18.png" />
  </li>
  <li>Choose the option to add the relying party metadata manually.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/jedsxww0yzokglp/?name=saml19.png" alt="saml19.png" />
  </li>
  <li>Name the relying party something like "CenturyLink Cloud Control Portal." Select the ADFS 2.0 profile. When asked for the <strong>Relying party trust identifier</strong>, use the following value (while filling in your specific account alias):&nbsp;https://&lt;alias&gt;.tier3cloud.com/SAMLAuth.
    <strong>Note that this value is case-sensitive!</strong>
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/mo3ipx4oyzordrf/?name=saml20.png" alt="saml20.png" />
  </li>
  <li>Finish the wizard, and plan on addition a pair of additional values later on. On the last wizard page, click the checkbox to <strong>Open the Edit Claims Rules dialog. </strong>Here is where we define which Active Directory values (claims) map to the
    SAML attributes sent back to CenturyLink Cloud.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/7w8ioj6npdkntyx/?name=saml21.png" alt="saml21.png" />
  </li>
  <li>Set the source of attributes (Active Directory), choose the <strong>User-Principal-Name </strong>as the <strong>LDAP Attribute</strong>, set the <strong>Outgoing Claim Type</strong> to <strong>Name ID</strong>.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/azv1hcjdnora6hm/?name=saml22.png" alt="saml22.png" />
  </li>
  <li>After completing this wizard, go back to the Relying Party Trusts folder and open the new entry. Switch to the <strong>Signatures </strong>tab, and add the certificate provided to you by the CenturyLink Cloud NOC.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/ockcfuosebhrmhn/?name=saml23.png" alt="saml23.png" />
  </li>
  <li>Switch to the <strong>Endpoints </strong>tab and add a <strong>SAML Assertion Consumer</strong> with a <strong>POST</strong> binding and set the URL to&nbsp;https://&lt;alias&gt;.tier3cloud.com/SAMLAuth/Post. Once again, this value is case-sensitive.
    <br
    />
    <br /><img src="https://t3n.zendesk.com/attachments/token/9henucevoitfslx/?name=saml24.png" alt="saml24.png" />
  </li>
  <li>Finally, on the <strong>Advanced </strong>tab, change the <strong>Secure Hash Algorithm</strong>&nbsp;to <strong>SHA-1</strong>. Save the Relying Party Trust entry.
    <br />
    <br />
  </li>
</ul>
<div><strong>4. Configure CenturyLink Cloud account with SAML settings.</strong>
</div>
<ul>
  <li>Log into the CenturyLink Cloud Control Portal and under <strong>Account</strong> menu, select the <strong>Users</strong> tab.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/sqeaotxl1baj1iv/?name=saml25.png" alt="saml25.png" />
  </li>
  <li>Switch to the <strong>Authentication</strong> sub-section and check the box labeled <strong>SAML Authentication</strong>. This opens up a series of configuration settings.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/ed3vhrol0jxstl7/?name=saml26.png" alt="saml26.png" />
  </li>
  <li>For the <strong>SAML SSO URL</strong>,set the ADFS service URL. This includes the domain name the ADFS server. Even if you don't own the public domain name used here, enter the domain created for the local server.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/y9ksfm4vt1wqafx/?name=saml27.png" alt="saml27.png" />
  </li>
  <li>To get the <strong>Signing Certificate Key</strong>, return to the ADFS server, view the ADFS Management Console, and find the <strong>Certificates</strong>&nbsp;directory under the <strong>Services </strong>node. Notice the <strong>Token-signing</strong>&nbsp;certificate.
    <br
    />
    <br /><img src="https://t3n.zendesk.com/attachments/token/2bzeosiruwltrt1/?name=saml28.png" alt="saml28.png" />
  </li>
  <li>Choose to view the certificate (by right-clicking it), switch to the <strong>Details </strong>tab and select <strong>Copy to File</strong>. Export a <strong>Base-64 encoded X.509</strong>&nbsp;certificate.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/a9tm8n8kgyyvikw/?name=saml29.png" alt="saml29.png" />
  </li>
  <li>Save the file to a known location on the file system. Open the file with a text editor and copy all of the text between the "Begin Certificate" and "End Certificate" indicators.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/0v2wi4n4tbhauhu/?name=saml30.png" alt="saml30.png" />
  </li>
  <li>Paste this value into the <strong>Signing Certificate Key</strong>&nbsp;field in the CenturyLink Cloud Control Portal. Click the <strong>Save </strong>button and switch back to the <strong>Users List </strong>view. Select the user that you want to perform SSO
    with, and locate the <strong>SAML Username</strong>&nbsp;field. Since we chose above to use the Active Directory User Principal Name as the lookup value to the CenturyLink Cloud account, we must plug in the User Principal Name associated with this user.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/jr0rr0owlohzukf/?name=saml33.png" alt="saml33.png" />
  </li>
  <li>Save the user record.
    <br />
    <br />
  </li>
</ul>
<div><strong>5. Exchange SAML messages to perform Single Sign On.</strong>
</div>
<ul>
  <li>Before testing, if you do not own the public domain name corresponding to the DNS name of your server, then your test will fail. To test successfully, change your local machine host file so that the browser translates the domain name to the public IP
    address of the server. When the SAML request comes in to ADFS, it tries to match the SAML Destination ID (retrieved from the SAML configuration in your CenturyLink Cloud account) to the Federation Service name in the ADFS server.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/fsrzrtbf05zjbnp/?name=saml34.png" alt="saml34.png" />
  </li>
  <li>If the values do not match, then ADFS will return an exception. In order to test this scenario without registering and owning the corresponding public domain name, navigate to your local machine's host file (C:\Windows\System32\Drivers\etc\hosts) and
    add an entry that maps the public IP address of the server to the DNS name of the server.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/tmjzodsx60r3uho/?name=saml35.png" alt="saml35.png" />
  </li>
  <li>Go to a web browser and plug in&nbsp;https://&lt;alias&gt;.tier3cloud.com. Here you can sign in via CenturyLink Cloud username and password, or choose the <strong>Sign In Using SAML </strong>option. If you choose the latter, then the CenturyLink Cloud SAML service redirects
    the browser to the URL specified in the account's <strong>SAML SSO URL</strong> setting.
    <br />
    <br /><img src="https://t3n.zendesk.com/attachments/token/c1papu1xttx1gae/?name=saml36.png" alt="saml36.png" />
  </li>
  <li>Clicking the&nbsp;<strong>Sign In Using SAML </strong>button&nbsp;results in the following message being sent to the ADFS (or any IdP) service.
    <br />
    <br />
    <pre>&lt;samlp:AuthnRequest 

	ID="--ID--" 

	Version="2.0" 

	IssueInstant="2012-12-06T21:30:41.385Z" 

	Destination="https://tier3samldemo.com/adfs/ls/" 

	ForceAuthn="false" 

	IsPassive="false" 

	ProtocolBinding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" 

	AssertionConsumerServiceURL="https://ALIAS.tier3cloud.com/SAMLAuth/Post" 

	xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"&gt;

	&lt;saml:Issuer xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"&gt;https://ALIAS.tier3cloud.com/SAMLAuth&lt;/saml:Issuer&gt;

	&lt;Signature xmlns="http://www.w3.org/2000/09/xmldsig#"&gt;

	  &lt;SignedInfo&gt;

		&lt;CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /&gt;

		&lt;SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" /&gt;

		  &lt;Reference URI="URI"&gt;

		   &lt;Transforms&gt;

		      &lt;Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" /&gt;

		      &lt;Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"&gt;

			&lt;InclusiveNamespaces PrefixList="#default samlp saml ds xs xsi" xmlns="http://www.w3.org/2001/10/xml-exc-14n#"/&gt;

		      &lt;/Transform&gt;

		    &lt;/Transforms&gt;

		    &lt;DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1" /&gt;

		    &lt;DigestValue&gt;VALUE&lt;/DigestValue&gt;

		  &lt;/Reference&gt;

	  &lt;/SignedInfo&gt;

  	&lt;SignatureValue&gt;VALUE&lt;/SignatureValue&gt;

	&lt;KeyInfo&gt;

	   &lt;X509Data&gt;

	     &lt;X509Certificate&gt;CERTIFICATE&lt;/X509Certificate&gt;

	   &lt;/X509Data&gt;

        &lt;/KeyInfo&gt;

        &lt;/Signature&gt;

	&lt;samlp:NameIDPolicy AllowCreate="true" /&gt;

&lt;/samlp:AuthnRequest&gt;

</pre>
  </li>
  <li>If the SAML request is successfully processed by the ADFS server, then ADFS sends a SAML response that the CenturyLink Cloud Control Portal uses to log in the federated user.
    <br />
    <br />
    <pre>&lt;samlp:Response ID="--ID--" 

	Version="2.0" 

	IssueInstant="2012-12-06T22:22:35.344Z" 

	Destination="https://ALIAS.tier3cloud.com/SAMLAuth/Post" 

	Consent="urn:oasis:names:tc:SAML:2.0:consent:unspecified" 

	InResponseTo="ID" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"&gt;

	&lt;Issuer xmlns="urn:oasis:names:tc:SAML:2.0:assertion"&gt;http://tier3samldemo.com/adfs/services/trust&lt;/Issuer&gt;

	&lt;samlp:Status&gt;

	  &lt;samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success" /&gt;

	&lt;/samlp:Status&gt;

	&lt;Assertion ID="ID" IssueInstant="2012-12-06T22:22:35.303Z" Version="2.0" xmlns="urn:oasis:names:tc:SAML:2.0:assertion"&gt;

	&lt;Issuer&gt;http://tier3samldemo.com/adfs/services/trust&lt;/Issuer&gt;

	   &lt;ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#"&gt;

	     &lt;ds:SignedInfo&gt;

		&lt;ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /&gt;

		&lt;ds:SignatureMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1" /&gt;

		&lt;ds:Reference URI="URI"&gt;

		   &lt;ds:Transforms&gt;

		     &lt;ds:Transform Algorithm="http://www.w3.org/2000/09/xmldsig#enveloped-signature" /&gt;

		     &lt;ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#" /&gt;

		   &lt;/ds:Transforms&gt;

		   &lt;ds:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/&gt;

		   &lt;ds:DigestValue&gt;VALUE&lt;/ds:DigestValue&gt;

		&lt;/ds:Reference&gt;

		&lt;/ds:SignedInfo&gt;

		  &lt;ds:SignatureValue&gt;VALUE&lt;/ds:SignatureValue&gt;

		  &lt;KeyInfo mlns="http://www.w3.org/2000/09/xmldsig#"&gt;

		    &lt;ds:X509Data&gt;

		      &lt;ds:X509Certificate&gt;CERTIFICATE&lt;/ds:X509Certificate&gt;

		    &lt;/ds:X509Data&gt;

		  &lt;/KeyInfo&gt;

	    &lt;/ds:Signature&gt;

	    &lt;Subject&gt;

		&lt;NameID&gt;rseroter@tier3samldemo.com&lt;/NameID&gt;

	 	&lt;SubjectConfirmation Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"&gt;

		&lt;SubjectConfirmation Data InResponseTo="ID" 

			NotOnOrAfter="2012-12-06T22:27:35.346Z" 

			Recipient="https://ALIAS.tier3cloud.com/SAMLAuth/Post" /&gt;

		&lt;/SubjectConfirmation&gt;

	     &lt;/Subject&gt;

	     &lt;Conditions NotBefore="2012-12-06T22:22:34.417Z" NotOnOrAfter="2012-1206T23:22:34.417Z"&gt;

		&lt;AudienceRestriction&gt;

		  &lt;Audience&gt;https://ALIAS.tier3cloud.com/SAMLAuth&lt;/Audience&gt;

		&lt;/AudienceRestriction&gt;

	     &lt;/Conditions&gt;

	     &lt;AuthnStatement AuthnInstant="2012-12-06T22:22:33.401Z" SessionIndex="ID"&gt;

		&lt;AuthnContext&gt;

		  &lt;AuthnContextClassRef&gt;urn:federation:authentication:windows&lt;/AuthnContextClassRef&gt;

		&lt;/AuthnContext&gt;

	     &lt;/AuthnStatement&gt;

	  &lt;/Assertion&gt;

&lt;/samlp:Response&gt;

</pre>
  </li>
  <li>The user experience when clicking that button is that the user is prompted for credentials (if the user is not hitting the website from within the domain itself) and once provided, the user is automatically logged into the CenturyLink Cloud portal. <strong>Because they used Single Sign On and SAML, they did NOT have to enter their CenturyLink Cloud account credentials, but rather, were able to use their regular network credentials.</strong>
    <br
    />
    <br /><img src="https://t3n.zendesk.com/attachments/token/jkuvvwgrukqohgn/?name=saml37.png" alt="saml37.png" />
  </li>
</ul>