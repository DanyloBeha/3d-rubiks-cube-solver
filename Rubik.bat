@REM This file glues everything together (is there really a lot of gluing to be done? :) ) and launches an application from the desktop
@REM Maybe I shoud create an .exe file?

@echo off
setlocal enabledelayedexpansion


cd /d "%~dp0" || (
    echo Error code 141: project directory unavailable
    pause
    exit /b 141
)

py main.py

pause