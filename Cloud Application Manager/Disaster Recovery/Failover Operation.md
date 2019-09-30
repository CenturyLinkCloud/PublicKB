{{{
  "title": "Failover Operation",
  "date": "09-26-2019",
  "author": "Sharon Wang",
  "attachments": [],
  "contentIsHTML": false
}}}

### Requirements
2. The production server is protected and 100% synced

### Failover
1. Navigate to the production windows server. Make sure BECR is running and you have last checkpoint taken, click on **Test Failover**
![image](https://user-images.githubusercontent.com/20582531/65725568-39ab5700-e070-11e9-882f-40bf0f60d630.png)
3. Fill in the detailed information of Test Failover instance:
 a. Choose a desired checkpoint
 b. Choose the **Instance Type**
 c. Choose the **VPC**
 d. Choose the **subnet**
 e. Choose a **Security Group**
 e. Click on ** Failover**
![image](https://user-images.githubusercontent.com/20582531/65725624-5a73ac80-e070-11e9-8fe6-2c04a24c2bb4.png)
4. Once the Recovery server is deployed, you will be able to see the Failover instance on Instances tab
![image](https://user-images.githubusercontent.com/20582531/65725661-6cede600-e070-11e9-9555-b54cbb60eb15.png)
