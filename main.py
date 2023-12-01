import os
if os.name == 'nt':
    url = input("URL:")
    path = f"C:/Users/{os.getenv("USERNAME")}/Music/%(title)s.%(ext)s"
    os.system(f"yt-dlp -f bestaudio -x --audio-format mp3 {url}  -o {path}")
else:
    url = input("URL:")
    os.system(f"yt-dlp -f bestaudio -x --audio-format mp3 {url}  -o '~/Music/%(title)s.%(ext)s'")
