import discord
import subprocess

class VDCsearch(object):
    
    async def searchTheVDC(self, message):
        searchTerm = message.content[3:]
        if len(searchTerm.split(" ")) < 1:
            await message.channel.send("I was not given enough arguments to search the VDC.")
            await log.logIt("I wasn't given enough arguments for a proper VDC search.", message)
            return
        p1 = subprocess.Popen(["C:\\Users\\Administrator\\source\\repos\\18swenskiq\\Squidski-Bot-PY\\SquidskiBot\\SquidskiBotMain\\csPrograms\\VDCSearch\\VDCSearch.exe", searchTerm], stdout=subprocess.PIPE)
        output = p1.communicate()
        returnString = output[0].decode("utf-8")
        if "NRF" in returnString:
            await message.channel.send("No results were found for your VDC search")
            return
        else:
            # Strip the whitespace from our list of results and turn it into an array
            returnString = "".join(returnString.split())
            returnString = returnString.split(",")
            try:
                vEmbed = discord.Embed(title="Your VDC Search Results:", color=0x060606)
                vEmbed.add_field(name="Result 1:", value=f"[{returnString[0][41:]}]({returnString[0]})" , inline=False)
                vEmbed.add_field(name="Result 2:", value=f"[{returnString[1][41:]}]({returnString[1]})" , inline=False)
                vEmbed.add_field(name="Result 3:", value=f"[{returnString[2][41:]}]({returnString[2]})" , inline=False)
                vEmbed.add_field(name="Result 4:", value=f"[{returnString[3][41:]}]({returnString[3]})" , inline=False)
                vEmbed.add_field(name="Result 5:", value=f"[{returnString[4][41:]}]({returnString[4]})" , inline=False)
            except:
                await message.channel.send(f"There were less than 5 results...", message)

            await message.channel.send(embed = vEmbed)

