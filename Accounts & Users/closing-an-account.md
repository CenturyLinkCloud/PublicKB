{{{
  "title": "Closing Your Account",
  "date": "09-10-2019",
  "author": "Derek Jansen",
  "keywords": ["terminate", "account"],
  "attachments": [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Overview
We're sorry to see you go. To make sure your off-boarding experience is as easy as possible, follow the steps below. Please be aware that it's not possible to recover an account or the associated assets after the account is deleted. Proceed cautiously to ensure you've recovered all data before proceeding to deletion.

### Prerequisites
- The Control Portal user must have [Account Administrator privileges][1] in order to perform an account closure.

### Exceptions
- Cloud Term Commitment Customers: If you have a cloud term commitment, please contact your sales representative to execute a terminate service order.

### Detailed Steps
1. Ascertain all the services in use created by the account. Viewing the account's [Usage History][2] can help with this.
2. Retrieve the data from those services. If you need help extracting a server or other data, you can request a billable [Service Task][3].
3. Use the Control Portal or [API][4] to delete any actively billed services.
    - __Services not deleted may accrue further charges before an account is completely deleted (e.g. server storage).__ Confirmation of account closure by the Lumen Cloud team doesn't necessarily mean that no further charges will accumulate, so you should ensure all services have been deleted __before__ requesting account closure.
    - The account's OpenVPN server and network can't be deleted and can safely be ignored. These reside in the account's primary data center and aren't billed as they come with the account by default. The OpenVPN server will follow [platform naming conventions][5] using the name "VPN" (e.g. VA1ABCDVPN01).
4. Please email [help@ctl.io][7] or [submit a separate ticket][8] to request the account to be closed.
    - There's no guarantee that any server data or configurations can be retrieved after this point.

### Final Invoice
If you have completely deleted the account resources __before__ requesting account closure, you'll receive your final invoice from Lumen after the close of the current month.

However, if you __didn't__ completely delete the account resourses as instructed in the steps above, they will continue to accrue charges until the account is finally deleted. This means you will receive an invoice for the current month __and__ an invoice for the resource usage accruing into the next month.

[1]: https://www.ctl.io/knowledge-base/accounts-&-users/user-permissions
[2]: https://control.ctl.io/Organization/payment/ledger
[3]: https://www.ctl.io/service-tasks
[4]: https://www.ctl.io/api-docs
[5]: https://www.ctl.io/knowledge-base/servers/server-naming-convention
[6]: https://control.ctl.io/organization/account
[7]: mailto:help@ctl.io
[8]: https://www.ctl.io/knowledge-base/support/using-the-help-desk-web-ui
[9]: ../images/close-your-account.png
