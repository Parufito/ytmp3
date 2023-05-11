# Agafa el primer paràmetre de la execució del script des del shell $1 (ho vaig canviar, abans ho pillava de una variable d'entorn $URL, però no hi podia accedir des del bot de telegram node-telegram-bot-api)
# --ppa fa un crop de la imatge, pq a youtube és 16:9 i els discos són squared.
yt-dlp --extract-audio --embed-thumbnail -o "music/single/%(title)s.%(ext)s" --audio-format mp3 --add-metadata  $1 --ppa "EmbedThumbnail+ffmpeg_o:-c:v mjpeg -vf crop=\"'if(gt(ih,iw),iw,ih)':'if(gt(iw,ih),ih,iw)'\""

