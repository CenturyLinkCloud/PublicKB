{{{ "title": "IPS-API",
        "date": "11-09-2015",
        "author": "Client-Security",
        "attachments": [],
        "contentIsHTML": false,
        "sticky": false }}}

# IPS-API

The IPS-API is a RESTful api.
IPS or Intrusion Prevention Service will require you to have a server and account in the CenturyLink Platform.

## Authentication

In order to use the IPS-API you must retrieve a bearer token from CLC.
This will be used during each of the calls. For more, see the [CLC Authentication](https://www.ctl.io/api-docs/v2/#authentication-login) documentation.

## Headers

To interact with the IPS-API you will need to provide in the headers two fields

|**Header**     |**Value**                  |
|---------------|---------------------------|
|Content-Type   |application/json           |
|Authorization  |Bearer (CLC Bearer Token)  |

## Install

Installs an IPS agent on the designated host.

#### URL

##### Structure

>POST https://api.client-security.ctl.io/ips/api/app/

    {
        "hostName":"serverName",
        "accountAlias":"CLC Account Alias"
    }

##### Content Properties

| **Name**     | **Type** | **Description**                                               | **REQ.**|
|--------------|----------|---------------------------------------------------------------|---------|
|accountAlias  |String    |Short code for a particular account                            |Yes      |
|hostName      |String    |The name of the server that the destination should be set for. |Yes      |

##### Example
    {
        "hostName":"VA1CLCDTEST04",
        "accountAlias":"CLCD"
    }


## Uninstall

Uninstalls an IPS agent from a designated host.

#### URL

##### Structure

>DELETE https://api.client-security.ctl.io/ips/api/app/

    {
        "hostName":"serverName",
        "accountAlias":"CLC Account Alias"
    }

##### Content Properties

| **Name**     | **Type** | **Description**                                               | **REQ.**|
|--------------|----------|---------------------------------------------------------------|---------|
|accountAlias  |String    |Short code for a particular account                            |Yes      |
|hostName      |String    |The name of the server that the destination should be set for. |Yes      |

##### Example
    {
        "hostName":"VA1CLCDTEST04",
        "accountAlias":"CLCD"
    }

## Notification Destination


### Configuration Process via our API

These calls will do all of the operations for configuring, retrieving, updating and deleting a notification destination.
Calls to this operation must include a token acquired from the authentication endpoint.
See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

#### URL

##### Structure

###### Create and Update
>PUT https://api.client-security.ctl.io/ips/api/notifications/{accountAlias}/{serverName}

    {
        "url":{some URL},
        "typeCode":{endpoint type}
    }

###### Retrieve
>GET https://api.client-security.ctl.io/ips/api/notifications/{accountAlias}/{serverName}

###### Delete
>DELETE https://api.client-security.ctl.io/ips/api/notifications/{accountAlias}/{serverName}


#### Request

##### URI Parameters

| **Name**     | **Type** | **Description**                                               | **REQ.**|
|--------------|----------|---------------------------------------------------------------|---------|
|accountAlias  |String    |Short code for a particular account                            |Yes      |
|serverName    |String    |The name of the server that the destination should be set for. |Yes      |

##### Content Properties

| **Name**                | **Type** | **Description**                      | **REQ.** |
|-------------------------|----------|--------------------------------------|----------|
|notificationDestinations |array     | List of Notification Destinations    |Yes       |       

##### Notification Destination Definition

| **Name**  | **Type**  | **Description**                                           | **REQ.** |
|-----------|-----------|-----------------------------------------------------------|----------|
|url        |String     |The URL endpoint for WEBHOOK or SLACK notification.        |No        |
|typeCode   |String     |This is the type of destination.                           |Yes       |
|sysLogSettings|SysLogSettings|This contains all of the options for SYSLOG          |No        |
|emailAddress|String    |This object will contain options for an EMAIL notification |No        |

TypeCode currently consists of: SYSLOG, EMAIL, WEBHOOK and SLACK

##### SysLogSettings Definition
| **Name**  | **Type**  | **Description**                                                 | **REQ.**  |
|-----------|---------- |-----------------------------------------------------------------|-----------|
|ipAddress  |String     |The IP address of customers syslog server                        |Yes        |
|udpPort    |Integer    |The port the syslog is listening on                              |Yes        |
|facility   |Integer    |This is an Integer, 16-23, for descriptions see below.           |Yes        |

Facility is to set the type of program logging messages.
The options are 16-23 for descriptions follow the link: [https://en.wikipedia.org/wiki/Syslog](https://en.wikipedia.org/wiki/Syslog)

* Note: Syslog server IP must reside outside of the UC1 datacenter at this time

##### Example

>PUT http://api.client-security.ctl.io/ips/api/notification/ALIAS/VA1ALIASMYSVR01

    {
        "url": "http://my.slack.webhook",
        "typeCode": "SLACK"
    },
    {
        "url": "http://my.generic.webhook",
        "typeCode": "WEBHOOK"
    },
    {
        "typeCode": "SYSLOG",
        "sysLogSettings":
            {
                "ipAddress": "12345",
                "udpPort": "8081",
                "facility": "16"
            }
    },
    {
        "typeCode": "EMAIL",
        "emailAddress": "youremail@site.com"
    }

The following key-value pairs are sent to the notification destination when an event is triggered. If you are using the generic "WEBHOOK" type for your notifications the following will be sent in json format.
##### Response Object
| **Name** | **Type** | **Description**                                                                     |
|----------|----------|-------------------------------------------------------------------------------------|
|packetSize|int       |Size of the packet which triggered the event                                         |
|rank      |int       |Name of the DPI filter which triggered the event                                     |
|driverTime|Long      |Epoch time the Agent driver recorded at the time of the event                        |
|startTime |Date      |Start time of the event if repeated multiple times                                   |
|endTime   |Date      |End time of the event if repeated multiple times                                     |
|action    |String    |Resulting action of the triggered event                                              |
|data      |String    |Any captured packet data in Base64 encoded format                                    |
|destinationIP|String |Destination IP Address                                                               |
|destinationMAC|String|Destination MAC Address                                                              |
|destinationPort|String|Destination Port                                                                    |
|direction |String    |Direction of the event                                                               |
|eventOrigin|String   |Origin of the event                                                                  |
|flags     |String    |Data packet flags                                                                    |
|flow      |String    |Flow of the packet the log was recorded for in relation to the connection direction  |
|hostName  |String    |HostTransport Name of the computer where the event was triggered                     |
|iface     |String    |Name of the physical network interface where the event was triggered                 |
|protocol  |String    |Protocol of the connection                                                           |
|reason    |String    |Name of the DPI filter which triggered the event                                     |
|sourceIP  |String    |Source IP Address                                                                    |
|sourceMAC |String    |Source MAC Address                                                                   |
|sourcePort|String    |Source Port                                                                          |
|tags      |String    |Name of any event tags assigned to this event                                        |
|severity  |String    |Severity                                                                             |
