{{{
  "title": "Test Failover Operation",
  "date": "09-26-2019",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Test Failover](#Test-Failover)

### Overview <a name="overview"></a>

This article is meant to assist users of Cloud Application Manager willing to use Disaster Recovery feature, trying to initiate Test Failover Operation

### Audience <a name="audience"></a>

All users of Cloud Application Manager who wants to use Disaster Recovery feature.

### Prerequisites <a name="prerequisites"></a>

* The production server is protected and 100% synced

### Test Failover <a name="Test-Failover"></a>
1. Navigate to the production windows server. Make sure BECR is running and you have last checkpoint taken, click on **Test Failover**
![image](https://user-images.githubusercontent.com/20582531/65725336-9ce8b980-e06f-11e9-9018-d9edaec3d888.png)

3. Fill in the detailed information of Test Failover instance:
 a. Choose a desired checkpoint
 b. Choose the **Instance Type**
 c. Choose the **VPC**
 d. Choose the **subnet**
 e. Click on ** Test Failover**
![image](https://user-images.githubusercontent.com/20582531/65725465-ee914400-e06f-11e9-882d-dd2952494c21.png)
4. Once the Recovery server is deployed, you will be able to see the Test Failover instance on Instances tab
![image](https://user-images.githubusercontent.com/20582531/65725483-02d54100-e070-11e9-9261-186b0187ea4a.png)
5. You Can delete the Test Failover clone by simply deleted by Terminating it:
![image](https://user-images.githubusercontent.com/20582531/65725517-197b9800-e070-11e9-93c8-40738fc04c1a.png)

If you have additional questions, please [contact CLoud Application Manager Support](mailto:incident@CenturyLink.com)
