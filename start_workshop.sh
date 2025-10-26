#!/bin/bash

# NLP Workshop Startup Script
# This script sets up and starts the NLP workshop environment

echo "🚀 Starting NLP Workshop Setup..."
echo "================================="

# Check if virtual environment exists
if [ ! -d "nlp_env" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please create the virtual environment first:"
    echo "python3 -m venv nlp_env"
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source nlp_env/bin/activate

# Check if pip is available
if ! command -v pip &> /dev/null; then
    echo "❌ pip is not available!"
    echo "Please ensure Python and pip are installed."
    exit 1
fi

# Install dependencies
echo "📥 Installing dependencies..."
if pip install -r requirements.txt; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install some dependencies"
    echo "Please check your internet connection and try again"
    exit 1
fi

# Setup NLTK data
echo "📚 Setting up NLTK data..."
if python setup_nltk.py; then
    echo "✓ NLTK data setup complete"
else
    echo "⚠️ NLTK setup had issues, but continuing..."
fi

# Verify setup
echo "🔍 Verifying setup..."
python verify_setup.py

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the workshop:"
echo "1. For Jupyter Notebook: jupyter notebook"
echo "2. For VS Code: Open the folder in VS Code"
echo "3. Open 'NLP_Workshop_Starter.ipynb' to begin"
echo ""
echo "Happy learning! 🚀"
