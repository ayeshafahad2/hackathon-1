@echo off
echo 🚀 Physical AI Backend - Hugging Face Deployment
echo ============================================================
echo.
echo Please enter your Hugging Face token:
echo Get it from: https://huggingface.co/settings/tokens
echo.
set /p HF_TOKEN=HF_TOKEN=
echo.
echo Deploying with your token...
echo.
python deploy_to_hf.py %HF_TOKEN%
pause
