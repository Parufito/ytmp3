# ytmp3
## Telegram bot to download mp3 from youtube using yt-dlp
Per aprendre coses he fet servir chatGPT per fer-me un bot que em faci coses. 

### Característiques
- Utilitza Docker, per configurar un entorn amb python3
- Funciona en Raspberry Pi
- Imatge base Docker: python:3-alpine

### Llibreries
- Telegram bot: python-telegram-bot [pip]
- Youtube: yt-dlp [pip]
- Conversió mp3: ffmpeg [apk]

### Docker
#### Build
``docker build -t ytmp3 .``
#### Execution
``docker run --name ytmp3 --rm -d -v "$(pwd)/music:/usr/src/app/music" -e TELEGRAM_TOKEN=YOURTELEGRAMBOTTOKEN ytmp3``

### Docker compose
``docker compose build``
``docker compose up``

### Utilització
#### Crear bot telegram
- Crea't un bot des de @botfather i aconsegueix un token

#### Des de telegram si executem 
Si al xat de telegram amb el bot hi incrustem una url de Youtube, aquest ens mostrarà uns botons per preguntar què hem de fer:
En tots els casos
- Descarrega les cançons
- Les converteix a MP3
- Omple el ID3 tag
- Afegeix el thumbnail, en fa crop perque sigui quadrat i l'afegeix al mp3

#### Single
- Guarda a la carpeta /music/single amb l'estructura ``music/single/%(title)s.%(ext)s``
#### Playlist
- Guarda a la carpeta /music amb l'estructura ``<artist>/<album/<pista> - <Trackname>.mp3``
#### Podcast
- Guarda a la carpeta /music/podcast ``podcast/%(title)s.%(ext)s``

 
### ToDo
En un futur vull afegir nous paràmetres per fer noves coses
- reparar el bug quan s'envia una playlist
- si no aconsegueix alguns noms posa /NA
- Quan es cliqui descàrrega de podcasts que actualitzi automàticament el rss.xml

