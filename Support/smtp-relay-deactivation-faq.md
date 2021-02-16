{{{
  "title": "Retirement of the SMTP Relay Service",
  "date": "9-23-2016",
  "author": "Matt Schwabenbauer",
  "attachments": []
}}}

### Description

In September 2016, Lumen announced that we would be retiring our SMTP Relay Service by the end of the year. After hearing from customers about the challenges they faced when transitioning to a new service, we have decided to extend our End of Life (EOL) date to February 14, 2017. This way, we are able to ensure that our customers have enough time to carry out the necessary testing and implementation plans to facilitate successful migrations to alternative SMTP delivery services.

### Deactivation Date

The SMTP Relay Service is being End of Serviced (EOS) on December 1, 2016 with an End of Life (EOL) on February 14, 2017. This means that customers have been unable to provision new SMTP Relay services since of December 1, 2016, but existing services will remain functional until February 14, 2017.

### What exactly is Changing?

* We will be deactivating the SMTP Relay Service on February 14, 2017. At this time, customers will be unable to send e-mail from the service.
* We recommend that existing SMTP Relay customers migrate to an alternative provider before the deactivation date.
* Recommendations for alternative SMTP relay providers are listed at the bottom of this document.

### Why is this change happening?

Customers choose Lumen as a technology service provider because of our cutting edge public cloud, private cloud, and networking products. If we feel that our customers are not receiving the best possible business value from any of our products, then we would rather partner with alternative service providers to enable a better customer experience.

After deciding that our SMTP Relay Service was one such product that was not living up to our expectations, we took action to enable our customers with preferable e-mail service providers as opposed to our offering. Now that our customers have had time to move to an alternative product, we are decommissioning our SMTP Relay Service.

### Why have we chosen to deactivate our service instead of improving it?

We feel that deactivating our service is the best option for our customers:

* We don't have a large amount of customers actively using our SMTP Relay Service.
* We feel our SMTP Relay Service has not resulted in a great customer experience.
* Based on input from our customers via feature requests and direct conversations, there are other product improvements that we feel are more important to the majority of our customers than improving our SMTP Service.

### What does this mean for me?

If you are a customer that actively uses our SMTP Relay Service, you will need to migrate to an alternative service by the February 14 deactivation date. If you have not moved to an alternative service by the deactivation date, your e-mail will no longer be delivered by our service.

### What new method should I use to send e-mail?

Since we aren't offering a replacement service, you must migrate to an alternative solution to continue to send e-mail. There are many e-mail delivery services or software solutions that can facilitate the necessary functionality. You are free to choose whatever method you wish for sending email. In effort to help you with this process, we are recommending a few options for your consideration.

#### Use an external email service

There are many great external SMTP Relay services available that provide customers with a wide range of functionality that meet and exceed our current SMTP feature list. A few of these services are:

* [SendGrid](https://sendgrid.com/)
* [MailChimp with Mandrill Addon](https://www.mandrill.com/)
* [MailJet](https://www.mailjet.com/)
* [Dyn](http://dyn.com/email-delivery/)

#### Use Lumen Servers + Software to send emails

For customers that would like more control over their e-mail delivery functionality, they can configure servers to send email manually as opposed to using a service. This requires additional manual overhead and is only recommended if there are specific business requirements that other e-mail delivery services do not offer. There are plenty of guides on the Internet that explain how to do this. For example:

* [CL Blueprint & Halon Software](https://www.ctl.io/knowledge-base/ecosystem-partners/marketplace-guides/getting-started-with-halon-partner-template/) - Use a Lumen Cloud Blueprint to install the Halon SMTP Software for sending emails.
* [Windows & IIS](https://support.office.com/en-us/article/How-to-configure-IIS-for-relay-with-Office-365-eb57abd2-3859-4e79-b721-2ed1f0f579c9?ui=en-US&rs=en-US&ad=US) - Setup a Windows SMTP server to send emails.
* [Linux & PostFix](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-14-04) - Setup the Postfix SMTP email server on Linux to send emails.

### Summary

Lumen will be decommissioning our SMTP Relay Service on February 14, 2017. If you have any questions about the retirement of our SMTP Relay Service, or if you need assistance with your transition to an alternative service, please contact us at [help@ctl.io](mailto:help@ctl.io).
