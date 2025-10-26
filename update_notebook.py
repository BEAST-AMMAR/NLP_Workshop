import json

# Load the notebook
with open('NLP_Workshop_Starter.ipynb', 'r') as f:
    notebook = json.load(f)

# Find the cell with speech recognition
for cell in notebook['cells']:
    if cell['cell_type'] == 'code' and cell['source'] and '# Now try importing the modules' in ''.join(cell['source']):
        # Update the source
        new_source = [
            "# Now try importing the modules\n",
            "try:\n",
            "    import os\n",
            "    import sys\n",
            "    import json\n",
            "    import pyaudio\n",
            "    from vosk import Model, KaldiRecognizer\n",
            "    print(\"Successfully imported vosk and pyaudio!\")\n",
            "except ImportError as e:\n",
            "    print(f\"Import error: {e}\")\n",
            "    print(\"Please install pyaudio: pip install pyaudio\")\n",
            "    print(\"You may need to install PortAudio first: brew install portaudio\")\n",
            "\n",
            "MODEL_PATH = \"models/vosk/vosk-model-small-en-us-0.15\"\n",
            "if not os.path.exists(MODEL_PATH):\n",
            "    print(\"Please download the Vosk model from https://alphacephei.com/vosk/models\")\n",
            "else:\n",
            "    print(\"Speech recognition model found. Ready to test!\")\n",
            "    print(\"Run 'python test_speech.py' in your terminal to test speech recognition.\")\n"
        ]
        cell['source'] = new_source
        break

# Save the notebook
with open('NLP_Workshop_Starter.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated successfully!")
