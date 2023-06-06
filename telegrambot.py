#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position

import os
import re

from telegram import ForceReply, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

import addfeed
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

async def refresh_rss(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    addfeed.generate_rss()
    await update.message.reply_html(
        rf"Regenerant RSS",
        reply_markup=ForceReply(selective=True),
    )

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    context.user_data['youtube_url'] = update.message.text

    # El missatge conté "youtube.com"
    if re.search(r"youtube\.com", update.message.text, re.IGNORECASE):
        """Sends a message with three inline buttons attached."""
        keyboard = [
            [
                InlineKeyboardButton("Playlist", callback_data=f"playlist"),
                InlineKeyboardButton("Single", callback_data=f"single"),
                InlineKeyboardButton("Podcast", callback_data=f"podcast"),
                InlineKeyboardButton("RES", callback_data=f"res"),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Què faig:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await update.callback_query.answer()

    url = context.user_data.get('youtube_url')
    opcio = update.callback_query.data  # Separar les dades

    await update.callback_query.edit_message_text(text=f"Has escollit: {opcio}")

    match opcio:
        case "res":
            pass
        case "single":
            path = 'music/single/%(title)s.%(ext)s'
            await download.download_video(url, path)
            await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="fet!")
        case "playlist":
            path = 'music/%(artist)s/%(album)s/%(playlist_index)s - %(title)s.%(ext)s'
            await download.download_video(url, path)
            await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="ok")
        case "podcast":
            path = 'music/podcast/%(title)s.%(ext)s'
            await download.download_video(url, path)
            await context.bot.send_message(chat_id=update.callback_query.message.chat_id, text="molon")
            addfeed.generate_rss()


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("rss", refresh_rss))
    application.add_handler(CallbackQueryHandler(button))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, youtube))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
