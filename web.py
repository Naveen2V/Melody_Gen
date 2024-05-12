import streamlit as st
import json
import numpy as np
import tensorflow.keras as keras
from preprocess import SEQUENCE_LENGTH, MAPPING_PATH  # Assuming preprocess.py defines these
from melodygenerator import MelodyGenerator
from io import BytesIO

# Load the MelodyGenerator model
mg = MelodyGenerator()

def generate_and_play(seed, seed2, num_steps, max_sequence_length, temperature):
  """Generates a melody, converts it to audio using simpleaudio, and plays it in the browser."""
  melody = mg.generate_melody(seed, num_steps, max_sequence_length, temperature)
  audio_data = mg.save_melody(melody, format="wav", file_name=None)  # Save to memory
  play_obj = sa.play_obj(audio_data)
  play_obj.wait_done()  # Wait for audio to finish playing

# Import SimpleAudio (assuming it's installed)
import simpleaudio as sa  # You might need to install it using !pip install simpleaudio

st.title("Melody Generator")

# Input fields for seeds
seed = st.text_input("Seed 1 (e.g., 67 _ 67 _ 60 _ _ 62...)", value="67 _ 67 _ 67 _ _ 65 64 _ 64 _ 64 _ _")
seed2 = st.text_input("Seed 2 (Optional)", value="")

# Parameters for melody generation
num_steps = st.slider("Number of Steps to Generate", min_value=50, max_value=1000, value=500)
max_sequence_length = st.slider("Max Sequence Length Considered", min_value=50, max_value=200, value=SEQUENCE_LENGTH)
temperature = st.slider("Temperature (Higher = More Random)", min_value=0.1, max_value=1.0, value=0.3)

# Generate button
if st.button("Generate Melody"):
  generate_and_play(seed, seed2, num_steps, max_sequence_length, temperature)

