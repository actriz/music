import os
l = input('Link:')
os.system(f"yt-dlp -f 'ba' -x --audio-format mp3 '{l}'  -o '~/Downloads/%(title)s.%(ext)s'")