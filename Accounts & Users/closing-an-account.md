{{{
  "title": "Closing Your Account",
  "date": "08-19-2018",
  "author": "Derek Jansen",
  "keywords": ["terminate", "account"],
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview
We're sorry to see you go. To make sure your off-boarding experience is as easy as possible, follow the steps below. Please be aware that it's not possible to recover an account or the associated assets after the account is deleted. Proceed cautiously to ensure you've recovered all data before proceeding to deletion.

### Exceptions
- Cloud Term Commitment Customers: If you have a cloud term commitment, please contract your sales representative to execute a terminate service order.

### Detailed Steps
1. Ascertain all the services in use created by the account. Viewing the account's [Usage History][1] can help with this.
2. Retrieve the data from those services. If you need help extracting a server or other data, you can request a billable [Service Task][2].
3. Use the Control Portal or [API][3] to delete any actively billed services.
    - __Services not deleted may accrue further charges before an account is completely deleted (eg, server storage).__ Confirmation of account closure by the CenturyLink Cloud team doesn't necessarily mean that no further charges will accumulate, so you should ensure all services have been deleted __before__ requesting account closure.
    - The account's OpenVPN server and network can't be deleted and can safely be ignored. These reside in the account's primary data center and aren't billed as they come with the account by default. The OpenVPN server will follow [platform naming conventions][4] using the name "VPN" (eg, VA1ABCDVPN01).
4. Submit the account closure request by navigating to the [Account Profile/Info page][5] and clicking the "request to close" link.
    - This link immediately generates a ticket for account closure __without__ an additional confirmation prompt. If you don't receive a confirmation by a member of the CenturyLink Cloud team after 1 hour, please email [help@ctl.io][6] or [submit a separate ticket][7] to verify the closure request was sent.
    - There's no guarantee that any server data or configurations can be retrieved after this point.
    ![Close Account](../images/close-your-account.png)

### Final Invoice
After the close of the current month, you'll receive your final invoice from CenturyLink.

[1]: https://control.ctl.io/Organization/payment/ledger
[2]: https://www.ctl.io/service-tasks
[3]: https://www.ctl.io/api-docs
[4]: https://www.ctl.io/knowledge-base/servers/server-naming-convention
[5]: https://control.ctl.io/organization/account
[6]: mailto:help@ctl.io
[7]: https://www.ctl.io/knowledge-base/support/using-the-help-desk-web-ui
