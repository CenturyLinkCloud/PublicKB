{{{
  "title": "Cloud Platform - Release Notes: December 16, 2014",
  "date": "12-12-2014",
  "author": "Bryan Friedman",
  "attachments": []
}}}

<p><strong>New Features (2)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong><strong>vRealize (vCAC) adapter. </strong></strong>CenturyLink Cloud is now supported by&nbsp;<a href="https://www.vmware.com/products/vrealize-suite" target="new">VMware’s vRealize</a>,&nbsp;a cloud management platform that enables users to
    perform functions against VMware vSphere, other hypervisors, and select public clouds.&nbsp;For CenturyLink customers who have built custom private clouds using VCE or hybrid solutions with vCloud Air, vRealize provides a seamless integration point
    for extending deployments to the CenturyLink Cloud. Likewise, VMware customers looking to extend their hybrid footprint into the CenturyLink Cloud can leverage vRealize to manage their CenturyLink Cloud virtual machines. You can find more about&nbsp;the
    full features of this integration in<a href="https://t3n.zendesk.com/entries/54755210-vRealize-6-1-formerly-vCAC-Support-for-CenturyLink-Cloud" target="new">&nbsp;our knowledge base</a>.
    <p><img src="https://t3n.zendesk.com/attachments/token/wP9LtW8dhUPUuzlJlA7qaRnMs/?name=vRealize_2.png" alt="vRealize_2.png" />
    </p>
  </li>
  <li><strong>Managed Services updates.&nbsp;</strong>Managed Services users can now see a complete list of managed applications installed on a server right from the Server Details page. In addition, the backend process for enabling a managed server was streamlined
    to include additional automation as well as waiting&nbsp;to start the billing subscription until installation is complete.
    <br /><img src="https://t3n.zendesk.com/attachments/token/QTRU3uqc5MCkKMQrWxdTlCDqT/?name=managed-apps-list.png" alt="managed-apps-list.png" />
  </li>
</ul>
<p></p>
<p><strong>Minor Enhancements (3)</strong>
</p>
<div>
  <hr />
</div>
<ul>
  <li><strong>Red Hat 7 support.&nbsp;</strong>CenturyLink Cloud now supports&nbsp;Red Hat 7 as an OS template for servers. Customers can now create and deploy 64-bit Red Hat Enterprise Linux 7 virtual instances to all data centers. Among other things, this
    latest version of RedHat has native support for Docker. Check out&nbsp;<a href="https://access.redhat.com/sites/default/files/pages/attachments/rhel_whatsnewrhel7beta_techoverview_.pdf">what else is new in version 7</a>&nbsp;and read
    the <a href="https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/7.0_Release_Notes/">Red Hat 7 Release Notes</a>&nbsp;for more information.
    <br /><img src="https://t3n.zendesk.com/attachments/token/3njshOW7fRrpnLRAWEIp1rLeJ/?name=rhel7-os.png" alt="rhel7-os.png" />
    <br />
    <br />
  </li>
  <li><strong>4 TB storage limit.&nbsp;</strong>While it has always been a recommended best practice for CenturyLink Cloud customers,&nbsp;the platform will now actually enforce a&nbsp;<em>four terabyte</em>&nbsp;(4,096 GB) limit on <em>total</em> storage
    for all standard and premium servers. The platform will continue to enforce the existing&nbsp;<em>one terabyte&nbsp;</em>(1,024 GB) maximum for each individual disk and hyperscale&nbsp;instances still support up to&nbsp;<em>one terabyte</em>&nbsp;(1,024
    GB) only of total storage.
    <br />
    <br />
  </li>
  <li><strong>WA1 Public IP enhancements.</strong>&nbsp;The US West (Seattle) WA1 data center now supports custom ports and source IP filtering when adding public IPs to servers. All other CenturyLink Cloud data centers already support this functionality.</li>
</ul>