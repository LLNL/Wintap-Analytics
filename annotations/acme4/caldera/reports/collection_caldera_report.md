
Collection
==========

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
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)

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

###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 560

  Start: 2024-09-13T18:02:31Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 4204

  Start: 2024-09-13T18:03:31Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 8356

  Start: 2024-09-13T18:04:12Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Failed

  PID: 5480

  Start: 2024-09-13T18:04:52Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 7104

  Start: 2024-09-13T18:03:06Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 2884

  Start: 2024-09-13T18:04:00Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 6904

  Start: 2024-09-13T18:04:38Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 4736

  Start: 2024-09-13T18:05:32Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 9492

  Start: 2024-09-13T18:02:52Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 6992

  Start: 2024-09-13T18:04:02Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 204

  Start: 2024-09-13T18:04:46Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 8836

  Start: 2024-09-13T18:05:45Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 1880

  Start: 2024-09-13T18:02:55Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 8840

  Start: 2024-09-13T18:03:37Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 1312

  Start: 2024-09-13T18:04:33Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 8544

  Start: 2024-09-13T18:05:24Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```

