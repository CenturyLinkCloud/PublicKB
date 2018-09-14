{{{
  "title": "Using the API to Create Users",
  "date": "05-28-2015",
  "author": "Ted Henley",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description
You can use the CenturyLink Cloud API to perform the same actions programmatically as you can from within the Control Portal. The below example shows how to create a user via the API.

For more details about the specific API functions used below, reference the complete [API documentation](https://www.ctl.io/api-docs/v1/).

### Steps
There are two steps to creating a user.  

1. Authenticate to the API (v1) using an account with appropriate permissions to create a user in the target account.  
2. Create the account.

#### 1. Prerequisites
Prior to creating a user via the API, you must have an API user created. To do that, you will need the API key and password.  Directions for creating a user via the API can be referenced [here](creating-users.md).

#### 2. Authentication
While there are multiple ways to authenticate, this example uses the REST method. In PowerShell you can authenticate using this code:
  ```
  Invoke-RestMethod -URI "https://api.ctl.io/REST/Auth/Logon" -Method POST -ContentType application/json -Body "{'APIKey': '[Your APIKey]', 'Password': '[Your APIPassword]'}" -SessionVariable session
  ```

Be sure to replace the API key and password in the string. Once you authenticate successfully, you will receive a message similar to the following:
  ```
  Success    : True
  Message    : Login Successful
  StatusCode : 0
  ```
#### 3. Create User
The API for creating a user is available at [https://www.ctl.io/api-docs/v1/#users-createuser](https://www.ctl.io/api-docs/v1/#users-createuser).

At a minimum, you must specify UserName, AccountAlias, EmailAddress, FirstName, and LastName. While it is not required, adding Roles at the same time is recommended. A sample PowerShell call may look like this:
  ```
  $UserInfo = @"
  {
  'UserName':'UserEmail@yourdomain.com', #This can be anything, but email is most common
  'AccountAlias':'ABCD', #This is the account alias the user will be in
  'EmailAddress': 'UserEmail@yourdomain.com',
  'FirstName':'John',
  'LastName':'Doe',
  'Roles':[12,14] #This gives him network manager and server operator roles
  }
  "@
  Invoke-WebRequest -URI ‘https://api.ctl.io/REST/User/CreateUser/JSON’ -Method POST -ContentType application/json -Body $UserInfo -WebSession $session -verbose
  ```
