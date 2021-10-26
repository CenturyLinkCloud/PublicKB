{{{
  "title": "Getting Started with Managed Microsoft IIS",
  "date": "10-26-2021",
  "author": "Jared Ruckle",
  "attachments": [],
  "contentIsHTML": false
}}}

The Internet Information Services (IIS) for Windows&reg; Server is a flexible, secure and manageable Web server for hosting anything on the Web. From media streaming to web applications, IIS's scalable and open architecture is ready to handle the most demanding tasks. The MS-IIS Web server application offers a reliable, high performance, and secure vehicle for delivering HTTP content to end users.

Here's how to create a managed IIS environment in Lumen Cloud. **NOTE**: Before you can deploy Managed Microsoft IIS, you must create a Managed Windows server.

1. Log on to the [Control Portal](//control.ctl.io/). Using the left side navigation bar, select **Orchestration** > **Blueprints Library**. Search for IIS. Then, click the **CLC Managed MS IIS** Blueprint.
    
2. Click the **DEPLOY BLUEPRINT** button.
    
3. Fill out the appropriate details for the CLC Managed MS IIS Blueprint, and click **Next**.

    **NOTE**: Please choose the same server for both the Installation and Registration of Managed MS IIS. The server must have Managed Windows installed, otherwise the Blueprint will fail.
    
4. Verify that the information is correct.

5. Once verified, please click the **DEPLOY BLUEPRINT** button. You will be presented with the deployment details along with an email stating the Blueprint has been queued.
    

You will receive an email that your Blueprint has been installed when the Blueprint is complete.

**NOTE**: The server now has the Managed MS IIS software installed and activated.

### FREQUENTLY ASKED QUESTIONS

**Q: How is the Lumen Cloud for Managed MS IIS priced?**

A: Lumen Cloud for Managed MS IIS is priced by the VM, billed hourly.

**Q: Can the customer have multiple MS IIS Instances installed on the same server?**

A: No, MS IIS can only be installed once per server, but IIS is capable of hosting thousands of web sites per server.

**Q: What Versions of MS IIS does Lumen Cloud support?**

A: Lumen Cloud Supports Microsoft IIS 7.5, Microsoft IIS 8.0 and Microsoft IIS 8.5.

**Q: What operating systems are supported for Managed MS IIS?**

A: Managed Windows 2008 R2, Managed Windows 2012 R2.

**Q: Can *un-managed* Microsoft IIS services be converted to *Managed* (or vice versa)?**

A: This capability is not available at this time.
