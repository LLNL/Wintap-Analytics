# Wintap Workshop Resources

This is a collection of scripts / commands that are used in the workshop. They are listed here in order, as refernce for easier copy/paste.

### Advanced Esper: Patterns

#### InternetProcess: a process that connects to an internet address

```sql
INSERT INTO InternetProcess​
SELECT ip.PidHash, ip.ProcessName, Connection.*​
FROM PATTERN[EVERY ip=WintapMessage(MessageType="Process" AND ActivityType='start')->​
    Connection=WintapMessage(MessageType="TcpConnection" ​
    AND PidHash=ip.PidHash​
    AND TcpConnection.DestinationAddress <> '127.0.0.1' ​
    AND TcpConnection.DestinationAddress NOT LIKE '192.168.%’)]​
```

#### InternetProcessPersist: an InternetProcess that writes to any Run key in the registry  ​

```sql
INSERT INTO InternetProcessPersist​
SELECT ip.ProcessName, reg.RegActivity.Path, ip.TcpConnection.DestinationAddress​
FROM PATTERN[EVERY ip=InternetProcess -> ​
    reg=WintapMessage(MessageType="Registry" ​
    AND PidHash=ip.PidHash​
    AND RegActivity.Path LIKE '%\run')]​
```

#### Internet Persistency: Example Script​

```ps
# Define the URL for the Sysinternals tool you want to download​
$toolUrl = "https://live.sysinternals.com/Procmon.exe"​

# Define the destination path where the tool will be saved​
# Ensure this directory exists or modify the path as needed​
$destinationPath = "C:\Temp\Procmon.exe"​

# Try to download the file using Invoke-WebRequest​
try {​
    Invoke-WebRequest -Uri $toolUrl -OutFile $destinationPath​
    Write-Host "File downloaded successfully to $destinationPath"​
} catch {​
    Write-Host "Failed to download the file. Error: $_"​
    exit​
}​

# If file download is successful, proceed to write a dummy value in the registry​
$registryPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run"​
$dummyName = "SysinternalsProcmon"​
$dummyValue = $destinationPath​

# Use Set-ItemProperty to add the dummy registry entry​
Set-ItemProperty -Path $registryPath -Name $dummyName -Value $dummyValue​
Write-Host "Registry entry for Sysinternals Procmon set successfully."​
```

### Python Environment Setup

1. Clone github Repo: `git clone https://github.com/LLNL/Wintap-Analytics.git`
1. Navigate to the Wintap-Analtyics directory (e.g. `cd Wintap-Analytics`)
1. Follow steps until option 1 for a conda setup and option 2 to use your system python 

#### Option 1: Using Conda

1. Create a new conda environment for wintap analytics: `conda create -n wintap-analytics python=3.10`
1. Activate the conda environment: `conda activate wintap-analytics​`
1. Install the requirements `pip install -r requirements.txt`

#### Option 2: Using System Python

Mac/Linux:
1. Use make to build the venv: `make venv`
1. Activate the pipenv shell: `pipenv shell`

Windows:
1. some windows instructions....
