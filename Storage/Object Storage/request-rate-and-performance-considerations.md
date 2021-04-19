{{{
  "title": "Request Rate and Performance Considerations",
  "date": "1-9-2020",
  "author": "Lumen",
  "keywords": ["clc", "cloud", "cdn", "object", "storage", "s3", "platform"],
  "attachments": [],
  "contentIsHTML": false
}}}

### Overview
Lumen Cloud's S3 compatible storage service provides geo-redundant storage (GRS) services to deliver or store unstructured data. In delivering this service customers may need to understand best practices and scaling considerations to maintain optimal performance of the service.

### Platform Maximums
* 1,200 requests (Get, Put, Delete, List) over a 60 second period **per Access Key ID (user)**.

### Workload Types
To design services to scale and performance we'll breakdown a few common types of workloads and align that with a general design best practice for the storage services.

##### GET-Intensive Workloads
GET-intensive workloads are best served by a [Content Delivery Network](http://ctl.io/lumen-cdn-options/) as you can distribute content to your users with low latency and a high data transfer rate. This results in significantly less direct requests to Lumen's storage service where a platform maximum is imposed that could impact user experience.

##### PUT-Intensive Workloads
PUT-intensive workloads, such as Backup to cloud methodologies, should be segmented into **unique** buckets and Access Key IDs (Users). This structure may take various forms but using the Backup to cloud approach a client would create a **new bucket and unique user** for each host/server or cloud vault repository allowing data backup jobs/agents to scale horizontally above the per access key ID (user) maximums.

**Quick Tip:** each user must have a unique email address and while this email is not used for any service delivery, clients may need to use a convention that allows reuse of the same email address. To do so use a ```+``` approach such as first.lastname+obj1@ctl.io, first.lastname+obj2@ctl.io, first.lastname+obj3@ctl.io.

##### Workloads with a Mix of Request Types
Clients with a wide range of request types may have to use market benchmark tools (during staging) and user performance monitoring (during production) to evaluate performance levels real-time and align them with business service levels. In the end the same platform maximums are imposed on a per access key ID (user) so care should be taken to scale users and buckets or augment web based content with [CDN services](http://ctl.io/lumen-cdn-options/).
