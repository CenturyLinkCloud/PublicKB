{{{ 
"title": "Timekeeping Best Practices For Windows Servers", 
"date": "9-10-2017",
"author": "John Bach",
"attachments": [],
"contentIsHTML": false 
}}}

### In this article:
1. We will describe the way to maintain proper time on Windows servers within the Lumen cloud environment.
2. We will cover Windows servers not joined to an active directory domain and standalone servers which aren't.
3. The summary of action to be taken in all cases is as follows:
   * Disable VMWare Tools hardware time sync feature.
   * Configure your cloud server to use a network time source.
   * Disabling hardware time sync

### Disabling VMWare Tools hardware time sync

All virtual machines start up using the BIOS time on the host, even before the operating system has started. VMWare tools has a feature to keep this time in sync with the host even after the operating system is started.  

If the host happens to be slightly off by 5 or more minutes, domain joined servers may fail to authenticate with protocols like kerberos, causing the trust relationship with the server to fail with its domain, or other issues with certificates.  

Rather than keep your virtual machine synced to the host, VMWare recommends keeping it in sync with a time server, preferably their own time service "time.windows.com" which utilizes a secure version of NTP on Windows 2016.  

In order to disable VMWare Tools time sync with the host, follow these instructions:  

* Deselect Time synchronization between the virtual machine and the host operating system in the VMware Tools toolbox GUI of the guest operating system.

*or*

* Run the VMwareService.exe -cmd "vmx.set_option synctime 1 0" command in the guest operating system. VMwareService.exe is typically installed in C:\Program Files\VMware\VMware Tools.

*or*

* Run the vmtoolsd.exe timesync {enable|disable} command from the guest operating system and located at c:\Program Files\VMware\VMware Tools\vmtoolsd.

**NOTE:** These options do not disable one-time synchronizations done by VMware Tools for events such as tools startup, taking a snapshot, resuming from a snapshot, resuming from suspend, or vMotion. These events synchronize time in the guest operating system with time in the host operating system even if VMware Tools periodic time sync is disabled,

So it is important to set your system up to a reliable network time source as well as report any time drift issues that could come from the scenarios above. Please report any time drift issues to us at help@ctl.io if you have enabled network time and disabled VMWare Tools time sync per our instructions and still are having issues.

### Standalone Windows Servers:

Per Microsoft, standalone machines are configured to use *time.windows.com* by default. That is the best option for a Windows 2016 server because it uses "secure NTP" and Microsoft recommends it.

If you should decide you'd like to use another source, Windows provides options to change that. Most machines won't ever need to change this value, but if you do decide to point your server to your own time source or another public one on the internet, then you'll need to follow these instructions which apply to Windows Server 2008 R2 (or similar).

#### Registry Entries to Change
There are a few registry entries that are recommended by VMWare for time sync:

**NOTE:** This entry below sets the time polling interval to 15 minutes

**Key:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient\SpecialPollInterval  
**Type:** REG_DWORD  
**Value:** 900  

**NOTE:** This entry below sets first, second and third NTP servers. (Modify the command to use the ntp servers available in your environment.)  

**Key:** HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\W32Time\Parameters\NtpServer  
**Type:** REG_SZ  
**Value(s):**  
  pool.ntp.org,0x1  
  pool.ntp.org,0x1  
  pool.ntp.org,0x1  

#### Additional configuration from CLI  
After creating the registry key entries, go to a command prompt and run the w32tm command as follows:

w32tm /config "/manualpeerlist:
pool.ntp.org,0x1
pool.ntp.org,0x1
pool.ntp.org,0x1"

### Domain Joined Servers
Member servers should have the VMWare Tools sync disabled as detailed above in the first section. Domain joined servers use time given by the domain controller with the PDC Emulator FSMO role.  

To determine which server has the role, run this on any domain joined member server:

**NOTE:** *XXXXXX.company.local* is an example server name.  

NetDOM /query FSMO  

(Example output)  
Schema master XXXXXX.company.local  
Domain naming master XXXXX1.company.local  
PDC XXXXX2.company.local  
RID pool manager XXXXX3.company.local  
Infrastructure master XXXXX4.company.local  
The command completed successfully.  

So in this case, you would want to set the NTP settings on XXXXX2.company.local using the registry entries and w32tm command above.
