@echo off
echo Starting AI_GURU_PRO Local Deployment...
echo.

cd /d "D:\New download\au"

echo 🌐 Starting Website on port 5000...
start python website_ai.py

timeout /t 3

echo 📱 Starting Mobile on port 5001...
start python mobile_ai.py

timeout /t 3

echo ✅ Local Deployment Complete!
echo 🌐 Website: http://localhost:5000
echo 📱 Mobile: http://localhost:5001
echo.
echo Press Ctrl+C in each terminal to stop