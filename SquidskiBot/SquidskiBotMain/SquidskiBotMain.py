# Packages
import discord

# Classes
import WorkshopSearch

# This string can be modified to change what prefix the bot responds to
global globalCall
globalCall = ">"

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

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
