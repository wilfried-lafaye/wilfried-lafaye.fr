#!/bin/bash

# Function to kill background processes on exit
cleanup() {
    echo "Stopping servers..."
    kill $(jobs -p) 2>/dev/null
    exit
}

trap cleanup SIGINT SIGTERM

echo "🚀 Starting Audio Vocoder..."

# Start Backend
echo "🎧 Starting Backend (FastAPI)..."
cd backend
source venv/bin/activate || python3 -m venv venv && source venv/bin/activate
pip install -q -r requirements.txt
uvicorn main:app --reload --port 8000 &
BACKEND_PID=$!
cd ..

# Start Frontend
echo "🎨 Starting Frontend (React)..."
cd frontend
npm install
npm run dev -- --port 3001 &
FRONTEND_PID=$!
cd ..

echo "✅ App is running!"
echo "   Frontend: http://localhost:3001"
echo "   Backend:  http://localhost:8000"
echo "Press Ctrl+C to stop."

wait
