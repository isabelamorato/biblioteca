# Limpa processos zumbi do Chrome dedicado de debug.
# Seguro: só mata processos cujo --user-data-dir aponta pra $env:USERPROFILE\.chrome-cdp-profile

$Profile = Join-Path $env:USERPROFILE ".chrome-cdp-profile"

$zombies = Get-CimInstance Win32_Process -Filter "Name = 'chrome.exe'" |
    Where-Object { $_.CommandLine -and $_.CommandLine -match [regex]::Escape($Profile) }

if ($zombies) {
    Write-Host "Matando $($zombies.Count) processo(s) do Chrome dedicado..."
    foreach ($p in $zombies) {
        Stop-Process -Id $p.ProcessId -Force -ErrorAction SilentlyContinue
    }
    Start-Sleep -Seconds 2
}

$portFile = Join-Path $Profile "DevToolsActivePort"
if (Test-Path $portFile) {
    Remove-Item $portFile -Force
    Write-Host "Port file removido."
}

Write-Host "Pronto. Rode `chrome-debug <url>` pra abrir limpo."
