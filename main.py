import os
url = input('Link:')
os.system(f"yt-dlp -f 'ba' -x --audio-format mp3 {url}  -o '~/Music/%(title)s.%(ext)s'")