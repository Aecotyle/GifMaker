@echo off
REM Production-ready build script for the tkinter GIF Maker app

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed or not in PATH. Please install pip and try again.
    pause
    exit /b 1
)

REM Check if PyInstaller is installed, install if missing
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing PyInstaller...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo Failed to install PyInstaller. Please install it manually and try again.
        pause
        exit /b 1
    )
)

REM Clean previous build folders
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist gif.spec del /f /q gif.spec

REM Build the executable using python -m PyInstaller
python -m PyInstaller --onefile --windowed --icon=interaction.ico gif.py

if errorlevel 1 (
    echo Build failed. Please check the errors above.
    pause
    exit /b 1
)

echo.
echo Build succeeded. The executable is located in the "dist" folder.
pause
