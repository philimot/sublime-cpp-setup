@echo off
chcp 65001 >nul
echo.
echo ====================================================
echo    Sublime Text C++ Setup - Auto Installer
echo    Repository: github.com/philimot/sublime-cpp-setup
echo ====================================================
echo.

:: Check if running as Administrator
NET SESSION >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠ WARNING: Not running as Administrator!
    echo Some operations may fail.
    echo.
    echo To run as Admin:
    echo 1. Right-click on install.bat
    echo 2. Select "Run as administrator"
    echo.
    set /p continue="Continue anyway? (Y/N): "
    if /i not "%continue%"=="Y" (
        echo Installation cancelled.
        pause
        exit /b 1
    )
    echo.
)

:: Variables
set "BACKUP_DATE=%date:~10,4%%date:~4,2%%date:~7,2%_%time:~0,2%%time:~3,2%"
set "BACKUP_NAME=User.backup.%BACKUP_DATE%"

:: Step 1: Detect Sublime Text path
echo [1/5] 🔍 Detecting Sublime Text installation...
set "ST_PATH="
set "ST_VERSION="

if exist "%APPDATA%\Sublime Text\Packages\" (
    set "ST_PATH=%APPDATA%\Sublime Text"
    set "ST_VERSION=4"
    echo ✅ Found Sublime Text 4
) else if exist "%APPDATA%\Sublime Text 3\Packages\" (
    set "ST_PATH=%APPDATA%\Sublime Text 3"
    set "ST_VERSION=3"
    echo ✅ Found Sublime Text 3
) else if exist "%LOCALAPPDATA%\Sublime Text\Packages\" (
    set "ST_PATH=%LOCALAPPDATA%\Sublime Text"
    set "ST_VERSION=4 (Local)"
    echo ✅ Found Sublime Text 4 (Local)
) else (
    echo ❌ ERROR: Sublime Text not found!
    echo.
    echo Please install Sublime Text first from:
    echo https://www.sublimetext.com/
    echo.
    pause
    exit /b 1
)

echo    Path: %ST_PATH%
echo.

:: Step 2: Backup existing configuration
echo [2/5] 📦 Backing up existing configuration...
cd "%ST_PATH%\Packages"

if exist "User" (
    echo Backing up 'User' folder to '%BACKUP_NAME%'...
    xcopy "User" "%BACKUP_NAME%" /E /I /H /Y >nul
    
    if %errorlevel% equ 0 (
        echo ✅ Backup created: %BACKUP_NAME%
        echo.
        echo ℹ To restore backup later:
        echo   1. Delete the new 'User' folder
        echo   2. Rename '%BACKUP_NAME%' to 'User'
        echo   3. Restart Sublime Text
    ) else (
        echo ⚠ Could not create backup, but continuing...
    )
    
    :: Remove old User folder
    rmdir /s /q "User" 2>nul
) else (
    echo ℹ No existing 'User' folder found
)

echo.

:: Step 3: Install C++ Setup from GitHub
echo [3/5] ⬇ Downloading C++ development setup...
echo Downloading from GitHub: philimot/sublime-cpp-setup
echo.

:: Check if git is available
where git >nul 2>nul
if %errorlevel% equ 0 (
    echo Using git to clone repository...
    git clone --depth 1 https://github.com/philimot/sublime-cpp-setup.git "User"
    
    if %errorlevel% equ 0 (
        echo ✅ Successfully cloned from GitHub
        goto :check_compiler
    ) else (
        echo ⚠ Git clone failed, trying alternative method...
    )
)

:: Alternative: Download ZIP
echo Downloading ZIP archive...
powershell -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; Invoke-WebRequest -Uri 'https://github.com/philimot/sublime-cpp-setup/archive/refs/heads/main.zip' -OutFile 'sublime-cpp-setup.zip'" 2>nul

if exist "sublime-cpp-setup.zip" (
    echo Extracting files...
    powershell -Command "Expand-Archive -Path 'sublime-cpp-setup.zip' -DestinationPath '.' -Force" 2>nul
    
    if exist "sublime-cpp-setup-main" (
        move "sublime-cpp-setup-main" "User" >nul 2>nul
        del "sublime-cpp-setup.zip" 2>nul
        echo ✅ Downloaded and extracted successfully
    ) else (
        echo ❌ Extraction failed
        goto :manual_setup
    )
) else (
    echo ❌ Download failed
    goto :manual_setup
)

:check_compiler
:: Step 4: Check for C++ compiler
echo.
echo [4/5] 🔧 Checking C++ compiler setup...
echo.

set "COMPILER_FOUND=0"
set "COMPILER_PATH="

:: Check for g++ in common locations
for %%c in (g++.exe g++) do (
    where %%c >nul 2>nul
    if !errorlevel! equ 0 (
        for /f "tokens=*" %%i in ('where %%c') do (
            set "COMPILER_PATH=%%i"
            set "COMPILER_FOUND=1"
        )
    )
)

if %COMPILER_FOUND% equ 1 (
    echo ✅ C++ compiler found:
    echo    %COMPILER_PATH%
    echo.
) else (
    echo ⚠ WARNING: C++ compiler NOT found!
    echo.
    echo To compile C++ programs, you need:
    echo 1. MSYS2 with UCRT64 (recommended)
    echo    - Download: https://www.msys2.org/
    echo    - Install to: C:\msys64
    echo    - Add to PATH: C:\msys64\ucrt64\bin
    echo.
    echo 2. OR MinGW-w64
    echo    - Download: https://www.mingw-w64.org/
    echo.
    echo 3. Restart your computer after adding to PATH
    echo.
)

:: Step 5: Create test files
echo [5/5] 🧪 Creating test files...
echo.

:: Create test.cpp on Desktop
(
echo // Test file for Sublime Text C++ Setup
echo // Created by auto-installer
echo // Test command: Ctrl+Alt+L then F5
echo.
echo #include ^<iostream^>
echo using namespace std;
echo.
echo int main^() {
echo     cout ^<^< "=== C++ SETUP TEST ===" ^<^< endl;
echo     cout ^<^< "✅ Installation successful!" ^<^< endl;
echo     cout ^<^< endl;
echo     int a, b;
echo     cout ^<^< "Enter two numbers: ";
echo     cin ^>^> a ^>^> b;
echo     cout ^<^< "Sum: " ^<^< a + b ^<^< endl;
echo     cout ^<^< "Product: " ^<^< a * b ^<^< endl;
echo     cout ^<^< "=== TEST COMPLETE ===" ^<^< endl;
echo     return 0;
echo }
) > "%USERPROFILE%\Desktop\test.cpp"

:: Create test.in with sample input
(
echo // Sample input for test.cpp
echo // This file should be in the same folder as test.cpp
echo.
echo 10 20
) > "%USERPROFILE%\Desktop\test.in"

echo ✅ Test files created on Desktop:
echo    - test.cpp
echo    - test.in
echo.

:: Final message
echo ====================================================
echo                 🎉 INSTALLATION COMPLETE!
echo ====================================================
echo.
echo What was installed:
echo ✓ C++ Auto Layout plugin
echo ✓ Build system with F5 shortcut
echo ✓ Keyboard shortcuts
echo ✓ Editor preferences
echo ✓ Context menu
echo.
echo Quick Start Guide:
echo 1. RESTART Sublime Text
echo 2. Open test.cpp from your Desktop
echo 3. Press Ctrl+Alt+L (creates 3-panel layout)
echo 4. Add input to test.in (right-top panel)
echo 5. Press F5 to compile ^& run
echo 6. View output in test.out (right-bottom panel)
echo.
echo Additional shortcuts:
echo • Ctrl+1/2/3 : Switch between panels
echo • Ctrl+Shift+L : Quick create .in/.out files
echo • Ctrl+F5 : Refresh output
echo • Ctrl+Shift+C : Clear output file
echo.
echo For more details, visit:
echo https://github.com/philimot/sublime-cpp-setup
echo.
echo Press any key to finish...
pause >nul

exit /b

:manual_setup
echo.
echo ⚠ Using manual setup method...
echo Creating basic configuration files...

cd "%ST_PATH%\Packages"
mkdir "User"
cd "User"

:: Create minimal auto_layout.py
(
echo import sublime
echo import sublime_plugin
echo.
echo class AutoCppLayoutCommand(sublime_plugin.TextCommand^):
echo     def run(self, edit^):
echo         self.view.window^(^).run_command^("set_layout", {
echo             "cols": [0.0, 0.7, 1.0],
echo             "rows": [0.0, 0.5, 1.0],
echo             "cells": [[0, 0, 1, 2], [1, 0, 2, 1], [1, 1, 2, 2]]
echo         }^)
echo         sublime.status_message^("✅ 3-panel layout created!")
) > auto_layout.py

:: Create minimal build system
(
echo {
echo     "shell_cmd": "g++ -std=c++17 \"^${file^}\" -o \"^${file_base_name^}.exe\" ^&^& if exist \"^${file_base_name^}.in\" (\"^${file_base_name^}.exe\" ^< \"^${file_base_name^}.in\" ^> \"^${file_base_name^}.out\" ^&^& echo ✅ Output saved to ^${file_base_name^}.out^) else (\"^${file_base_name^}.exe\"^)",
echo     "selector": "source.cpp",
echo     "shell": true
echo }
) > "C++ Basic.sublime-build"

:: Create minimal keymap
(
echo [
echo     {"keys": ["ctrl+alt+l"], "command": "auto_cpp_layout"},
echo     {"keys": ["f5"], "command": "build"}
echo ]
) > Default.sublime-keymap

echo ✅ Manual setup completed with basic features
goto :check_compiler
