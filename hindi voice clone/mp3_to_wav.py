from moviepy.editor import AudioFileClip

# Function to convert MP3 to WAV using moviepy
def convert_mp3_to_wav(mp3_file, wav_file):
    try:
        # Load the MP3 file
        audio_clip = AudioFileClip(mp3_file)
        
        # Write the audio clip to a WAV file
        audio_clip.write_audiofile(wav_file, codec='pcm_s16le')  # Use the WAV codec
        
        print(f"Conversion complete: {mp3_file} to {wav_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

audio_path = 'C:/Users/VINOD SHUKLA/Desktop/voice clone/Python-Text-To-Speech-Hindi-master/result.mp3'
wav_file = "output.wav"  # Output WAV file path

convert_mp3_to_wav(audio_path, wav_file)