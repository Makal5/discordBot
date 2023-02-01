"""Bot python file"""

import logging

import discord
from discord.ext import commands, tasks

import sensitive
from Responses import responses

LOGGER = logging.getLogger(__name__)


async def send_message(message, user_message, isPrivate):
    """Bot set up"""
    try:
        # logger if is private channel or community channel
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
        """On ready log to info"""
        LOGGER.info(f'{client.user} is up and running')

    @client.event
    async def on_message(message):
        """Message working"""
        # Check if message author == to bot
        if message.author == client.user:
            return

        # Check if message does not contain bad words
        if message.content.contains != "ass" or message.content.contains != "fuck":
            pass
        else:
            message.channel.purge(limit=1)

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # logger debug with username, channel and said message
        LOGGER.debug(f'{username} in {channel} said: "{user_message}"')

        # check if user message starts with ?
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, isPrivate=True)
        else:
            await send_message(message, user_message, isPrivate=False)

    client.run(sensitive.TOKEN)
