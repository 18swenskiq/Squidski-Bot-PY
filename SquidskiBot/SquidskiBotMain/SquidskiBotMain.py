# Packages
import discord

# Classes
from WorkshopSearch import WorkshopSearch

# This string can be modified to change what prefix the bot responds to
global globalCall
globalCall = ">"

# Initialization alerts
print("The call symbol for the bot is " + globalCall)
print("Successfully imported WorkshopSearch class")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if ((globalCall + 'sws') in message.content):
           newWSSearch = WorkshopSearch()
           messageArray = newWSSearch.getResults('csgo', 'map', 'abbey')
           await message.channel.send("Result 1: <" + messageArray[0] + ">\nResult 2: <" + messageArray[1] + ">\nResult 3: <" + messageArray[2] + ">\nResult 4: <" + messageArray[3] + ">\nResult 5: <" + messageArray[4] + ">")
            
client = MyClient()

# Read bot token
tokenReader = open("token.txt", "r")
client.run(tokenReader.read())
tokenReader.close()
