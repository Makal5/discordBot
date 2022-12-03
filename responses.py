"""These are response for the bot now"""

import random
import logging

LOGGER = logging.getLogger(__name__)


def get_response(message: str) -> str:
    """Get response on user sent message"""
    if message.startswith('!'):

        p_message = message[1:].lower()

        if p_message == 'hello':
            return 'Hey there!'

        if p_message == 'roll':
            return str(random.randint(1, 6))
                            #!<@1047912725621264444>
        if p_message == '<@1047912725621264444>':
            return 'Yes, how can i help you?'

        if p_message == 'help':
            return '`These are all the available: `\n`roll`\n`hello`\n`@MieraSargs`'



        return 'I didn\'t get that try writing "!help"'

    if message.find("<@1047912725621264444>") >= 0:
        return "What's up?"

    return None
