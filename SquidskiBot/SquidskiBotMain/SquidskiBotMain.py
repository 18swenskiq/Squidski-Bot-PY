# Packages
import discord
import sys
import logging

# Various other files
from ChiefMuteInsurance import ChiefMuteInsurance
from CommandHandler import CommandHandler

# Picks the symbol to prefix onto commands
globalCall = ">"

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
    async def on_member_join(member):
        await member.add_roles(discord.utils.get(message.guild.roles, name='Pings'))
        print(str(member) + " was given the pings role!")

    # Initializes stuff
    async def on_ready(self):
        print('Logged on as', self.user)

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
print("Successfully read bot token")
tokenReader.close()
