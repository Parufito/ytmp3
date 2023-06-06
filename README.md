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
- ID3 extract info: mutagen [pip]


### Configuració
#### Crear bot telegram
- Crea't un bot des de @botfather i aconsegueix un token
- Edita el fitxer docker-compose.yaml per editar les variables d'entorn
    - TELEGRAM_TOKEN: El token obtingut 
    - PODCAST_URL: la ip o hostname des d'on estàs executant la imatge. Serveix per generar el RSS amb el path correcte

### Execució Docker
#### Build
``docker compose build``

#### Execution
``docker compose up -d``

### Telegram
Si al xat de telegram amb el bot hi incrustem una url de Youtube, aquest ens mostrarà uns botons per preguntar què hem de fer:
En tots els casos
- Descarrega les cançons
- Les converteix a MP3
- Omple el ID3 tag
- Afegeix el thumbnail, en fa crop perque sigui quadrat i l'afegeix al mp3 [no m'està funcionant sempre]
la comanda */rss* permet regenerar el rss en cas que hi hagi hagut algun problema

#### Single
- Guarda a la carpeta /music/single amb l'estructura ``music/single/%(title)s.%(ext)s``
#### Playlist
- Guarda a la carpeta /music amb l'estructura ``<artist>/<album/<pista> - <Trackname>.mp3``
#### Podcast
- Guarda a la carpeta /music/podcast ``podcast/%(title)s.%(ext)s``
- Afegeix aquest fitxer a un rss.xml exposat via nginx per tenir un podcast amb els vídeos que vulguem

 
### ToDo
- Repassar la generació de thumbnails
- Millorar l'estructura del rss.xml generat
- Afegir una creation date als podcast per saber quan me'ls he descarregat i que es vegin "en ordre" des de la app de podcasts
- Opció per esborrar fitxers

