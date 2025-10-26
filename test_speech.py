#!/usr/bin/env python3

import os
import sys
import wave
import json
from vosk import Model, KaldiRecognizer
import pyaudio

# Path to the Vosk model
MODEL_PATH = "models/vosk/vosk-model-en-us-0.22"  # <-- update this line

# Check if model exists
if not os.path.exists(MODEL_PATH):
    print("Please download the model from")
    print("https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit(1)

# Load the model
model = Model(MODEL_PATH)
rec = KaldiRecognizer(model, 16000)

# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Listening... Say something!")

try:
    while True:
        data = stream.read(CHUNK)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            result_dict = json.loads(result)
            if 'text' in result_dict:
                print("Recognized: " + result_dict['text'])
except KeyboardInterrupt:
    print("\nDone")
except Exception as e:
    print(f"Error: {e}")
finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
