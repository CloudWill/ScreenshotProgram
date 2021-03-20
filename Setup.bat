@ECHO OFF

Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %~dp0

ECHO Installing Required Programs

ECHO Installing Autohotkey
SetupFiles\AutoHotkey_1.1.32.00_setup

ECHO Installing Python
SetupFiles\python-3.8.2.exe InstallAllUsers=0 Include_launcher=0 Include_test=0 SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."

cd %~dp0

ECHO installing required dependencies
python -m pip install --upgrade pip

pip install pyautogui

cd %~dp0

ECHO Running script setup
python SetupFiles\ScreenshotSetup.py

ECHO Creating AHK File
python SetupFiles\SetupAhkFile.py


ECHO Starting AHK

:: the path to the AutoHotkey.exe to be used:
@set AHK_PATH=%PROGRAMFILES%\AutoHotkey\AutoHotkey.exe

:: the (relative or absolute) path to the script to be launched:
@set SCRIPT_PATH=%~dp0\SetupFiles\AutoHotKeysSettings.ahk

:: run AHK
START "" "%AHK_PATH%" "%SCRIPT_PATH%"

exit