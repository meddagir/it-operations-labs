# Run on a personal Windows lab PC. This collects only; it does not fix anything.
# Hostname is deliberately replaced with a lab alias.
param([string]$OutputPath = ".\local-readiness.json")
$ErrorActionPreference = "Stop"
$disk = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='$($env:SystemDrive)'"
$computer = Get-CimInstance Win32_ComputerSystem
$spooler = Get-Service -Name Spooler
[ordered]@{
    asset = "LAB-WOW-01"
    free_disk_gb = [math]::Round($disk.FreeSpace / 1GB, 2)
    spooler = $spooler.Status.ToString()
    domain_joined = [bool]$computer.PartOfDomain
} | ConvertTo-Json | Set-Content -Encoding UTF8 -Path $OutputPath
Write-Output "Collected read-only lab data: $OutputPath"
