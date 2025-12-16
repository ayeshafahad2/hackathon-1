@echo off
REM Batch script to start the fully functional RAG Chatbot
REM Usage: double-click this file or run from command line

echo.
echo ========================================
echo    PHYSICAL AI & HUMANOID ROBOTICS
echo         RAG CHATBOT STARTUP
echo ========================================
echo.

echo Checking prerequisites...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

node --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo Prerequisites OK!

echo.
echo Installing backend dependencies (if needed)...
cd backend
pip install -r requirements.txt >nul 2>&1
pip install python-dotenv asyncpg >nul 2>&1

echo.
echo Loading textbook content to vector database...
python load_textbook_content.py
if errorlevel 1 (
    echo WARNING: Content loading failed, but system may still work
)

echo.
echo Starting backend server...
start cmd /k "cd /d %~dp0\backend && python start_server.py"

echo.
echo Starting frontend development server...
cd ..\frontend
start cmd /k "cd /d %~dp0\frontend && npm install && npm start"

echo.
echo ========================================
echo Your RAG Chatbot is now starting!
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000 
echo.
echo The fully functional RAG system is ready!
echo ========================================
echo.

pause