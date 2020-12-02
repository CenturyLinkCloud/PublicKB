{{{
  "title": "Runner SSH Key Management Service",
  "date": "04-29-2016",
  "author": "Anthony Hakim",
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}


## Audience

This article is to support customers of Runner, a product that enables teams, developers, and engineers to quickly provision, interact, and modify their environments anywhere - Lumen Cloud, third-party cloud providers, and on-premises.  Additionally, the responses in this FAQ document are specific to using the service through the Control Portal.


## SSH Key Management Service Overview

Runner’s SSH Key Management Service will help you to manage and deploy SSH credentials on Lumen Cloud servers. With the keys deployed from this service, you can securely create and execute tasks using our Job service. The job actions can be performed via REST API calls. The API works with JSON messages over HTTP. It relies on the standard HTTP verbs including GET, POST, PUT, and DELETE.

The URL format of the service is: `https://api.runner.ctl.io/keypairs/{accountAlias}`.

For example, to retrieve information of all deployed keypairs created at the account alias level, you would issue a GET request to `https://api.runner.ctl.io/keypairs/ALIAS`. Below are the various features of the service:

 - [Create Keypair](#CreateKeypair)
 - [Delete Keypair](#DeleteKeypair)
 - [Deploy Keypair](#DeployKeypair)
 - [Get Keypair](#GetKeypair)
 - [Deploy Keypair to Server Users](#DeployKeypairToServerUsers)
 - [Get Server Users](#GetServerUsers)
 - [Get Keypairs](#GetKeypairs)
 - [Undeploy Keypair for Server Users](#UndeployKeypairForServerUsers)


### CREATE KEYPAIR <a id="CreateKeypair"></a>

Creates an SSH Keypair and allows you to deploy those credentials to Lumen servers in your account.  The key can then be used to authenticate to these resources when executing a Runner Job. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to create, deploy and manage SSH keys on Lumen servers.

Note: The SSH privateKey is generated only once, so you have to save the privateKey from the response.

#### URL
**Structure**

`POST https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}`

**Example**

`POST https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Categorize and manage your keys with an alias name. |	Yes |

**Content Properties**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| deployToServers |	array |	Array list of servers and their user names. |	No |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key(s) to be deployed. |	Yes |
| usernames |	array |	Array of server usernames to be authorized with the key. |	Yes |

```
"deployToServers": [
    {
        "serverId": "UC1ACCTUBUSVR04",
        "usernames": ["username1", "username2"]
    }
  ]
```

**Example**

```
{
    "deployToServers": [
        {
            "serverId": "UC1ACCTUBUSVR04",
            "usernames": [ "root"]
        }
    ]
}
```

#### Response

The response will be an object with the created SSH key information deployed on the specified server(s).

**Entity Definition**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| alias |	string |	The custom alias name provided to categorize your keys. |
| privateKey |	string |	The SSH privateKey is generated only once, so you have to save the privateKey for future reference. |
| publicKey |	string |	The SSH publicKey deployed on the specified server(s). |
| fingerprint |	string |	ECDSA key fingerprint. |
| deployedServers |	array |	Array list of servers and their user names. |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key(s) is deployed. |
| usernames |	array |	Array of server usernames to be authorized with the key. |

**Example**

```
{
  "alias": "TestGroup",
  privateKey: "-----BEGIN RSA PRIVATE KEY----- XIEOASASAS......M7ezqzt3jM0aA== -----END RSA PRIVATE KEY----- "
  "publicKey": "ssh-rsa CYXYXHXY3NzaC1yc2.....Ug42vKgh abc.def@fghijk.com",
  fingerprint: "6d:3e:d2:6a.....e:e0:bf:20:0c",
  "deployedServers": [
    {
      "serverId": "UC1ACCTUBUSVR04",
      "usernames": ["root"]
    }
  ]
}
```


### DELETE KEYPAIR <a id="DeleteKeypair"></a>

Delete deployed SSH credentials to Lumen servers. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to remove a deployed key pair from your Lumen Cloud account alias.

#### URL
**Structure**

`DELETE https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}`

**Example**

`DELETE https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	The keypair alias name that you would like to delete. |	Yes |

**Example**

`https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Response

The response will be a standard HTTP 200 OK response upon deletion of the keypair.


### DEPLOY KEYPAIR <a id="DeployKeypair"></a>

Deploys SSH credentials to Lumen Cloud servers in a given account, so the keys can be used to authenticate these servers when executing Runner jobs. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to manage and deploy SSH keys to machines involved in a Runner job.

#### URL
**Structure**

`PUT https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}`

**Example**

`PUT https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Your keypair alias name. |	Yes |

**Content Properties**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| deployToServers |	array |	Array list of servers and their user names. |	Yes |
| publicKey |	string |	The SSH publicKey to be deployed for the servers. |	Yes |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key to be deployed. |	Yes |
| usernames |	array |	Array of server usernames to be authorized with the key. |	Yes |

```
"deployToServers": [
    {
        "serverId": "UC1ACCTUBUSVR04",
        "usernames": ["username1", "username2"]
    }
```

**Example**

```
{
    "deployToServers": [
        {
            "serverId": "UC1ACCTUBUSVR04",
            "usernames": [ "root"]
        }
    ],
    "publicKey" : "ssh-rsa CYXYXHXY3NzaC1yc2EAA.......mYr9triUlZNSx0Ug42vKgh abc.def@fghijk.com"
}
```


#### Response

The response will be an object with the key deployed to servers.

**Entity Definition**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| alias |	string |	The custom alias name provided to categorize your keys. |
| publicKey |	string |	The SSH publicKey deployed for the servers. |
| deployedServers |	array |	Array list of servers and their user names |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key(s) is deployed. |
| usernames |	array |	Array of server usernames to be authorized with the key. |

**Example**

```
{
  "alias": "TestGroup",
  "publicKey": "ssh-rsa CYXYXHXY3NzaC1yc2EAAAADA.........riUlZNSx0Ug42vKgh abc.def@fghijk.com",
  "deployedServers": [
    {
      "serverId": "UC1ACCTUBUSVR04",
      "usernames": ["root"]
    }
  ]
}
```


### GET KEYPAIR <a id="GetKeypair"></a>

Retrieve the details of an existing keypair alias. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to retrieve the details of a deployed key pair to your Lumen Cloud account alias.

#### URL
**Structure**

`GET https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}`

**Example**

`GET https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Your keypair alias name. |	Yes |

**Example**

`https://api.runner.ctl.io/keypairs/XXXX/TestGroup`


#### Response

The response will be an object with the key deployed to servers.

**Entity Definition**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| alias |	string |	The custom alias name provided to categorize your keys. |
| publicKey |	string |	The SSH publicKey deployed for the servers. |
| deployedServers |	array |	Array list of servers and their user names. |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key(s) is deployed. |
| usernames |	array |	Array of server usernames to be authorized with the key. |

**Example**

```
{
    alias: "TestGroup"
    publicKey: "ssh-rsa CYXYXHXY3NzaC1yc.........Ug42vKgh abc.def@fghijk.com"
    deployedServers: [
    {
        serverId: "UC1ACCTUBUSVR04"
        usernames: ["root"]
    },
    {
        serverId: "UC1ACCTUBUSVR05"
        usernames: ["root"]
    }
}
```


### DEPLOY KEYPAIR TO SERVER USERS <a id="DeployKeypairToServerUsers"></a>

Add server users for a deployed SSH keypair. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to add server users to an already deployed key pair.

#### URL
**Structure**

`POST https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}/{serverId}`

**Example**

`POST https://api.runner.ctl.io/keypairs/XXXX/TestGroup/UC1ACCTUBUSVR04`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Your keypair alias name. |	Yes |
| serverId |	string |	Server ID for which the key(s) is/are deployed. |	Yes |

**Content Properties**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| usernames |	array |	Array of additional server usernames to be authorized with the key. | Yes |

**Example**

```
{
    "usernames": ["admin"]
}
```
#### Response

The response will be a standard HTTP 200 OK response upon new server user name addition.


### GET SERVER USERS <a id="GetServerUsers"></a>

Get server usernames for a deployed SSH keypair. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to get the list of usernames (of a specific server) for deployed key pairs.

#### URL
**Structure**

`GET https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}/{serverId}`

**Example**

`GET https://api.runner.ctl.io/keypairs/XXXX/TestGroup/UC1ACCTUBUSVR04`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Your keypair alias name. |	Yes |
| serverId |	string |	Server ID for which the key(s) is deployed. |	Yes |

**Example**

`https://api.runner.ctl.io/keypairs/XXXX/TestGroup/UC1ACCTUBUSVR04`

#### Response

The response will be server usernames (listed as array of string) for a deployed SSH keypair.

`["root"]`


### GET KEYPAIRS <a id="GetKeypairs"></a>

To get the details of all deployed SSH credentials to Lumen servers. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to retrieve the details of all deployed key pair to your Lumen account alias.

#### URL
**Structure**

`GET https://api.runner.ctl.io/keypairs/{accountAlias}`

**Example**

`GET https://api.runner.ctl.io/keypairs/XXXX`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |

`https://api.runner.ctl.io/keypairs/XXXX/TestGroup`

#### Response

The response will be list of objects (based on keypair alias) that were created within Lumen Cloud account alias.

**Entity Definition**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| alias |	string |	The custom alias name provided to categorize your keys. |
| publicKey |	string |	The SSH publicKey deployed for the servers. |
| deployedServers |	array |	Array list of servers and their user names. |

**Server Entity**

| NAME | TYPE |	DESCRIPTION	|
| --- | --- | --- |
| serverId |	string |	Server ID for which the key(s) is deployed. |
| usernames |	array |	Array of server usernames to be authorized with the key. |

```
[
    {
        alias: "TestGroup"
        publicKey: "ssh-rsa CYXYXHXY3NzaC1yc2E......iUlZNSx0Ug42vKgh abc.def@fghijk.com"
        deployedServers: [
        {
            serverId: "UC1ACCTUBUSVR04"
            usernames: ["root"]
        },
        {
            serverId: "UC1ACCTUBUSVR05"
            usernames: ["root"]
        }
    },
    {
        alias: "ProdGroup"
        publicKey: "ssh-rsa DZZZYXHXY3NzaC1yc2EAAA......NSx0Ug42vKgh abc.def@fghijk.com"
        deployedServers: [
        {
            serverId: "UC1PRODUBUSVR04"
            usernames: ["root"]
        },
        {
            serverId: "UC1PRODUBUSVR05"
            usernames: ["root"]
        }
    }
]
```


### UNDEPLOY KEYPAIR FOR SERVER USERS <a id="UndeployKeypairForServerUsers"></a>

Undeploy key pair for a specific server user. Calls to this operation must include a token acquired from the authentication endpoint. See the [Login API](https://www.ctl.io/api-docs/v2/#authentication-login) for information on acquiring this token.

**When to use it**

Use this API operation when you would like to undeployed a key pair for certain server users.

#### URL
**Structure**

`DELETE https://api.runner.ctl.io/keypairs/{accountAlias}/{keypairAlias}/{serverId}`

**Example**

`DELETE https://api.runner.ctl.io/keypairs/XXXX/TestGroup/UC1ACCTUBUSVR04`

#### Request
**URI Parameters**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| accountAlias |	string |	Short code for a particular account. |	Yes |
| keypairAlias |	string |	Your keypair alias name. |	Yes |
| serverId |	string |	Server ID for which the key has to be undeployed for a specific user(s). |	Yes |

**Content Properties**

| NAME | TYPE |	DESCRIPTION	| REQ.|
| --- | --- | --- | --- |
| usernames |	array |	Array of server usernames for which the keys have to be undeployed. |	Yes |

**Example**

```
{
    "usernames": ["admin"]
}
```

#### Response

The response will be a standard HTTP 200 OK response upon key has been undeployed for the server user name.
