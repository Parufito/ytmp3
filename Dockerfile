# Utilitzem una imatge base amb Python instal·lat
FROM node:20-alpine

# Actualitzem el sistema i instal·lem dependències
RUN apk add --no-cache ffmpeg py3-pip

# Instal·lem les llibreries de Python
RUN pip install yt-dlp

# Copiem el script i els fitxers necessaris a la imatge
WORKDIR /usr/src/app

# Instalar el bot de telegram
RUN npm install node-telegram-bot-api

# Copiar arxius del projecte
COPY . .
RUN chmod ugo+x *.sh

# Executem el script en l'entrada de la imatge
CMD ["node", "telegram.js"]
