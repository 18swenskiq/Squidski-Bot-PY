import random
import sys
from ErrorPrintingModule import ErrorPrintingModule
from LoggingModule import LoggingModule

class seinfeldme():
    quoteList = []

    # Reads SeinfeldQuotes.txt and puts all lines into a list
    def __init__(self):
        myFile = open("SeinfeldQuotes.txt", "r")
        self.quoteList = (myFile.read()).split("\n")
        myFile.close();

    # Pulls and sends a random quote
    async def getQuote(self, message):
        try:
            log = LoggingModule()
            quoteOfChoice = random.choice(self.quoteList)
            await log.logIt(f"Sent the seinfeld quote '{quoteOfChoice}'", message)
            await message.channel.send(quoteOfChoice)
        except:
            e = ErrorPrintingModule()
            await e.reportError(message, sys.exc_info()[0])