from moviepy.editor import VideoFileClip

clip = VideoFileClip("C:/Users/VINOD SHUKLA/Desktop/voice clone/Python-Text-To-Speech-Hindi-master/Video 3_ Aatmaribharta.mp4")

audio = clip.audio

path = "result.mp3"

audio.write_audiofile(path)
clip.close()