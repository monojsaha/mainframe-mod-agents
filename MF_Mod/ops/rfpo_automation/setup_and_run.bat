@echo off
:: RFPO Automation - Setup and Run (Windows)
:: ==========================================
:: Run this script once to install dependencies and launch the hourly scheduler.

echo ============================================================
echo  RFPO Automation Setup
echo ============================================================

:: Install Python dependencies
echo [1/3] Installing Python dependencies...
pip install -r "%~dp0requirements.txt"
if errorlevel 1 (
    echo ERROR: pip install failed. Ensure Python 3.9+ is in PATH.
    pause & exit /b 1
)

:: Install Playwright browsers
echo [2/3] Installing Playwright Chromium browser...
playwright install chromium
if errorlevel 1 (
    echo ERROR: Playwright install failed.
    pause & exit /b 1
)

:: Launch the scheduler
echo [3/3] Starting hourly scheduler...
echo       Press Ctrl+C in this window to stop.
echo.
python "%~dp0rfpo_automation.py"

pause
