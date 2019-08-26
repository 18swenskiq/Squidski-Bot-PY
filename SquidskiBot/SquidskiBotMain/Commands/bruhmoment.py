import discord
import random
import sys

class bruhmoment():

    # Rolls a random number to determine if something is a 'bruh' moment
    async def isBruhMoment(self, message):
        myVal = random.random()
        if (myVal > .5):
            await self.classifyBruhMoment(message)
        else:
            await message.channel.send("I have determined that this is not a bruh moment.")

    # If it is a 'bruh' moment, reads and writes to file containing total amount of bruh moments
    async def classifyBruhMoment(self, message):
        await message.channel.send("***THIS IS A CERTIFIED BRUH MOMENT***")
        myFile = open("./BruhMoments.txt","r")
        bruhMoments = myFile.read()
        await message.channel.send(f"This server has had {int(bruhMoments) + 1} bruh moments.")
        myFile.close()
        myFile = open("./BruhMoments.txt","w")
        myFile.write(str(int(bruhMoments) + 1))
        await log.logIt(f"This server has had {int(bruhMoments) + 1} bruh moments.", message)
        myFile.close()

