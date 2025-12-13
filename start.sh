#!/bin/bash

# Function to kill background processes on exit
cleanup() {
    echo "Stopping servers..."
    kill $(jobs -p)
}

# Trap SIGINT (Ctrl+C) to run cleanup
trap cleanup SIGINT

echo "🚀 Starting Local Development Environment..."

# Start Backend
echo "📦 Starting Backend on port 10000..."
(cd backend && PORT=10000 npm start) &
BACKEND_PID=$!

# Start Frontend
# Using python3 http.server as a simple static server
echo "🎨 Starting Frontend on http://localhost:8080..."
python3 -m http.server 8080 -d docs &
FRONTEND_PID=$!

echo "✅ Environment running!"
echo "   - Frontend: http://localhost:8080"
echo "   - Backend:  http://localhost:10000"
echo ""
echo "Press Ctrl+C to stop."

# Wait for processes
wait
