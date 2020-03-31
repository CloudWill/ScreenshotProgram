@ECHO OFF

Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %~dp0

ECHO Upgrading Python Pip
python -m pip install --upgrade pip

ECHO Installing Pythong Package 'Pyautogui'
pip install pyautogui
