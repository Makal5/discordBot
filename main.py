"""Run bot"""
import json

from Bot import bot
import logging.config
import os

# setup logging
# create log folder if does not exist
if not os.path.exists("./log"):
    os.mkdir("./log")
logger = logging.getLogger(__name__)
log_config_file = 'logging/logging.json'
try:
    with open(log_config_file, 'rt') as f:
        config = json.load(f)
    logging.config.dictConfig(config)
except Exception as e:
    logging.basicConfig(level=logging.DEBUG)
    logging.error('Loading logging configuration file failed.', exc_info=e)


if __name__ == '__main__':
    logging.info('Starting up')
    bot.run_discord_bot()
