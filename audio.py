import os
from pydub import AudioSegment

# Create tmp directory in current working dir for saving audio files 
TMP_DIR="./tmp"

# utility function to convert mp4 audio to wav (sr 48k by default)
def mp4_to_wav(mp4_file_path, output_dir, audio=None, out_file="audio.wav", frame_rate=48000):
    wav_file_path = os.path.join(output_dir, out_file)
    if not audio:
        audio = AudioSegment.from_file(mp4_file_path, format="mp4")
    audio.set_frame_rate(frame_rate).export(
        wav_file_path, format="wav"
    )
    return wav_file_path

# chunked audio to 15 seconds
audio = AudioSegment.from_file(f"{TMP_DIR}/audio.mp4", format="mp4")[1000:15000]
mp4_to_wav(mp4_file_path=None, audio=audio, output_dir="./tmp")