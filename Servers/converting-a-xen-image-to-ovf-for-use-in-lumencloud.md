{{{
  "title": "Converting a Xen Image to OVF for use in the Lumen Cloud",
  "date": "10-26-2021",
  "author": "Jake Malmad",
  "attachments": [],
  "contentIsHTML": true
}}}

<p>The .OVF (Open Virtualization Format) standard is an open-source, secure, and portable format compatible across nearly all hypervisors (VMware, Hyper-V, Xen, VirtualBox, etc.). Lumen Cloud recommends converting all virtual servers to OVF format prior to delivering
  to Lumen Cloud for import into our platform.</p>
<p>To convert a Citrix XenServer machine to OVF, begin by downloading <a href="http://www.citrix.com/downloads/xenserver/tools/conversion.html">XenServer Convert</a> (if converting multiple machines, it is recommended to install the Conversion
  Manager as well).</p>
<p>After installing and launching XenConvert, you will be prompted to select your source and destination workloads. If you are converting a single machine, you should be running the conversion tool from within the guest OS. Select "OFV" as the destination
  workload, and click next.</p>

<p>On the next screen, make any required changes to the destination partition layout.</p>

<p>On the next screen you will be prompted for your destination location, as well as the option to convert to an OVA (Open Virtualization Appliance), compress, encrypt or add a EULA.</p>

<p>You will be presented with a summary screen, and upon clicking "Convert," the conversion process will begin.</p>

<p>Once you have converted the Virtual Machine, please contact your Account Executive or our Professional Services team to import the OVF/OVA in to the Lumen Cloud.</p>
