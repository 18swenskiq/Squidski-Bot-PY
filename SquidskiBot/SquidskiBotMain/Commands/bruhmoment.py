import discord
from LoggingModule import LoggingModule
import random

class bruhmoment():

    # Rolls a random number to determine if something is a 'bruh' moment
    async def isBruhMoment(self, message):
        log = LoggingModule()
        myVal = random.random()
        if (myVal > .5):
            await self.classifyBruhMoment(message)
        else:
            await message.channel.send("I have determined that this is not a bruh moment.")
            await log.logIt(f"Message wasn't a bruh moment", message)

    # If it is a 'bruh' moment, reads and writes to file containing total amount of bruh moments
    async def classifyBruhMoment(self, message):
        log = LoggingModule()
        await message.channel.send("***THIS IS A CERTIFIED BRUH MOMENT***")
        await log.logIt(f"Certified something as a bruh moment", message)
        myFile = open("./BruhMoments.txt","r")
        bruhMoments = myFile.read()
        await message.channel.send("This server has had " + str(int(bruhMoments) + 1)  + " bruh moments.")
        myFile.close()
        myFile = open("./BruhMoments.txt","w")
        myFile.write(str(int(bruhMoments) + 1))
        await log.logIt("This server has had " + str(int(bruhMoments) + 1) + " bruh moments.")
        myFile.close()

