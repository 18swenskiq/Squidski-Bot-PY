import random
import sys

class seinfeldme():
    quoteList = []

    # Reads SeinfeldQuotes.txt and puts all lines into a list
    def __init__(self):
        myFile = open("SeinfeldQuotes.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    # Pulls and sends a random quote
    async def getQuote(self, message):
        quoteOfChoice = random.choice(self.quoteList)
        await message.channel.send(quoteOfChoice)