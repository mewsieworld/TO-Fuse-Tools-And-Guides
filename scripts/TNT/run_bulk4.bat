@echo off
setlocal enabledelayedexpansion

:: Path to TNT.jar (change this if needed)
set "SCRIPT_DIR=%~dp0"
set "TNT_PATH=%SCRIPT_DIR%TNT.jar"


echo.
echo ============================================
echo     TNT Bulk Extractor - Multi Folder
echo ============================================
echo.

:START
echo Enter full path to folder containing .nri files or main Trickster Data folder (or Q to quit):
set /p TARGETFOLDER=

if /I "%TARGETFOLDER%"=="Q" goto END

:: Strip quotes if they exist
set "TARGETFOLDER=%TARGETFOLDER:"=%"

if not exist "%TARGETFOLDER%" (
    echo [!] Folder not found: %TARGETFOLDER%
    goto START
)

echo Recurse into subfolders (recommended for extracting all from main Trickster Data folder)? (Y/N):
set /p RECURSE=
echo.

:: Extract NRI files
if /I "%RECURSE%"=="Y" (
    for /R "%TARGETFOLDER%" %%F in (*.nri) do call :process "%%F"
) else (
    for %%F in ("%TARGETFOLDER%\*.nri") do call :process "%%F"
)

:: Clean up empty folders after extraction
echo.
echo Cleaning up empty folders in: %TARGETFOLDER%
echo.

pushd "%TARGETFOLDER%"
for /L %%i in (1,1,5) do (
    for /f "delims=" %%d in ('dir /ad/b/s ^| sort /R') do (
        rd "%%d" 2>nul
    )
)
popd

echo.
echo Done with folder: %TARGETFOLDER%
goto START

:process
set "FILE=%~1"
set "FILENAME=%~nx1"
set "FILEDIR=%~dp1"

:: Remove trailing backslash
if "%FILEDIR:~-1%"=="\" set "FILEDIR=%FILEDIR:~0,-1%"

:: Quote-escape for PowerShell
set "ESC_TNT_PATH=%TNT_PATH:'=''%"
set "ESC_FILENAME=%FILENAME:'=''%"

echo -------------------------------------
echo Extracting (20s max): %FILENAME%

powershell -NoProfile -Command ^
  "$job = Start-Job { cd -LiteralPath '%FILEDIR%'; & java -jar '%ESC_TNT_PATH%' e '%ESC_FILENAME%' }; " ^
  "if (Wait-Job -Job $job -Timeout 20) { Receive-Job $job | Out-Null; Write-Host '[+] Extracted: %ESC_FILENAME%' } " ^
  "else { Stop-Job $job; Remove-Job $job; Write-Host '[!] Timeout reached. Skipped: %ESC_FILENAME%' }"

exit /b




:END
echo.
echo All done!
pause
