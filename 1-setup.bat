@ECHO OFF

Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %~dp0

ECHO Installing Required Pdrograms
call SetupFiles\1-install_programs

ECHO Setting up required packages
call 2-install_python_packages

ECHO Changing Screenshot coordinates
call 3-change_screenshot_pos.bat
