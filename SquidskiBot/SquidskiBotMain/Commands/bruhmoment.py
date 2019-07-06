import discord
import random

from LoggingModule import LoggingModule

class bruhmoment():

    # Rolls a random number to determine if something is a 'bruh' moment
    async def isBruhMoment(self, message):
        myVal = random.random()
        if (myVal > .5):
            await self.classifyBruhMoment(message)
        else:
            await message.channel.send("I have determined that this is not a bruh moment.")
            LoggingModule.logMessage("Checked if something was a bruh moment. It wasn't.")

    # If it is a 'bruh' moment, reads and writes to file containing total amount of bruh moments
    async def classifyBruhMoment(self, message):
        await message.channel.send("***THIS IS A CERTIFIED BRUH MOMENT***")
        LoggingModule.logMessage("Certified something as a bruh moment.")
        myFile = open("./BruhMoments.txt","r")
        bruhMoments = myFile.read()
        await message.channel.send("This server has had " + str(int(bruhMoments) + 1)  + " bruh moments.")
        myFile.close()
        myFile = open("./BruhMoments.txt","w")
        myFile.write(str(int(bruhMoments) + 1))
        LoggingModule.logMessage("This server has had " + str(int(bruhMoments) + 1) + " bruh moments.")
        myFile.close()

