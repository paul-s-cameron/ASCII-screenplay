@echo off

REM Set up virtual environment
python.exe -m venv venv

REM Update pip and setuptools
.\venv\Scripts\python.exe -m pip install --upgrade pip setuptools

REM Install required packages
.\venv\Scripts\python.exe -m pip install -r .\requirements.txt

REM Finished
echo.
echo Finished...
pause