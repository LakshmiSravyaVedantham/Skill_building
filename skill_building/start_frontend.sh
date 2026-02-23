#!/bin/bash

# Skill Building Frontend Startup Script

echo "🎨 Starting Financial Literacy Frontend..."

# Navigate to frontend directory
cd "$(dirname "$0")/frontend"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing npm dependencies..."
    npm install
fi

# Start the development server
echo "🌟 Starting Vite dev server on http://localhost:5173"
echo ""
npm run dev
