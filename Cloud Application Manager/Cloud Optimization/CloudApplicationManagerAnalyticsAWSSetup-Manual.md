{{{
  "title": "Cloud Optimization AWS Configuration - Manual",
  "date": "06-01-2017",
  "author": "Chris Meyer",
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
This process details the steps needed to manually configure your AWS account for Cloud Application Manager Analytics functionality.

If you prefer the set-up of your environment to be automated, you can find that procedure [here](CloudApplicationManagerAnalyticsAWSSetup.md).

#### Login to your AWS Account
1. Login to the target AWS account [here](https://console.aws.amazon.com/iam).
2. Access the IAM dashboard.

#### Create CenturyLink Cloud Optimization IAM Policy
1. Navigate to IAM "Policy."
2. Click "Create Policy."
3. Select "Create Your Own Policy."
4. Name the Policy as follows: CTLCloudOptimizationPolicy.
5. Add the following Description: Access Policy for CTL's Cloud Optimization Functionality.
6. Paste the CenturyLink Cloud Optimization IAM policy documented [below](#centuryLink-cloud-optimization-iam-policy).
7. Click "Validate Policy."
8. Click "Create Policy."

#### Create CenturyLink Cloud Optimization IAM Role
1. Navigate to IAM "Roles."
2. Click "Create New Role."
3. Click "Role for Cross-account access."
4. Select "Provide access between your AWS account and 3rd party AWS account."
5. Add Account ID as follows: 540339316802.
6. Add External ID as follows: [as provided by Cloud Optimization].
7. Do NOT check "require MFA."
8. Click "Next Steps."
9. Select "CTLCloudOptimizationPolicy."
10. Click "Next Step."
11. Name the Role as "CTLCloudOptimization."
12. Add the following Description: "CTL's Cloud Optimization Functionality."
13. Click "Create Role."

#### Retrieve ARN role
1. Select the CenturyLink Cloud Optimization AMI Role.
2. Record listed ARN.
3. Paste ARN into the Cloud Optimization Portal or send it to your on-boarding representative.


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
