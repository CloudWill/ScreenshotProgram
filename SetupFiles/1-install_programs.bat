Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %~dp0

ECHO Installing Autohotkey
AutoHotkey_1.1.32.00_setup

ECHO Installing Python
python-3.8.2.exe InstallAllUsers=0 Include_launcher=0 Include_test=0 SimpleInstall=1 SimpleInstallDescription="Just for me, no test suite."

Pause