import discord
import random
import sys

class fanfic():

    async def getLine(self, message):
        whichPart = str(random.randint(1,6))
        fanficTxt = open(f"FanficTxt/Part{whichPart}.txt", "r").read().split("\n")
        whichLine = random.randint(1, len(fanficTxt))
        await message.channel.send("Getting line...")
        await self.buildEmbed(whichPart, whichLine, fanficTxt[whichLine])

    async def buildEmbed(self, part, lineNum, lineTxt):
        partTitle = self.getPartName(part)
        embed = discord.Embed(title="SE Discord Fanfiction", color=0x00ff00)
        embed.add_field(name="Your Random Line:", value=lineTxt)
        embed.set_footer(text=f"You are reading line {lineNum} from {partTitle}")
        await message.channel.send(embed = embed)

    def getPartName(self, part):
        if(part == "1"):
            return "'My Traumatic Experience'"
        elif(part == "2"):
            return "'SDK Mansion'"
        elif(part == "3"):
            return "'What it Means to be a Mapper'"
        elif(part == "4"):
            return "'SDK's Secret VMF'"
        elif(part == "5"):
            return "'Entity Control'"
        elif(part == "6"):
            return "'Active Injustice'"
        else:
            return "***Unknown title***"