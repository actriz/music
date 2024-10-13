import os
url = input("URL: ")
if os.name == "nt":
    path = f"C:/Users/{os.getenv("USERNAME")}/Music/%(title)s.%(ext)s"
    os.system(f"yt-dlp -f bestaudio -x --audio-format mp3 {url}  -o {path}")
else:
    os.system(f"yt-dlp -f bestaudio -x --audio-format mp3 {url} -o '~/Music/%(title)s.%(ext)s'")