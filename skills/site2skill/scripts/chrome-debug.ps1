# Chrome dedicado pra CDP (skills /site2skill, etc).
# Perfil isolado em $env:USERPROFILE\.chrome-cdp-profile
#
# Instalação (1x): adicionar a function abaixo no $PROFILE do PowerShell:
#   notepad $PROFILE
# Cole e salve. Reabra o PowerShell.

function chrome-debug {
    param(
        [string]$Url = "about:blank"
    )

    $chromeCandidates = @(
        "${env:ProgramFiles}\Google\Chrome\Application\chrome.exe",
        "${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe",
        "${env:LocalAppData}\Google\Chrome\Application\chrome.exe"
    )
    $chrome = $chromeCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1

    if (-not $chrome) {
        Write-Error "Google Chrome não encontrado."
        return
    }

    Start-Process $chrome -ArgumentList @(
        "--user-data-dir=$env:USERPROFILE\.chrome-cdp-profile",
        "--remote-debugging-port=0",
        "--no-first-run",
        "--no-default-browser-check",
        $Url
    )
}
