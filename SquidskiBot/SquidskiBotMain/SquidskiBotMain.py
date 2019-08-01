# Packages
import asyncio
import datetime
import discord
import json
import sys
import logging

# Various other files
from ChiefMuteInsurance import ChiefMuteInsurance
from CommandHandler import CommandHandler
from LoggingModule import LoggingModule

# This settings file contains a bunch of variables
with open('settings.json') as json_file:
    settingsFile = json.load(json_file)

# Picks the symbol to prefix onto commands
globalCall = settingsFile["globalCall"]

# Initialization alerts
print("The call symbol for the bot is " + globalCall)

# Logger setup
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# Here's where the magic happens
class MyClient(discord.Client):

    # Adds Pings role on join
    async def on_member_join(self, member):
        await member.add_roles(discord.utils.get(member.guild.roles, name='Pings'))
        print(str(member) + " was given the pings role!")

    # Initializes stuff
    async def on_ready(self):
        log = LoggingModule()
        await log.logIt(f"Logged on as {self.user}", self.get_channel(settingsFile["loggingChannel"]))

    # Respond to messages starts here
    async def on_message(self, message):
        if message.author == self.user:
            return

        # Handle the Commands with globalCall
        if (message.content.startswith(globalCall)):
            myCommand = CommandHandler()
            await myCommand.commandParser(message, globalCall)

        # Good night response
        if (message.content.lower() in ["good night","gn","goodnight"]):
            await (message.channel.send("Good night " + str(message.author)[:-5]))


# Instantiate client
client = MyClient()

# Read bot token
client.run(settingsFile["botKey"])
print("Successfully read bot token")
tokenReader.close()
