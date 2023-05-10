# ytmp3
## Telegram bot to download mp3 from youtube using yt-dlp
Per aprendre coses he fet servir chatGPT per fer-me un bot que em faci coses. 

### Característiques
- Utilitza Docker, per configurar un entorn amb python3 i node.js
- Funciona en Raspberry Pi
- Imatge base Docker: node alpine

### Llibreries
- Telegram bot: node-telegram-bot-api [npm]
- Youtube: yt-dlp [pip]
- Conversió mp3: ffmpeg [apk]

### Docker
#### Build
``docker build -t ytmp3 .``
#### Execution
``docker run --name ytmp3 --rm -d -v "$(pwd)/music:/usr/src/app/music" -e TELEGRAM_TOKEN=YOURTELEGRAMBOTTOKEN ytmp3``

### Utilització
#### Crear bot telegram
- Crea't un bot des de @botfather i aconsegueix un token

#### Des de telegram si executem 
``/start``
Envia un missatge de salutació

``/ytplaylist``
Necessita com a paràmetre una URL de youtube (o youtube music) pot ser una cançó sola o una playlist.
- Descarrega les cançons
- Les converteix a MP3
- Omple el ID3 tag
- Afegeix el thumbnail, en fa crop perque sigui quadrat i l'afegeix al mp3
- Guarda a la carpeta /music amb l'estructura ``<artist>/<album/<pista> - <Trackname>.mp3``
  
*cal depurar una mica l'estructura de directoris, si no aconsegueix alguns noms posa /NA* 
  
### ToDo
En un futur vull afegir nous paràmetres per fer noves coses
- Reordenar els scripts i directoris
- Crear directoris d'us (els que seran volums externs)
- Afegir descàrrega de podcasts i que crei un rss.xml
- Afegir nginx o similar per publicar el podcast
- Crear un docker compose file 

