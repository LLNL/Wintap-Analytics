
Noisy Neighbor
==============

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
		* [  Description: Stop terminal from logging history](#--description-stop-terminal-from-logging-history)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Locate all active IP and FQDNs on the network](#--description-locate-all-active-ip-and-fqdns-on-the-network)
		* [  Description: Identify system processes](#--description-identify-system-processes)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Turn a computers WIFI off](#--description-turn-a-computers-wifi-off)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: Stop terminal from logging history](#--description-stop-terminal-from-logging-history)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Locate all active IP and FQDNs on the network](#--description-locate-all-active-ip-and-fqdns-on-the-network)
		* [  Description: Identify system processes](#--description-identify-system-processes)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Turn a computers WIFI off](#--description-turn-a-computers-wifi-off)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: Stop terminal from logging history](#--description-stop-terminal-from-logging-history)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Locate all active IP and FQDNs on the network](#--description-locate-all-active-ip-and-fqdns-on-the-network)
		* [  Description: Identify system processes](#--description-identify-system-processes)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Turn a computers WIFI off](#--description-turn-a-computers-wifi-off)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: Stop terminal from logging history](#--description-stop-terminal-from-logging-history)
		* [  Description: Find user running agent](#--description-find-user-running-agent)
		* [  Description: Locate all active IP and FQDNs on the network](#--description-locate-all-active-ip-and-fqdns-on-the-network)
		* [  Description: Identify system processes](#--description-identify-system-processes)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Turn a computers WIFI off](#--description-turn-a-computers-wifi-off)

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

###   Description: Stop terminal from logging history


  Attack: {'tactic': 'defense-evasion', 'technique_name': 'Indicator Removal on Host: Clear Command History', 'technique_id': 'T1070.003'}

  Status: Success

  PID: 3772

  Start: 2024-09-13T17:48:09Z

  Command: 
```powershell
Clear-History;Clear
```


###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 7620

  Start: 2024-09-13T17:48:44Z

  Command: 
```powershell
$env:username
```


###   Description: Locate all active IP and FQDNs on the network


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 788

  Start: 2024-09-13T17:49:38Z

  Command: 
```powershell
arp -a
```


###   Description: Identify system processes


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 5252

  Start: 2024-09-13T17:50:28Z

  Command: 
```powershell
Get-Process
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 4060

  Start: 2024-09-13T17:51:05Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 4032

  Start: 2024-09-13T17:51:58Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Turn a computers WIFI off


  Attack: {'tactic': 'impact', 'technique_name': 'Endpoint Denial of Service', 'technique_id': 'T1499'}

  Status: Failed

  PID: 9172

  Start: 2024-09-13T17:52:52Z

  Command: 
```powershell
.\wifi.ps1 -Off
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: Stop terminal from logging history


  Attack: {'tactic': 'defense-evasion', 'technique_name': 'Indicator Removal on Host: Clear Command History', 'technique_id': 'T1070.003'}

  Status: Success

  PID: 1168

  Start: 2024-09-13T17:47:14Z

  Command: 
```powershell
Clear-History;Clear
```


###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 440

  Start: 2024-09-13T17:48:37Z

  Command: 
```powershell
$env:username
```


###   Description: Locate all active IP and FQDNs on the network


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 4032

  Start: 2024-09-13T17:49:26Z

  Command: 
```powershell
arp -a
```


###   Description: Identify system processes


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 1876

  Start: 2024-09-13T17:50:18Z

  Command: 
```powershell
Get-Process
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 2264

  Start: 2024-09-13T17:51:06Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 7008

  Start: 2024-09-13T17:51:59Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Turn a computers WIFI off


  Attack: {'tactic': 'impact', 'technique_name': 'Endpoint Denial of Service', 'technique_id': 'T1499'}

  Status: Success

  PID: 6856

  Start: 2024-09-13T17:52:39Z

  Command: 
```powershell
.\wifi.ps1 -Off
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: Stop terminal from logging history


  Attack: {'tactic': 'defense-evasion', 'technique_name': 'Indicator Removal on Host: Clear Command History', 'technique_id': 'T1070.003'}

  Status: Success

  PID: 7788

  Start: 2024-09-13T17:47:52Z

  Command: 
```powershell
Clear-History;Clear
```


###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 8628

  Start: 2024-09-13T17:48:30Z

  Command: 
```powershell
$env:username
```


###   Description: Locate all active IP and FQDNs on the network


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 8772

  Start: 2024-09-13T17:49:12Z

  Command: 
```powershell
arp -a
```


###   Description: Identify system processes


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 9596

  Start: 2024-09-13T17:50:02Z

  Command: 
```powershell
Get-Process
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 8512

  Start: 2024-09-13T17:50:56Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 9628

  Start: 2024-09-13T17:51:49Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Turn a computers WIFI off


  Attack: {'tactic': 'impact', 'technique_name': 'Endpoint Denial of Service', 'technique_id': 'T1499'}

  Status: Success

  PID: 6628

  Start: 2024-09-13T17:52:51Z

  Command: 
```powershell
.\wifi.ps1 -Off
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: Stop terminal from logging history


  Attack: {'tactic': 'defense-evasion', 'technique_name': 'Indicator Removal on Host: Clear Command History', 'technique_id': 'T1070.003'}

  Status: Success

  PID: 9856

  Start: 2024-09-13T17:48:00Z

  Command: 
```powershell
Clear-History;Clear
```


###   Description: Find user running agent


  Attack: {'tactic': 'discovery', 'technique_name': 'System Owner/User Discovery', 'technique_id': 'T1033'}

  Status: Success

  PID: 8484

  Start: 2024-09-13T17:49:03Z

  Command: 
```powershell
$env:username
```


###   Description: Locate all active IP and FQDNs on the network


  Attack: {'tactic': 'discovery', 'technique_name': 'Remote System Discovery', 'technique_id': 'T1018'}

  Status: Success

  PID: 9856

  Start: 2024-09-13T17:49:42Z

  Command: 
```powershell
arp -a
```


###   Description: Identify system processes


  Attack: {'tactic': 'discovery', 'technique_name': 'Process Discovery', 'technique_id': 'T1057'}

  Status: Success

  PID: 4036

  Start: 2024-09-13T17:50:22Z

  Command: 
```powershell
Get-Process
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 6856

  Start: 2024-09-13T17:51:14Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 3856

  Start: 2024-09-13T17:52:05Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Turn a computers WIFI off


  Attack: {'tactic': 'impact', 'technique_name': 'Endpoint Denial of Service', 'technique_id': 'T1499'}

  Status: Success

  PID: 3616

  Start: 2024-09-13T17:53:05Z

  Command: 
```powershell
.\wifi.ps1 -Off
```

