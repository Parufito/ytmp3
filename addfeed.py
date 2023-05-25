import os
from mutagen.id3 import ID3

directori = 'music/podcast'
rss_file = 'music/podcast/rss.xml'
podcast_url = os.environ.get('PODCAST_URL')

rss = '<?xml version="1.0" encoding="UTF-8"?>\n'
rss += '<rss version="2.0"\n'
rss += '    xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd">\n'
rss += '  <channel>\n'
rss += '    <title>ParufitoYtmp3 Podcast</title>\n'
rss += '    <itunes:owner>\n'
rss += '        <itunes:email>parufito@example.com</itunes:email>\n'
rss += '    </itunes:owner>\n'
rss += '    <itunes:author>Parufito</itunes:author>\n'
rss += '    <description>YAP Youtube as a podcast</description>\n'
rss += '    <itunes:image href="http://192.168.1.111/logo.png"/>\n'
rss += '    <language>ca-es</language>\n'
rss += '    <link>https://www.parufito.info</link>\n'

for filename in os.listdir(directori):
    fitxer_path = os.path.join(directori, filename)
    if os.path.isfile(fitxer_path) and filename.endswith('.mp3'):
        tags = ID3(fitxer_path)
        title = tags.get('TIT2', [''])[0]
        artist = tags.get('TPE1', [''])[0]
        album = tags.get('TALB', [''])[0]
        file_url = f"{podcast_url}{filename}"

        rss += '    <item>\n'
        rss += f'      <title>{title}</title>\n'
        rss += f'      <description>{artist} - {album}</description>\n'
        rss += '      <pubDate>Tue, 14 Mar 2017 12:00:00 GMT</pubDate>\n'
        rss += f'      <enclosure url="{file_url}" type="audio/mpeg"/>\n'
        rss += f'      <guid isPermaLink="false">{filename}</guid>\n'
        rss += '    </item>\n'

rss += '  </channel>\n'
rss += '</rss>'

with open(rss_file, 'w') as file:
    file.write(rss)

