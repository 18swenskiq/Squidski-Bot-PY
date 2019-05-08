# Packages
import discord
import sys
import logging

sys.path.append('./Commands')

# Commands
from sws import sws

# This string can be modified to change what prefix the bot responds to
globalCall = ">"

# Administrator role ID
adminRoleID = "574763874201501696"

# Initialization alerts
print("The call symbol for the bot is " + globalCall)
print("Successfully imported sws command module")
print("Successfully imported purge command module")

# Logger setup

logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # Help message
        if (message.content.lower() == globalCall + "help"):
            embed = discord.Embed(title="Squidski-Bot PY", description="I am a bot made by Squidski#9545. I can do multiple things and I am still in development", color=0x00ff00)
            embed.add_field(name="Search Workshop", value=">sws <game> <type> <search term>", inline=False)
            await message.channel.send(embed=embed)

        # Good night response
        if (message.content.lower() in ["good night","gn","goodnight"]):
            await (message.channel.send("Good night " + str(message.author)[:-5]))

        # Search workshop
        if (message.content.startswith((globalCall + 'sws'))):
           try:
              searchWorkshop = sws()
              await message.channel.send("Searching the workshop. Please wait...")
              searchIt = searchWorkshop.theMain(message.content)
              if not searchIt:
                  await message.channel.send("That's a fat error from me dawg. The search came up empty.")
              else:
                await message.channel.send(searchIt)
           except ValueError as e:
              print("Could not parse search results")

        # Purge messages
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            shortened = str(message.content.lower().split(" ")[1])
            if adminRoleID in str(message.author.roles):
                await message.channel.purge(limit=int(shortened))
                await message.channel.send("Purged " + shortened + " messages.")
            else:
                print(message.author.roles)
                await message.channel.send("You must have the `Administrator` role to do this...")


            
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
