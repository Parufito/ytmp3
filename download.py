from yt_dlp import YoutubeDL
import os

async def download_video(url, path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'restrictfilenames': True,
        'outtmpl': path,
        'extractaudio': True,
        'audioformat': 'mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
            },
            {
                'key': 'FFmpegMetadata'
            },
            {
                'key': 'EmbedThumbnail'
            }],
        'addmetadata': True,
        'writethumbnail': True,
        'postprocessor_args': ['-c:v', 'mjpeg', '-vf', "crop='if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'"],
        'embedthumbnail': True,
    }

    success = False
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        success = True
    except Exception as e:
        print(f"Error en descarregar el vídeo: {str(e)}")

    if success:
        return "La descàrrega s'ha completat amb èxit."
    else:
        return "Hi ha hagut un error en la descàrrega del vídeo."
