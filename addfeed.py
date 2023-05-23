import os
import subprocess
from datetime import datetime
from feedgen.feed import FeedGenerator


def add_rss_entry(youtube_url):
    # Executa yt-dlp per obtenir la informació del vídeo de YouTube
    command = f"yt-dlp --restrict-filenames -j {youtube_url}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error en executar yt-dlp: {result.stderr}")
        return

    # Parseja la sortida de yt-dlp com a JSON
    video_info = result.stdout.strip().split("\n")[-1]

    # Extreu les dades necessàries
    video_data = json.loads(video_info)
    video_title = video_data.get("title", "")
    video_description = video_data.get("description", "")
    video_pubdate = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")
    video_file = video_data.get("id", "")

    # Crea una nova entrada per al feed RSS
    fg = FeedGenerator()
    fg.load("music/podcast/rss.xml")  # Carrega el fitxer RSS existent
    fe = fg.add_entry()
    fe.title(video_title)
    fe.description(video_description)
    fe.pubDate(video_pubdate)
    fe.enclosure(f"http://192.168.1.111/{video_file}.mp3", type="audio/mpeg")
    fe.guid(video_file, isPermaLink=False)

    # Guarda el feed RSS actualitzat
    fg.rss_file("music/podcast/rss.xml", pretty=True)

    print("Entrada afegida amb èxit al feed RSS.")


# Exemple d'ús de la funció add_rss_entry
youtube_url = "https://www.youtube.com/watch?v=YmQcV3OBxpk"
add_rss_entry(youtube_url)
