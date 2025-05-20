import logging
from telegram import Update, Bot, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = os.environ.get("TELEGRAM_TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Bot is active! Add me to a group and make me admin to start.")

def welcome(update: Update, context: CallbackContext):
    for member in update.message.new_chat_members:
        surname = member.last_name if member.last_name else member.first_name
        group_name = update.message.chat.title
        print(f"✅ Welcome triggered for: {surname} in {group_name}")
        welcome_text = f"""😊 Hai {surname}, Selamat datang ke {group_name}! ❤️
Kami super teruja sebab kamu join! 🌟
🎊 Jom enjoy sama-sama & sebarkan vibe positif dalam group ni!
"""
        update.message.reply_text(welcome_text, parse_mode=ParseMode.MARKDOWN)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
