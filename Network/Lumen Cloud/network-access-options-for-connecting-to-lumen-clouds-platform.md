{{{
  "title": "Network Access Options for Connecting to Lumen Cloud's Platform",
  "date": "8-28-2014",
  "author": "Dave Burkhardt",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Network Access Options for Connecting to Lumen Cloud's Platform</strong>
</p>
<p>The following document is intended to be a basic overview of the possible network connectivity options for connecting to the Lumen Cloud platform. In summary, Lumen Cloud’s customers can leverage four different access methods to systems on
  the Lumen Cloud platform: 1.) Client Based VPN Tunnels, 2.) IPSec Point-to-Point VPN Tunnels, 3.) Direct Access Connectivity (i.e., bypassing the public Internet)&nbsp;and/or 4.) Assigning a Public IP(s) to a Virtual Machine(s). Moreover, if the
  utmost network resiliency is required, customers can easily deploy a combination of these access methods in-conjunction with each other. The descriptions below provide more details regarding the aforementioned access methods, and also connectivity scenarios
  for typical organizations.</p>

<p><strong>Client Based VPN Tunnels</strong>
</p>
<p>A virtual private network (VPN) is a virtual network built on top of existing physical networks that can provide a secure communications mechanism for data and control information transmitted between networks. VPNs are used most often to protect communications
  carried over public networks such as the Internet. A VPN can provide several types of data protection, including confidentiality, integrity, data origin authentication, replay protection and access control. This said, Lumen Cloud allows customers
  who wish to directly connect Windows, Linux and/or Macintosh based clients to their provisioned systems on Lumen’s platform (e.g., Exchange, SharePoint, AD, LAMP, etc servers) via a VPN client. This VPN connectivity is enabled by installing the
  OpenVPN software on the said operating systems. The software and instructions for installing the OpenVPN software can found on Lumen Cloud’s Control portal.</p>

<p><strong>IPSec Point-to-Point VPN Tunnels</strong>
</p>
<p>IPsec is a framework of open standards for ensuring private communications over public networks. It has become the most common network layer security control, typically used to create a VPN tunnel. There are two primary IPSec point-to-point tunnel configuration
  models Lumen Cloud supports, and they are as follows:</p>
<p>a)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Gateway-to-gateway. This model protects communications between two specific networks, such as an organization’s main office network and a branch office network, or two business partner’s networks.</p>
<p>b)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Host-to-gateway. This model protects communications between one or more individual hosts and a specific network belonging to an organization.</p>
<p>Possible Connectivity Scenarios for IPSec point-to-point tunnels:</p>
<p>1. A customer who wishes to extend their network and/or infrastructure to Lumen Cloud’s platform.</p>
<p>2. Customer who may want to off-load their backoffice systems (e.g., Exchange, SharePoint, etc) from their network/premises and have Lumen Cloud provide these services instead, but would like to maintain one seamless/contiguous network to its end-users.
  &nbsp;In addition with this scenario, a customer’s laptop/desktop would not need utilize the OpenVPN client while their system is connected to the corporate LAN. Although, if the OpenVPN infrastructure is configured, clients may chose to connect into
  their corporate network and/or Lumen Cloud’s platform when these users laptops are remote.</p>

<p><strong>Direct Access Connectivity</strong>
</p>
<p>Ethernet connectivity via data center cross connects and/or other dedicated circuit services are available options for Lumen Cloud’s customers who wish to bypass the public Internet and connect their infrastructure with dedicated connectivity.&nbsp;
  Bypassing the public Internet and deploying dedicated connectivity can improve performance between networks since Internet bound traffic typically will need to traverse multiple geographic points of presence (POPs) to get to its final destination. Moreover,
  enabling direct connectivity bypasses multiple other issues that are inherent with the Internet – e.g., DDOS attacks, ISP outages, network over subscription, etc.</p>

<p>Possible Connectivity Scenarios for Direct Access:</p>
<ol>
  <li>
    <p>If a customer has multiple branch offices, they can centralize all of their connectivity by meshing together all of their offices with a MPLS network, and then also extending this MPLS network to the Lumen Cloud platform. These types of MPLS
      <a href="http://www.centurylink.com/business/data/index.html">network services</a> can be purchased separately from Lumen, or from alternate network service providers. Enabling this type of architecture provides centralization of the
      Internet access and the security policies, and can be enforced from the head office.</p>
  </li>
  <li>
    <p>Customers who reside in the same data centers as Lumen Cloud (please see the following URL for the complete list of Lumen Cloud's data center locations: <a href="https://www.ctl.io/data-centers/">https://www.ctl.io/data-centers/</a>. You can leverage <a href="https://www.ctl.io/knowledge-base/network/intra-data-center-cross-connects-options-with-lumen-cloud/">Intra-Data Center Cross Connects</a> that will allow direct connectivity between the Lumen Cloud cage(s) and a customer’s infrastructure in that same facility. This direct connectivity will allow for fast, low-latency secure connections for the perfect combination of private and enterprise-grade public cloud for those enterprises who want to securely extend their network into the cloud. These intra-facility cross-connects can be configured through the Lumen Cloud Help Desk. More details of that process can be found here:&nbsp;<a href="https://www.ctl.io/knowledge-base/network/intra-data-center-cross-connects-options-with-lumen-cloud/">https://www.ctl.io/knowledge-base/network/intra-data-center-cross-connects-options-with-lumen-cloud/</a>
    </p>
  </li>
</ol>
