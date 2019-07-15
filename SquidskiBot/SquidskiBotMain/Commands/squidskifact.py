import discord
import random
from LoggingModule import LoggingModule

class squidskifact():
    quoteList = []

    # Reads SeinfeldQuotes.txt and puts all lines into a list
    def __init__(self):
        myFile = open("squidskifacts.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    # Pulls and sends a random quote
    async def getQuote(self, message):
        log = LoggingModule()
        quoteOfChoice = random.choice(self.quoteList)
        await log.logIt(f"Sent the Squidski fact '{quoteOfChoice}' for {message.author}", message)
        return self.buildEmbed(quoteOfChoice)

    def buildEmbed(self, quoteOfChoice):
        embed = discord.Embed(color=0x00BFFF)
        embed.add_field(name=f"Squidski Fact #{random.randint(1,100000):}", value=f"{quoteOfChoice}", inline=False)
        return embed