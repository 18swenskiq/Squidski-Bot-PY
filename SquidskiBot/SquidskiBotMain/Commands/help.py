import discord
from LoggingModule import LoggingModule

class help():

    # Builds a discord embed object to display as the help message
    async def myEmbed(self, message):
        log = LoggingModule()
        embed = discord.Embed(title="Squidski-Bot PY", description="I am a bot made by Squidski#9545. I can do multiple things and I am still in development", color=0x00ff00)
        embed.add_field(name="Search Workshop", value=">sws <game> <type> <search term>", inline=False)
        embed.add_field(name="Get Random Seinfeld Quote", value=">seinfeldme", inline=False)
        embed.add_field(name="Subscribe or Unsubscribe from pings", value=">pings", inline=False)
        embed.add_field(name="Check if something is a bruh moment", value=">bruhmoment", inline=False)
        embed.add_field(name="Admin only commands", value=">helpadmin",inline=False)
        await log.logIt(f"Sent help message for {message.author}", message)
        return embed


