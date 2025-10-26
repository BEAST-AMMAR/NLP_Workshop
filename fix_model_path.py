import json

# Load the notebook
with open('NLP_Workshop_Starter.ipynb', 'r') as f:
    notebook = json.load(f)

# Find the cell with speech recognition
for cell in notebook['cells']:
    if cell['cell_type'] == 'code' and cell['source'] and 'MODEL_PATH' in ''.join(cell['source']):
        # Update the MODEL_PATH
        source_str = ''.join(cell['source'])
        new_source_str = source_str.replace('MODEL_PATH = "models/vosk/vosk-model-small-en-us-0.15"', 'MODEL_PATH = "vosk-model-en-us-0.22"')
        cell['source'] = new_source_str.split('\n')
        break

# Save the notebook
with open('NLP_Workshop_Starter.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook updated with correct Vosk model path.")
