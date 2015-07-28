{{{
  "title": "Using SAML for Single-Sign-On to the CenturyLink Platform Control Portal with Windows 2012 R2",
  "date": "7/21/2015",
  "author": "Kelly Malloy",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
The purpose of this guide is to provide step by step instructions for configuring Windows 2012 R2 with ADFS 3.0 to authenticate with CenturyLink Cloud SAML.  For simplicity sake, a single server will be used for directory services and certificate services.  Depending on your company's requirements you may choose to use multiple servers for the various roles and services that are required.  If you choose to segregate the roles and services this guide will still provide a useful instruction set for configuration guidelines.

### Description
CenturyLink Cloud supports the use of Security Assertion Markup Language (SAML) for exchanging user authentication data as XML between trusted parties. This industry standard protocol empowers our customers to use their **own** identity management system for authenticating users of the CenturyLink Cloud Control Portal.

SAML has three main parties: the user, the identity provider (IdP), and service provider (SP). The IdP is the repository that holds identity information. The SP is the party that wants to authenticate a particular user who is using an application.

The SAML flow occurs as shown below.

  ![SAML Flow](../images/adfs_saml_2012_01.png)

  Specific steps in this flow are:

1. The enterprise user of the CenturyLink Cloud hits a URL that is dedicated to their account. The user is asked how they would like to log into the system and they choose SAML.

2. The web application contacts the CenturyLink Cloud SAML service to initiate the SAML message exchange.

3. The CenturyLink Cloud SP sends a digitally signed SAML authentication request to the enterprise IdP. This IdP takes the user's Kerberos token and validates them as a user on the enterprise network.

4. The IdP returns a signed (and optionally, encrypted) SAML authentication response message to the CenturyLink Cloud SP. This message includes a Name ID assertion and that value is matched to a User record in the CenturyLink Cloud.

5. The user is logged into the CenturyLink Cloud and operates under the roles and permissions assigned to their CenturyLink Cloud user account.

The steps below walk through the process of building an entire SSO and SAML scenario based on Microsoft Active Directory Federation Services as the IdP proxy. If you already have an identity provider, you can skip to step 3 where trust is established between CenturyLink Cloud and the IdP.

### Prerequisites
* Domain Administrator permissions in Active Directory  
* Account Administrator Role in the CenturyLink Cloud Control Panel
* A valid public domain name and DNS record for name resolution.  Tip: If you do not have access to a valid public domain name there will be an Additional Information section at the end provided that will enable you to test this scenario, without using valid public domain names using hosts file entries in your operating system.  
* Private SSL certificates signed by the Certificate Authority in this guide will be leveraged.  Organizations should use third party trusted certificates for production use, just Substitute your trusted certificates in the appropriate step.  

### Provision server to act as Identity Provider

1. Log into the CenturyLink Cloud Control Portal and choose to create a new Blueprint. This takes you to the Blueprint Designer wizard.

    ![Blueprint Menu](../images/adfs_saml_2012_02.png)

2.  Using Blueprint Designer you have several choices for versioning, privacy settings, etc.  In this step you can choose the settings that are appropriate for your intended use.  There is one required field, Description.  Populate with a description that is accurate for your use.

3.  Add a single Windows 2012 R2 server to the Blueprint (you may have to scroll down to see this option).  Name the server and accept the sizing defaults (2 CPU/4GB RAM).  In this example we have used server name DE1CCTSADFS301.  Within the "Add Server Tasks" section, choose "execute script".  Add "Install Active Directory on Windows 2012 (1 of 2) [Primary Node]".  Under "run task", choose "Reboot Server".  Under "execute script", choose "Install IIS 8 on Windows".  Under "run task" choose "Add Public IP".  Select the option for "HTTPS" which uses port 443 for communication. Click "Add Global Tasks". IMPORTANT: Click the "+add" button in this window after the choices have been made. Then, click "next, tasks & order".

	The Active Directory packages give us a custom domain to work with, and an identity directory for our user records. Microsoft Internet Information Services (IIS) provides a web application host for the Active Directory Federation Services (ADFS) web services used later in this configuration guide.

    ![Blueprint Designer](../images/adfs_saml_2012_03.png)

4.  No steps required.  Click "next, review"

5.  Click "submit for publishing"  Note: Blueprint may take up to 15 mins to create.

	Once the Blueprint has been published, navigate to the Blueprint Library, use the "Refine Results" column to find your Blueprint, and select your Blueprint by clicking on it.  Click the "Deploy Blueprint" button to initiate the provisioning process.

    ![Deploy Blueprint](../images/adfs_saml_2012_04.png)

6. On the "Customize Blueprint" step of the deployment wizard, the user is asked to provide deploy-time build parameters such as the server password, host network, and Active Directory domain name. Note a few key values: first, the **Primary DNS** value *must be equal to the name of the server being created*. Recall that we already added DNS services to the server itself, so THIS is the domain that the new server should use for resolution. The **Domain Name** parameter typically contains the full name of the domain (including a suffix such as ".com") while the Net BIOS Name omits the suffix.

    ![Server Build](../images/adfs_saml_2012_05.png)

7. After clicking "Next: Step 2" you will be taken to the "review blueprint" page. Once you have confirmed your choices, complete the deployment process by clicking "deploy blueprint", and wait for the new server to be built by the CenturyLink Cloud Blueprint engine. It may take up to 20 minutes and you can monitor progress in the queue.

    ![Blueprint Queue](../images/adfs_saml_2012_06.png)

8. Locate the server that has been deployed by clicking "Servers" within the Control Panel.  View the information within the "Server Info" section, to record the public and private IP addresses for your new server.

    ![Confirm Server Details](../images/adfs_saml_2012_07.png)

### Install and configure Active Directory Federation Services

1. Use the OpenVPN client software or Tunnelblick client software to connect to the CenturyLink Cloud network. Once connected, create a Remote Desktop session to your server using the private IP address recorded above. In the Server Manager, confirm the installation of DNS, Active Directory, and IIS.

    ![Confirm Roles](../images/adfs_saml_2012_08.png)

2. In order to issue certificates easily from this server, install the **Active Directory Certificate Services** role on the server using the "Add roles and features" wizard. Choose "Role based or feature based installation". Accept the defaults for the remaining installation choices but make sure the box is checked for "Active Directory Certificate Services" on the "Server Roles" step. (see screenshot)  Click the "Close" button once complete.

    ![Certificate Services](../images/adfs_saml_2012_09.png)

3. When the role installation has been completed additional configuration will now be required.  A link to the required configuration will be shown in Server Manager - AD CS.  Choose the Setup Type as "Enterprise CA".  Choose the CA Type as "Root CA".  Choose to create a new private key.  For Cryptography use the default provider and encryption settings of "Key length 2048" and hash algorithm "SHA1".  CA Name, Validity Period, and Certificate Database can use default settings.  Click the "Configure" button to complete.

    ![Configure Certificate Services](../images/adfs_saml_2012_10.png)

4. Open IIS Manager via the "Tools" menu, click the host name, and locate the **Server Certificates** feature.

    ![Server Certificates](../images/adfs_saml_2012_11.png)

5. Double-click the **Server Certificates** icon and select the option on the right to **Create Domain Certificate**. Use this wizard to complete all fields.  In this example we will be using a common name of clcsamldemo.falconinfosec.com.  The common name will need to match the external DNS A record you create for your servers public IP address.  In this example we have created an A record of clcsamldemo.falconinfosec.com mapping to external IP address 66.155.94.111 which we verified in the Server Info tab in the Control Panel.  Click "Next".

    ![Create Certificate](../images/adfs_saml_2012_12.png)

6. On the next page of the wizard, choose the Online Certificate Authority and set a friendly name for the certificate.  It is useful to set a friendly name that corresponds with information that will help an administrator easily identify basics about this certificate, especially if an organization has numerous certificates. Click "Finish".

    ![Friendly Name](../images/adfs_saml_2012_13.png)

7. Within IIS Manager, click on "Sites" in the left column to expand the list, select the "Default Web Site", Right click to "Edit Bindings", or use the right menu option to do the same.  Click "Add".  Select Type as "https".  In the SSL certificate drop down box, select the certificate previously created.  Click "OK".  Click "Close".

    ![Add Site Binding](../images/adfs_saml_2012_14.png)

8. Launch Active Directory Users and Computers via the "Tools" menu and create a service account for ADFS.  This service account does not need special permissions, a normal user account is permitted.  In this example we have created an account named samldemo.  Create another account that will be used for authenticating a user against CenturyLink Cloud Control Portal.  In this example we have created an account named kellytest.  The full User Principal account name for this account is kellytest@ccts.dom.

	Windows 2012 has ADFS included.  Return to Server Manager to Add the "Active Directory Federation Services" Role via the "Add roles and features" wizard. Choose "Role based or feature based installation". Accept the defaults for the remaining installation choices but make sure the box is checked for "Active Directory Federation Services" on the "Server Roles" step. (see screenshot below)

    ![Add ADFS Role](../images/adfs_saml_2012_15.png)

9. Once the role has been added select "Configure the federation service on this server", which will be a hyperlink on the "Results" screen.

    ![Configuration Wizard](../images/adfs_saml_2012_16.png)

10. Ensure the option "Create the first federation server in a federation server farm" is selected, click "Next".  Select the appropriate account with domain administrator permissions, click "Next".  Select the correct SSL Certificate from the drop down box.  This will automatically populate the Federation Service Name.  Federation Service Display Name can be customized as desired.  In this example we choose "clcsamldemo".  Click "Next".  Choose the option "Use an existing domain user account or group Managed Service Account"  After selecting this, select the service account created earlier.  Specify the correct account password, click "Next".  Select "Create a database on this server using Windows Internal Database"  Click "Next".  Review your summary, Click "Next".  Click "Configure".  Click "Close", twice.

    ![ADFS Configuration](../images/adfs_saml_2012_17.png)

### Create trust relationship with CenturyLink Cloud

1. Launch "AD FS Management" from Administrative "Tools" menu.  Expand "Trust Relationships", right click on "Relying Party Trusts" and select "Add Relying Party Trust", or use the right menu to do the same.  This part of the configuration uses a public certificate from CenturyLink Cloud for the local IdP so the system recognizes the SAML authentication request in order to validate the inbound signature.

    ![Add Party Trust](../images/adfs_saml_2012_18.png)

2. Click "Start".  Select the option "Enter data about the relying party manually".  Click "Next".

    ![Enter Data Manually](../images/adfs_saml_2012_19.png)

3. Enter a display name in order to easily identify this relying party, something like "CenturyLink Cloud Control Portal".  Click "Next".  Select "AD FS Profile", click "Next". Click "Next". Click "Next".  At the Configure Identifiers step, enter the following value for "Relying party trust identifier", <code>https://alias.cloudportal.io/SAMLAuth</code>.  Substitute "alias" with your CenturyLink Cloud Control Portal alias.  In this example we will use ccts **Note that this value is case-sensitive!** Click "Add", click "Next". Ensure "Multi-factor" is set to "disabled", click "Next".  Ensure "Permit all users" is selected, click "Next".

    ![Configure Identifiers](../images/adfs_saml_2012_20.png)

4. Finish the wizard.  On the last wizard page, click the checkbox to **Open the Edit Claims Rules dialog.** Here is where we define which Active Directory values (claims) map to the SAML attributes sent back to CenturyLink Cloud.

    ![Select Rule Template](../images/adfs_saml_2012_21.png)

5. Click "Add Rule".  Ensure "Send LDAP Attributes as Claims" is selected. Click "Next".

	Enter a Claim rule name such as Map UPN to Name ID.  Set the Attributes store to Active Directory. choose the **User-Principal-Name** as the **LDAP Attribute**, set the **Outgoing Claim Type** to **Name ID**.  Click "Apply". Click "Ok".

    ![Configure Claim Rule](../images/adfs_saml_2012_22.png)

6. Open Notepad and paste in the contents of this entire text string below, omitting no characters.

    ```
    -----BEGIN CERTIFICATE-----
    MIIFWTCCBEGgAwIBAgIRAIaoEvXi1F232F/HCw8kRFQwDQYJKoZIhvcNAQELBQAw
    gZAxCzAJBgNVBAYTAkdCMRswGQYDVQQIExJHcmVhdGVyIE1hbmNoZXN0ZXIxEDAO
    BgNVBAcTB1NhbGZvcmQxGjAYBgNVBAoTEUNPTU9ETyBDQSBMaW1pdGVkMTYwNAYD
    VQQDEy1DT01PRE8gUlNBIERvbWFpbiBWYWxpZGF0aW9uIFNlY3VyZSBTZXJ2ZXIg
    Q0EwHhcNMTUwMjA5MDAwMDAwWhcNMTkwMjA5MjM1OTU5WjBeMSEwHwYDVQQLExhE
    b21haW4gQ29udHJvbCBWYWxpZGF0ZWQxHjAcBgNVBAsTFUVzc2VudGlhbFNTTCBX
    aWxkY2FyZDEZMBcGA1UEAxQQKi5jbG91ZHBvcnRhbC5pbzCCASIwDQYJKoZIhvcN
    AQEBBQADggEPADCCAQoCggEBAJ1d0VSSzywVLVAxVxHPLSdMcH5xdPBkPE2VELD1
    2BMhyuhS2TQ7D8MAQFLS0FZjTXkOIRdccWUU9tZw3sQRxwDSgMc4xXrQAIgPxVgr
    Bwfqtm5a4+bJqdTHpQzSv3KcsnEl+Ha/nq7mydjRQ0Xu0iETON6JWAd8Wtzw7pZo
    LNkSn7WarhG9orwh03Q+vzPMnowR0wrVqTXF9mjFqyPuGAwgtO45BfRPobc0FSEt
    RuYiIlfQ1eZCXfD/Mg4uh+kIOe8LXd2GokZ3vdvI4zlsgUe5FmRqAFoTtX4MNSgt
    R5vrDcilTzbRFJ+BwOPuwOy4j8xiHqpsNUWPxDLdD6GVfj0CAwEAAaOCAd0wggHZ
    MB8GA1UdIwQYMBaAFJCvajqUWgvYkOoSVnPfQ7Q6KNrnMB0GA1UdDgQWBBQ83AlA
    ZTxRkOtGeS94uIwMrtDaEDAOBgNVHQ8BAf8EBAMCBaAwDAYDVR0TAQH/BAIwADAd
    BgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwTwYDVR0gBEgwRjA6BgsrBgEE
    AbIxAQICBzArMCkGCCsGAQUFBwIBFh1odHRwczovL3NlY3VyZS5jb21vZG8uY29t
    L0NQUzAIBgZngQwBAgEwVAYDVR0fBE0wSzBJoEegRYZDaHR0cDovL2NybC5jb21v
    ZG9jYS5jb20vQ09NT0RPUlNBRG9tYWluVmFsaWRhdGlvblNlY3VyZVNlcnZlckNB
    LmNybDCBhQYIKwYBBQUHAQEEeTB3ME8GCCsGAQUFBzAChkNodHRwOi8vY3J0LmNv
    bW9kb2NhLmNvbS9DT01PRE9SU0FEb21haW5WYWxpZGF0aW9uU2VjdXJlU2VydmVy
    Q0EuY3J0MCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5jb21vZG9jYS5jb20wKwYD
    VR0RBCQwIoIQKi5jbG91ZHBvcnRhbC5pb4IOY2xvdWRwb3J0YWwuaW8wDQYJKoZI
    hvcNAQELBQADggEBACmkIX6Elg3wcJi8Is7bp3fpDfeGPXfIFsSCXp5dNyuAXkCP
    DKhpCnXZqmS8uWOGlU5H9rIn4rqlbRg4/t7Wxca9Gxi6FQ+D0+LO9ljQFN+qgqc0
    FgyEgx9AN4lf1wZpJ782v83NXIVt/qiRtJueCKhIWnh2PmgbO7JwDdk2HNFc5dGP
    e1LteC6ByXx9mHAsBX366IlcoNOpBlQjj9mX0atCMrlW6q6kYrQ1ZgPEf+o8TBHR
    lNaLaTC0C8pixcdubTIkPNs3cQijzsxkyGvivsSkkAPTZe3AzdvHeSqNIrKUjo+j
    bdS+NhURkFTdtV0/YCSvbAukw6l4WY8ZqaJYcCk=
    -----END CERTIFICATE-----
    ```

7. Save your notepad session with .cer extension.  In this example we are saving the file name as control.cer

	Under "AD FS Relying Party Trusts" right click the "Relying Party Trusts" you just created, and choose "Properties", or use the right menu to do the same. Switch to the **Signatures** tab, and add the certificate you created above.

    ![Properties](../images/adfs_saml_2012_23.png)

8. Switch to the **Endpoints** tab and add a **SAML Assertion Consumer** with a **POST** binding and set the URL to <code>https://alias.cloudportal.io/SAMLAuth/Post</code>. Once again, this value is case-sensitive.  Substitute "alias" with your CenturyLink Cloud Control Portal alias.  In this example we will use "ccts".  Click "Ok".

    ![Add Endpoint](../images/adfs_saml_2012_24.png)

9. Switch to the **Advanced** tab, change the **Secure Hash Algorithm** to **SHA-1**. Click "Ok".

### Configure CenturyLink Cloud account with SAML settings

1. Log into the CenturyLink Cloud Control Portal and under **Account** menu, select the **Users** tab. Switch to the **Authentication** sub-section and check the box labeled **SAML Authentication**. This opens up a series of configuration settings.

    ![SAML Config](../images/adfs_saml_2012_25.png)

2. For the **SSO IdP URL**,set the ADFS service URL. This includes the full public domain name of the ADFS server. In this example we are using the URL https://clcsamldemo.falconinfosec.com/adfs/ls/  For the **SLO IdP URL** set the URL as indicated in the CenturyLink Cloud Control Portal.  The URL for this test account is https://ccts.cloudportal.io/SAMLAuth/LogoutPost

    ![SAML SSO URL](../images/adfs_saml_2012_26.png)

3. The next required field is the **Signing Certificate Key**.  Return to the ADFS server, view the AD FS Management Console, and find the **Certificates** directory under the **Service** node. Notice the **Token-signing** certificate.

    ![Token Signing](../images/adfs_saml_2012_27.png)

4. Right click the certificate, choose "View Certificate", or use the right menu to do the same.  Switch to the **Details** tab and select **Copy to File**. Click "Next". Export a **Base-64 encoded X.509** certificate.  Click "Next".

    ![Export](../images/adfs_saml_2012_28.png)

5. Save the file to a known location on the file system. Open the file with a text editor and copy all of the text between the "Begin Certificate" and "End Certificate" indicators.

    ![Cert](../images/adfs_saml_2012_29.png)

6. Paste this string of text into the **Signing Certificate Key** field in the CenturyLink Cloud Control Portal. Click the **Save** button and switch back to the **Users List** view. Select the user that you want to perform SSO with, and locate the **SAML Username** field. Since we chose above to use the "Active Directory User Principal Name" as the lookup value to the CenturyLink Cloud account, we must plug in the User Principal Name associated with this user.  in the example the User Principal Name is kellytest@ccts.dom.  Click "Save".

    ![SAML User](../images/adfs_saml_2012_30.png)

### Exchange SAML messages to perform Single Sign On

1. Go to a web browser and plug in <code>https://alias.cloudportal.io</code>. Here you can sign in via CenturyLink Cloud Portal username and password, or choose the **Sign In Using SAML** option. If you choose the latter, then the CenturyLink Cloud SAML service redirects the browser to the URL specified in the account's **SAML SSO URL** setting.

    ![Sign In Page](../images/adfs_saml_2012_31.png)

2. The user experience when clicking the Sign In Using SAML button is that the user is prompted for credentials (if the user is not hitting the website from within the domain itself) and once provided, the user is automatically logged into the CenturyLink Cloud portal. **Because they used Single Sign On and SAML, they did NOT have to enter their CenturyLink Cloud account credentials, but rather, were able to use their regular network credentials.  In this example we logged in with User Principal Name kellytest@ccts.dom that we created earlier in this guide.**

### Additional Information

If you do not own the public domain name corresponding to the DNS name of your server, then your testing will fail. To test successfully, change your local machine host file so that the browser translates the domain name to the public IP address of the server. When the SAML request comes in to ADFS, it tries to match the SAML Destination ID (retrieved from the SAML configuration in your CenturyLink Cloud account) to the Federation Service name in the ADFS server.  If the values do not match, then ADFS will return an exception. In order to test this scenario without registering and owning the corresponding public domain name, navigate to your local machine's host file (C:\Windows\System32\Drivers\etc\hosts) and add an entry that maps the public IP address of the server to the DNS name of the server.
