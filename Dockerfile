# Utilitzem una imatge base amb Python instal·lat
FROM python:3-alpine

# Actualitzem el sistema i instal·lem dependències
RUN apk add --no-cache ffmpeg

# Instal·lem les llibreries de Python
RUN pip install yt-dlp python-telegram-bot feedgen

# Copiem el script i els fitxers necessaris a la imatge
WORKDIR /usr/src/app

# Copiar arxius del projecte
COPY . .

# Executem el script en l'entrada de la imatge
CMD ["python", "telegrambot.py"]
