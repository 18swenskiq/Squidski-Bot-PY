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

# Testing Github webhook

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
        if ((message.content.lower()).split(" ").startswith(globalCall + "purge")):
            if "Administrator" in message.author.roles:
                client.http.delete_message(message.channel,)
            else:
                await message.channel.send("You must have the `Administrator` role to do this...")


            
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
