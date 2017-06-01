{{{
  "title": "Cloud Optimization AWS Configuration - Manual",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
The below process details the steps to manual configure your AWS account for Cloud Application Manager Analytics functionality.

If you prefer for set-up of your environment to be automated those setup steps can be found [here](CloudApplicationManagerAnlyticsAWSSetup.md).

#### Login to your AWS Account
* Login to the target AWS account [here](https://console.aws.amazon.com/iam)
* Access the IAM dashboard

#### Create CenturyLink Cloud Optimization IAM Policy
* Navigate to IAM "Policy"
* Click "Create Policy"
* Select "Create Your Own Policy"
* Name the Policy as: CTLCloudOptimizationPolicy
* Add the following Description: Access Policy for CTL's Cloud Optimization Functionality
* Paste the CenturyLink Cloud Optimization IAM policy documented [below](#centuryLink-cloud-optimization-iam-policy)
* Click "Validate Policy"
* Click "Create Policy"

#### Create CenturyLink Cloud Optimization IAM Role
* Navigate to IAM "Roles"
* Click "Create New Role"
* Click "Role for Cross-account access"
* Select "Provide access between your AWS account and 3rd party AWS account"
* Add Account ID as: 540339316802
* Add External ID as : [as provided by Cloud Optimization]
* Do NOT check "require MFA"
* Click "Next Steps"
* Select "CTLCloudOptimizationPolicy"
* Click "Next Step"
* Name the Role as "CTLCloudOptimization"
* Add the following Description: "CTL's Cloud Optimization Functionality"
* Click "Create Role"

#### Retrieve ARN role
* Select the CenturyLink Cloud Optimization AMI Role
* Record listed ARN
* Paste ARN into the Cloud Optimization Portal or send it to your on-boarding representative


##### CenturyLink Cloud Optimization IAM Policy
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "FullPolicy",
            "Action": [
                "acm:DescribeCertificate",
                "acm:ListCertificates",
                "acm:GetCertificate",
                "autoscaling:Describe*",
                "cloudformation:DescribeStacks",
                "cloudformation:GetStackPolicy",
                "cloudformation:GetTemplate",
                "cloudformation:ListStackResources",
                "cloudfront:List*",
                "cloudfront:GetDistributionConfig",
                "cloudfront:GetStreamingDistributionConfig",
                "cloudhsm:Describe*",
                "cloudhsm:List*",
                "cloudsearch:DescribeDomains",
                "cloudsearch:DescribeServiceAccessPolicies",
                "cloudsearch:DescribeStemmingOptions",
                "cloudsearch:DescribeStopwordOptions",
                "cloudsearch:DescribeSynonymOptions",
                "cloudsearch:DescribeDefaultSearchField",
                "cloudsearch:DescribeIndexFields",
                "cloudsearch:DescribeRankExpressions",
                "cloudtrail:DescribeTrails",
                "cloudtrail:GetTrailStatus",
                "cloudwatch:DescribeAlarms",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics",
                "config:DescribeConfigRules",
                "config:GetComplianceDetailsByConfigRule",
                "config:DescribeDeliveryChannels",
                "config:DescribeDeliveryChannelStatus",
                "config:DescribeConfigurationRecorders",
                "config:DescribeConfigurationRecorderStatus",
                "datapipeline:ListPipelines",
                "datapipeline:GetPipelineDefinition",
                "datapipeline:DescribePipelines",
                "directconnect:DescribeLocations",
                "directconnect:DescribeConnections",
                "directconnect:DescribeVirtualInterfaces",
                "dynamodb:ListTables",
                "dynamodb:DescribeTable",
                "ec2:Describe*",
                "ec2:GetConsoleOutput",
                "ecs:ListClusters",
                "ecs:DescribeClusters",
                "ecs:ListContainerInstances",
                "ecs:DescribeContainerInstances",
                "ecs:ListServices",
                "ecs:DescribeServices",
                "ecs:ListTaskDefinitions",
                "ecs:DescribeTaskDefinition",
                "ecs:ListTasks",
                "ecs:DescribeTasks",
                "elasticache:DescribeCacheClusters",
                "elasticache:DescribeReservedCacheNodes",
                "elasticache:DescribeCacheSecurityGroups",
                "elasticache:DescribeCacheParameterGroups",
                "elasticache:DescribeCacheParameters",
                "elasticache:DescribeCacheSubnetGroups",
                "elasticbeanstalk:DescribeApplications",
                "elasticbeanstalk:DescribeConfigurationSettings",
                "elasticbeanstalk:DescribeEnvironments",
                "elasticbeanstalk:DescribeEvents",
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeInstanceHealth",
                "elasticloadbalancing:DescribeLoadBalancerAttributes",
                "elasticloadbalancing:DescribeTags",
                "elasticmapreduce:DescribeJobFlows",
                "elasticmapreduce:DescribeStep",
                "elasticmapreduce:DescribeCluster",
                "elasticmapreduce:DescribeTags",
                "elasticmapreduce:ListSteps",
                "elasticmapreduce:ListInstanceGroups",
                "elasticmapreduce:ListBootstrapActions",
                "elasticmapreduce:ListClusters",
                "elasticmapreduce:ListInstances",
                "es:ListDomainNames",
                "es:DescribeElasticsearchDomains",
                "glacier:List*",
                "glacier:DescribeVault",
                "glacier:GetVaultNotifications",
                "glacier:DescribeJob",
                "glacier:GetJobOutput",
                "iam:Get*",
                "iam:List*",
                "iot:DescribeThing",
                "iot:ListThings",
                "iam:GenerateCredentialReport",
                "kinesis:ListStreams",
                "kinesis:DescribeStream",
                "kinesis:GetShardIterator",
                "kinesis:GetRecords",
                "kms:Describe*",
                "kms:Get*",
                "kms:List*",
                "lambda:ListFunctions",
                "rds:Describe*",
                "rds:ListTagsForResource",
                "redshift:Describe*",
                "redshift:ViewQueriesInConsole",
                "route53:ListHealthChecks",
                "route53:ListHostedZones",
                "route53:ListResourceRecordSets",
                "s3:GetBucketACL",
                "s3:GetBucketLocation",
                "s3:GetBucketLogging",
                "s3:GetBucketPolicy",
                "s3:GetBucketTagging",
                "s3:GetBucketWebsite",
                "s3:GetBucketNotification",
                "s3:GetLifecycleConfiguration",
                "s3:GetNotificationConfiguration",
                "s3:GetObject",
                "s3:GetObjectMetadata",
                "s3:List*",
                "sdb:ListDomains",
                "sdb:DomainMetadata",
                "ses:ListIdentities",
                "ses:GetSendStatistics",
                "ses:GetIdentityDkimAttributes",
                "ses:GetIdentityVerificationAttributes",
                "ses:GetSendQuota",
                "sns:GetSnsTopic",
                "sns:GetTopicAttributes",
                "sns:GetSubscriptionAttributes",
                "sns:ListTopics",
                "sns:ListSubscriptionsByTopic",
                "sqs:ListQueues",
                "sqs:GetQueueAttributes",
                "storagegateway:Describe*",
                "storagegateway:List*",
                "support:*",
                "swf:ListClosedWorkflowExecutions",
                "swf:ListDomains",
                "swf:ListActivityTypes",
                "swf:ListWorkflowTypes",
                "workspaces:DescribeWorkspaceDirectories",
                "workspaces:DescribeWorkspaceBundles",
                "workspaces:DescribeWorkspaces"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchLogsSpecific",
            "Effect": "Allow",
            "Action": [
                "logs:GetLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": [
                "arn:aws:logs:*:*:*"
            ]
        }
    ]
}
```
