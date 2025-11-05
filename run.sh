#!/bin/bash
# Simple script to run the Water Remover App
# Usage: ./run.sh
# Note: You may need to make this script executable first with: chmod +x run.sh

echo "================================="
echo "Water Remover App - Startup"
echo "================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies if needed
echo "Checking dependencies..."
pip install -q -r requirements.txt

echo ""
echo "================================="
echo "Starting Water Remover App..."
echo "================================="
echo ""
echo "Access the app at: http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the app
python app.py
