@ECHO OFF
Echo Launch dir: "%~dp0"
Echo Current dir: "%CD%"

cd %~dp0

ECHO Running script setup
python position.py

Pause