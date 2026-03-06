@echo off
echo ========================================
echo  RAG Chatbot Backend - Quick Start
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)
echo.

echo [2/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo.

echo [3/4] Creating environment file...
if not exist ".env" (
    copy .env.example .env
    echo Created .env file from .env.example
    echo.
    echo IMPORTANT: Edit .env to add your QWEN_API_KEY for AI responses (optional)
    echo.
) else (
    echo .env file already exists
)
echo.

echo [4/4] Starting RAG Chatbot Backend...
echo.
echo ========================================
echo  Server will start on: http://localhost:8000
echo  API Docs: http://localhost:8000/docs
echo  Health Check: http://localhost:8000/api/v1/health
echo ========================================
echo.
echo Press Ctrl+C to stop the server
echo.

python main.py

pause
