import html
import os
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

from datetime import datetime
import email.utils

directori = 'music/podcast'
rss_file = 'music/podcast/rss.xml'
podcast_url = os.environ.get('PODCAST_URL')

def timestamp_a_rfc822(timestamp):
    data_dt = datetime.fromtimestamp(timestamp)
    return email.utils.format_datetime(data_dt)

def generate_rss():
    rss = '<?xml version="1.0" encoding="UTF-8"?>\n'
    rss += '<rss version="2.0"\n'
    rss += '    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">\n'
    rss += '  <channel>\n'
    rss += '    <title>Parufito Ytmp3 Podcast</title>\n'
    rss += '    <description>YAP Youtube as a podcast</description>\n'
    rss += f'    <itunes:image href="{podcast_url}logo.png"/>\n'
    rss += '    <language>ca-es</language>\n'
    rss += '    <link>https://www.parufito.info</link>\n'

    for filename in os.listdir(directori):
        fitxer_path = os.path.join(directori, filename)
        if os.path.isfile(fitxer_path) and filename.endswith('.mp3'):
            tags = ID3(fitxer_path)
            title = tags.get('TIT2', [''])[0]
            synopsis = tags.get('TXXX:synopsis', [''])[0]
            file_url = f"{podcast_url}{filename}"
            pubDate = timestamp_a_rfc822(os.path.getmtime(fitxer_path))
            duration_in_seconds = int((MP3(fitxer_path)).info.length)


            rss += '    <item>\n'
            rss += f'      <title>{html.escape(title)}</title>\n'
            rss += f'      <description>{html.escape(synopsis)}</description>\n'
            rss += f'      <pubDate>{pubDate}</pubDate>\n'
            rss += f'      <itunes:duration>{int(duration_in_seconds)}</itunes:duration>\n'
            rss += f'      <enclosure url="{file_url}" type="audio/mpeg"/>\n'
            rss += f'      <guid isPermaLink="false">{filename}</guid>\n'
            rss += '    </item>\n'

    rss += '  </channel>\n'
    rss += '</rss>'

    with open(rss_file, 'w') as file:
        file.write(rss)

    return "RSS actualitzat"
