import discord

class help():
    def myEmbed(self):
        embed = discord.Embed(title="Squidski-Bot PY", description="I am a bot made by Squidski#9545. I can do multiple things and I am still in development", color=0x00ff00)
        embed.add_field(name="Search Workshop", value=">sws <game> <type> <search term>", inline=False)
        embed.add_field(name="Get Random Seinfeld Quote", value=">seinfeldme", inline=False)
        embed.add_field(name="Subscribe or Unsubscribe from pings", value=">pings", inline=False)
        embed.add_field(name="Check if something is a bruh moment", value=">bruhmoment", inline=False)
        return embed


