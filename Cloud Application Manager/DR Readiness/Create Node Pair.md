{{{
  "title": "Create Node Pair",
  "date": "09-26-2019",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

**In this article:**

* [Overview](#overview)
* [Audience](#audience)
* [Prerequisites](#prerequisites)
* [Create a Node Pair](#create-node-pair)

### Overview <a name="overview"></a>

This article is meant to assist users of Cloud Application Manager willing to use Disaster Recovery feature, trying to create new Replication Node Pairs

### Audience <a name="audience"></a>

All users of Cloud Application Manager who wants to use Disaster Recovery feature.

### Prerequisites <a name="prerequisites"></a>

* An active *Cloud Application Manager* account
* An existing *AWS* account configured in an [*AWS*](../Deploying Anywhere/using-your-aws-account.md) provider.
* Both CLC and AWS providers are registered

 
### Create a Node Pair <a name="create-node-pair"></a>
1. Click on **Disaster Recovery** on the navigation bar, then click on the button **New** to create a new pair.
![image](https://user-images.githubusercontent.com/20582531/65722771-357c3b00-e06a-11e9-9ffd-9b4386eb679c.png)

2. Click on **Start**
 ![image](https://user-images.githubusercontent.com/20582531/65722732-1bdaf380-e06a-11e9-8542-4d9f06389baa.png)
3. Fill in the information of the Node Pair:  
 a. Choose an Icon if needed  
 b. Give this Node Pair a name   
 c. Choose Production Provider  
 d. Choose Recovery Provider  
 e. Click on Next  
![image](https://user-images.githubusercontent.com/20582531/65728950-cd355580-e079-11e9-8ed3-97d58e72d642.png)
3. Fill in the detailed information of each Provider:  
 a. Decide the maximum servers to protect  
 b. Choose where to deploy your Prod node 
 c. Choose where to deploy your Recovery node  
 d. Click on Create  
![image](https://user-images.githubusercontent.com/20582531/65723513-c7d10e80-e06b-11e9-9f9c-2e91dd5580bc.png)

If you have additional questions, please [contact CLoud Application Manager Support](mailto:incident@CenturyLink.com)
