@echo off
REM Simple script to run the Water Remover App on Windows

echo =================================
echo Water Remover App - Startup
echo =================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
echo Checking dependencies...
pip install -q -r requirements.txt

echo.
echo =================================
echo Starting Water Remover App...
echo =================================
echo.
echo Access the app at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

REM Run the app
python app.py

pause
