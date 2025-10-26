# NLP Workshop Setup Guide

Welcome to the Natural Language Processing Workshop! This comprehensive guide will help you set up your development environment and get started with NLP concepts and techniques.

## 📋 Prerequisites

- **Python 3.8+** (recommended: 3.8-3.11)
- **VS Code** or **Jupyter Notebook**
- **Virtual Environment** (already set up as `nlp_env/`)
- **Microphone** (for speech recognition features)

## 🚀 Quick Setup

### Step 1: Activate Virtual Environment

```bash
# Navigate to the workshop directory
cd /Users/ammar/Desktop/NLP_Workshop

# Activate the virtual environment
source nlp_env/bin/activate
```

### Step 2: Install Dependencies

**Option A: Automated Installation (Recommended)**
```bash
# Run the automated installation script
python install_dependencies.py
```

**Option B: Manual Installation**
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Install additional packages for the workshop
pip install jupyter notebook matplotlib pandas seaborn scikit-learn
```

### Step 3: Set Up NLTK Data

```bash
# Run the NLTK setup script
python setup_nltk.py
```

### Step 4: Start Jupyter Notebook

```bash
# Start Jupyter Notebook
jupyter notebook
```

## 💻 Development Environment Options

### Option A: VS Code (Recommended)

1. **Open the workshop folder** in VS Code
2. **Install Python extension** if not already installed
3. **Select the interpreter**: Choose `nlp_env/bin/python` from the command palette
4. **Open any Python file** to start coding
5. **Use the debug configurations** in `.vscode/launch.json`

**VS Code Features:**
- ✅ Code completion and IntelliSense
- ✅ Integrated debugging
- ✅ Jupyter notebook support
- ✅ Git integration
- ✅ Extensions for Python development

### Option B: Jupyter Notebook

1. **Activate virtual environment**: `source nlp_env/bin/activate`
2. **Start Jupyter**: `jupyter notebook`
3. **Open `NLP_Workshop_Starter.ipynb`** in your browser
4. **Follow the interactive tutorial**

## 📚 Available Tools and Libraries

### Core NLP Libraries
- **NLTK** (Natural Language Toolkit) - Text processing, tokenization, POS tagging
- **Vosk** - Offline speech recognition
- **spaCy** - Advanced NLP (if installed)
- **Transformers** - Pre-trained language models (if installed)

### Data Analysis & Visualization
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Matplotlib** - Plotting and visualization
- **Seaborn** - Statistical visualization

### Machine Learning
- **Scikit-learn** - Machine learning algorithms
- **TensorFlow/PyTorch** - Deep learning (if installed)

## 🎯 Workshop Structure

### 1. Basic Text Processing
- Tokenization (word and sentence splitting)
- Stop word removal
- Stemming and lemmatization
- Part-of-speech tagging

### 2. Advanced NLP Tasks
- Named Entity Recognition (NER)
- Sentiment Analysis with VADER
- Text classification
- Language modeling

### 3. Speech Recognition
- Real-time speech-to-text with Vosk
- Audio processing with PyAudio
- Speech analysis

### 4. Projects and Applications
- Chatbot development
- Text summarization
- Sentiment analysis applications
- Language detection

## 🔧 Running Examples

### Test Speech Recognition

```bash
# Activate environment and run speech test
source nlp_env/bin/activate
python test_speech.py
```

**Note**: Make sure you have a microphone connected and the Vosk model downloaded.

### Run NLTK Setup

```bash
python setup_nltk.py
```

### Open Workshop Notebook

```bash
jupyter notebook NLP_Workshop_Starter.ipynb
```

## 📁 Project Structure

```
NLP_Workshop/
├── requirements.txt          # Python dependencies
├── setup_nltk.py            # NLTK data setup script
├── test_speech.py           # Speech recognition test
├── NLP_Workshop_Starter.ipynb # Main workshop notebook
├── README.md                # This file
├── .vscode/                 # VS Code configuration
│   ├── settings.json        # Editor settings
│   └── launch.json          # Debug configurations
├── nlp_env/                 # Virtual environment
├── models/                  # ML models (Vosk, etc.)
├── nltk_data/               # NLTK datasets
└── bin/                     # Binary files (ffmpeg, etc.)
```

## 🐛 Troubleshooting

### Common Issues

**1. Virtual Environment Not Activated**
```bash
# Check if you're in the virtual environment
which python  # Should show path to nlp_env/bin/python
```

**2. Missing Dependencies**
```bash
pip install -r requirements.txt
```

**3. NLTK Data Not Found**
```bash
python setup_nltk.py
```

**4. Jupyter Notebook Kernel Issues**
```bash
# Reinstall Jupyter in the virtual environment
pip uninstall jupyter notebook ipykernel
pip install jupyter notebook ipykernel
```

**5. Speech Recognition Not Working**
- Check microphone permissions
- Ensure Vosk model is downloaded
- Verify PyAudio installation

### Getting Help

If you encounter issues:
1. Check the error messages carefully
2. Verify all steps in the setup guide
3. Check that you're using the correct Python interpreter
4. Ensure all dependencies are installed

### Common Issues and Solutions

**1. "No module named 'nltk'"**
```bash
# Install NLTK
pip install nltk
```

**2. "No matching distribution found for vosk==0.3.45"**
- The requirements.txt has been updated to use vosk==0.3.44
- Run: `pip install -r requirements.txt`

**3. "jupyter: command not found"**
```bash
# Install Jupyter in your virtual environment
pip install jupyter notebook
```

**4. Virtual Environment Issues**
```bash
# Recreate virtual environment if needed
rm -rf nlp_env
python3 -m venv nlp_env
source nlp_env/bin/activate
pip install -r requirements.txt
```

**5. Permission Errors on macOS**
```bash
# Use --user flag if you have permission issues
pip install --user -r requirements.txt
```

## 🎓 Learning Resources

### Recommended Reading
- "Natural Language Processing with Python" by Steven Bird
- NLTK Documentation: https://www.nltk.org/
- Python Documentation: https://docs.python.org/

### Online Resources
- NLTK Book: https://www.nltk.org/book/
- Kaggle NLP Tutorials: https://www.kaggle.com/learn/natural-language-processing
- Hugging Face Transformers: https://huggingface.co/docs/transformers/

## 📝 Workshop Agenda

### Day 1: Fundamentals
- Environment setup
- Basic text processing
- Tokenization and normalization

### Day 2: Text Analysis
- POS tagging
- Named entity recognition
- Sentiment analysis

### Day 3: Speech Recognition
- Audio processing
- Speech-to-text conversion
- Voice applications

### Day 4: Advanced Topics
- Text classification
- Topic modeling
- Building NLP applications

### Day 5: Projects
- Final project development
- Presentation and review

## 🎉 Next Steps

1. **Complete the setup** following the instructions above
2. **Open the workshop notebook** and work through the examples
3. **Experiment with the code** and modify it to understand concepts
4. **Try the speech recognition** features
5. **Build your own NLP projects** using the provided tools

Happy learning! 🚀

---

**Contact**: If you need help or have questions, feel free to ask during the workshop sessions.
