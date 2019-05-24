import discord
import random

class bruhmoment():
    async def isBruhMoment(self, message):
        myVal = random.random()
        if (myVal > .5):
            await self.classifyBruhMoment(message)
        else:
            await message.channel.send("I have determined that this is not a bruh moment.")
            print("Checked if something was a bruh moment. It wasn't.")

    async def classifyBruhMoment(self, message):
        await message.channel.send("***THIS IS A CERTIFIED BRUH MOMENT***")
        print("Certified something as a bruh moment.")
        myFile = open("./BruhMoments.txt","r")
        bruhMoments = myFile.read()
        await message.channel.send("This server has had " + str(int(bruhMoments) + 1)  + " bruh moments.")
        myFile.close()
        myFile = open("./BruhMoments.txt","w")
        myFile.write(str(int(bruhMoments) + 1))
        print("This server has had " + str(int(bruhMoments) + 1) + " bruh moments.")
        myFile.close()

