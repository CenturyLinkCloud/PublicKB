{{{
  "title": "Connecting Data Center Networks Through Firewall Policies",
  "date": "12-12-2012",
  "author": "Richard Seroter",
  "attachments": [],
  "contentIsHTML": true
}}}

<p><strong>Description:</strong>
</p>
<p>CenturyLink Cloud Platform users can now connect networks within a particular data center through the use of configurable firewall policies. This is useful when a customer has multiple vlans within a particular account, or has a range of sub-accounts with
  their own vlans, and wants to selectively choose the traffic that can flow among them.</p>
<p><strong>Steps:</strong>
</p>
<p><strong>1. Confirm that you are working with servers on multiple networks.&nbsp;</strong>
</p>
<ul>
  <li>View the available networks for the parent account. Notice a single network for the account with alias <strong>RSDA</strong>.
    <br /><img src="https://t3n.zendesk.com/attachments/token/pr4zw73lkszj5hn/?name=firewalloverview01.png" alt="firewalloverview01.png" />
  </li>
  <li>Create or identify a server that is part of this account and this network. See that the server below has an IP address that is part of the above vlan.
    <br /><img src="https://t3n.zendesk.com/attachments/token/fp3mesplizlt7rf/?name=firewalloverview03.png" alt="firewalloverview03.png" />
  </li>
  <li>Navigate to a sub-account and view the available networks. In the image below, see a single network for the sub-account with alias <strong>SSUB</strong>.
    <br /><img src="https://t3n.zendesk.com/attachments/token/snavywmq9cyiyfw/?name=firewalloverview02.png" alt="firewalloverview02.png" />
  </li>
  <li>Create or identify a server that is part of this particular account and network. See that the server below has an IP address that is part of the above vlan.
    <br /><img src="https://t3n.zendesk.com/attachments/token/9s1lw1a1twdqrhy/?name=firewalloverview04.png" alt="firewalloverview04.png" />
  </li>
</ul>
<div><strong>2. Check to see if the servers on different networks can "see" each other.</strong>
</div>
<div>
  <ul>
    <li>Log into each server.
      <br /><img src="https://t3n.zendesk.com/attachments/token/lr9utt2jcpag7e9/?name=firewalloverview05.png" alt="firewalloverview05.png" />
    </li>
    <li>Attempt to ping one server from the other.
      <br /><img src="https://t3n.zendesk.com/attachments/token/qx7sjd1lawbb4ne/?name=firewalloverview06.png" alt="firewalloverview06.png" />
    </li>
    <li>Notice that the server in the parent account's vlan is unable to see the server in the sub-account's vlan.</li>
  </ul>
  <div><strong>3. Create a firewall policy that connects these two networks.</strong>
  </div>
  <div>
    <ul>
      <li>Navigate back to the parent account's <strong>Network </strong>settings. If you have appropriate permissions, then a menu item called <strong>Firewall </strong>should appear in the Network navigation.
        <br /><img src="https://t3n.zendesk.com/attachments/token/khmpd6qbg6uxina/?name=firewalloverview07.png" alt="firewalloverview07.png" />
      </li>
      <li>On the Firewalls page, there are two key sections (highlighted below) beneath either the&nbsp;<strong>Intra Data Center </strong>and <strong>Cross Data Center </strong>tabs. The <strong>first section</strong> identifies the account connections being
        made. Once an account is selected, all vlans that are part of that account can become part of the firewall policy. <strong>Note that this screen does not show ALL firewall policies in place for an account. It only shows the policies that are in place for the selected "source account" and "destination account" combination. </strong>The
        <strong>second section</strong>&nbsp;of this screen is where firewall policies are created, edited and ordered.
        <br /><img src="https://t3n.zendesk.com/attachments/token/7vz1ebnfc1puyso/?name=firewalloverview08.png" alt="firewalloverview08.png" />
      </li>
      <li>Set the <strong>Destination Account </strong>to the appropriate sub-account, or keep the same account name of the <strong>Account Account</strong>&nbsp;if you are planning to link multiple networks within the same account.
        <br /><img src="https://t3n.zendesk.com/attachments/token/7vpflfmsslcftxr/?name=firewalloverview09.png" alt="firewalloverview09.png" />
      </li>
      <li>Click the <strong>add policy </strong>button to define a new firewall policy between vlans in these two accounts. From here you can set the status ("on" or "off"), source IP addresses, destination IP addresses, and ports to expose.
        <br /><img src="https://t3n.zendesk.com/attachments/token/cjomfru8jscgrfy/?name=firewalloverview10.png" alt="firewalloverview10.png" />
      </li>
      <li>Click the <strong>add source address </strong>button to choose the vlan and IP address (range) that is part of this policy. This pop up lets you narrow down the pool of source IP addresses by selecting a subnet size and the starting IP address.
        <br
        /><img src="https://t3n.zendesk.com/attachments/token/k8ujnbnc78uls8c/?name=firewalloverview11.png" alt="firewalloverview11.png" />
      </li>
      <li>When these settings are saved, the firewall policy shows the source address in <a href="http://en.wikipedia.org/wiki/CIDR_notation" target="_blank">Classless Inter-Domain Routing (CIDR) notation</a>&nbsp;(see an <a href="http://technet.microsoft.com/en-us/library/cc958832.aspx"
        target="_blank">additional explanation of CIDR here</a>).
        <br /><img src="https://t3n.zendesk.com/attachments/token/46jc6gtxktmmsc1/?name=firewalloverview12.png" alt="firewalloverview12.png" />
      </li>
      <li>Next, choose the <strong>add destination address</strong>&nbsp;button and select a network and IP range that will satisfy the needs of the firewall policy.
        <br /><img src="https://t3n.zendesk.com/attachments/token/d6d0e1hwezulvuy/?name=firewalloverview13.png" alt="firewalloverview13.png" />
      </li>
      <li>Finally, click the <strong>add port</strong>&nbsp;button to select which ports are being opened as part of this firewall policy.
        <br /><img src="https://t3n.zendesk.com/attachments/token/noalky2hyx9a7wb/?name=firewalloverview14.png" alt="firewalloverview14.png" />
      </li>
      <li>In this example, the PING port was selected to enable simple ping communication between the networks.
        <br /><img src="https://t3n.zendesk.com/attachments/token/u5u4rzv2ukzwfzm/?name=firewalloverview15.png" alt="firewalloverview15.png" />
      </li>
      <li>Save the firewall policy and it is instantly applied to the firewall. You can then see the policy and click it to edit it.
        <br /><img src="https://t3n.zendesk.com/attachments/token/mmf28xgrohw7itv/?name=firewalloverview16.png" alt="firewalloverview16.png" />
      </li>
      <li>Note that there can be multiple firewall policies defined between networks, and the <strong>order of policies matters</strong>. The policies are evaluated in a "first match" manner, so the most restrictive policies should be at the top, and the
        most unrestricted at the bottom.</li>
    </ul>
    <div><strong>4. Confirm that firewall policy is working.</strong>
    </div>
    <div>
      <ul>
        <li>From the server in the parent account's network, once again attempt to ping the server in the sub-account's network.
          <br /><img src="https://t3n.zendesk.com/attachments/token/mtdute2j3pmbxkz/?name=firewalloverview17.png" alt="firewalloverview17.png" />
        </li>
        <li>See that the ping attempt is now successful because there is now a firewall policy in place that allows ping communication between the two networks.</li>
      </ul>
    </div>
  </div>
</div>