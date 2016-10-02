from telegram.ext import CommandHandler

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi! I'm a bot.")
