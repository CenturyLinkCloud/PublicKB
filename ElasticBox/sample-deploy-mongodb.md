{{{
"title": "Sample: Deploy a MongoDB instance via the API",
"date": "09-01-2016",
"author": "",
"attachments": [],
"contentIsHTML": false
}}}

### Sample: Deploy a MongoDB instance via the API

Here you can see how to deploy a mongoDB instance using the ElasticBox API. Typically you want to structure API calls to mirror your workflow in ElasticBox. Most workflows involve tasks such as these: defining a [box](./boxes.md), for example a Jenkins box to automate continuous integration and delivery; registering a [provider](./providers.md) like AWS, Google Cloud, vSphere, OpenStack, or CloudStack to host your box application deployments; creating a [deployment profile](./deploying-managing-instances.md) to specify provider specific options for a deployment; deploying an instance to launch a box in the virtual environment; or performing lifecycle tasks like deploying, reconfiguring, and terminating an instance.

In this sample, we follow this workflow to deploy a MongoDB instance using the existing MongoDB public box:

* Declare deployment arguments
* Authenticate with ElasticBox
* Create a deployment profile
* Deploy a MongoDB instance
* Terminate the instance

**Note:** We use cURL commands to send HTTP requests to the API objects in JSON. JSON is the required format for all API requests and responses.

Now let’s look at the script in sections to understand how you can make API calls from any code you like.

### Declare Deployment Arguments

MongoDB deployment arguments such as username, password, environment, owner are declared as variables because they can differ between deployments. That way, each time you run the script, you can pass different arguments. In this case we decided to use AWS as provider so we will need the account key and secret to register it as provider. Those are variables too.

```
aws_provider_key=$1
aws_provider_secret=$2

environment=$3
elasticBox_token=$4
owner=$5

username=$1
password=$2
```

### Authenticate with ElasticBox

All API calls start with signing in to the ElasticBox website and [getting an authentication token](./api-overview-and-access.md). You use this token to perform tasks in your ElasticBox workflow. In this example, we pass the token in the format as shown to all of the API requests that relate to deploying MongoDB.

```
ElasticBox-Token:8ccc8203-2efd-44a9-8819-e95fd2277be2
```

### Create a Deployment Policy Box

A deployment policy box is where you specify settings to deploy applications in a specific virtual environment. We send parameters for creating the deployment profile in a POST request to the Profiles object. If there’s an error in creating the profile, we output the error. Else, we output the created profile.

```
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
        -H "elasticbox-release:4.0" \
        -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
        -H "Accept: application/json" \
        -H "Content-Type: application/json;charset=UTF-8" \
        -d "$payload" https://$environment/services/boxes)
policy_box_id=$(echo $policy_box | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $policy_box_id ]; then
        echo "Created Deployment Policy Box $policy_box_id"
else
        echo "Error launching the Deployment Policy Box: $policy_box"
        exit 1
fi;
```

### Deploy a MongoDB Instance

In a POST request to the Instances object, we send along the deployment profile with other instance parameters to launch a MongoDB instance in the virtual environment.

```
#Deploy the instance
payload="{
    \"schema\": \"http://elasticbox.net/schemas/deploy-instance-request\",
    \"owner\": \"$owner\",
    \"name\": \"ScriptBoxSample\",
    \"box\": {
        \"id\": \"$mongo_box_id\",
        \"variables\": [
            {
              \"name\": \"username\",
              \"type\": \"Text\",
              \"value\": \"$username\",
              \"required\": true
            },
            {
              \"name\": \"password\",
              \"type\": \"Password\",
              \"value\": \"$password\",
              \"required\": true
            }
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
    -H "elasticbox-release:4.0" \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json;charset=UTF-8" \
    -d "$payload" https://$environment/services/instances)
instance_id=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["id"]')
if [ -z != $instance_id ]; then
    echo "Deployed Instance $instance_id"
else
    echo "Error deploying the Instance: $instance_id"
    exit 1
fi;
```

We store the response and check if the instance launched. If it failed to launch, we output an error or say that the instance is available and give its ID.

While the instance is launching, we check its state every 30 seconds with a GET request to the Instances object by passing the instance ID. Then we evaluate whether to wait or continue: If it’s still processing, we say so and wait or we output the current instance state and move to the next task.

```
COUNTER=0
while [ $COUNTER -lt $cycles_to_wait ]; do
  instance=$(curl -k -s \
    -X GET\
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    https://$environment/services/instances/${instance_id})
  instance_state=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["state"]')
  instance_operation=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["operation"]')
  if [[ "$instance_state" == "processing" ]]; then
    echo "The state of the Instance is $instance_state $instance_operation Waiting for it to be done or unavailable"
    let COUNTER=COUNTER+1
    sleep 30
  else
    echo "The state of the Instance is $instance_state $instance_operation. Process completed"
    break
  fi
done
```

### Terminate the Instance

To remove the instance from the virtual machine, we send a DELETE request to the Instances object with the instance ID. Then we check its response status. If it’s 200, we say that the specific instance is terminated. Else, we output the error state from the response.

```
status=$(curl -s -k \
  -X DELETE \
  -H "Accept: application/json" \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
  -H "Content-Type:application/json" \
  -H "elasticBox-token:$elasticBox_token" \
  -H "elasticbox-release:4.0" \
  -w '%{http_code}' \
  -o /dev/null \
  https://$environment/services/instances/${instance_id}?operation=terminate)
if [[ ! $status -eq 202 ]]; then
  echo "Error terminating the instance: Error $status"
  exit 1
else
  echo "Terminated Instance $instance_id"
fi
```

While waiting for the instance to terminate, we do a GET on the Instances object with the instance ID to know the operation running on the instance and its current state. If it’s processing, we say so and wait for it to complete or we output the operation that was run and the instance state.

```
#Wait for the instance to be terminated
COUNTER=0
while [[ $COUNTER -lt 30 ]]; do
  instance=$(curl -k -s \
    -X GET \
    -H "Accept: application/json" \
    -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
    -H "Content-Type:application/json" \
    -H "elasticBox-token:$elasticBox_token" \
    -H "elasticbox-release:4.0" \
    https://$environment/services/instances/${instance_id})
  instance_state=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["state"]')
  instance_operation=$(echo $instance | python -c 'import json,sys; print json.load(sys.stdin)["operation"]')
  if [[ "$instance_state" == "processing" ]]; then
    echo "The state of the instance is $instance_state $instance_operation Waiting for it to be done or unavailable"
    let COUNTER=COUNTER+1
    sleep 30
  else
    echo "The state of the Instance is $instance_state $instance_operation"
    break
  fi
done
```

Lastly, we delete the instance and its logs from ElasticBox by sending a DELETE request with the instance ID to the Instances object. Once done, we say that the instance is deleted. Similarly we delete the deployment policy box with a DELETE request to the Profiles object and confirm that it’s done.

```
#Remove the deployment policy box
status=$(curl -s -k \
  -X DELETE \
  -H "Accept: application/json" \
  -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30" \
  -H "Content-Type:application/json" \
  -H "elasticBox-token:$elasticBox_token" \
  -H "elasticbox-release:4.0" \
  -w '%{http_code}' \
  -o /dev/null \
  https://$environment/services/boxes/${policy_box_id})
if [[ ! $status -eq 204 ]]; then
  echo "Error terminating the Deployment Policy Box: Error $status"
  exit 1
else
  echo "Terminated Deployment Policy Box $policy_box_id"
fi
```

### Contacting ElasticBox Support

We’re sorry you’re having an issue in [ElasticBox](https://www.ctl.io/elasticbox/). Please review the [troubleshooting tips](./troubleshooting-tips.md), or contact [ElasticBox support](mailto:support@elasticbox.com) with details and screen shots where possible.

For issues related to API calls, send the request body along with details related to the issue. In the case of a box error, share the box in the workspace that your organization and ElasticBox can access and attach the logs.
* Linux: SSH and locate the log at /var/log/elasticbox/elasticbox-agent.log
* Windows: RDP into the instance to locate the log at ProgramDataElasticBoxLogselasticbox-agent.log
