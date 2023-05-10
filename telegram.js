const TelegramBot = require('node-telegram-bot-api');
const { exec } = require('child_process');

// Token del bot de Telegram
const token = process.env.TELEGRAM_TOKEN;

// Comprova si s'ha definit el token
if (!token) {
  console.error('El token de Telegram no s\'ha definit a la variable d\'entorn TELEGRAM_TOKEN.');
  process.exit(1);
}

// Crea una instància del bot de Telegram
const bot = new TelegramBot(token, { polling: true });


// Escolta "/start"
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const message = 'Hola! Sóc el parubot\nTens dues (o més) comandes\n/start \n/ytplaylist \n/pwd';
  bot.sendMessage(chatId, message);
});

// Escolta "/ytplaylist" seguit d'una url de youtube music playlist
bot.onText(/\/ytplaylist (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  const yt_url = match[1]; // Obté la url de Youtube

  // Executa el shellscript
  downloadPlaylist(chatId, yt_url);
});

// Escolta "/pwd" seguit d'una url de youtube music playlist
bot.onText(/\/pwd (.+)/, (msg, match) => {
  const chatId = msg.chat.id;
  // Executa el shellscript
  pwd(chatId);
});


// Funció per executar el shell script i confirmar
function downloadPlaylist(chatId, yt_url) {
  exec("sh /usr/src/app/playlist.sh "+yt_url, (error, stdout, stderr) => {
    if (error) {
      bot.sendMessage(chatId, `Hi ha hagut un error a l'executar el script:\n${error.message}`);
      return;
    }

    if (stderr) {
      bot.sendMessage(chatId, `Hi ha hagut un error a l'executar el script:\n${stderr}`);
      return;
    }

    bot.sendMessage(chatId, `Execució correcta:\n${stdout}`);
  });
}

// Funció per executar el shell script i confirmar
function pwd(chatId) {
  exec(pwd, (error, stdout, stderr) => {
    if (error) {
      bot.sendMessage(chatId, `Hi ha hagut un error a l'executar el script:\n${error.message}`);
      return;
    }

    if (stderr) {
      bot.sendMessage(chatId, `Hi ha hagut un error a l'executar el script:\n${stderr}`);
      return;
    }

    bot.sendMessage(chatId, `Execució correcta:\n${stdout}`);
  });
}
