{{{
  "title": "Using the V1 API to get all Servers in an Account Alias with PowerShell",
  "date": "2-12-2016",
  "author": "Chris Blydenstein",
  "attachments": [],
  "contentIsHTML": false
}}}

### Description

Customers interested in quickly obtaining details of all servers in an account can use this PowerShell script.

### Prerequisites

* A Lumen Cloud Account

### Detailed Instructions

Before you can begin you need to create a V1 API account. Do that in the Control Portal by clicking on the `API` link in the main navigation menu. Click `Create API User` and enter your email address. A key and password will be automatically generated. **Note:** Occasionally, the system will generate passwords that have special characters reserved by PowerShell, and you’ll get a login error. If that happens, delete and recreate your API account.

Now that you have your API key and password, you can use the below PowerShell code to create a session variable:

```
$body = @{Password = "PASTE PASSWORD HERE"; APIKey = "PASTE APIKEY HERE"} | ConvertTo-Json
$restreply = Invoke-RestMethod -uri "https://api.ctl.io/REST/Auth/Logon/" -ContentType "Application/JSON" -Body $body -Method Post -SessionVariable session
$global:session = $session
Write-Host $restreply.Message
```
Once you have run that code in place you can add API calls like the example below:

```
$JSON = @{AccountAlias = "ALIAS"; Location = "IL1" } | ConvertTo-Json
$Groups = Invoke-RestMethod -Uri "https://api.ctl.io/REST/Group/GetGroups/" -ContentType "Application/JSON" -WebSession $session -Method Post -Body $JSON
$Groups

$JSON = @{AccountAlias = "ALIAS"; HardwareGroupUUID = "7d5ceb1921a743af954cc1010f7341de"; Location = "IL1" } | ConvertTo-Json
$Servers = Invoke-RestMethod -Uri "https://api.ctl.io/REST/Server/GetAllServers/" -ContentType "Application/JSON" -WebSession $session -Method Post -Body $JSON
$Servers
```

You can put it all together using a couple of nested loops. The result is the code below. Copy and paste everything below this line into a new file (or tab) within the PowerShell ISE. You can then paste in your API password and APIKEY and finally hit F5 to run it. The code below will return your data as a grid you can paste into Excel.

**Create Login Header**

```
$body = @{Password = "PASTE PASSWORD HERE"; APIKey = "PASTE APIKEY HERE"} | ConvertTo-Json
$restreply = Invoke-RestMethod -uri "https://api.ctl.io/REST/Auth/Logon/" -ContentType "Application/JSON" -Body $body -Method Post -SessionVariable session
$global:session = $session
Write-Host $restreply.Message
```

**Define Variables**
```
$allServers = @()
$account = "ALIAS"
$datacenters = @('IL1', 'NY1')
```

**Loop through API**

Now, find and add servers to an array.

```
foreach($datacenter in $datacenters)
{
	#Get Groups in DC
	$JSON = @{AccountAlias = $account; Location = $datacenter } | ConvertTo-Json
	$Groups = Invoke-RestMethod -Uri "https://api.ctl.io/REST/Group/GetGroups/" -ContentType "Application/JSON" -WebSession $session -Method Post -Body $JSON
	foreach($group in $groups)
	{
		#Get Servers in Group
		$JSON = @{AccountAlias = $account; HardwareGroupUUID = $group.HardwareGroups.ID; Location = $datacenter } | ConvertTo-Json
		$Servers = Invoke-RestMethod -Uri "https://api.ctl.io/REST/Server/GetAllServers/" -ContentType "Application/JSON" -WebSession $session -Method Post -Body $JSON
		#Add Server to Array
		$allServers += $Servers.Servers
	}
}
```

**Output Array as data grid (for copy/paste to Excel)**

```
$allServers | Out-GridView
```       
