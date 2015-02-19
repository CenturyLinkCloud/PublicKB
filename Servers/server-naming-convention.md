{{{
  "title": "Server Naming Convention",
  "date": "1-2-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": false
}}}

All CenturyLink Cloud servers follow a standard naming convention that incorporates a number of pieces of information to make a unique key.

![Server Naming](https://t3n.zendesk.com/attachments/token/6ZkqLpC49JT7NGiB5GmYWPzfL/?name=Screen+Shot+2015-01-22+at+7.56.50+AM.png)

* **Datacenter**: 3 character alphanumeric code associated with the cloud datacenter.  Always two letters and one number. (system defined)
* **Account Alias**: 2 to 5 letter alphanumeric code associated with the account that owns the server.  Account owner selects the account alias when creating the account and afterwards this is immutable.
* **Name**: 1 to 6 character alphanumeric code associated with the server itself.  User selects this when deploying the server.  If deploying a Blueprint a default value will be provided.
* **Incrementor**: 2 character numeric code (up to 99) beginning with 01 and incrementing each time a server with this naming prefix is deployed to guarantee a globally unique naming key within the cloud portal. (system defined)

###Example

![Example name](https://t3n.zendesk.com/attachments/token/wqzYkzdmcv7H9hsaV1Shj7puD/?name=Screen+Shot+2015-01-22+at+7.57.03+AM.png)

###Considerations
The name associated with a server in the control portal need not match the actual server name at the OS, internal DNS, or external DNS levels.  On initial deployment the server's OS name and control portal name match.
When servers are moved between datacenters as a Service Task they are renamed to match the new geography
