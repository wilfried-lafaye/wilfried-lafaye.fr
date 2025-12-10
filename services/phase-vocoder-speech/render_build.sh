#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Building Phase Vocoder Service..."

# Build Frontend
echo "Building Frontend..."
cd frontend
npm install
npm run build
cd ..

# Install Backend Deps
echo "Installing Backend Dependencies..."
cd backend
pip install -r requirements.txt
cd ..

echo "Build Complete!"
