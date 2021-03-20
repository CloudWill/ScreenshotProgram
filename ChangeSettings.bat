@ECHO OFF

cd %~dp0

ECHO Running new settings
python SetupFiles\ChangeSettings.py

cd %~dp0

ECHO Creating AHK File
python SetupFiles\SetupAhkFile.py

ECHO Running AHK

:: the path to the AutoHotkey.exe to be used:
@set AHK_PATH=%PROGRAMFILES%\AutoHotkey\AutoHotkey.exe

:: the (relative or absolute) path to the script to be launched:
@set SCRIPT_PATH=D:\OneDrive\Sorted\Programming\Python\PrintScreen\SetupFiles\AutoHotKeysSettings.ahk

START "" "%AHK_PATH%" "%SCRIPT_PATH%"

exit