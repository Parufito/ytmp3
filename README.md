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


En un futur vull afegir nous paràmetres per fer noves coses
