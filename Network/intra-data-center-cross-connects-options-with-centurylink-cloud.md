{{{
  "title": "Intra-Data Center Cross Connects Options with CenturyLink Cloud",
  "date": "9-16-2014",
  "author": "Dave Burkhardt",
  "attachments": [
    {
      "url":"../attachments/XC_Questionnaire_2013222.pdf",
      "type":"application/pdf",
      "file_name":"XC_Questionnaire_2013222.pdf"
    },
    {
      "url":"../attachments/Letter of Authorization_Template.docx",
      "type":"application/vnd.openxmlformats-officedocument.wordprocessingml.document",
      "file_name":"Letter of Authorization_Template.docx"
    }
  ],
  "contentIsHTML": true
}}}

<p>Updated 9/15/14</p>
<p>This Knowledge Base and associated “Intra-Data Center Cross Connect Questionnaire“ (please see attached below) provides an overview for customers who are considering deploying an intra-data center cross connect. The labor for this deployment is
  a service task, performed by platform engineers to specifications provided by the customer.</p>
Cross Connects Description and Benefits
<p>As noted in the Knowledge Base article entitled “Network Access Options for Connecting to CenturyLink Cloud’s Platform” (see: https://www.ctl.io/knowledge-base/network/network-access-options-for-connecting-to-centurylink-clouds-platform/), CenturyLink Cloud offers multiple connectivity options
  for its customers to leverage when deciding how they will connect to their resources hosted on CenturyLink Cloud’s platform (e.g., VPN tunnels, CNS, Cross Connects, etc). That said, as a point of clarity, this knowledge base article specifically pertains
  to the deployment of cross connects that are described within the aforementioned URL.</p>
<p>In summary, cross connects are directly connected network circuits between two physically isolated organizations within a data center provider’s facility. Currently, CenturyLink Cloud has presence within the data centers listed at the following URL: https://www.ctl.io/data-centers/.
  This direct connectivity allows for fast, low-latency secure connections – a perfect combination for enterprises who want to securely extend their network into the cloud. While this process may differ slightly in each data center, this article describes
  the general options, decisions, etc. that need to be considered.</p>
<p>Many of our data center providers are within in multiple building across their respective metropolitan areas, and therefore “campus cross connects” are also an option for customers to consider (e.g., Customer is in Equinix’s CH1 building and CenturyLink
  Cloud is in Equinix’s CH3 building). These connections are usually more costly, but are a feasible option to be considered.</p>
Planning Your Cross Connect
<p>The first decision a customer needs to determine is how they want to purchase the cross connect. There are generally two options available to a customer:</p>
<p>Option #1 - The customer purchases the cross connect directly from the data center provider:
  <br />•&nbsp;Pros: In the long run, this is cheaper for the customer as they are purchasing the cross connect directly from the data center provider.
  <br />•&nbsp;Cons: The customer is responsible for the coordination of the cross connect implementation with the data center provider directly.</p>
<p>Option #2 - The customer purchases the cross connect from CenturyLink Cloud (CLC):
  <br />•&nbsp;Pros:</p>
<p>a. CLC manages the implementation of the cross connect with the data center provider.
  <br />b. The costs of the cross connect will come as part of the customer’s normal CLC monthly invoice.</p>
<p>•&nbsp;Cons: Cost of the cross connect is ~20% more expensive, since CenturyLink Cloud adds an administrative processing fee on top of our data center providers fees.</p>
<p>Regardless, if a customer chooses to purchase the cross connect on their own, there still will be a Professional Services fee that will include the following services:</p>
<p>• Verify cross connect connectivity options with data center provider
  <br />• Process Letter of Authorization (LOA) data center provider
  <br />• Coordinate schedules to hold 30min "pre-turn-up" call and actual turn-up call
  <br />• 1hr of time to work with customer to test and turn-up circuit</p>
<p>Note: additional fees may need to be authorized if customer requests CenturyLink Cloud (CLC) to:</p>
<p>• Provide assistance with completing the Intra Data Center Cross Connect Questionnaire (please see below for more information)
  <br />• Manage customer's 3rd party vendors
  <br />• Design or document cross connect configurations
  <br />• Setup a test environment
  <br />• Turn-up calls last longer than 1hr
  <br />• Provide recommendations/guidance on routing configurations (e.g., BGP, OSPF, etc)</p>
<p>Also, in addition to the Professional Services fee, a monthly port fee will be charged by CLC to cover cost for:</p>
<p>• Parts associated to connect the data center provider’s cross connect to CLC’s router – this typically includes cabling and the Single Mode Fiber (SMF, 1310nm) 1Gbps (1000base-LX) and/or or 10gbps (10G-LR) transceiver optics.
  <br />• Usage of the router port required for the cross connect
  <br />• 24x7x365 monitoring and incident resolution of the connection/port</p>
Ordering Cross Connects
<p>Once a purchasing decision is made, the following will need to be ascertained/submitted:</p>
<p>• ALL data center providers require a Letter of Authorization (LoA) to install a cross connect. In summary, LoAs provide data center authorization to provision the cross connects- although the responsibility to create the LoA is dependent on who is ordering
  the cross connect (e.g., CLC or our customer):</p>
<p>o If the <strong>customer purchases the cross connect</strong> from the data center provider, <strong>CLC will supply a LoA to the customer</strong>, and then the customer will need to submit it to the data center.
  <br />o If <strong>the customer buys the cross connect from CLC</strong>, <strong>the customer will need to give CLC a LoA</strong> (customers who don’t have a LoA template, please see the LoA template listed below), and then the CenturyLink Cloud will submit the completed
  LoA the data center provider.</p>
<p>• Determine the circuit requirements. CLC's currently only offers Single Mode Fiber (SMF, 1310nm) 1Gbps (1000base-LX) or 10gbps (10G-LR) fiber. We can also support 1 Gbps copper if the cross connect is less than 100m in length. Additionally, as a few
  points of clarity <strong>we do not offer support for</strong>:</p>
<p>o Multi-Mode fiber (MMF, generally 850nm wavelength) is not supported (Note: 1 Gbps is 1000base-SX, 10 Gbps is 10G-SR)
  <br />o Extended fiber distances (10G-ER, 10G-ZR, CWDM, DWDM etc).
  <br />o Desktop initiated Internet access</p>
<p>• Verify circuit hand-off will be native Ethernet hand-offs – e.g., no DS-3, SONET, OC3</p>
<p>• Determine the preferred routing protocol (e.g., static, BGP, OSPF).</p>
<p>• Will the cross connect be deployed within one of data centers/campuses listed at: https://www.ctl.io/data-centers/</p>
<p>• Determine if any specific IP address ranges are required for CLC. Note, CLC can generally only provide /24 networks for customers, but if a specific requirement is needed CenturyLink Cloud will evaluate such requests.</p>
<p>Once the aforementioned is decided, the next steps are for CLC’s customers to complete the LoA (if CenturyLink Cloud is purchasing the cross connect on the customer’s behalf), the Intra-Data Center Cross Connect Questionnaire (please see the attached "XC_Questionnaire_2013222.pdf"
  listed below), and authorize an agreement for any associated costs. Customers should expect a minimum of two week lead time to provision most cross connect deployments once all of the paperwork has been finalized.</p>
