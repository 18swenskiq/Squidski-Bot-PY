import discord
import random
from LoggingModule import LoggingModule

class squidskifact():
    quoteList = []

    # Reads squidskifacts.txt and puts all lines into a list
    def __init__(self):
        myFile = open("squidskifacts.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    # Pulls and sends a random quote
    async def getQuote(self, message):
        log = LoggingModule()
        quoteOfChoice = random.choice(self.quoteList)
        await log.logIt(f"Sent the Squidski fact '{quoteOfChoice}'", message)
        return self.buildEmbed(quoteOfChoice)

    def buildEmbed(self, quoteOfChoice):
        embed = discord.Embed(title=f"Squidski Fact #{random.randint(1,100000):}", description=f"{quoteOfChoice}",  color=0x00BFFF)
        return embed