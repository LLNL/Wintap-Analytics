
Advanced Thief
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
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)

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

## Host: ACME-HH-EUO (paw: acpuoe)

## Host: ACME-WS-PLU (paw: hkrmxr)

## Host: ACME-HH-ESO (paw: nowkww)
