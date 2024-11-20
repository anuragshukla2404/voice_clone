import pyttsx3
import pyaudio
import wave
import librosa  
import numpy as np
from gtts import gTTS

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Initialize pyaudio instance
p = pyaudio.PyAudio()

# Set properties for the speech engine (Optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level

# Output file where the synthesized speech will be saved
output_filename = "modi.mp3"

# Function to load the audio sample
def load_audio_sample(audio_path):
    # Load the sample audio using librosa
    audio_data, sample_rate = librosa.load(audio_path, sr=22050)  # Default sampling rate to 22050 Hz
    print(f"Audio loaded: {audio_path}, Sample rate: {sample_rate} Hz")
    return audio_data, sample_rate

# Function to save speech to a file
def save_speech_to_file(text, output_filename):
    # Open the stream to write to a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(1)  # Mono audio
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))  # Sample width for audio
    wf.setframerate(22050)  # Sample rate
    
    def callback(name, location, length):
        # Callback to write audio to the file
        data = location[:length]
        wf.writeframes(data)
    
    engine.say(text, callback)  # Pass text to the engine to generate speech
    engine.runAndWait()  # Run the engine to generate speech
    
    # Close the wave file after completion
    wf.close()

# Example usage:

# Load the audio sample (input file with speech)
audio_path = 'C:/Users/VINOD SHUKLA/Desktop/voice clone/Python-Text-To-Speech-Hindi-master/output.wav'  # Provide your input audio file path
audio_data, sample_rate = load_audio_sample(audio_path)

text_to_speak = "आज आपने अबुजा में अजूबा कर दिया है। अबुजा में अद्भुत समा बांध दिया है। और ये सब देखकर के कल शाम से मैं देख रहा हूं, ऐसा लगता है, मैं अबुजा में नहीं बल्कि भारत के ही किसी शहर में मौजूद हूं।"

tts = gTTS(text=text_to_speak,lang='hi')
output_path = "output_audio.wav"
tts.save(output_path)

print(f"Speech generated and saved to: {output_path}")
