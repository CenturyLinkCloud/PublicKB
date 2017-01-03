{{{
"title": "Using the API: from registering a provider to the deployment of an instance",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Using the API: from Registering a Provider to the Deployment of an Instance

This guide shows all the steps you need to deploy a box using the ElasticBox API.
* Authentication and Deployment Variables
* Register a Provider
* Create a New Deployment Policy Box
* Create a Box
* Deploy the Instance
* Terminate the Instance

**Note:** We use cURL commands to send HTTP requests to the API objects in JSON. JSON is the required format for all API requests and responses.

Now let’s look at the script in sections to understand how you can make API calls from any code you like.

### Authenticate with ElasticBox
Before calling to the API you have to sig in into the ElasticBox website and [getting an authentication token](./admin-access.md). You use this token as an http header to perform every call to the ElasticBox API.

**Declare Deployment Variables**

In this case we decided to use AWS so we will need the account key and secret to register it as provider. Box deployment arguments such as owner, environment and token are declared as variables because they can differ between deployments. That way, each time you run the script, you can pass different arguments.
```
aws_provider_key=$1
aws_provider_secret=$2
environment=$3
elasticBox_token=$4
owner=$5
```

### Register a Provider in ElasticBox

A provider is a public or private cloud account you can register in ElasticBox. In this case we choose AWS as provider. From the AWS account credential we will need the key and the secret right now.
```
# Register the provider in Elastic Box
payload="{
  \"icon\": \"images/platform/aws.png\",
  \"type\": \"Amazon Web Services\",
  \"description\": \"Manage EC2, ECS, S3, Dynamo DB, RDS, ElasticCache, and CloudFormation instances\",
  \"schema\": \"http://elasticbox.net/schemas/aws/provider\",
  \"name\": \"AWS Example Provider via CURL\",
  \"credentials\": {
    \"key\": \"$example_provider_key\",
    \"secret\": \"$example_provider_secret\"
  },
  \"owner\": \"$owner\"
}"
provider=$(curl -k -s \
    -X POST \
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json, text/plain, */*" \
    -H "Accept-encoding: gzip, deflate" \
    -H "Content-Type: application/json" \
    -d "$payload" https://$environment/services/providers)
provider_id=$(echo $provider | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $provider_id ]; then
    echo "Created provider $provider_id"
else
    echo "Error creating the provider: $provider"
fi;
```

### Create a New Deployment Policy Box

A deployment policy box is where you specify settings to deploy applications in a specific virtual environment. We send parameters for creating the deployment policy box in a POST request to the box object. If there’s an error in creating the policy box, we output the error. Else, we output the created box.
```
# Once we have created the provider we can set the proper policy box
payload="{
  \"owner\": \"$owner\",
  \"schema\": \"http://elasticbox.net/schemas/boxes/policy\",
  \"claims\": [
    \"linux\"
  ],
  \"lifespan\": {
    \"operation\": \"none\"
  },
  \"automatic_updates\": \"off\",
  \"provider_id\": \"$provider_id\",
  \"name\": \"Deployment Policy Box Example\",
  \"description\": \"Just one example of deployment policy box creation via API\",
  \"profile\": {
    \"schema\": \"http://elasticbox.net/schemas/aws/ec2/profile\",
    \"flavor\": \"t1.micro\",
    \"location\": \"us-east-1\",
    \"instances\": 1,
    \"image\": \"Linux Compute\",
    \"keypair\": \"None\",
    \"cloud\": \"EC2\",
    \"security_groups\": [

    ],
    \"subnet\": \"us-east-1a\"
  }
}"
policy_box=$(curl -k -s \
    -X POST \
    -H "Content-Type:application/json" \
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json, text/plain, */*" \
    -H "Accept-encoding: gzip, deflate" \
    -H "Content-Type: application/json;charset=UTF-8" \
    -d "$payload" https://$environment/services/boxes)
policy_box_id=$(echo $policy_box | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $policy_box_id ]; then
    echo "Created policy_box $policy_box_id"
else
    echo "Error launching the policy_box: $policy_box"
fi;
```

### Create a Custom Box in Order to Deploy It Using the Previous Deployment Policy Box

In a POST request to the Box object, we send the features for our script box. Also we will use two already created blobs. You can take a look to the [blobs](./api-blobs.md), API doc if you need to know how you can create them.
```
# We create a box to deploy with that policy box, in this case we are going to use a previously uploaded scripts.
payload="{
  \"automatic_updates\": \"off\",
  \"requirements\": [

  ],
  \"description\": \"sample box created via API\",
  \"name\": \"ScriptBoxSample\",
  \"deleted\": null,
  \"variables\": [
    {
      \"required\": true,
      \"type\": \"Text\",
      \"name\": \"variable_name\",
      \"value\": \"variable_value\",
      \"visibility\": \"public\"
    }
  ],
  \"visibility\": \"workspace\",
  \"members\": [

  ],
  \"owner\": \"$owner\",
  \"organization\": \"elasticbox\",
  \"events\": {
    \"configure\": {
      \"url\": \"/services/blobs/download/5631fa7614841250525226cc/configure\",
      \"length\": 5,
      \"destination_path\": \"scripts\",
      \"content_type\": \"text/x-shellscript\"
    },
    \"install\": {
      \"url\": \"/services/blobs/download/5631fa6614841250525226ca/install\",
      \"length\": 5,
      \"destination_path\": \"scripts\",
      \"content_type\": \"text/x-shellscript\"
    }
  },
  \"schema\": \"http://elasticbox.net/schemas/boxes/script\"
}"
box=$(curl -k -s \
    -X POST \
    -H "Content-Type:application/json" \
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json, text/plain, */*" \
    -H "Accept-encoding: gzip, deflate" \
    -H "Content-Type: application/json;charset=UTF-8" \
    -d "$payload" https://$environment/services/boxes) \
box_id=$(echo $box | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $box_id ]; then
    echo "Created box $box_id"
else
    echo "Error launching the box: $box"
fi;
```

### Deploy the Instance

To remove the instance from the virtual machine, we send a DELETE request to the Instances object with the instance ID. Then we check its response status. If it’s 200, we say that the specific instance is terminated. Else, we output the error state from the response.
```
# Finally we are going to deploy the instance
payload="{
    \"schema\": \"http://elasticbox.net/schemas/deploy-instance-request\",
    \"owner\": \"$owner\",
    \"name\": \"ScriptBoxSample\",
    \"box\": {
        \"id\": \"$box_id\",
        \"variables\": [
        ]
    },
    \"instance_tags\": [

    ],
    \"automatic_updates\": \"off\",
    \"policy_box\": {
        \"id\": \"$policy_box_id\",
        \"variables\": [

        ]
     }
}"
instance=$(curl -k -s \
    -X POST \
    -H "Content-Type:application/json" \
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json, text/plain, */*" \
    -H "Accept-encoding: gzip, deflate" \
    -H "Content-Type: application/json;charset=UTF-8" \
    -d "$payload" https://$environment/services/instances)
instance_id=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $instance_id ]; then
    echo "Deployed instance $instance_id"
else
    echo "Error deploying the instance: $instance_id"
fi;
```

### Terminate the Instance

To remove the instance from the virtual machine, we send a DELETE request to the Instances object with the instance ID. Then we check its response status. If it’s 200, we say that the specific instance is terminated. Else, we output the error state from the response.
```
curl -k -s \
-X DELETE \
-H "elasticBox-token:$elasticBox_token" \
-H "elasticbox-release:4.0" \
-A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
-H "Accept: application/json, text/plain, */*" \
-H "Accept-encoding: gzip, deflate" \
 https://$environment/services/instances/$instance_id

echo "Undeployed box: $instance_id"
```

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](//www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
