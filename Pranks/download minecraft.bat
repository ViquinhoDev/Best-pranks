@echo off
set "tlauncher_url=https://tlauncher.org/installer"
set "installer_path=%temp%\tlauncher-installer.exe"

:: download the installer with `-k` to bypass SSL certificate validation
echo Downloading TLauncher installer...
curl -L -k -o "%installer_path%" "%tlauncher_url%"

:: run the installer in silent mode
echo Installing TLauncher...
"%installer_path%" /S

:: remove traces >:)
del "%installer_path%"
echo Installation completed.
pause
