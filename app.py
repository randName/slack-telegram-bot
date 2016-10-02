import os
import logging
import .config

from telegram.ext import Updater
from slackbot.bot import Bot

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def main():
    slackb = Bot()
    slackb.run()

    updater = Updater(token=TELEGRAM_TOKEN)
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
