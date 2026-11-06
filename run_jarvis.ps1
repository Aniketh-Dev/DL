# JARVIS Voice Assistant Launcher for PowerShell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "JARVIS - Voice Assistant"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "              🎙️  JARVIS VOICE ASSISTANT                    " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check Python availability
try {
    $pyVersion = & python --version 2>&1
    Write-Host "[*] Found Python: $pyVersion" -ForegroundColor Green
} catch {
    Write-Host "[ERROR] Python is not installed or not found in PATH." -ForegroundColor Red
    Pause
    exit 1
}

# Activate virtual environment if available
if (Test-Path "venv\Scripts\Activate.ps1") {
    Write-Host "[*] Activating virtual environment (venv)..." -ForegroundColor Yellow
    & "venv\Scripts\Activate.ps1"
} elseif (Test-Path ".venv\Scripts\Activate.ps1") {
    Write-Host "[*] Activating virtual environment (.venv)..." -ForegroundColor Yellow
    & ".venv\Scripts\Activate.ps1"
}

# Launch JARVIS
Write-Host "[*] Launching JARVIS..." -ForegroundColor Cyan
Write-Host ""
python main.py

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "[JARVIS Exited]" -ForegroundColor Gray
Write-Host "============================================================" -ForegroundColor Cyan
Pause
