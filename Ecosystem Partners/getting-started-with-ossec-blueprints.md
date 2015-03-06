{{{
  "title": "Getting Started With OSSEC Blueprints",
  "date": "3-6-2015",
  "author": "Keith Resar",
  "attachments": [],
  "contentIsHTML": true
}}}

### Partner Profile

<a href="http://www.ossec.net/"><img src="http://www.ossec.net/wp-content/uploads/2012/06/ossec-hids.png" style="border:0;float:right;margin:1em;"/></a>

 * OSSEC - Open Source SECurity
 * <a href="http://www.ossec.net/">http://www.ossec.net/</a>
 * Customer Support:
  * <a href="http://www.ossec.net/?page_id=21">OSSEC Community Site</a>
  * Paid Support from Trend Micro
  * Partner Tier: Silver

<strong>Description</strong>
<p>CenturyLink has integrated the OSSEC HIDS solution in to the CenturyLink Cloud platform to enable customers to perform self-service installation of an OSSEC manager and HIDS agents on Windows or Linux servers. The purpose of this KB article is to help
  the reader take advantage of this integration to achieve rapid time-to-value for this HIDS solution.</p>
<p>OSSEC is a free, open-source host-based intrusion detection system (HIDS). It performs log analysis, integrity checking, Windows registry monitoring, rootkit detection, time-based alerting, and active response. It provides intrusion detection for most
  operating systems, including Linux, OpenBSD, FreeBSD, Mac OS X, Solaris and Windows. OSSEC has a centralized, cross-platform architecture allowing multiple systems to be easily monitored and managed.</p>
<p>As a Silver-certified member of the&nbsp;<a href="https://t3n.zendesk.com/entries/58187134-CenturyLink-Cloud-Ecosystem-Program-Guide-">CenturyLink Cloud Ecosystem Program</a>, the only thing which CenturyLink Cloud certifies is that the Partner technology
  deploys successfully to the CenturyLink Cloud. We provide complementary knowledge-base articles to get the customer started but all support is available directly from the existing OSSEC community and not CenturyLink.</p>

<strong>Audience</strong>
<ul>
  <li>CenturyLink Cloud Users</li>
</ul>

<strong>Impact</strong>
<p>After reading this article, the user should feel comfortable getting started installing OSSEC managers and agents on CenturyLink Cloud.</p>

<strong>Prerequisite</strong>&nbsp;
<ul>
  <li>Access to the CenturyLink Cloud platform as an authorized user.</li>
</ul>
<strong>&nbsp;</strong>
<strong>Detailed Steps</strong>
<p>Follow these step by step instructions to install OSSEC.</p>
<p><strong>OSSEC Manager Installation on Linux</strong>
</p>
<p>CenturyLink has developed a script package that installs and configures an OSSEC Manager on an existing Linux server (we recommend CentOS or RHEL). This can be installed&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>.</p>
<table>
  <tbody>
    <tr>
      <td>
        <p>1.&nbsp;Navigate to a group of servers, hover over the "actions" menu and choose the “execute package” option as described in the&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>&nbsp;KB</p>
      </td>
      <td>&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;2.&nbsp;Select the public package "Security - Install OSSEC Manager for Linux"</p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/84QNbdKX4R2aVV8JP6zyKaKZj/?name=Screen+Shot+2015-01-02+at+2.37.58+PM.png" alt="Screen_Shot_2015-01-02_at_2.37.58_PM.png" />
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;3. Provide required information. An administrator email address is coded into the OSSEC manager configuration and is used for all alerts generated on the manager and associated agents. For production use this should probably
          be a group alias.</p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/DLUf9Oab2yQ7B8fIaTkQEnrl0/?name=Screen+Shot+2015-01-02+at+2.43.49+PM.png" alt="Screen_Shot_2015-01-02_at_2.43.49_PM.png" />
      </td>
    </tr>
    <tr>
      <td>
        <p>4. Provide optional information. </p>
        <p>Set "ossec id" to provide a unique cluster ID. This can be left blank in most deployments and should only be populated if there will be multiple OSSEC Managers on the local submit.</p>
        <p>"ossec key" is a security string which must be known to register the agent. This can be left blank in most deployments as the OSSEC Manager can only be access from other trusted hosts.</p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/0DQHi9ihXHTZhSvVzPOe2lWOa/?name=Screen+Shot+2015-01-02+at+2.44.13+PM.png" alt="Screen_Shot_2015-01-02_at_2.44.13_PM.png" />
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;5. Select a single server to install package on</p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/U3UqLKww4AMDPVruZ48R5AUry/?name=Screen+Shot+2015-01-02+at+2.52.07+PM.png" alt="Screen_Shot_2015-01-02_at_2.52.07_PM.png" />
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;6. Select to execute package and watch deployment process. </p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/qQV4Qk213s8YFgGi8Kor42mjH/?name=Screen+Shot+2015-01-02+at+2.52.57+PM.png" alt="Screen_Shot_2015-01-02_at_2.52.57_PM.png" />
      </td>
    </tr>
    <tr>
      <td>
        <p>7.&nbsp;If all works as expected your administrator email address will get an automated startup notification from OSSEC (email is only sent if running on CentOS/RHEL).</p>
      </td>
      <td><img src="https://t3n.zendesk.com/attachments/token/szjdjoSBFb6X8nq6Ftb0krUZa/?name=email.png" alt="email.png" />
      </td>
    </tr>
  </tbody>
</table>

<p><strong>OSSEC Agent Installation on Linux and Windows</strong>
</p>
<p>CenturyLink has developed a script package that installs and configures an OSSEC Agent on an existing Linux or Windows server. This can be installed&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>.</p>
<table>
  <tbody>
    <tr>
      <td>
        <p>1. Enable bidirectional <strong>1514/UDP</strong> traffic between the manager server and the new agent. UDP is stateless so you'll need to add two rules - one for the manager as source and one for the agent as source</p>
      </td>
      <td>
        <p>&nbsp;<a href="https://t3n.zendesk.com/entries/22196842-Connecting-Data-Center-Networks-Through-Firewall-Policies">Connecting Data Center Networks Through Firewall Policies></a>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p>2.&nbsp;Navigate to a group of servers, hover over the "actions" menu and choose the “execute package” option as described in the&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>&nbsp;KB</p>
      </td>
      <td>
        <p>&nbsp;<a href="https://t3n.zendesk.com/entries/21807618-Using-Group-Tasks-to-Install-Software-and-Run-Scripts-on-Groups">Using Group Tasks to Install Software and Run Scripts on Groups</a>
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;3.&nbsp;Select the public package "Security - Install OSSEC Agent for Linux" or&nbsp;"Security - Install OSSEC Agent for Windows"</p>
      </td>
      <td>
        <p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/m2mzaqxxZq85mfTFM4luqfai1/?name=Screen+Shot+2015-01-02+at+3.01.01+PM.png" alt="Screen_Shot_2015-01-02_at_3.01.01_PM.png" />
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p>4. Provide optional information. </p>
        <p>Set "ossec id" and "ossec key" if they were specified as part of the OSSEC manager installation.</p>
        <p>Set "ossec manager" if your OSSEC Manager is located on another subnet. Otherwise this may be left blank and the agent will automatically discover the manager and begin the registration process.</p>
      </td>
      <td>
        <p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/bAXhN2Kq9XaRMCNgwm2Wf84iz/?name=Screen+Shot+2015-01-02+at+3.02.55+PM.png" alt="Screen_Shot_2015-01-02_at_3.02.55_PM.png" />
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;5. Select a single server to install package on</p>
      </td>
      <td>
        <p>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/U3UqLKww4AMDPVruZ48R5AUry/?name=Screen+Shot+2015-01-02+at+2.52.07+PM.png" alt="Screen_Shot_2015-01-02_at_2.52.07_PM.png" />
        </p>
      </td>
    </tr>
    <tr>
      <td>
        <p>&nbsp;6. Select to execute package and watch deployment process. If all works as expected your administrator email address will get an automated startup notification from OSSEC (email is only sent if running on CentOS/RHEL).</p>
      </td>
      <td>&nbsp;<img src="https://t3n.zendesk.com/attachments/token/qQV4Qk213s8YFgGi8Kor42mjH/?name=Screen+Shot+2015-01-02+at+2.52.57+PM.png" alt="Screen_Shot_2015-01-02_at_2.52.57_PM.png" />
      </td>
    </tr>
  </tbody>
</table>

### Pricing

The costs listed above in Steps 1 and 2 are for the infrastructure only.

OSSEC is Open Source community owned software with no associated cost to acquire.

### Frequently Asked Questions

**Where do I get my OSSEC&nbsp;License?**

OSSEC is Open Source community owned software with no associated cost to acquire.

**Who should I contact for support?**

OSSEC is packaged and provided by CenturyLink as a courtesy to ease startup time. All support for this Open Source software is provided by the community. Please start at http://www.ossec.net/

For issues related to cloud infrastructure, please open a ticket using the [CenturyLink Cloud Support Process](../../Support/how-do-i-report-a-support-issue.md).
