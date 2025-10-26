#!/usr/bin/env python3
"""
Setup Verification Script for NLP Workshop
This script verifies that all components are properly installed and working
"""

import sys
import importlib

def check_import(module_name, description):
    """Check if a module can be imported"""
    try:
        importlib.import_module(module_name)
        print(f"✓ {description} - {module_name}")
        return True
    except ImportError as e:
        print(f"✗ {description} - {module_name} (Error: {e})")
        return False

def check_nltk_data():
    """Check if NLTK data is available"""
    try:
        import nltk
        from nltk.tokenize import word_tokenize
        from nltk.corpus import stopwords
        from nltk.stem import WordNetLemmatizer

        # Test tokenization
        test_text = "This is a test sentence."
        tokens = word_tokenize(test_text)
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()

        print("✓ NLTK core functionality working")
        return True
    except Exception as e:
        print(f"✗ NLTK data issue: {e}")
        return False

def check_vosk_model():
    """Check if Vosk model exists"""
    import os
    model_path = "models/vosk/vosk-model-small-en-us-0.15"
    if os.path.exists(model_path):
        print("✓ Vosk speech recognition model found")
        return True
    else:
        print("⚠ Vosk model not found (optional for basic NLP)")
        print("  Download from: https://alphacephei.com/vosk/models")
        return False

def main():
    print("🔍 NLP Workshop Setup Verification")
    print("=" * 40)

    # Check Python version
    python_version = sys.version.split()[0]
    print(f"✓ Python version: {python_version}")

    # Check essential libraries
    libraries = [
        ('nltk', 'Natural Language Toolkit'),
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('sklearn', 'Scikit-learn'),
        ('vosk', 'Vosk Speech Recognition'),
        ('pyaudio', 'PyAudio'),
        ('sounddevice', 'SoundDevice'),
    ]

    working_libs = 0
    for module, description in libraries:
        if check_import(module, description):
            working_libs += 1

    print(f"\n📊 Library Status: {working_libs}/{len(libraries)} working")

    # Check NLTK data
    if check_nltk_data():
        nltk_status = "✓"
    else:
        nltk_status = "✗"

    # Check Vosk model
    check_vosk_model()

    print("\n🎯 Summary:")
    print(f"  {nltk_status} NLTK Data: Ready for text processing")
    print(f"  {'✓' if working_libs >= 5 else '⚠'} Core Libraries: {'Ready' if working_libs >= 5 else 'Some missing'}")

    if working_libs >= 5:
        print("\n🎉 Setup looks good! You can start the workshop.")
        print("   - Open 'NLP_Workshop_Starter.ipynb' in Jupyter")
        print("   - Or open any .py file in VS Code")
    else:
        print("\n⚠️  Some libraries are missing. Please run:")
        print("   pip install -r requirements.txt")

    print("\n📝 Next Steps:")
    print("   1. Open README.md for detailed instructions")
    print("   2. Run 'jupyter notebook' to start Jupyter")
    print("   3. Open 'NLP_Workshop_Starter.ipynb'")
    print("   4. Follow the interactive tutorial")

if __name__ == "__main__":
    main()
