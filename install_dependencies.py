#!/usr/bin/env python3
"""
Dependency Installation Script for NLP Workshop
This script installs all required dependencies with proper error handling
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"📥 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 NLP Workshop Dependency Installation")
    print("=" * 45)

    # Check if we're in a virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✓ Running in virtual environment")
    else:
        print("⚠️ Not in virtual environment. Consider activating nlp_env first:")
        print("source nlp_env/bin/activate")

    # Install Python packages
    success_count = 0
    total_commands = 0

    # Install core requirements
    total_commands += 1
    if run_command("pip install --upgrade pip", "Upgrading pip"):
        success_count += 1

    total_commands += 1
    if run_command("pip install -r requirements.txt", "Installing core dependencies"):
        success_count += 1

    # Install additional packages for workshop
    total_commands += 1
    if run_command("pip install jupyter notebook matplotlib pandas seaborn scikit-learn",
                   "Installing workshop packages"):
        success_count += 1

    # Setup NLTK data
    total_commands += 1
    if run_command("python setup_nltk.py", "Setting up NLTK data"):
        success_count += 1

    print(f"\n📊 Installation Summary: {success_count}/{total_commands} steps completed")

    if success_count == total_commands:
        print("🎉 All dependencies installed successfully!")
        print("\nNext steps:")
        print("1. Run 'python verify_setup.py' to verify installation")
        print("2. Start Jupyter: 'jupyter notebook'")
        print("3. Open 'NLP_Workshop_Starter.ipynb'")
    else:
        print("⚠️ Some installations failed. Please check the errors above.")
        print("You may need to:")
        print("- Check your internet connection")
        print("- Try installing packages individually")
        print("- Check Python version compatibility")

if __name__ == "__main__":
    main()
