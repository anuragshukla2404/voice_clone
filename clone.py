import torch
from TTS.api import TTS

device = "cuda" if torch.cuda.is_available() else "cpu"

print(TTS().list_models())

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Run TTS
wav = tts.tts_to_file(text="आज आपने अबुजा में अजूबा कर दिया है। अबुजा में अद्भुत समा बांध दिया है। और ये सब देखकर के कल शाम से मैं देख रहा हूं, ऐसा लगता है, मैं अबुजा में नहीं बल्कि भारत के ही किसी शहर में मौजूद हूं।", speaker_wav="tmp/audio.wav", language="hi", file_path="tmp/modi.wav")