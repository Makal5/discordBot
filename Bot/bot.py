"""Bot python file"""

import discord
from Responses import responses
import logging
import sensitive

LOGGER = logging.getLogger(__name__)


async def send_message(message, user_message, isPrivate):
    """Bot set up"""
    try:
        resp_channel = 'channel'
        if isPrivate:
            resp_channel = 'private'
        response = responses.get_response(user_message)
        if response is not None:
            await message.author.send(response) if isPrivate else await message.channel.send(response)
            LOGGER.debug(f'sent response to {resp_channel} - {response}')
    except Exception as e:
        LOGGER.error("Send msg exception:", exc_info=e)


def run_discord_bot():
    """Bot running function"""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        LOGGER.info(f'{client.user} is up and running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content != "ass" or message.content != "fuck":
            pass
        else:
            message.channel.purge(limit=1)

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        LOGGER.debug(f'{username} in {channel} said: "{user_message}"')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, isPrivate=True)
        else:
            await send_message(message, user_message, isPrivate=False)

    client.run(sensitive.TOKEN)
