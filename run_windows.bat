@echo off
cd /d "%~dp0"
py -3 src\permission_manager.py
if errorlevel 1 pause
