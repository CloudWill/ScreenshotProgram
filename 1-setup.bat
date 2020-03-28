ECHO OFF

Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %CD%

ECHO Installing Autohotkey
SetupFiles\AutoHotkey_1.1.32.00_setup

ECHO Installing Python
SetupFiles\python-3.8.2.exe InstallAllUsers=0 Include_launcher=0 Include_test=0
    SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."

ECHO Upgrading Python Pip
python -m pip install --upgrade pip


ECHO Installing Pythong Package 'Pyautogui'
pip install pyautogui

ECHO Running script setup
python position.py

Pause