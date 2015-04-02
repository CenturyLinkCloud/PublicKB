{{{
  "title": "Log into the CenturyLink Cloud API with PowerShell",
  "date": "3-31-2015",
  "author": "Mark Turpin",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview

CenturyLink Cloud customers can use PowerShell to log into the CenturyLink Cloud API and use the resulting session token for additional API calls

### Prerequisites

* A CenturyLink Cloud Account
* [An API user has been created](../Accounts & Users/creating-users.md)
* PowerShell v4+ has been installed on client machine and is being run as administrator

### EXCEPTIONS

This KB has not been tested on API v2

### General Notes

* Recommended to use PowerShell v4+ because PowerShell v3 Invoke-RestMethod has a bug with [accept headers](https://connect.microsoft.com/PowerShell/feedback/details/757249/invoke-restmethod-accept-header)
* Tested on [API v1](https://www.centurylinkcloud.com/api-docs/v1/#authentication-logon)
* API user and API password need to be entered into the script
* Script can be used from anywhere - does not have to be on CenturyLink Cloud network

### PowerShell Steps

1. Use the below PowerShell code to retrieve an API session token

  ```
  #log into API
  $URL = 'http://api.ctl.io/REST/Auth/Logon'

  #enter in your api user (v1) key and password below
  $json = @"
  {
    'APIKey': 'insert api user guid', 'Password': 'insert api user password'
  } "@

  #log into the API via Invoke-RestMethod using JSON payload
  $Result = Invoke-RestMethod -URI $URL -Method POST -ContentType application/json -Body $json -SessionVariable session -verbose

  #view results. Session variable can be used in future Invoke-RestMethod requests
  $Result | FL
  ```

2. You can now use the $session variable for authenticating further API calls.  Example:

  ```
  $RequestURL = 'https://api.ctl.io/REST/Account/GetAccounts/XML'
  $content = Invoke-WebRequest -URI $RequestURL -Method POST -ContentType application/xml -WebSession $session -verbose
  ```
