@echo off
title JARVIS - Voice Assistant
chcp 65001 >nul
color 0B

echo ============================================================
echo               🎙️  JARVIS VOICE ASSISTANT
echo ============================================================
echo.

:: Navigate to the project directory where this script lives
cd /d "%~dp0"

:: 1. Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    color 0C
    echo [ERROR] Python is not installed or not found in your system PATH.
    echo Please install Python 3.9+ from https://www.python.org/
    echo and make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

:: 2. Check if a virtual environment exists and activate it
if exist "venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment (venv)...
    call venv\Scripts\activate.bat
) else if exist ".venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment (.venv)...
    call .venv\Scripts\activate.bat
)

:: 3. Check dependencies (optional auto-install helper)
echo [*] Checking core dependencies...
python -c "import torch, faster_whisper, sounddevice, pyttsx3" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Missing dependencies detected. Installing required packages...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        color 0C
        echo [ERROR] Failed to install dependencies. Please run 'pip install -r requirements.txt' manually.
        pause
        exit /b 1
    )
)

:: 4. Launch JARVIS
echo [*] Starting JARVIS...
echo.
python main.py

:: 5. Keep window open when closed
echo.
echo ============================================================
echo [JARVIS Exited]
echo ============================================================
pause
