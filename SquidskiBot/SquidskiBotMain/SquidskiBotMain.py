# Packages
import discord
import bs4
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

# Classes
import WorkshopSearch

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

client = MyClient()
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
