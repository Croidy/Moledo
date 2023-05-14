@echo off
rem if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
title promptMoledo
start hide_moledo.bat
moledo-venv\Scripts\python.exe App.py
exit