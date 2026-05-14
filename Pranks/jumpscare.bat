@echo off
title JUMPSCARE
powershell -c "(New-Object -ComObject WScript.Shell).SendKeys([char]175)" >nul 2>&1
powershell -c "(New-Object -ComObject WScript.Shell).SendKeys([char]175)" >nul 2>&1
powershell -c "(New-Object -ComObject WScript.Shell).SendKeys([char]175)" >nul 2>&1
powershell -c "(New-Object -ComObject WScript.Shell).SendKeys([char]175)" >nul 2>&1
powershell -c "(New-Object -ComObject WScript.Shell).SendKeys([char]175)" >nul 2>&1

:: Tenta abrir sem autoplay primeiro (mais compatível)
start chrome.exe --new-window "https://www.youtube.com/shorts/lV1w-BI7AJQ"

timeout /t 2 /nobreak >nul

:: Força um refresh na página após 2 segundos
powershell -c "$wshell = New-Object -ComObject wscript.shell; $wshell.AppActivate('YouTube'); Start-Sleep -Seconds 1; $wshell.SendKeys('{F5}')"

exit
