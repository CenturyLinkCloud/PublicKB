{{{
  "title": "Wordpress SMTP Configuration",
  "date": "04-29-2015",
  "author": "Bill Burge",
  "attachments": [],
  "contentIsHTML": false
}}}

Out of the box, WordPress sends email using the [PHP mail()](http://php.net/manual/en/function.mail.php "PHP mail ()") function. This function is unauthenticated and, for this reason, CenturyLink Cloud WordPress does not allow this functionality and does not include an alternate SMTP relay.  In order to send WordPress user emails, like password resets, you will first need to configure a SMTP server using one of the many freely available plugins found on [WordPress.org](https://wordpress.org/plugins/ "WordPress.org")

[Postman SMTP Mailer](https://wordpress.org/plugins/postman-smtp/ "Postman SMTP Mailer") is one example capable of utilizing many freely available SMTP servers as well as your enterprise's own.

---
In this example, Gmail will be used as the SMTP Relay and assumes the following:

1. Ownership of a Gmail account.
2. Activation of the the [Less Secure Apps](https://www.google.com/settings/security/lesssecureapps "Gmail Less Secure Apps") functionality of Gmail.
3. A working knowledge of how to install WordPress plugins to a CenturyLink Cloud WordPress site following the Knowledgebase article for [WordPress Plugin Installation](wordpress-plugin-installation.md).

---

**1. Download and install [Postman SMTP Mailer](https://wordpress.org/plugins/postman-smtp/ "Postman SMTP Mailer") to your WordPress site.**

**2. Activate Postman SMTP**

![](../images/wp_postman_smtp/wp_postman_smtp01.png "wp_postman_smtp01.png")

**3. Browse to Settings > Postman SMTP**

![](../images/wp_postman_smtp/wp_postman_smtp02.png "wp_postman_smtp02.png")

**4. Select configure manually.**

![](../images/wp_postman_smtp/wp_postman_smtp03.png "wp_postman_smtp03.png")

**5. Update the following settings with specifics for your SMTP Relay and click _Save Changes_.**

Transport Settings:

* Authentication
* Security
* Outgoing Mail Server Hostname
* Outgoing Mail Server Port

Authentication:

* Username
* Password

![](../images/wp_postman_smtp/wp_postman_smtp04.png "wp_postman_smtp04.png")

**6. Select Send a Test Email.**

![](../images/wp_postman_smtp/wp_postman_smtp05.png "wp_postman_smtp05.png")

**7. Input a Recipient Email Address and click Next.**

![](../images/wp_postman_smtp/wp_postman_smtp06.png "wp_postman_smtp06.png")

**8. If successful you will see the following success message.**

![](../images/wp_postman_smtp/wp_postman_smtp07.png "wp_postman_smtp07.png")



