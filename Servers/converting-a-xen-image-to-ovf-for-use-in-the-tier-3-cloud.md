{{{
  "title": "Converting a Xen Image to OVF for use in the CenturyLink Cloud",
  "date": "5-28-2013",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The .OVF (Open Virtualization Format) standard is an open-source, secure, and portable format compatible across nearly all hypervisors (VMware, Hyper-V, Xen, VirtualBox, etc.). CenturyLink Cloud recommends converting all virtual servers to OVF format prior to delivering
  to CenturyLink Cloud for import into our platform.</p>
<p>To convert a Citrix XenServer machine to OVF, begin by downloading <a href="http://www.citrix.com/downloads/xenserver/tools/conversion.html">XenServer Convert</a> (if converting multiple machines, it is recommended to install the Conversion
  Manager as well).</p>
<p>After installing and launching XenConvert, you will be prompted to select your source and destination workloads. If you are converting a single machine, you should be running the conversion tool from within the guest OS. Select "OFV" as the destination
  workload, and click next.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/aybtrcxixvlzvha/?name=xen.png" alt="xen.png" />
</p>
<p>On the next screen, make any required changes to the destination partition layout:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/u425ibzpjgxfzcj/?name=x2.PNG" alt="x2.PNG" />
</p>
<p>On the next screen you will be prompted for your destination location, as well as the option to convert to an OVA (Open Virtualization Appliance), compress, encrypt or add a EULA:</p>
<p><img src="https://t3n.zendesk.com/attachments/token/vb8uo6cpncswpuo/?name=x3.PNG" alt="x3.PNG" />
</p>
<p>You will be presented with a summary screen, and upon clicking "Convert" the conversion process will begin.</p>
<p><img src="https://t3n.zendesk.com/attachments/token/ihs2y9scaaa6qae/?name=x4.PNG" alt="x4.PNG" />
</p>
<p>Once you have converted the Virtual Machine, please contact your Account Executive or our Professional Services team to import the OVF/OVA in to the CenturyLink Cloud.</p>