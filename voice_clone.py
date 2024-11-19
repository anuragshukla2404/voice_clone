from pytube import YouTube
youtube_url = "https://www.youtube.com/watch?v=Saje4-TqRdo&t=3556s"
yt = YouTube(youtube_url)

TMP_DIR="./tmp"

audio = yt.streams.filter(only_audio=True).first() 
audio.download(output_path=TMP_DIR, filename="audio.mp4")

