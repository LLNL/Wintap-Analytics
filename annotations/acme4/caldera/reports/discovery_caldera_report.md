
Discovery
=========

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
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Identify all local users](#--description-identify-all-local-users)
		* [  Description: Get process info for processes running as a user](#--description-get-process-info-for-processes-running-as-a-user)
		* [  Description: Network Share Discovery](#--description-network-share-discovery)
		* [  Description: Identify the remote domain controllers](#--description-identify-the-remote-domain-controllers)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: Summary of permission and security groups](#--description-summary-of-permission-and-security-groups)
		* [  Description: Identify Firewalls](#--description-identify-firewalls)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Identify all local users](#--description-identify-all-local-users)
		* [  Description: Get process info for processes running as a user](#--description-get-process-info-for-processes-running-as-a-user)
		* [  Description: Network Share Discovery](#--description-network-share-discovery)
		* [  Description: Identify the remote domain controllers](#--description-identify-the-remote-domain-controllers)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: Summary of permission and security groups](#--description-summary-of-permission-and-security-groups)
		* [  Description: Identify Firewalls](#--description-identify-firewalls)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Identify all local users](#--description-identify-all-local-users)
		* [  Description: Get process info for processes running as a user](#--description-get-process-info-for-processes-running-as-a-user)
		* [  Description: Network Share Discovery](#--description-network-share-discovery)
		* [  Description: Identify the remote domain controllers](#--description-identify-the-remote-domain-controllers)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: Summary of permission and security groups](#--description-summary-of-permission-and-security-groups)
		* [  Description: Identify Firewalls](#--description-identify-firewalls)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Identify all local users](#--description-identify-all-local-users)
		* [  Description: Get process info for processes running as a user](#--description-get-process-info-for-processes-running-as-a-user)
		* [  Description: Network Share Discovery](#--description-network-share-discovery)
		* [  Description: Identify the remote domain controllers](#--description-identify-the-remote-domain-controllers)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: Summary of permission and security groups](#--description-summary-of-permission-and-security-groups)
		* [  Description: Identify Firewalls](#--description-identify-firewalls)

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

###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 5892

  Start: 2024-09-13T17:16:48Z

  Command: 
```powershell
$env:username
```


###   Description: Identify all local users


  Attack: {'tactic': 'discovery', 'technique_name': 'Account Discovery: Local Account', 'technique_id': 'T1087.001'}

  Status: Success

  PID: 3848

  Start: 2024-09-13T17:17:57Z

  Command: 
```powershell
Get-WmiObject -Class Win32_UserAccount
```


###   Description: Get process info for processes running as a user


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 8112

  Start: 2024-09-13T17:19:02Z

  Command: 
```powershell
$owners = @{};gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user};$ps = get-process | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}};foreach($p in $ps) {    if($p.Owner -eq "grantj") {        $p;    }}
```


###   Description: Network Share Discovery


  Attack: {'tactic': 'discovery', 'technique_name': 'Network Share Discovery', 'technique_id': 'T1135'}

  Status: Success

  PID: 3212

  Start: 2024-09-13T17:19:58Z

  Command: 
```powershell
Get-SmbShare | ConvertTo-Json
```


###   Description: Identify the remote domain controllers


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 5804

  Start: 2024-09-13T17:20:35Z

  Command: 
```powershell
nltest /dsgetdc:$env:USERDOMAIN
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 2204

  Start: 2024-09-13T17:21:38Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: Summary of permission and security groups


  Attack: {'tactic': 'discovery', 'technique_name': 'Permission Groups Discovery: Local Groups', 'technique_id': 'T1069.001'}

  Status: Success

  PID: 3224

  Start: 2024-09-13T17:22:21Z

  Command: 
```powershell
gpresult /R
```


###   Description: Identify Firewalls


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 8696

  Start: 2024-09-13T17:23:10Z

  Command: 
```powershell
$NameSpace = Get-WmiObject -Namespace "root" -Class "__Namespace" | Select Name | Out-String -Stream | Select-String "SecurityCenter";$SecurityCenter = $NameSpace | Select-Object -First 1;Get-WmiObject -Namespace "root\$SecurityCenter" -Class AntiVirusProduct | Select DisplayName, InstanceGuid, PathToSignedProductExe, PathToSignedReportingExe, ProductState, Timestamp | Format-List;
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 6696

  Start: 2024-09-13T17:17:00Z

  Command: 
```powershell
$env:username
```


###   Description: Identify all local users


  Attack: {'tactic': 'discovery', 'technique_name': 'Account Discovery: Local Account', 'technique_id': 'T1087.001'}

  Status: Success

  PID: 1284

  Start: 2024-09-13T17:17:36Z

  Command: 
```powershell
Get-WmiObject -Class Win32_UserAccount
```


###   Description: Get process info for processes running as a user


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 7080

  Start: 2024-09-13T17:18:15Z

  Command: 
```powershell
$owners = @{};gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user};$ps = get-process | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}};foreach($p in $ps) {    if($p.Owner -eq "grantj") {        $p;    }}
```


###   Description: Network Share Discovery


  Attack: {'tactic': 'discovery', 'technique_name': 'Network Share Discovery', 'technique_id': 'T1135'}

  Status: Success

  PID: 5496

  Start: 2024-09-13T17:19:07Z

  Command: 
```powershell
Get-SmbShare | ConvertTo-Json
```


###   Description: Identify the remote domain controllers


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 2176

  Start: 2024-09-13T17:20:27Z

  Command: 
```powershell
nltest /dsgetdc:$env:USERDOMAIN
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 7020

  Start: 2024-09-13T17:21:14Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: Summary of permission and security groups


  Attack: {'tactic': 'discovery', 'technique_name': 'Permission Groups Discovery: Local Groups', 'technique_id': 'T1069.001'}

  Status: Success

  PID: 5988

  Start: 2024-09-13T17:22:00Z

  Command: 
```powershell
gpresult /R
```


###   Description: Identify Firewalls


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 6576

  Start: 2024-09-13T17:22:57Z

  Command: 
```powershell
$NameSpace = Get-WmiObject -Namespace "root" -Class "__Namespace" | Select Name | Out-String -Stream | Select-String "SecurityCenter";$SecurityCenter = $NameSpace | Select-Object -First 1;Get-WmiObject -Namespace "root\$SecurityCenter" -Class AntiVirusProduct | Select DisplayName, InstanceGuid, PathToSignedProductExe, PathToSignedReportingExe, ProductState, Timestamp | Format-List;
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 1564

  Start: 2024-09-13T17:16:46Z

  Command: 
```powershell
$env:username
```


###   Description: Identify all local users


  Attack: {'tactic': 'discovery', 'technique_name': 'Account Discovery: Local Account', 'technique_id': 'T1087.001'}

  Status: Success

  PID: 816

  Start: 2024-09-13T17:17:41Z

  Command: 
```powershell
Get-WmiObject -Class Win32_UserAccount
```


###   Description: Get process info for processes running as a user


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 9420

  Start: 2024-09-13T17:18:28Z

  Command: 
```powershell
$owners = @{};gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user};$ps = get-process | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}};foreach($p in $ps) {    if($p.Owner -eq "grantj") {        $p;    }}
```


###   Description: Network Share Discovery


  Attack: {'tactic': 'discovery', 'technique_name': 'Network Share Discovery', 'technique_id': 'T1135'}

  Status: Success

  PID: 7012

  Start: 2024-09-13T17:19:20Z

  Command: 
```powershell
Get-SmbShare | ConvertTo-Json
```


###   Description: Identify the remote domain controllers


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 1916

  Start: 2024-09-13T17:20:18Z

  Command: 
```powershell
nltest /dsgetdc:$env:USERDOMAIN
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 5116

  Start: 2024-09-13T17:21:17Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: Summary of permission and security groups


  Attack: {'tactic': 'discovery', 'technique_name': 'Permission Groups Discovery: Local Groups', 'technique_id': 'T1069.001'}

  Status: Success

  PID: 2924

  Start: 2024-09-13T17:21:59Z

  Command: 
```powershell
gpresult /R
```


###   Description: Identify Firewalls


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 1432

  Start: 2024-09-13T17:23:00Z

  Command: 
```powershell
$NameSpace = Get-WmiObject -Namespace "root" -Class "__Namespace" | Select Name | Out-String -Stream | Select-String "SecurityCenter";$SecurityCenter = $NameSpace | Select-Object -First 1;Get-WmiObject -Namespace "root\$SecurityCenter" -Class AntiVirusProduct | Select DisplayName, InstanceGuid, PathToSignedProductExe, PathToSignedReportingExe, ProductState, Timestamp | Format-List;
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 9552

  Start: 2024-09-13T17:17:03Z

  Command: 
```powershell
$env:username
```


###   Description: Identify all local users


  Attack: {'tactic': 'discovery', 'technique_name': 'Account Discovery: Local Account', 'technique_id': 'T1087.001'}

  Status: Success

  PID: 5588

  Start: 2024-09-13T17:18:00Z

  Command: 
```powershell
Get-WmiObject -Class Win32_UserAccount
```


###   Description: Get process info for processes running as a user


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 5836

  Start: 2024-09-13T17:18:51Z

  Command: 
```powershell
$owners = @{};gwmi win32_process |% {$owners[$_.handle] = $_.getowner().user};$ps = get-process | select processname,Id,@{l="Owner";e={$owners[$_.id.tostring()]}};foreach($p in $ps) {    if($p.Owner -eq "grantj") {        $p;    }}
```


###   Description: Network Share Discovery


  Attack: {'tactic': 'discovery', 'technique_name': 'Network Share Discovery', 'technique_id': 'T1135'}

  Status: Success

  PID: 8224

  Start: 2024-09-13T17:19:21Z

  Command: 
```powershell
Get-SmbShare | ConvertTo-Json
```


###   Description: Identify the remote domain controllers


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 8244

  Start: 2024-09-13T17:20:16Z

  Command: 
```powershell
nltest /dsgetdc:$env:USERDOMAIN
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 9404

  Start: 2024-09-13T17:21:13Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: Summary of permission and security groups


  Attack: {'tactic': 'discovery', 'technique_name': 'Permission Groups Discovery: Local Groups', 'technique_id': 'T1069.001'}

  Status: Success

  PID: 584

  Start: 2024-09-13T17:22:06Z

  Command: 
```powershell
gpresult /R
```


###   Description: Identify Firewalls


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 8204

  Start: 2024-09-13T17:22:52Z

  Command: 
```powershell
$NameSpace = Get-WmiObject -Namespace "root" -Class "__Namespace" | Select Name | Out-String -Stream | Select-String "SecurityCenter";$SecurityCenter = $NameSpace | Select-Object -First 1;Get-WmiObject -Namespace "root\$SecurityCenter" -Class AntiVirusProduct | Select DisplayName, InstanceGuid, PathToSignedProductExe, PathToSignedReportingExe, ProductState, Timestamp | Format-List;
```

