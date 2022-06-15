import os
import sys
l = input('Link:')
if sys.platform == 'win32':
    os.system(f"yt-dlp -x --audio-format mp3 {l} -o C:/Users/%username%/Downloads/%(title)s.%(ext)s")
else:
    os.system(f"yt-dlp -f 'ba' -x --audio-format mp3 '{l}'  -o '~/Downloads/%(title)s.%(ext)s'")