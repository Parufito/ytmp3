#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position

import os, re
from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

import download

# Token del bot de Telegram
token = os.environ.get('TELEGRAM_TOKEN')

# Define a few command handlers. These usually take the two arguments update and context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    text = update.message.text

    # El missatge conté "youtube.com"
    if re.search(r"youtube\.com", text, re.IGNORECASE):
        """Sends a message with three inline buttons attached."""
        keyboard = [
            [
                InlineKeyboardButton("Playlist", callback_data=f"playlist;{text}"),
                InlineKeyboardButton("Single", callback_data=f"single;{text}"),
                InlineKeyboardButton("Podcast", callback_data=f"podcast;{text}"),
                InlineKeyboardButton("RES", callback_data=f"res;{text}"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Què faig:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    #query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await update.callback_query.answer()
    #data = update.callback_query.data  # Dades rebudes en el callback

    opcio, url = update.callback_query.data.split(";")  # Separar les dades
    await update.callback_query.edit_message_text(text=f"Has escollit: {opcio}")

    match opcio:
        case "res":
            pass
        case "single":
            path = 'music/single/%(title)s.%(ext)s'
        case "playlist":
            path = 'music/%(artist)s/%(album)s/%(playlist_index)s - %(title)s.%(ext)s'
        case "podcast":
            path = 'podcast/%(title)s.%(ext)s'

    result = await download.download_video(url,path)
    await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text=result)

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, youtube))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
