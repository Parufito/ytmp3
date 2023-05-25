from yt_dlp import YoutubeDL
import os

def download_video(url, path):
    ydl_opts = {
        'restrictfilenames': True,
        'outtmpl': path,
        'extractaudio': True,
        'audioformat': 'mp3',
        'embedthumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'addmetadata': True,
        'postprocessor_args': ['-c:v', 'mjpeg', '-vf', "crop='if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'"],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Comprovar si l'execució ha estat correcta
    video_id = url.split('=')[-1]
    file_path = f"podcast/{video_id}.mp3"
    if os.path.exists(file_path):
        return("Execució correcta!")
    else:
        return("Hi ha hagut un error en l'execució.")