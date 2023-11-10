@echo off
setlocal enabledelayedexpansion
for /f "delims=" %%i in ( 'netstat -ano^|findstr 0.0.0.0:80' ) do (
    set "line=%%i"
    echo "!line!"
    set "pid=!line:~-8!"
    echo "taskkill /pid !pid! /f"
    taskkill /pid !pid! /f
)