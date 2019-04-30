# Packages
import discord
import sys

sys.path.append('./Commands')

# Commands
from sws import sws

# This string can be modified to change what prefix the bot responds to
globalCall = ">"

# Initialization alerts
print("The call symbol for the bot is " + globalCall)
print("Successfully imported sws command module")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if (message.content.startswith((globalCall + 'sws'))):
           try:
              searchWorkshop = sws()
              await message.channel.send("Searching the workshop. Please wait...")
              await message.channel.send(searchWorkshop.theMain(message.content))
           except ValueError as e:
              print("Could not parse search results")
            
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
