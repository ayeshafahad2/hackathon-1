@echo off
REM Deploy Physical AI Backend to Hugging Face Spaces
REM Usage: deploy_hf_manual.bat YOUR_HF_TOKEN

if "%1"=="" (
    echo Error: Please provide your Hugging Face token
    echo Usage: deploy_hf_manual.bat YOUR_HF_TOKEN
    echo.
    echo Get your token from: https://huggingface.co/settings/tokens
    echo Make sure it has 'write' permissions for Spaces
    exit /b 1
)

set HF_TOKEN=%1
set SPACE_ID=ayeshafahad2/physical-ai-backend

echo ============================================================
echo Deploying Physical AI Backend to Hugging Face Spaces
echo ============================================================
echo Space ID: %SPACE_ID%
echo.

REM Login to Hugging Face
echo [1/4] Logging in to Hugging Face...
huggingface-cli login --token %HF_TOKEN%

REM Create the Space
echo.
echo [2/4] Creating Space repository...
python -c "from huggingface_hub import create_repo; create_repo('%SPACE_ID%', repo_type='space', space_sdk='docker', exist_ok=True, token='%HF_TOKEN%')"

REM Run the deployment script
echo.
echo [3/4] Uploading files...
python deploy_to_hf.py --token %HF_TOKEN% --space-id %SPACE_ID%

echo.
echo [4/4] Setting Space variables...
echo Note: You may need to set secrets manually at:
echo https://huggingface.co/spaces/%SPACE_ID%/settings/secrets
echo.
echo Secrets to configure:
echo   GEMINI_API_KEY=AIzaSyA42AJ8opmeUqD3xFkVuDpGuk3nGd1Aklo
echo   QDRANT_URL=https://e6f47427-0567-4d1b-97c1-0135dd98ddd2.us-east4-0.gcp.cloud.qdrant.io:6333
echo   QDRANT_API_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
echo   SECRET_KEY=supersecretkeychangethisinproduction
echo.

echo ============================================================
echo DEPLOYMENT COMPLETE!
echo ============================================================
echo.
echo Space URL: https://huggingface.co/spaces/%SPACE_ID%
echo Direct URL: https://ayeshafahad2-physical-ai-backend.hf.space
echo Health Check: https://ayeshafahad2-physical-ai-backend.hf.space/health
echo.
echo The Space is building now. This may take 5-10 minutes.
echo Check the Space URL for build progress.
echo ============================================================

pause
