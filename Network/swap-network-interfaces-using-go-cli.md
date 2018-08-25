{{{
  "title": "Add or Remove Network Interface to Server using Go CLI",
  "date": "3-28-2016",
  "author": "Chris Little",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Customers may wish to implement additional network interfaces (NICs) on CenturyLink Cloud [Virtual](//www.ctl.io/servers/) or [Bare Metal](//www.ctl.io/bare-metal/) Servers.  To implement this CenturyLink has provided an API to [add](//www.ctl.io/api-docs/v2/#servers-add-secondary-network) or [remove](//www.ctl.io/api-docs/v2/#servers-remove-secondary-network) network interfaces.  Customers who wish to simply use a CLI tool to implement these additional interfaces can leverage our [Go CLI.](//github.com/CenturyLinkCloud/clc-go-cli)
