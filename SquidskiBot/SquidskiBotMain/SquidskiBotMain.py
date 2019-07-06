# Packages
import discord
import sys
import logging

# Various other files
from ChiefMuteInsurance import ChiefMuteInsurance
from CommandHandler import CommandHandler
from LoggingModule import LoggingModule

# Picks the symbol to prefix onto commands
globalCall = ">"

# Initialization alerts
log = LoggingModule()

# Logger setup (I don't actually use this but I'm scared to remove it)
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
        log.logMessage(str(member) + " was given the pings role!", member)

    # Initializes stuff
    async def on_ready(self):
        log.logMessage(f'Logged on as, {self.user}')

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

        # Mute if ping chief
        if ("<@208272642640314389>" in message.content):
            chiefMute = ChiefMuteInsurance()
            await chiefMute.the_muter(message)


# Instantiate client
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
log.logMessage("Successfully read bot token")
tokenReader.close()

