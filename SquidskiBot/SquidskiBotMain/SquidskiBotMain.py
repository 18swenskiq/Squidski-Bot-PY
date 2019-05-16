# Packages
import datetime
import discord
import sys
import time
import logging

sys.path.append('./Commands')

# Commands
from seinfeldme import seinfeldme
from sws import sws

# This string can be modified to change what prefix the bot responds to
globalCall = ">"

# Administrator role ID
adminRoleID = "574763874201501696"

# Initialization alerts
print("The call symbol for the bot is " + globalCall)
print("Successfully imported sws command module")
print("Successfully imported purge command module")

#Squidski Time

# Logger setup
logger = logging.getLogger('discord')
logger.setLevel(logging.CRITICAL)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class MyClient(discord.Client):
    async def is_me(self, m):
        mybool = m.author == client.user
        return await myBool  

    # Initializes stuff
    async def on_ready(self):
        print('Logged on as', self.user)

    # Don't respond to ourselves
    async def on_message(self, message):
        if message.author == self.user:
            return

        # Help message
        if (message.content.lower() == globalCall + "help"):
            embed = discord.Embed(title="Squidski-Bot PY", description="I am a bot made by Squidski#9545. I can do multiple things and I am still in development", color=0x00ff00)
            embed.add_field(name="Search Workshop", value=">sws <game> <type> <search term>", inline=False)
            embed.add_field(name="Get Random Seinfeld Quote", value=">seinfeldme", inline=False)
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

        # Get random Seinfeld quote
        if (message.content.startswith((globalCall + 'seinfeldme'))):
            getSeinfeldQuote = seinfeldme()
            await message.channel.send(getSeinfeldQuote.getQuote())


        # Purge messages (Administrator Only)
        if (((message.content.lower()).split(" "))[0].startswith(globalCall + "purge")):
            shortened = str(message.content.lower().split(" ")[1])
            if adminRoleID in str(message.author.roles):
                await message.channel.purge(limit=(int(shortened) + 1))
                await message.channel.send("Purged " + shortened + " messages.")
                time.sleep(3)
                await message.channel.purge(limit=1, check=self.is_me)
            else:
                print(message.author.roles)
                await message.channel.send("You must have the `Administrator` role to do this...")


            
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
