{{{
  "title": "CPC Metrics",
  "date": "6-17-2021",
  "author": "Anthony Hakim",
  "keywords": ["cpc", "cloud", "vm", "metrics", "vapp", "vcloud", "vcf"],
  "attachments": [],
  "related-products" : [],
  "contentIsHTML": false,
  "sticky": true
}}}

### Description
Lumen Private Cloud on VMware Cloud Foundation (LPC on VCF) customers can now view eight (8) different metrics for running VMs that are within the VMware Cloud Director (vCD) environment. Those eight metrics include the following:

1.	disk.read.average
2.	disk.provisioned.latest
3.	cpu.usage.average
4.	disk.write.average
5.	cpu.usagemhz.average
6.	mem.usage.average
7.	cpu.usage.maximum
8.	disk.used.latest

There are also four (4) different time periods to choose from, including the following:

1. 1/2 Hour
2. Hour
3. Day
4. Week

### Steps
* To view metrics, log in to LPC on VCF, select **Data Centers**, and then click the Data Centers summary box.

  ![CPC Metrics](../../images/dccf/data-centers-summary.png)

 * Select **DETAILS** on a running VM for which you would like to view metrics.

  ![CPC Metrics](../../images/dccf/cpc-metrics1.png)

* In the VM details page, select **Monitoring Chart**.

  ![CPC Metrics](../../images/dccf/cpc-metrics2.png)

* Select the appropriate **Metric** and **Period**. You may need to click **REFRESH**.

  ![CPC Metrics](../../images/dccf/cpc-metrics3.png)
