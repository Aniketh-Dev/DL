@echo off
title JARVIS Voice Assistant
color 0b

echo ============================================================
echo                 JARVIS VOICE ASSISTANT
echo ============================================================
echo.

:: Navigate to the folder where this batch file is located
cd /d "%~dp0"

:: 1. Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    color 0c
    echo [ERROR] Python was not found in your system PATH.
    echo Please install Python 3.9+ from https://www.python.org/
    echo and ensure "Add Python to PATH" is checked during setup.
    echo.
    pause
    exit /b 1
)

:: 2. Activate virtual environment if present
if exist "venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment: venv
    call "venv\Scripts\activate.bat"
)
if exist ".venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment: .venv
    call ".venv\Scripts\activate.bat"
)

:: 3. Run JARVIS
echo [*] Launching JARVIS...
echo.
python main.py
if errorlevel 1 (
    echo.
    echo [!] If JARVIS failed to start due to missing packages,
    echo     try installing dependencies with:
    echo     pip install -r requirements.txt
    echo.
)

echo.
echo ============================================================
echo [JARVIS Exited]
echo ============================================================
pause
